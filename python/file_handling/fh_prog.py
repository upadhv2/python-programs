import json 

d = {}
fname = "/home/vishal/vupadhye"
with open(fname, "r") as fd:
    for line in fd:
        words = line.split()
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

print json.dumps(d)

        
