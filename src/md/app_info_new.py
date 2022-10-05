# Scrap App Description for an Android app from the PlayStore url. 
# - Urls are taken from input file
# - Page is parsed using beautiful soup after opening from a headless 
#   browser phantomjs

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
#from nltk.collocations import BigramCollocationFinder
#from nltk.stem import PorterStemmer
#from nltk.util import ngrams
import ftfy
import re

# Create bi-grams from App textual description
#def get_bigrams(myString):
#    tokenizer = WordPunctTokenizer()
#    tokens = tokenizer.tokenize(myString)
#    #print("\ntokens: %s" %tokens)
#    # Convert all to lowercase
#    tokens = [x.lower() for x in tokens]
#
#    # Exclude English stopwords
#    stops = set(stopwords.words('english'))
#    # Update stopwords with punctuation and special characters
#    stops.update(['.', '*', ',', '!', '?', '\/', '€™', 's', 'â', '€”', '(', ')', '!)'])
#
#    # Generate bigrams without stopwords
#    bigram = [b for b in nltk.bigrams(tokens) if ((b[0] not in stops and b[1] not in stops) 
#        and (not b[0].isdigit()) 
#        and (not b[1].isdigit()) )]
#    #print(bigram)
#    return bigram

# Format text description for corner cases
def format_des(des):
    res = ""
    for c in des:
        if c == '\n':
            # replace newline with space
            res = res + " "
        elif c == '\'':
            # fix apostrope character
            #res = res + "\\'"
            res = res + ""
        else:
            res = res + str(c)
    return res


# Given category of App, return directory to store information
def get_app_category(category):
  import re

  # input category text to ../apk/apps_CATEGORY/ dir

  if re.search("art", category, re.IGNORECASE):
    cat_dir = 'ART_AND_DESIGN'
  elif re.search("auto", category, re.IGNORECASE):
    cat_dir = 'AUTO_AND_VEHICLES'
  elif re.search("beauty", category, re.IGNORECASE):
    cat_dir = 'BEAUTY'
  elif re.search("books", category, re.IGNORECASE):
    cat_dir = 'BOOKS_AND_REFERENCE'
  elif re.search("business", category, re.IGNORECASE):
    cat_dir = 'BUSINESS'
  elif re.search("comics", category, re.IGNORECASE):
    cat_dir = 'COMICS'
  elif re.search("communication", category, re.IGNORECASE):
    cat_dir = 'COMMUNICATION'
  elif re.search("events", category, re.IGNORECASE):
    cat_dir = 'EVENTS'
  elif re.search("dating", category, re.IGNORECASE):
    cat_dir = 'DATING'
  elif re.search("education", category, re.IGNORECASE):
    cat_dir = 'EDUCATION'
  elif re.search("entertainment", category, re.IGNORECASE):
    cat_dir = 'ENTERTAINMENT'
  elif re.search("house", category, re.IGNORECASE):
    cat_dir = 'HOUSE_AND_HOME'
  elif re.search("finance", category, re.IGNORECASE):
    cat_dir = 'FINANCE'
  elif re.search("food", category, re.IGNORECASE):
    cat_dir = 'FOOD_AND_DRINK'
  elif re.search("health", category, re.IGNORECASE):
    cat_dir = 'HEALTH_AND_FITNESS'
  elif re.search("medical", category, re.IGNORECASE):
    cat_dir = 'MEDICAL'
  elif re.search("libraries", category, re.IGNORECASE):
    cat_dir = 'LIBRARIES_AND_DEMO'
  elif re.search("lifestyle", category, re.IGNORECASE):
    cat_dir = 'LIFESTYLE'
  elif re.search("maps", category, re.IGNORECASE):
    cat_dir = 'MAPS_AND_NAVIGATION'
  elif re.search("personal", category, re.IGNORECASE):
    cat_dir = 'PERSONALIZATION'
  elif re.search("music", category, re.IGNORECASE):
    cat_dir = 'MUSIC_AND_AUDIO'
  elif re.search("news", category, re.IGNORECASE):
    cat_dir = 'NEWS_AND_MAGAZINES'
  elif re.search("parenting", category, re.IGNORECASE):
    cat_dir = 'PARENTING'
  elif re.search("social", category, re.IGNORECASE):
    cat_dir = 'SOCIAL'
  elif re.search("photography", category, re.IGNORECASE):
    cat_dir = 'PHOTOGRAPHY'
  elif re.search("productivity", category, re.IGNORECASE):
    cat_dir = 'PRODUCTIVITY'
  elif re.search("shopping", category, re.IGNORECASE):
    cat_dir = 'SHOPPING'
  elif re.search("video", category, re.IGNORECASE):
    cat_dir = 'VIDEO_PLAYERS'
  elif re.search("sports", category, re.IGNORECASE):
    cat_dir = 'SPORTS'
  elif re.search("tools", category, re.IGNORECASE):
    cat_dir = 'TOOLS'
  elif re.search("travel", category, re.IGNORECASE):
    cat_dir = 'TRAVEL_AND_LOCAL'
  elif re.search("weather", category, re.IGNORECASE):
    cat_dir = 'WEATHER'
  elif re.search("arcade", category, re.IGNORECASE):
    cat_dir = 'GAMES/ARCADE'
  elif re.search("puzzle", category, re.IGNORECASE):
    cat_dir = 'GAMES/PUZZLE'
  elif re.search("card", category, re.IGNORECASE):
    cat_dir = 'GAMES/CARDS'
  elif re.search("casual", category, re.IGNORECASE):
    cat_dir = 'GAMES/CASUAL'
  elif re.search("racing", category, re.IGNORECASE):
    cat_dir = 'GAMES/RACING'
  elif re.search("sports", category, re.IGNORECASE):
    cat_dir = 'GAMES/SPORTS'
  elif re.search("action", category, re.IGNORECASE):
    cat_dir = 'GAMES/ACTION'
  elif re.search("adventure", category, re.IGNORECASE):
    cat_dir = 'GAMES/ADVENTURE'
  elif re.search("board", category, re.IGNORECASE):
    cat_dir = 'GAMES/BOARD'
  elif re.search("casino", category, re.IGNORECASE):
    cat_dir = 'GAMES/CASINO'
  elif re.search("educational", category, re.IGNORECASE):
    cat_dir = 'GAMES/EDUCATIONAL'
  elif re.search("music", category, re.IGNORECASE):
    cat_dir = 'GAMES/MUSIC'
  elif re.search("role", category, re.IGNORECASE):
    cat_dir = 'GAMES/ROLE_PLAYING'
  elif re.search("simulation", category, re.IGNORECASE):
    cat_dir = 'GAMES/SIMULATION'
  elif re.search("strategy", category, re.IGNORECASE):
    cat_dir = 'GAMES/STRATEGY'
  elif re.search("trivia", category, re.IGNORECASE):
    cat_dir = 'GAMES/TRIVIA'
  elif re.search("word", category, re.IGNORECASE):
    cat_dir = 'GAMES/WORD'
  else:
    cat_dir = 'OTHERS'
    print('No match found for category ' + category + '!')
  return cat_dir


# Given App category, find directory to store the json file containing App data
# and move the json file to appropriate place
def move_json_file(category, output_file):
  import re
  import os

  # move output_file .json file to ../json/CATEGORY/ dir

  cat_dir = get_app_category(category)

  # construct command and move the file
  if len(cat_dir) > 4:
    cmd = 'mv ' + output_file + '  ../json/' + cat_dir + '/'
    print(cmd)
    os.system(cmd)
  else:
    print('File ' + output_file + ' of category ' + category + ' not moved!')
  return 0


# Given URL of App page on Play Store, collect information about App, 
# permissions, and prepare statistics to analyze
def get_data(app_id):
    # Import libraries

    import requests

    from bs4 import BeautifulSoup
    import time
    import os

    # Get a headless browser
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    import html2text

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(chrome_options=chrome_options)

    # Convert html to text para, write into an output json file
    h = html2text.HTML2Text()
    h.ignore_links = True

    url = 'https://play.google.com/store/apps/details?id=' + app_id

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html5lib")

    # Output file name
    pac = url.split("=")
    #package = pac[1]
    #output_file = package + ".json"
    package = app_id
    output_file = app_id + ".json"
    f = open(output_file, "w+")

    print("Processing started for app: {0} ".format(package))

    # Extracting the title of the App
    try:
        temp = soup.findAll("h1", attrs={"class":"AHFaub"})
        temp1 = temp[0].findAll("span")
        title = temp1[0].text
    except IndexError:
        print("\n\nIndexError for app_id = %s\n\n" %app_id)
        return
    #temp = soup.findAll("h1", attrs={"itemprop":"name"})
    #print(temp)
    #print(temp[0].text)
    #title = temp[0].text

    f.write("{\n")
    # App Title
    f.write("\"name\" : \"%s\",\n" %title)

    # App URL
    f.write("\"url\" : \"%s\",\n" %url)

    # Package Name
    f.write("\"package\" : \"%s\",\n" %package)

    # Extracting Category
    temp = soup.findAll("a", attrs={"itemprop":"genre"})
    category = temp[0].text

    f.write("\"category\" : \"%s\",\n" %category)

    # Extracting App description   
    description = soup.findAll("meta", attrs={"itemprop":"description"})
    temp = description[0]["content"]

    # Fix mojibakes and character corruption by removing non-ascii characters
    ascii_text = ''.join([i for i in temp if (ord(i) < 128 and i != "\"") ])
    temp = ascii_text

    f.write("\"description\" : \"%s\",\n" %ftfy.fix_encoding(format_des(temp)))

    # get rid of special characters -> ' apostrophe
    temp = re.sub('[\']','',temp)

    # Write bigrams
    ####f.write("\"bigrams\":\"%s\",\n" %get_bigrams(temp))

    # P_t: Write permissions obtained from app description
    desc_permissions = get_desc_perms(temp, package, category)
    f.write("\"desc_perms\" : \"%s\",\n" %desc_permissions)

    ####browser.get(url)
    ####browser.find_element_by_link_text('View details').click()
    # You may need to update this sleep duration 
    # depending upon slow Internet Connection.
    ####time.sleep(2)
    ####html = browser.page_source
    ####soup = BeautifulSoup(html, "html5lib")

    # Extracting App permissions
    ####f.write("\"permissions_text\":{\n")
    ####per_data_all = soup.findAll("div", attrs={"class":"fnLizd"})
    ####for per_data_each in per_data_all[0].findAll("div", attrs={"class":"yk0PFc"}):
    
    ####    per_head = per_data_each.find("span", attrs={"class":"BR7Zgd"}).find("span")
    ####    f.write("\n\"%s\":[" %per_head.text)
    
    ####    per_sub = per_data_each.find("ul", attrs={"class":"l5zUie"})

    ####    for sub in per_sub.findAll("li", attrs={"class":"NLTG4"}):
    ####        permission = sub.find("span")
    ####        f.write("\"%s\"," %permission.text)
    ####    f.seek(0, os.SEEK_END)              
    ####    f.seek(f.tell() - 1, os.SEEK_SET)
    ####    f.truncate()
    ####    f.write("],")   

    ####f.seek(0, os.SEEK_END)              
    ####f.seek(f.tell() - 1, os.SEEK_SET)
    ####f.truncate()
    ####f.write("\n},\n")

    # P_m: Get permissions from AndroidManifest.xml file from inside the App
    # From apk file - we do not know file name yet
    # get apk_dir name, e.g. "../apps_SOCIAL/"
    #apk_dir = "../../../../../apk/apps_" + get_app_category(category)
    apk_dir = "../../../../apk_new/"
    apk_file = apk_dir + package + ".apk"

    from androguard.core.bytecodes.apk import APK
    a = APK(apk_file)
    manifest_permissions = a.get_permissions()
    f.write("\"manifest_perms\" : \"%s\",\n" %manifest_permissions)
    #f.write("%s"  %manifest_permissions)
    #f.write("")

    # P_c: Get permissions from API calls from inside the App
    # Using Androguard provided axplorer permissions mappings for API calls
    from androguard.misc import AnalyzeAPK
    a, d, dx = AnalyzeAPK(apk_file)

    sdk_version = 25
    perm_in_use = []
    for meth, perm in dx.get_permissions(sdk_version):
        for p in perm:
            perm_in_use.append(p)
        #print(perm_in_use)

    perms_with_call = list(set(perm_in_use))
    print("Permissions with API calls: {0}".format(perms_with_call))

    f.write("\"perms_with_call\" : \"%s\" \n" %perms_with_call)
    #f.write("%s"  %perms_with_call)
    #f.write("")

    # EP_Mapper: permission set difference {MANIFEST}-{APP_DESCRIPTION}

    extra_permissions = []
    #print(set(desc_permissions))
    #print(set(manifest_permissions))
    #print(set(manifest_permissions)-set(desc_permissions))
    #<<<<extra_permissions = list(set(manifest_permissions)-set(desc_permissions))

    # EP_MapperDroid: permission set {P_c - P_m} U {P_c - P_t} U {P_m - P_t}
    Pc_minus_Pm = list(set(perms_with_call)-set(manifest_permissions))

    Pc_minus_Pt = list(set(perms_with_call)-set(desc_permissions))

    Pm_minus_Pt = list(set(manifest_permissions)-set(desc_permissions))

    extra_permissions = set(Pc_minus_Pm).union(set(Pc_minus_Pt), set(Pm_minus_Pt))


    # remove 3rd party unknown permissions and some normal permissions
    from exclude_permissions import excl_permissions
    from exclude_permissions import unknown_permissions
    extra_permissions = list(set(extra_permissions)-set(excl_permissions))
    extra_permissions = list(set(extra_permissions)-set(unknown_permissions))

    ignore_permissions =[]
    if 'C2D_MESSAGE' in '\t'.join(manifest_permissions) and 'android.permission.INTERNET' in manifest_permissions:
        p = package + ".permission.C2D_MESSAGE"
        ignore_permissions.append(p)

    extra_permissions = list(set(extra_permissions) - set(ignore_permissions))

    print("extra_permissions = '%s'" %set(extra_permissions))
    print("%d extra permissions for package %s " %(len(set(extra_permissions)), package))
    if len(extra_permissions) == 0:
        print("App is not over-privileged looking at app description!")
    else:
        print("App is over-privileged looking at app description!")

    f.write("\"extra_perms\" : \"%s\",\n" %extra_permissions)
    #f.write("%s"  %extra_permissions)
    #f.write("\n}")


    f.write("}")

    # dump stats in csv
    app_desc_length = len(temp)
    generate_stats_csv(package, category, app_desc_length, perms_with_call, manifest_permissions, desc_permissions, extra_permissions)

    print("Done for app: {0}  under category: {1}".format(package, category))
    f.close()

    # tap apk file, to confirm we checked recently
    cmd = 'touch ' + apk_file
    print(cmd)
    os.system(cmd)

    # Now move file to ../json/ dir
    move_json_file(category, output_file)
    print("----")
    print("\n")


# TODO
# make constants for classes fnLizd, NLTG4, etc. 
# add date modified and version info

# Given text description, gather permissions required from the app description
def get_desc_perms(app_desc, package, category):
    import mysql.connector # for now connect to mysql
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import sent_tokenize
    from nltk.stem.lancaster import LancasterStemmer
    import spacy # for POS tagging
    import re

    # for now connect to testdb in mysql
    mydb = mysql.connector.connect(host="localhost", user="root",
        passwd="nopass", database="testdb")

    my_cursor = mydb.cursor(buffered=True)

    # convert add_desc to lower case for improving pos tagging
    app_desc = app_desc.lower()
    # convert _ to space for actual permissions mentioned in the text
    app_desc = re.sub('[_]',' ', app_desc)

    # desc_perms is permissions from text description app_desc
    desc_perms = []
    permission_list = []

    sent_tokenize_list = sent_tokenize(app_desc)
    lancaster_stemmer = LancasterStemmer()

    special_tokens = ["online", "wifi"]

    # do for every sentence in text app description
    for i in range (len(sent_tokenize_list)):
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(sent_tokenize_list[i])
        noun_list = []
        verb_list = []
        rootnoun_list = []
        rootverb_list = []

        # create root NOUN and VERB lists for each sentence
        # TODO should we see root names or original text?
        for token in doc:
            if token.pos_ == "NOUN":
                #noun_list.append(token.text)
                rt = lancaster_stemmer.stem(token.text)
                if len(rt) > 1:
                  rootnoun_list.append(rt)
                #rootnoun_list.append(lancaster_stemmer.stem(token.text))
            elif token.pos_ == "VERB" :
                #verb_list.append(token.text)
                rt = lancaster_stemmer.stem(token.text)
                if len(rt) > 1:
                  rootverb_list.append(rt)
                #rootverb_list.append(lancaster_stemmer.stem(token.text))
                ## wee need to add dependancy of VERB with other token.pos_
            elif token.text in '\t'.join(special_tokens):
                rootnoun_list.append(lancaster_stemmer.stem(token.text))

        # remove duplicates to reduce pairs and hence comparisions
        rootnoun_list = list(set(rootnoun_list))
        rootverb_list = list(set(rootverb_list))

        # TEMPorary, collect stemmed lists
        dump_file = "listdump_" + category + ".txt"
        #dump_file = "listdump.txt"
        fd = open(dump_file, "a+")
        fd.write("\npackage : '%s'\n" %package)
        for i in range (len(rootverb_list)):
            for j in range (len(rootnoun_list)):
                fd.write("(, , , '%s', '%s', ,)" %(rootverb_list[i], rootnoun_list[j]))
                fd.write("\n")
                #print("(, , , '%s', '%s', ,)" %(rootverb_list[i], rootnoun_list[j]))
        fd.close()

        for i in range (len(rootverb_list)):
            for j in range (len(rootnoun_list)):
                my_cursor.execute("select perms from testdb.pmap where rootverb='%s' AND rootnoun='%s';" %(rootverb_list[i], rootnoun_list[j]))
                res = my_cursor.fetchall()

                y = [x.split(',') for t in res for x in t]
                res1 = [item for sublist in y for item in sublist]

                for k in range(len(res1)):
                    permission_list.append(res1[k].strip(' '))

                if ("download" in rootverb_list[i]) or ("onlin" in rootnoun_list[j]):
                    permission_list.append("android.permission.INTERNET")
                    permission_list.append("android.permission.ACCESS_NETWORK_STATE")

    desc_perms = list(set(permission_list))

    # how many sentences?
    sentences = len(sent_tokenize_list)

    # close db handle
    mydb.close()

    return desc_perms


# Generate statistics in csv to analyze
def generate_stats_csv(package, category, app_desc_length, perms_with_call, manifest_permissions, desc_permissions, extra_permissions):
    # Dump stats
    # row = package | category | app_desc_len | #perms_with_call | #manifest_permissions | #desc_permissions | #extra_permissions | INTERNET (in API call 1) | INTERNET(in manifest 1) | internet (in app_desc 1) |...
    row = []
    # Permissions from Android API calls
    if 'android.permission.INTERNET' in perms_with_call:
        c_INTERNET = '1'
    else:
        c_INTERNET = '0'

    if 'android.permission.ACCESS_NETWORK_STATE' in perms_with_call:
        c_ACCESS_NETWORK_STATE = '1'
    else:
        c_ACCESS_NETWORK_STATE = '0'

    if 'android.permission.ACCESS_WIFI_STATE' in perms_with_call:
        c_ACCESS_WIFI_STATE = '1'
    else:
        c_ACCESS_WIFI_STATE = '0'

    if 'android.permission.READ_PHONE_STATE' in perms_with_call:
        c_READ_PHONE_STATE = '1'
    else:
        c_READ_PHONE_STATE = '0'

    if 'android.permission.CALL_PHONE' in perms_with_call:
        c_CALL_PHONE = '1'
    else:
        c_CALL_PHONE = '0'

    if 'android.permission.PROCESS_OUTGOING_CALLS' in perms_with_call:
        c_PROCESS_OUTGOING_CALLS = '1'
    else:
        c_PROCESS_OUTGOING_CALLS = '0'

    if 'android.permission.READ_PHONE_NUMBERS' in perms_with_call:
        c_READ_PHONE_NUMBERS = '1'
    else:
        c_READ_PHONE_NUMBERS = '0'

    if 'android.permission.READ_CONTACTS' in perms_with_call:
        c_READ_CONTACTS = '1'
    else:
        c_READ_CONTACTS = '0'

    if 'android.permission.READ_CALENDAR' in perms_with_call:
        c_READ_CALENDAR = '1'
    else:
        c_READ_CALENDAR = '0'

    if 'android.permission.READ_CALL_LOG' in perms_with_call:
        c_READ_CALL_LOG = '1'
    else:
        c_READ_CALL_LOG = '0'

    if 'android.permission.WRITE_CONTACTS' in perms_with_call:
        c_WRITE_CONTACTS = '1'
    else:
        c_WRITE_CONTACTS = '0'

    if 'android.permission.WRITE_CALENDAR' in perms_with_call:
        c_WRITE_CALENDAR = '1'
    else:
        c_WRITE_CALENDAR = '0'

    if 'android.permission.WRITE_CALL_LOG' in perms_with_call:
        c_WRITE_CALL_LOG = '1'
    else:
        c_WRITE_CALL_LOG = '0'

    if 'android.permission.GET_ACCOUNTS' in perms_with_call:
        c_GET_ACCOUNTS = '1'
    else:
        c_GET_ACCOUNTS = '0'

    if 'android.permission.READ_EXTERNAL_STORAGE' in perms_with_call:
        c_READ_EXTERNAL_STORAGE = '1'
    else:
        c_READ_EXTERNAL_STORAGE = '0'

    if 'android.permission.WRITE_EXTERNAL_STORAGE' in perms_with_call:
        c_WRITE_EXTERNAL_STORAGE = '1'
    else:
        c_WRITE_EXTERNAL_STORAGE = '0'

    if 'android.permission.CAMERA' in perms_with_call:
        c_CAMERA = '1'
    else:
        c_CAMERA = '0'

    if 'com.android.vending.BILLING' in perms_with_call:
        c_BILLING = '1'
    else:
        c_BILLING = '0'

    if 'SYSTEM_ALERT_WINDOW' in '\t'.join(perms_with_call):
        c_SYSTEM_ALERT_WINDOW = '1'
    else:
        c_SYSTEM_ALERT_WINDOW = '0'

    if 'android.permission.READ_SMS' in perms_with_call:
        c_READ_SMS = '1'
    else:
        c_READ_SMS = '0'

    if 'android.permission.SEND_SMS' in perms_with_call:
        c_SEND_SMS = '1'
    else:
        c_SEND_SMS = '0'

    if 'android.permission.RECORD_AUDIO' in perms_with_call:
        c_RECORD_AUDIO = '1'
    else:
        c_RECORD_AUDIO = '0'

    if 'android.permission.ACCESS_FINE_LOCATION' in perms_with_call:
        c_ACCESS_FINE_LOCATION = '1'
    else:
        c_ACCESS_FINE_LOCATION = '0'

    if 'android.permission.ACCESS_COARSE_LOCATION' in perms_with_call:
        c_ACCESS_COARSE_LOCATION = '1'
    else:
        c_ACCESS_COARSE_LOCATION = '0'


    # Permissions in MANIFEST file
    if 'android.permission.INTERNET' in manifest_permissions:
        m_INTERNET = '1'
    else:
        m_INTERNET = '0'

    if 'android.permission.ACCESS_NETWORK_STATE' in manifest_permissions:
        m_ACCESS_NETWORK_STATE = '1'
    else:
        m_ACCESS_NETWORK_STATE = '0'

    if 'android.permission.ACCESS_WIFI_STATE' in manifest_permissions:
        m_ACCESS_WIFI_STATE = '1'
    else:
        m_ACCESS_WIFI_STATE = '0'

    if 'android.permission.READ_PHONE_STATE' in manifest_permissions:
        m_READ_PHONE_STATE = '1'
    else:
        m_READ_PHONE_STATE = '0'

    if 'android.permission.CALL_PHONE' in manifest_permissions:
        m_CALL_PHONE = '1'
    else:
        m_CALL_PHONE = '0'

    if 'android.permission.PROCESS_OUTGOING_CALLS' in manifest_permissions:
        m_PROCESS_OUTGOING_CALLS = '1'
    else:
        m_PROCESS_OUTGOING_CALLS = '0'

    if 'android.permission.READ_PHONE_NUMBERS' in manifest_permissions:
        m_READ_PHONE_NUMBERS = '1'
    else:
        m_READ_PHONE_NUMBERS = '0'

    if 'android.permission.READ_CONTACTS' in manifest_permissions:
        m_READ_CONTACTS = '1'
    else:
        m_READ_CONTACTS = '0'

    if 'android.permission.READ_CALENDAR' in manifest_permissions:
        m_READ_CALENDAR = '1'
    else:
        m_READ_CALENDAR = '0'

    if 'android.permission.READ_CALL_LOG' in manifest_permissions:
        m_READ_CALL_LOG = '1'
    else:
        m_READ_CALL_LOG = '0'

    if 'android.permission.WRITE_CONTACTS' in manifest_permissions:
        m_WRITE_CONTACTS = '1'
    else:
        m_WRITE_CONTACTS = '0'

    if 'android.permission.WRITE_CALENDAR' in manifest_permissions:
        m_WRITE_CALENDAR = '1'
    else:
        m_WRITE_CALENDAR = '0'

    if 'android.permission.WRITE_CALL_LOG' in manifest_permissions:
        m_WRITE_CALL_LOG = '1'
    else:
        m_WRITE_CALL_LOG = '0'

    if 'android.permission.GET_ACCOUNTS' in manifest_permissions:
        m_GET_ACCOUNTS = '1'
    else:
        m_GET_ACCOUNTS = '0'

    if 'android.permission.READ_EXTERNAL_STORAGE' in manifest_permissions:
        m_READ_EXTERNAL_STORAGE = '1'
    else:
        m_READ_EXTERNAL_STORAGE = '0'

    if 'android.permission.WRITE_EXTERNAL_STORAGE' in manifest_permissions:
        m_WRITE_EXTERNAL_STORAGE = '1'
    else:
        m_WRITE_EXTERNAL_STORAGE = '0'

    if 'android.permission.CAMERA' in manifest_permissions:
        m_CAMERA = '1'
    else:
        m_CAMERA = '0'

    if 'com.android.vending.BILLING' in manifest_permissions:
        m_BILLING = '1'
    else:
        m_BILLING = '0'

    if 'SYSTEM_ALERT_WINDOW' in '\t'.join(manifest_permissions):
        m_SYSTEM_ALERT_WINDOW = '1'
    else:
        m_SYSTEM_ALERT_WINDOW = '0'

    if 'android.permission.READ_SMS' in manifest_permissions:
        m_READ_SMS = '1'
    else:
        m_READ_SMS = '0'

    if 'android.permission.SEND_SMS' in manifest_permissions:
        m_SEND_SMS = '1'
    else:
        m_SEND_SMS = '0'

    if 'android.permission.RECORD_AUDIO' in manifest_permissions:
        m_RECORD_AUDIO = '1'
    else:
        m_RECORD_AUDIO = '0'

    if 'android.permission.ACCESS_FINE_LOCATION' in manifest_permissions:
        m_ACCESS_FINE_LOCATION = '1'
    else:
        m_ACCESS_FINE_LOCATION = '0'

    if 'android.permission.ACCESS_COARSE_LOCATION' in manifest_permissions:
        m_ACCESS_COARSE_LOCATION = '1'
    else:
        m_ACCESS_COARSE_LOCATION = '0'

    #if 'C2D_MESSAGE' in '\t'.join(manifest_permissions):
    #    C2D_MESSAGE = '1'
    #else:
    #    C2D_MESSAGE = '0'

    # Permissions from application description
    if 'android.permission.INTERNET' in desc_permissions:
        internet = '1'
    else:
        internet = '0'

    if 'android.permission.ACCESS_NETWORK_STATE' in desc_permissions:
        access_network_state = '1'
    else:
        access_network_state = '0'

    if 'android.permission.ACCESS_WIFI_STATE' in desc_permissions:
        access_wifi_state = '1'
    else:
        access_wifi_state = '0'

    if 'android.permission.READ_PHONE_STATE' in desc_permissions:
        read_phone_state = '1'
    else:
        read_phone_state = '0'

    if 'android.permission.CALL_PHONE' in desc_permissions:
        call_phone = '1'
    else:
        call_phone = '0'

    if 'android.permission.PROCESS_OUTGOING_CALLS' in desc_permissions:
        process_outgoing_calls = '1'
    else:
        process_outgoing_calls = '0'

    if 'android.permission.READ_PHONE_NUMBERS' in desc_permissions:
        read_phone_numbers = '1'
    else:
        read_phone_numbers = '0'

    if 'android.permission.READ_CONTACTS' in desc_permissions:
        read_contacts = '1'
    else:
        read_contacts = '0'

    if 'android.permission.READ_CALENDAR' in desc_permissions:
        read_calendar = '1'
    else:
        read_calendar = '0'

    if 'android.permission.READ_CALL_LOG' in desc_permissions:
        read_call_log = '1'
    else:
        read_call_log = '0'

    if 'android.permission.READ_CONTACTS' in desc_permissions:
        read_contacts = '1'
    else:
        read_contacts = '0'

    if 'android.permission.WRITE_CONTACTS' in desc_permissions:
        write_contacts = '1'
    else:
        write_contacts = '0'

    if 'android.permission.WRITE_CALENDAR' in desc_permissions:
        write_calendar = '1'
    else:
        write_calendar = '0'

    if 'android.permission.WRITE_CALL_LOG' in desc_permissions:
        write_call_log = '1'
    else:
        write_call_log = '0'

    if 'android.permission.GET_ACCOUNTS' in desc_permissions:
        get_accounts = '1'
    else:
        get_accounts = '0'

    if 'android.permission.READ_EXTERNAL_STORAGE' in desc_permissions:
        read_external_storage = '1'
    else:
        read_external_storage = '0'

    if 'android.permission.WRITE_EXTERNAL_STORAGE' in desc_permissions:
        write_external_storage = '1'
    else:
        write_external_storage = '0'

    if 'android.permission.CAMERA' in desc_permissions:
        camera = '1'
    else:
        camera = '0'

    if 'com.android.vending.BILLING' in desc_permissions:
        billing = '1'
    else:
        billing = '0'

    if 'SYSTEM_ALERT_WINDOW' in '\t'.join(desc_permissions):
        system_alert_window = '1'
    else:
        system_alert_window = '0'

    if 'android.permission.READ_SMS' in desc_permissions:
        read_sms = '1'
    else:
        read_sms = '0'

    if 'android.permission.SEND_SMS' in desc_permissions:
        send_sms = '1'
    else:
        send_sms = '0'

    if 'android.permission.RECORD_AUDIO' in desc_permissions:
        record_audio = '1'
    else:
        record_audio = '0'

    if 'android.permission.ACCESS_FINE_LOCATION' in desc_permissions:
        access_fine_location = '1'
    else:
        access_fine_location = '0'

    if 'android.permission.ACCESS_COARSE_LOCATION' in desc_permissions:
        access_coarse_location = '1'
    else:
        access_coarse_location = '0'

    #if 'C2D_MESSAGE' in '\t'.join(desc_permissions):
    #    c2d_message = '1'
    #else:
    #    c2d_message = '0'

    acperms = len(perms_with_call)
    mperms = len(manifest_permissions)
    descperms = len(desc_permissions)
    extperms = len(extra_permissions)

    row = [package, category.upper(), app_desc_length,
        acperms, mperms, descperms, extperms,
        c_INTERNET, m_INTERNET, internet, classify_stats(c_INTERNET, m_INTERNET, internet),
        c_ACCESS_NETWORK_STATE, m_ACCESS_NETWORK_STATE, access_network_state, classify_stats(c_ACCESS_NETWORK_STATE, m_ACCESS_NETWORK_STATE, access_network_state),
        c_ACCESS_WIFI_STATE, m_ACCESS_WIFI_STATE, access_wifi_state, classify_stats(c_ACCESS_WIFI_STATE, m_ACCESS_WIFI_STATE, access_wifi_state), #not using
        c_READ_PHONE_STATE, m_READ_PHONE_STATE, read_phone_state, classify_stats(c_READ_PHONE_STATE, m_READ_PHONE_STATE, read_phone_state),
        c_CALL_PHONE, m_CALL_PHONE, call_phone, classify_stats(c_CALL_PHONE, m_CALL_PHONE, call_phone),
        c_READ_PHONE_NUMBERS, m_READ_PHONE_NUMBERS, read_phone_numbers, classify_stats(c_READ_PHONE_NUMBERS, m_READ_PHONE_NUMBERS, read_phone_numbers), #not using
        c_READ_CONTACTS, m_READ_CONTACTS, read_contacts, classify_stats(c_READ_CONTACTS, m_READ_CONTACTS, read_contacts),
        c_READ_CALENDAR, m_READ_CALENDAR, read_calendar, classify_stats(c_READ_CALENDAR, m_READ_CALENDAR, read_calendar),
        c_READ_CALL_LOG, m_READ_CALL_LOG, read_call_log, classify_stats(c_READ_CALL_LOG, m_READ_CALL_LOG, read_call_log),
        c_WRITE_CONTACTS, m_WRITE_CONTACTS, write_contacts, classify_stats(c_WRITE_CONTACTS, m_WRITE_CONTACTS, write_contacts),
        c_WRITE_CALENDAR, m_WRITE_CALENDAR, write_calendar, classify_stats(c_WRITE_CALENDAR, m_WRITE_CALENDAR, write_calendar),
        c_WRITE_CALL_LOG, m_WRITE_CALL_LOG, write_call_log, classify_stats(c_WRITE_CALL_LOG, m_WRITE_CALL_LOG, write_call_log),
        c_GET_ACCOUNTS, m_GET_ACCOUNTS, get_accounts, classify_stats(c_GET_ACCOUNTS, m_GET_ACCOUNTS, get_accounts),
        c_READ_EXTERNAL_STORAGE, m_READ_EXTERNAL_STORAGE, read_external_storage, classify_stats(c_READ_EXTERNAL_STORAGE, m_READ_EXTERNAL_STORAGE, read_external_storage),
        c_WRITE_EXTERNAL_STORAGE, m_WRITE_EXTERNAL_STORAGE, write_external_storage, classify_stats(c_WRITE_EXTERNAL_STORAGE, m_WRITE_EXTERNAL_STORAGE, write_external_storage),
        c_CAMERA, m_CAMERA, camera, classify_stats(c_CAMERA, m_CAMERA, camera),
        c_BILLING, m_BILLING, billing, classify_stats(c_BILLING, m_BILLING, billing), #not using
        c_SYSTEM_ALERT_WINDOW, m_SYSTEM_ALERT_WINDOW, system_alert_window, classify_stats(c_SYSTEM_ALERT_WINDOW, m_SYSTEM_ALERT_WINDOW, system_alert_window),
        c_READ_SMS, m_READ_SMS, read_sms, classify_stats(c_READ_SMS, m_READ_SMS, read_sms),
        c_RECORD_AUDIO, m_RECORD_AUDIO, record_audio, classify_stats(c_RECORD_AUDIO, m_RECORD_AUDIO, record_audio),
        c_ACCESS_FINE_LOCATION, m_ACCESS_FINE_LOCATION, access_fine_location, classify_stats(c_ACCESS_FINE_LOCATION, m_ACCESS_FINE_LOCATION, access_fine_location),
        c_ACCESS_COARSE_LOCATION, m_ACCESS_COARSE_LOCATION, access_coarse_location, classify_stats(c_ACCESS_COARSE_LOCATION, m_ACCESS_COARSE_LOCATION, access_coarse_location),
        c_PROCESS_OUTGOING_CALLS, m_PROCESS_OUTGOING_CALLS, process_outgoing_calls, classify_stats(c_PROCESS_OUTGOING_CALLS, m_PROCESS_OUTGOING_CALLS, process_outgoing_calls), #not using
        c_SEND_SMS, m_SEND_SMS, send_sms, classify_stats(c_SEND_SMS, m_SEND_SMS, send_sms)
        ]
    #    C2D_MESSAGE, C2D_MESSAGE, c2d_message, classify_stats(C2D_MESSAGE, c2d_message)]
    print(row)

    import csv
    csv_file_name = "stats_" + category + ".csv"
    #csv_file_name = "stats.csv"
    with open(csv_file_name, 'a+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(row)
    csv_file.close()

## Given two values a and b (1 or 0) find out TP, FN, FP, TN
# Given three values c, a, b (1 or 0) find out TP, FN, FP, TN
#def classify_stats(a,b):
def classify_stats(c, a, b):
    # c = permission found in api call (1) or not found (0)
    # a = permission found in manifest (1) or not found (0)
    # b = permission found in description (1) or not found (0)
    res = ""
    # MapperDroid 2x2x2 possibilities
    if c == '1' and a == '1' and b == '1':
        res = "TP" # found in calls, manifest and app_desc -- all good
    elif c == '1' and a == '1' and b == '0':
        res = "FN" # found in calls and manifest and not found in app_desc -- missed
    elif c == '1' and a == '0' and b == '1':
        res = "TP" # found in calls and not found in manifest and found in app_desc -- still good
    elif c == '1' and a == '0' and b == '0':
        res = "FN" # found in calls and not found in manifest and not found in app_desc -- still missed
    elif c == '0' and a == '1' and b == '1':
        res = "TP" # not found in calls and found in manifest and found in app_desc -- still good
    elif c == '0' and a == '1' and b == '0':
        res = "FN" # not found in calls and found in manifest and not found in app_desc -- still missed
    elif c == '0' and a == '0' and b == '1':
        res = "FP" # not found in calls and not found in manifest and found in app_desc -- imprecision
    elif c == '0' and a == '0' and b == '0':
        res = "TN" # not found in calls and not found in manifest and not found in app_desc -- all good
    """
    # Mapper 2x2 possibilities
    if a == '1':
        if b == '1':
            res = "TP" # found in both manifest and app_desc -- good
        elif b == '0': 
            res = "FN" # not found in app_desc and found in manifest -- missed
    elif a == '0':
        if b == '1':
            res = "FP" # found in app_desc and not found in manifest -- imprecision
        elif b == '0':
            res = "TN" # not found in both manifest and app_desc -- good
    """
    return res

