import re
emphasis_pattern = re.compile(r'''
	\* 		# Beginning emphasis tag --an asterisk
	( 		# Begin group for capturing phrase
	[^'*]+	# Capture anything except asterisk
	)		# End group
	\*		# Ending emphasis tag
''', re.VERBOSE) 

print re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello, *world*!')
print re.sub(emphasis_pattern, r'<em>\1</em>', '*Hello*, *world*!')
