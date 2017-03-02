a = set([0,1,2,3,4,5])
b = set([2,4,6,8])

print a.union(b)

print a.intersection(b)

band=["mel", "geri", "victoria", "mel", "emma"]
counts = {}
for member in band: 
    if member not in counts: 
        counts[member]=1
    else:
        counts[member] +=1

for member in counts: 
    print member, counts[member]

if {}: 
    print "hi"

d = {"maggie": "uk", "ronnie": "usa"}

print d.items()
print d.keys()
print d.values()

print d.get("maggie","nowhere")
print d.get("ronnie","nowhere")
print d.get("ringo","nowhere")
res = d.setdefault("mikhail", "ussr")
print res, d["mikhail"]
