# bing-wallpaper-for-mac
Bing wallpaper for mac

This program is written in python specifically for OSX and tested on Yosemite 10.10.2 running python 2.7.9 and 3.4.3

###Notes

-  The app calls the python scripts on execution.
-  In order to save space, the script assumes that *only 1 image* is kept in the ~/Pictures/bing-wallpaper folder.
-  Place all the files into a single folder. Here it is in the Applications folder within the users home directory - ~/Applications/Bing\ Wallpaper
	- You can change the location in the script
	- `homeFolder = os.path.expanduser("~")`
	- `pictureLocation = homeFolder + "/Pictures/bing-wallpaper"`
	- `appLocation = homeFolder + "/Applications/Bing\ Wallpaper/Bing.app"`
-  Add the CheckBingStatus.app to your startup item and set it to hidden like so.

![Image](http://i.imgur.com/4zDj2AE.png)

###The App
- The application is split in the following ways
	- The checker app checks to ensure there is internet connectivity, then checks to see if an image file already exists in the ~/Pictures/bing-wallpaper folder.
		- If there are file, it will check to see if the file was created today.
			- If the file was created today, stop and don't do anything
			- Else, run the app to download the wallpaper.
		- If there are no file, run the app to download the wallpaper
	- The wallpaper downloader app ensures that you only have the latest wallpaper in your folder. It ensures to delete all files from that folder before downloading the new wallpaper.

###Caveat
~~I have noticed that the Automator App files do not run the first time you download it to you machine. You will need to open the file with Automator and run it once, save and close. You should be good after that.~~
With the dmg file, this may be fixed. Awaiting user input to confirm.

###Thanks
Feel free to share you comments and thoughts. I am new to github.
