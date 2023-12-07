import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 1, 6, 8]

plt.plot(x_values, y_values, marker='o', linestyle='-')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Простой ломаный график')

plt.show()