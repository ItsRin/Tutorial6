import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
data = pd.read_csv('loki-bot-analysis.csv')

# Setting the aesthetic style of the plots
sns.set(style="whitegrid")

# Create a subplot structure
fig, axes = plt.subplots(3, 2, figsize=(14, 12))

# Plotting Payload vs Source IP
sns.scatterplot(data=data, x='payload', y='source', ax=axes[0, 0])
axes[0, 0].set_title('Payload vs Source IP')

# Plotting Payload vs Destination IP
sns.scatterplot(data=data, x='payload', y='destination', ax=axes[0, 1])
axes[0, 1].set_title('Payload vs Destination IP')

# Plotting Payload vs Protocol
sns.scatterplot(data=data, x='payload', y='protocol', ax=axes[1, 0])
axes[1, 0].set_title('Payload vs Protocol')

# Plotting Source IP vs Destination IP
sns.scatterplot(data=data, x='source', y='destination', ax=axes[1, 1])
axes[1, 1].set_title('Source IP vs Destination IP')

# Plotting Source IP vs Protocol
sns.scatterplot(data=data, x='source', y='protocol', ax=axes[2, 0])
axes[2, 0].set_title('Source IP vs Protocol')

# Plotting Destination IP vs Protocol
sns.scatterplot(data=data, x='destination', y='protocol', ax=axes[2, 1])
axes[2, 1].set_title('Destination IP vs Protocol')

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()

# Counting occurrences of each unique protocol
protocol_counts = data['protocol'].value_counts()
print("Protocol Occurrences:\n", protocol_counts)
