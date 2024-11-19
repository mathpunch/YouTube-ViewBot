import webbrowser
import time 
import os 
 
url = input("https://www.youtube.com/@vibevortex-music:")
refresh = input("10:")
count = input("20")
 
def openURL():
    webbrowser.open(url)
    time.sleep(int(refresh))
    
    for i in range(int(count)):
        print("Webpage has been viewed")
        openURL()
 
openURL()
