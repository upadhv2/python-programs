file = open("/home/vishal/sample", 'r')
#Read the file line by line
#for line in file:
#    print line

# read enite file into a string
str = file.read()
print str
# read first 5 chars
print file.read(10)

