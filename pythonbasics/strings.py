s = "I love to write python" 
for l in s: 
    print l
    print s[5]
    print s[-1]

print len(s)
print s[0]
print s[0][0]
print s[0][0][0]

split_s = s.split()
print split_s

for word in split_s: 
    if word.find("i") > -1:
        print "I found 'i' in: {}".format(word)

something= "completely different"
print dir(something)

something.count("t")
something.find("plete")
something.split("e")

thing2 = something.replace("different","silly")
print thing2

    
