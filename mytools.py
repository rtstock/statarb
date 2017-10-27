# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 10:57:01 2014

@author: jmalinchak
"""

def builddates(date1,date2):
	from datetime import date, timedelta
	a1 = date1.split('-')
	a2 = date2.split('-')
	d1 = date(int(a1[0]),int(a1[1]),int(a1[2]))
	d2 = date(int(a2[0]),int(a2[1]),int(a2[2]))

	# this will give you a list containing all of the dates
	dd = [d1 + timedelta(days=x) for x in range((d2-d1).days + 1)]
        return dd
##
##	# you can't join dates, so if you want to use join, you need to
##	# cast to a string in the list comprehension:
##	ddd = [str(d1 + timedelta(days=x)) for x in range((d2-d1).days + 1)]
##	# now you can join
##	ret = "\n".join(ddd)
##	return ret
	
def make_sure_path_exists(self,path):
	import errno
	import os
	try:
		os.makedirs(path)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise


def make_sure_filepath_exists(filepath):
	import errno
	import os
	try:
		print(filepath)
		path = os.path.dirname(os.path.abspath(filepath))
		print(path)
		os.makedirs(path)
		
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

	
def datetimenormal():
	import datetime
	sdatetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	return sdatetime
	
def appendnormaldateddirectorybasedoncurrenttime15(root):
	import datetime
	sdate = datetime.datetime.now().strftime("%Y-%m-%d")
	stime = datetime.datetime.now().strftime("%H:%M:%S")
	shour = stime.split(':')[0]
	sminute = stime.split(':')[1]
	#print(int(sminute))
	sminutenormal = '0'
	if int(sminute) < 15:
		sminutenormal = '15'
	if int(sminute) >= 15 and int(sminute) < 30:
		sminutenormal = '30'
	if int(sminute) >= 30 and int(sminute) < 45:
		sminutenormal = '45'
	if int(sminute) >= 45 and int(sminute) < 60:
		sminutenormal = '60'
	
	#root = "C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\downloads"
	final = root + "\\" + sdate + "\\" + shour + "\\" + sminutenormal
	return final
def appendnormaldateddirectorybasedondatetimeparameter(root,datetimeparameter):
   
	sdate = datetimeparameter.strftime("%Y-%m-%d")
	stime = datetimeparameter.strftime("%H:%M:%S")
	shour = stime.split(':')[0]
	sminute = stime.split(':')[1]
	print('======== =======================================')
	print('========',datetimeparameter,'converts to minute',int(sminute))
	
	sminutenormal = '0'
	if int(sminute) < 15:
		sminutenormal = '15'
	if int(sminute) >= 15 and int(sminute) < 30:
		sminutenormal = '30'
	if int(sminute) >= 30 and int(sminute) < 45:
		sminutenormal = '45'
	if int(sminute) >= 45 and int(sminute) < 60:
		sminutenormal = '60'
	
	#root = "C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\downloads"
	final = root + "\\" + sdate + "\\" + shour + "\\" + sminutenormal
	print(final)
	print('======== =======================================')
	return final
def ConvertDatetime14(self):
	import datetime
	s = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
	return s
	
def ConvertStringToDate(MyString):
	import datetime

	minyear = 1900
	maxyear = 2060
	
	mydate = MyString
	
	dateparts = mydate.split('-')
#        print(dateparts[0])
#        print(dateparts[1])
#        print(dateparts[2])
	try:
		if len(dateparts) != 3:
		   raise ValueError("Invalid date format")
		if int(dateparts[0]) > maxyear or int(dateparts[0]) <= minyear:
		   raise ValueError("Year out of range")
		
		dateobj = datetime.date(int(dateparts[0]),int(dateparts[1]),int(dateparts[2]))
		#print(str(dateobj)) #str(dateobj
		return dateobj
	except:
		return datetime.date(1900,1,1)
#                                          
#                                          
#C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\inputs\\Symbols.txt
#C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\inputs\\Expirations.txt
