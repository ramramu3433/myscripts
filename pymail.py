import gmail
import re
import datetime
import sys
def minutedelta(delta):
    if delta<0:
       return 60+delta 
    else:
       return delta

def hourdelta(hour,minute):
    if minute<0:
       return  hour-1
    else:
       return hour

def getstat():
   now= datetime.datetime.now()
   sender2=sys.argv[1]
   print sys.argv[1]
   password="janakiram@123"
   getmail=gmail.login("ramramu.jr",password)
   if ( getmail.logged_in):
       #print "hi" 
       #print datetime.datetime(now.year,now.month,now.day,hourdelta(now.hour,now.minute-43),minutedelta(now.minute-43),now.second)
       t=getmail.inbox().mail(unread=True,after=datetime.datetime(now.year,now.month,now.day,hourdelta(now.hour,now.minute-2),minutedelta(now.minute-2),now.second),sender=sender2)
       #print len(t)
       for i in range(len(t)):
           t[i].read() 
           t[i].fetch()
           #print t[i].body
           pattern= re.compile("Enable USB ")
           if  pattern.search(t[i].subject):
               pat=re.compile("yes")
               if  pat.search(t[i].body):
                   print "yes" 
                   return 1
               #t[i].delete()     
               else: 
                   print "no" 
                   return 0
                        

if(__name__=="__main__"):
   getstat()
