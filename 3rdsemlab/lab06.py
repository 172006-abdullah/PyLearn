import matplotlib.pyplot as plt
age = [10, 20, 30, 40, 50]
weight = [35, 45, 55, 65, 75]
# Plot scatter diagram
plt.scatter(age, weight, color='red', marker='o')
plt.title("Disadvantages of Smoking with Increasing Age & Weight")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.grid(True)
plt.show()
