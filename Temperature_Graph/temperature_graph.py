import matplotlib.pyplot as plt

# Temperature readings for each day of the week
temperatures = [20, 22, 19, 23, 21, 24, 20]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

plt.plot(days, temperatures, marker='*', linestyle='dotted', color='green', markersize=9, linewidth=2)
plt.title('Temperature Readings Over a Week')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True, color='gray', linestyle='dotted', linewidth=0.5)
plt.show()