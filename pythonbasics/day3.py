t=(1,)
print t[-1]

l = range(100,201)
tup = tuple(l)
print tup[0] , tup[-1]

mylist=[23,"hi",2.4e-10]
for (count,item) in enumerate(mylist):
    print count, item

(first,middle,last)=mylist 
print first,middle,last
(first,middle,last)=(middle,last,first)

with open("weathertask.csv", "r") as reader: 
    data = reader.read()
print data

with open("weathertask.csv" ,"r") as reader: 
    line=reader.readline()
    while line:
        print line
        line = reader.readline()
print "It's over"

with open("weathertask.csv") as reader: 
    header = reader.readline() #ignore
    rain=[]
    for line in reader.readlines(): 
        r=line.strip().split(",")[-1]
        r = float(r)
        rain.append(r)

print rain

with open("myrain.txt", "w") as writer: 
     for r in rain:  
        writer.write(str(r)+"\n")

import struct 
bin_data = struct.pack("bbbb", 123, 12, 45, 34)
with open("mybinary.dat", "wb") as writer: 
    for
