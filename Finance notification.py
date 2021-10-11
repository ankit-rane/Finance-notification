#For being financially sound, one needs to stay updated with his/her bills, and they need to be paid at the right time.
#this program pushes a notification every month so that the user gets reminded of paying the bills.
import time
from plyer import notification # installed plyer by giving the command pip install plyer.
if __name__=="__main__": # it helps in encapsulation
       while True: 
           # running a loop to push notification after a given time.
        notification.notify(title = "**Please pay your bills on time!",
         message = "Kindly pay your SIPs and Bills on time, so that you can fromulate a better budget",
          timeout=10 
          # the amount of time the notfication would be displayed
         )
        time.sleep(60*60*24*30) #defines the time after which the notification would be displayed, here one month
   
#used pythonw.exe .\main.py