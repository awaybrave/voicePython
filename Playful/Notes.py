#Flexibility: Be willing and prepared to revise and change every respect
#of your program.

#Prototyping: Write a simply program to prove your initial ideas. 

#Configuration files

#Making global variables as constants (trade-off: less modular)
#use ConfigParser to read a formatted config file like the following
"""
[numbers]
pi: 3.1415926

[messages]
greeting: Welcome to the area calculation program!
question: Please enter the radius:
result_message: The area is
"""

from ConfigParser import ConfigParser

CONFIGFILE = "config.txt"
config = ConfigParser()
config.read(CONFIGFILE) #hook the config file

print config.get('messages', 'greeting') #read by key works
radius = input(config.get('messages', 'question') + ' ')

print config.get('messages', 'result_message'),
print config.getfloat('numbers', 'pi') * radius ** 2

#Logging(finding bugs)
#logging is import but make sure that flushing the buffer logs into
#the log file or use logging module
import logging

logging.basicConfig(level=logging.INFO, filename='mylog.log')

logging.info('Starting program')

logging.info('Trying to divide 1 by 0')

try:
	print 1 / 0
	logging.info('Division successed!')
except ZeroDivisionError:
	logging.info('Could not divide a number by 0')
