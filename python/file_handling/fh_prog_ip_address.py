
d = {}
fname = "/home/vishal/ipaddr"

with open(fname, 'r') as fd:
    for line in fd:
        key,value = line.split()
        d[key] = value

print d
