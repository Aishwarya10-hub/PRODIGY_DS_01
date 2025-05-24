import matplotlib.pyplot as plt

# Dataset
age_groups = ["0-14", "15-24", "25-59", "60+"]
population_percent = [25, 18, 48, 9]

# Histogram (bar chart style, since data is categorical)
plt.figure(figsize=(8, 6))
plt.bar(age_groups, population_percent, color='skyblue', edgecolor='black')

# Chart details
plt.title("Population Distribution by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Percentage of Population")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.ylim(0, max(population_percent) + 10)

# Show the plot
plt.show()
