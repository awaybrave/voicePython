import fileinput, random
# randomly select the line
fortunes = list(fileinput.input())
print random.choice(fortunes)
