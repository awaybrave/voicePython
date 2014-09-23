def lines(file):
	for line in file: yield line
	yield '\n'

def blocks(file):
	#@ param file:
	block = []
	for line in lines(file):
		# strip return '' when it meets an empty string.
		if line.strip():
			block.append(line)
		#when it comes to an empty line, yield the exsisting block
		elif block:
			yield ''.join(block).strip()
			block = []
