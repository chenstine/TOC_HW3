#-*- coding: UTF-8 -*-

# Theory of computation hw3 103.6.21
# 陳亭宇 F74002272
# 103.6.21
# Function:
# 	Find the average of all sale prices matching the condition user inputs(city, road name, year)
# 	Output the average price(in integer)
# How:
# 	use function dict.get(key[, default])
#	get the value of the key and inspect if match

import json
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

url = raw_input(u"url:")
if url == "":
	print ("Please enter url!")
	sys.exit(0)
city = raw_input(u"鄉鎮市區:")
if city == "":
	print ("Please enter city!")
	sys.exit(0)
road = raw_input(u'Road_Name:')
if road == "":
	print ("Please enter road!")
	sys.exit(0)
year = input('year:')
if year == "":
	print ("Please enter year!")
	sys.exit(0)

#response = urllib2.urlopen('http://www.datagarage.io/api/5365dee31bc6e9d9463a0057')
response = urllib2.urlopen(url)
data = json.load(response)
key1 = u"鄉鎮市區"
key2 = u"土地區段位置或建物區門牌"
key3 = u"交易年月"
key4 = u"總價元"

total = 0
count = 0
i = 0
while i < len(data):
	if data[i].get(key1) == city:
		j = 0
		length = len(data[i].get(key2))-len(city)/2-len(road)/2
		while j < length:
			length2 = len(city)/3+len(road)/3
			if data[i].get(key2)[j:j+length2] == city+road:
				if dict(data[i]).get(key3) >= year*100:
					total += dict(data[i]).get(key4)
					count += 1
			j += 1
	i += 1
if count > 0:
	print (int)(total/count)
elif count == 0
	print ("no match")
