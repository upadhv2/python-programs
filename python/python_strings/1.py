str = raw_input("Enter the string: ")
# Method 1 - loop in reverse way
s = ""
for i in range(len(str),0,-1):
    s += str[i-1]
print s

# Method 2 - reverse slicing

print s[::-1]

# Method 3 - append chars in revers order
ts = "Happy New Year"
rs = ""
for x in ts:
    rs = x + rs
print rs
