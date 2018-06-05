import json

#Try with python3
try:
    from urllib.request import urlopen, urlretrieve
    from urllib.request import urlretrieve

#Else try python2
except:
    from urllib2 import urlopen
    from urllib import urlretrieve

from os import path
from subprocess import call
from time import sleep
import os
import sqlite3
import glob

# User home folder
homeFolder = path.expanduser("~")

# Save pictures to a folder
pictureLocation = homeFolder + "/Pictures/bing-wallpaper/"

# Get current picture
currentPicture = glob.glob(pictureLocation + "*.jpg")[0]

# DB File
db_file = homeFolder + "/Library/Application Support/Dock/desktoppicture.db"


def main():
    # #######Defining variables#######

    # URL in json format for latest wallpaper

    url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"

    getHighRes = 1 # Manually change the resolution in the url to 1920x1200. Change to 0 if url breaks.

    # Get json response from bing.com
    response = urlopen(url)

    # Trying python 3
    try:
        output = response.readall().decode('utf-8')

    # Else trying python2
    except:
           output = response.read()

    # Get json output
    data = json.loads(output)
    #print(data)
    #print(response)
    #print(data["images"][0]["url"])

    # Form image url from json
    output_url = "https://www.bing.com" + data["images"][0]["url"]

    # Form 1920x1200 image from above url
    output_url_highres = output_url.replace("1080", "1200")

    # If higher resolution is preferred(default)
    if getHighRes == 1:

        # Use try block to catch any failure in getting the high res image
        try:
            process_url(output_url_highres)

        except:
            process_url(output_url)

    else:
        process_url(output_url)


def process_url(image_url):
    if not check_url(image_url) == 1:
        # Get the filename of the new file from the url
        redirect_url = urlopen(image_url).geturl()
        if image_url != redirect_url:
            image_url = image_url.replace("1200", "1080")
        filename = pictureLocation + image_url.split('/')[-1]

        print(currentPicture)
        print(filename)

        # Retrieve the image from the web and save it to desired location
        if not currentPicture == filename:
                os.remove(currentPicture)
                print(image_url)
                req = urlretrieve(image_url, filename)
                connection = sqlite3.connect(db_file)
                cursor = connection.cursor()
                format_str = """UPDATE data SET VALUE = "{filename}";"""
                sql_command = format_str.format(filename=filename)
                result = cursor.execute(sql_command)
                connection.commit()
                os.system('killall Dock')
        else:
                print("Already there")
                # Save the file path + filename to the output variable
                bingImage = path.abspath(filename)
    else:
        raise Exception('bad url')


def check_url(image_url):
    conn = urlopen(image_url)
    if not conn.getcode() == 200:
        return 1
main()
