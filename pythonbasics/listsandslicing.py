mylist= [1,2,3,4,5]
print mylist[1]
print mylist[-2]
print mylist [:]
print mylist[2:5]

one_to_ten = [range(1,10)]
one_to_ten[0]=10
one_to_ten.append(11)
one_to_ten.extend([12,13,14])

forward=[]
backward=[]

values=["a","b","c"]
for item in values:
    forward.append(item)
    backward.append(item)
print forward
print backward 

forward.reverse()
if forward == backward is True :
    print True
else:
    print False 

countries=["uk","usa","uk","uae"]
dir(countries)
print countries.count("uk")
