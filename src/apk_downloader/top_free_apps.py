#few notes--
# 'https://play.google.com/store/apps/details?id=' is common in every url so skip this part while matching 

import os
import numpy as np
from queue import Queue
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import time

def get_top_free_apps(category, applied_filter, file_handler):
	Chrome_options=Options()
	Chrome_options.add_argument("--headless")
	driver=webdriver.Chrome(chrome_options=Chrome_options)

	base_url = 'https://play.google.com/store/apps/details?id='

	for i in range(3):
		search_url = "https://www.appbrain.com/apps/" + applied_filter + "/" + category + "/free/?o=" + str(i*10)
		driver.get(search_url)
		top_apps = driver.find_elements_by_xpath("//div[@class='vmargin-s']/div/a[1]")
		for app in top_apps:
			url=str(app.get_attribute("href"))
			splitter = url.split('/')
			size = len(splitter)
			package_name = splitter[size-1]
			file_handler.write(base_url + package_name + '\n')


			

if __name__=="__main__":
	
	
	file_name='free_apps.txt'
	
	categories = [
			"art-and-design", 
			"auto-and-vehicles",
			"beauty",
			"books-and-reference",
			"business",
			"comics",
			"communication",
			"dating",
			"education",
			"entertainment",
			"events",
			"finance",
			"food-and-drink",
			"health-and-fitness",
			"house-and-home",
			"libraries-and-demo",
			"lifestyle",
			"maps-and-navigation",
			"medical",
			"music-and-audio",
			"news-and-magazines",
			"parenting",
			"personalization",
			"photography",
			"productivity",
			"social",
			"sports",
			"tools",
			"travel-and-local",
			"video-players-and-editors",
			"weather",
	]

	filters = ["hot", "hot-week", "popular", "highest-rated"]

	previous_record_exists=os.path.isfile(file_name)

	file_handler=open('free_apps.txt','a+')

	for category in categories:
		file_handler.write(category + ':\n')
		get_top_free_apps(category, filters[2], file_handler)
		file_handler.write('\n')
	
	file_handler.close()
