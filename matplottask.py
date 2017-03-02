import matplotlib.pyplot as plt 

plt.plot(range(10))
plt.show()

times = range(7)
co2 = [250, 265, 272, 260, 300, 320, 389]
temp = [14.1, 15.1, 16.3, 18.1, 17.3, 19.1, 20.2] 
plt.plot(times,co2)
plt.plot(times, co2, 'b--', times, temp, 'r*-')
plt.title("co2 vs time")
plt.ylabel("co2")
plt.xlabel("time(decade)")
plt.show()
