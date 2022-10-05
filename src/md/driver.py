# Driver program to get App name, category, url, description, permissions, etc.
# Run this program using
# python3 driver.py

from app_info_new import get_data

# Get data from one app URL
#url = 'https://play.google.com/store/apps/details?id=com.instagram.android&hl=en'
#get_data(url)

# Create URL_LIST
#URL_LIST = [
#'https://play.google.com/store/apps/details?id=com.instagram.android',
#'https://play.google.com/store/apps/details?id=com.csam.icici.bank.imobile',
#'https://play.google.com/store/apps/details?id=net.one97.paytm',
#'https://play.google.com/store/apps/details?id=com.appworld.meditation.relax'
#]

# URL_LIST from a file contains url or app_id
URL_LIST = [line.rstrip('\n') for line in open("urls.txt")]

# Do this for each url or app_id in URL_LIST
for url in URL_LIST:
#    get_data(app_id)
    get_data(url)

# File url_records.txt has urls
#with open("url_records.txt") as q:
#    for line in q:
#        url = line
#        get_data(url)

