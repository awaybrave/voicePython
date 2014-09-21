import logging

logging.basicConfig(level=logging.INFO, filename='mylog.log')

logging.info('Starting program')

logging.info('Trying to divide 1 by 0')

#try statement redirect the error stream from stderr(terminal) to
#the program workflow
try:
	print 1 / 0
	logging.info('Division successed!')
except ZeroDivisionError:
	logging.info('Could not divide a number by 0')
