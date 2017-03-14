#!/usr/bin/python
from __future__ import print_function
import pyinotify
import os
import sys
import subprocess
import time
import requests
mask = pyinotify.IN_CREATE | pyinotify.IN_MODIFY | pyinotify.IN_DELETE | pyinotify.IN_CLOSE_WRITE
def printing(message,event):
       f=open('/var/log/notifier.log','a')
       f.write(time.strftime("%c"))
       f.write("\t %s : %s " %(message , os.path.join(event.path,event.name)))
       f.write("\n")
       f.close()
def curling(ip1):
       r="admin"
       t="password"
       url = "http://"+ip1+"/reload"
       requests.post(url,auth=(r,t))

#def curling2(ip)
#       subprocess.call(["curl","-u admin:password","-X POST",ip+"/reload"])
class notifyme(pyinotify.ProcessEvent):
   def process_IN_CREATE(self,event):
       message = "Creating File  "
       printing (message,event)
       curling("197.97.234.168:8080" )
       curling("197.97.234.165:8080" )

   def process_IN_MODIFY(self,event):
       message = "modifying File  "
       printing (message,event)
       curling("197.97.234.168:8080")
       curling("197.97.234.165:8080")

   def process_IN_DELETE(self,event):
       message = " Deleted File "
       printing (message,event)
       curling("197.97.234.168:8080")
       curling("197.97.234.165:8080")

   def process_IN_CLOSE_WRITE(self,event):
       message = " Write at File "
       printing(message,event)
#       curling("197.97.234.168:8080","197.97.234.165:8080")

wm = pyinotify.WatchManager()
notifier =pyinotify.Notifier(wm , notifyme())

watcher = wm.add_watch ( sys.argv[1] , mask ,rec=True,auto_add=True)

while True:
  try:
   notifier.process_events()
   if notifier.check_events():
      notifier.read_events()
  except KeyboardInterrupt:
     notifier.stop()
     break


