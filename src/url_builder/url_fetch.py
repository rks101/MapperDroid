#
# 'https://play.google.com/store/apps/details?id=' is a common prefix in every app url.
# Therefore, we skip this part while matching url.
# The current approach will never let urls repeat.

import os
import numpy as np
from queue import Queue
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import time

# fetch URLs using given seed URL
def fetch_urls(seed_url, file_handler):
	Chrome_options = Options()
	Chrome_options.add_argument("--headless")
	driver = webdriver.Chrome(chrome_options=Chrome_options)
	global visited_urls
	q = Queue() 
	itr = 0 
	visited_urls.add(seed_url)
	q.put(seed_url)
	print(itr)
	while not q.empty():
		time.sleep(0.1)
		lets_go = 'https://play.google.com/store/apps/details?id=' + q.get()
		file_handler.write(lets_go + '\n')
		driver.get(lets_go)
		itr += 1
		print(itr)
		print(lets_go)
		for links in driver.find_elements_by_class_name("poRVub"):
			url = str(links.get_attribute("href"))
			url = url[46:]
			if url not in visited_urls:
				q.put(url)
				visited_urls.add(url)

# main driver
if __name__=="__main__":
	# for seed_url, specify app package name only
	#seed_url = "com.google.android.googlequicksearchbox" # 2,000
	#seed_url = "com.google.android.youtube" # 1
	#seed_url = "com.endomondo.android" # 53,000
	#seed_url = "in.gov.uidai.mAadhaarPlus" # 10,624
	#seed_url = "com.rstudioz.habits" # 6
	#seed_url = "com.samsung.android.app.sprotect" # 87
	#seed_url = "com.horseboxsoftware.heathrowairportflights" # 17
	#seed_url = "com.makemytrip" # 17
	#seed_url = "com.huawei.global" # 25
	#seed_url = "com.olacabs.customer" # 16
	#seed_url = "com.jio.media.jiobeats" # 83
	#seed_url = "com.google.vr.expeditions" # 35
	#seed_url = "org.videolan.vlc" # 33
	#seed_url = "com.netflix.mediaclient" # 35
	#seed_url = "com.ekigai.android" # 226
	seed_url = "us.zoom.zrc" # 
	#seed_url = "" # 
	#seed_url = "" # 

	# File url_records.txt contains already explored app URLs
	file_name = 'url_records.txt'

	# the multigraph data structure works assuming no url is a subset of
        # another and also a url contains atleast 2 chars (adjacency matrix)
	visited_urls = set()
	previous_record_exists = os.path.isfile(file_name)

	if previous_record_exists:
		# read and build the multigraph. Last url as seed url
		file_handler = open('url_records.txt', 'r')
		existing = file_handler.readlines()
		for url in existing:
			url = url.strip()
			visited_urls.add(url[46:])
		
		file_handler.close()
		print(len(visited_urls))

	file_handler = open('url_records.txt', 'a+')
	
	if seed_url not in visited_urls:
		fetch_urls(seed_url, file_handler)
	else:
		print("Seed URL is already present")
	file_handler.close()

# EOS
