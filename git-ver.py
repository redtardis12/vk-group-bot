import vk_api
from vk_api import VkUpload
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import requests
import time
import os

driver = webdriver.Chrome()
sched = BlockingScheduler()
main_link = []  # list where images' url will be store

def GetImageLInk(link_list):   # function searches for images and stores in list "link_list"
	driver.get('web-site url')  #place your web-site url here
	time.sleep(5)
	images = driver.find_elements_by_tag_name('img')
	for image in images:
	    link_list.append(image.get_attribute('src'))  # stores images' url in the list
	driver.refresh()


login, password = 'vk login', 'password'  # login vk.com as user
vk_session = vk_api.VkApi(login, password)
vk_session.auth()
upload = VkUpload(vk_session) 


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=some_hour)  # bot starts every day at some_hour 
def main():
	current_date_and_time = datetime.datetime.now()
	hours = 1
	hours_added = datetime.timedelta(hours = hours)
	future_date_and_time = current_date_and_time + hours_added  # creates current date and time

	for i in range(1,15):  # the number of cycle iterations means how many wall posts you want per day
		GetImageLInk(main_link)
		
		p = requests.get(main_link[1])
		out = open("img.jpg", "wb")
		out.write(p.content)
		out.close() # downloads and saves image from recieved urls in "img.jpg" file
			
		photos = ['img.jpg']
		photo_list = upload.photo_wall(photos)
		attachment = ','.join('photo{owner_id}_{id}'.format(**item) for item in photo_list)  # upload image on vk servers
	
		vk_session.method("wall.post", {
		    'owner_id': "-group id",  # place your group id here
		    'from_group': '1',
		    'message': '', #place your text for the post
		    'attachment': attachment,
		    'publish_date': future_date_and_time.timestamp() # the post will be delayed in certain hours
		})
		
		hours = hours + 1
		hours_added = datetime.timedelta(hours = hours)
		future_date_and_time = current_date_and_time + hours_added  # increases hour delay
		main_link.clear()  # clears list with urls
		os.remove('img.jpg')
	driver.close()

sched.start()