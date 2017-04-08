#Python3 script that looks up a mac address in seconds
import sys

if len(sys.argv) < 2:
    sys.exit("Usage: 'python3 mac_lookup.py [MAC ADDRESS]'")

else:
    address = sys.argv[1]

#The list the website data we scrape will be added to
website_data = []

try:
    from bs4 import BeautifulSoup
except ImportError as msg:
    print(msg)
    sys.exit("This tool requires the 'bs4' module to run. Install it using 'pip3 install bs4'")

try:
    import requests
except ImportError as msg:
    print(msg)
    sys.exit("This tool requires the 'requests' module in order to run. Install it using: 'pip3 install requests'")

#Checking if the length of the entered address is valid
if len(address) != 17:
    sys.exit("Invalid MAC! Please provide a MAC address in this format: ff:ff:ff:ff:ff:ff")

print(" ")

#Cutting the entered string, so we can add it to the URL we use for lookup
#11:11:11:11:11:11 would become 111111111111, as the website only accepts this format in their URL for lookup
raw_string = address[:2]+address[3:5]+address[6:8]+address[9:11]+address[12:14]+address[15:17]

#Downloading the website source, which we will use to scrape later on
r = requests.get("http://www.miniwebtool.com/mac-address-lookup/?s="+raw_string)

#Making the source usable by BeautifulSoup
soup = BeautifulSoup(r.content, "html.parser")

#Scraping the website data we need and appending it to the list 'website_data'
try:
    for item in soup.find_all("td"):
        website_data.append(item)

except:
    sys.exit("[*] No manufacturer found!")

#Assigning the variable 'tag_format_manufacturer' to the third value in the 'website_data' list
try:
    tag_format_manufacturer = str(website_data[3])

except IndexError:
    sys.exit("[*] No manufacturer found!")

length_tag = len(tag_format_manufacturer)

cut_count = length_tag - 5

#Cutting the tag that contains the manufacturer name, so that we can view it without the annoying html tags
manufacturer = tag_format_manufacturer[4:cut_count]

#Returning the name of the manufacturer(if we found it)
print("Your manufacturer is: "+str(manufacturer))

print(" ")
