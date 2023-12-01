

function_string = """
import matplotlib.pyplot as plt

# Sample data
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]

# Create a line chart
plt.plot(x_values, y_values, label='Line Chart')

# Add labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Simple Line Chart')

# Add a legend
plt.legend()

# Show the plot
plt.show()

"""

exec(function_string)


