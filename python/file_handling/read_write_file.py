# Open/read/write/append operations on a file

file = open("/home/vishal/doesnotexist",'w+') # read and write a file, create a file if it does not exists.
message = "This is first line\n"
file.write(message)
message = "This is first line\n"
file.write(message)
message = "This is first line\n"
file.write(message)
print file.read()
file.close()

