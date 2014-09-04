import sys                               # 1
#sys.argv[0] is the file name of the executed script. # 2
args = sys.argv[1:]                      # 3
args.reverse()                           # 4
print args                               # 5
