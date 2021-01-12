import datetime

time_loads = [
	datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y 10:00:00"), '%m/%d/%Y %H:%M:%S'),
	datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y 11:00:00"), '%m/%d/%Y %H:%M:%S'),
	datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y 12:00:00"), '%m/%d/%Y %H:%M:%S'),
	datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y 13:00:00"), '%m/%d/%Y %H:%M:%S'),
	datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y 14:00:00"), '%m/%d/%Y %H:%M:%S'),
	datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y 15:00:00"), '%m/%d/%Y %H:%M:%S'),
	datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y 16:00:00"), '%m/%d/%Y %H:%M:%S'),
	datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y 17:00:00"), '%m/%d/%Y %H:%M:%S'),
	datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y 18:00:00"), '%m/%d/%Y %H:%M:%S'),
	datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y 19:00:00"), '%m/%d/%Y %H:%M:%S'),
	datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y 20:00:00"), '%m/%d/%Y %H:%M:%S'),
	datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y 21:00:00"), '%m/%d/%Y %H:%M:%S'),
	datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y 22:00:00"), '%m/%d/%Y %H:%M:%S'),
	datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y 23:00:00"), '%m/%d/%Y %H:%M:%S'),
	datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y 23:59:00"), '%m/%d/%Y %H:%M:%S')
]