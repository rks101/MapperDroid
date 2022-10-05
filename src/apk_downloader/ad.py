# this script reads urls from a file , searches apkpure for that app and downloads the first result
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import time
def download_apk_from_file(file_handler, apk_not_found):
	global driver
	import random
	
	
	number_of_apps=0
	for url in file_handler:
		app_id=str(url[46:])
		#app_id=str(url)
		search_url='https://apkpure.com/search?q='+app_id
		driver.get(search_url)

		if number_of_apps == 0:
			time.sleep(60)

		time.sleep(random.randint(3,10))
		try:
			first_result=driver.find_element_by_xpath('//*[@id="search-res"]/dl[1]/dd/p[1]/a') # get the first search result of all
		except NoSuchElementException: # in case no app is found in search results
			apk_not_found.write(url)
			continue

		download_page_link=first_result.get_attribute('href') # get the href attribute of the first search result
		app_id_len = len(app_id)
		check_app = str(download_page_link[-app_id_len+1:])

		if app_id[:-1] != check_app: # If the apps apk is not found on apkpure, dump its name to new file 
			apk_not_found.write(url)
			continue
		
		driver.get(download_page_link)

		try:
			download_button=driver.find_element_by_class_name('da')
			time.sleep(random.randint(3,10))
			download_button.click()
			number_of_apps+=1
			print('Download #'+str(number_of_apps)+' initiated for '+app_id)
			time.sleep(random.randint(6,10))  # wait for 4 seconds ,,, use when there is a good estimate or wait for download
		except NoSuchElementException:  # if either the page has been removed or apk is not available for download
			apk_not_found.write(url)
			pass



if __name__=="__main__":
	chrome_options = Options()
	chrome_options.add_argument("--window-size=1920,1080")
	chrome_options.add_argument("--no-sandbox")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--dns-prefetch-disable")
	chrome_options.add_argument("--disable-gpu")
	chrome_options.add_argument("--disable-browser-side-navigation")
	chrome_options.add_argument("enable-automation")
	chrome_options.add_argument("start-maximized")
	chrome_options.add_experimental_option("prefs", {
  	"download.default_directory": "apps",
  	"download.prompt_for_download": False,
  	"download.directory_upgrade": True,
  	"safebrowsing.enabled": True
	})
	print("Starting Chrome...")
	driver=webdriver.Chrome(chrome_options=chrome_options)
	all_ok=True
	try:
		file_handler=open("urls_social.txt","r")
		apk_not_found=open('apk_not_found.txt','a+')  # file stores the url of apps whose apk was not found in apkpure
		#file_handler=open("education_pkg.txt","r")
		#file_handler=open("tools_pkg.txt","r")
		#file_handler=open("finance_pkg.txt","r")
		#file_handler=open("business_pkg.txt","r")
		#file_handler=open("productivity_pkg.txt","r")
		#file_handler=open("personalization_pkg.txt","r")
		#file_handler=open("books_and_reference_pkg.txt","r")
		#file_handler=open("entertainment_pkg.txt","r")
		#file_handler=open("communication_pkg.txt","r")
		#file_handler=open("music_and_audio_pkg.txt","r")
		#file_handler=open("lifestyle_pkg.txt","r")
		#file_handler=open("others_pkg.txt","r")
	except IOError:
		print('Records not found. Exiting Chrome')
		driver.quit()
		all_ok=False

	if all_ok:
		download_apk_from_file(file_handler, apk_not_found)
		print('Job Done')
		file_handler.close()
		apk_not_found.close()
		print('Exiting Chrome... in 5 mins ')
		time.sleep(5*60)
		driver.quit()

