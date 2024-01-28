import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv(r'Workplace Video Project\athlete_events.csv')

# Introduction
print("Welcome to our journey through the history of the Olympics!")

# Part 1: Most awarded country and sport
most_awarded = df.groupby(['NOC', 'Sport'])['Medal'].count().idxmax()
us_gold_wins = df[(df['NOC'] == 'USA') & (df['Medal'] == 'Gold')]['Medal'].count()
print(f"\nLet's start by looking at the most successful country and sport combination in the history of the Olympics. It turns out to be {most_awarded}!")
print(f"\nThe United States has won {us_gold_wins} medals in the history of the Olympics!")

# Part 3: Jamaica's sprinters
jamaica_medals = df[(df['NOC'] == 'JAM') & (df['Medal'] == 'Gold')].groupby('Season')['Medal'].count()
print(f"\nNow, let's turn our attention to Jamaica. The number of medals they won in each season is:\n{jamaica_medals}")

# Part 3: Lowest participation
lowest_participants = df.groupby(['Year', 'Sport'])['ID'].nunique().idxmin()
print(f"\nInterestingly, the year and sport with the lowest number of participants is {lowest_participants}. Let's explore why that might be.")

# Part 4: Oldest gold medalist
oldest_athlete = df[df['Medal'] == 'Gold'].sort_values('Age', ascending=False).iloc[0][['Name', 'Sport']]
print(f"\nDid you know? The oldest athlete to win a gold medal is {oldest_athlete['Name']} in the sport {oldest_athlete['Sport']}!")

# Part 5: Frequent Olympic hosts
multiple_hosts = df.groupby('City')['Games'].nunique()
multiple_hosts = multiple_hosts[multiple_hosts > 1].index.tolist()
print(f"\nThere are a few countries that have had the honor of hosting the Olympics more than once. They are: {', '.join(multiple_hosts)}.")

# Part 6: Evolution of the Olympics
olympics = df.groupby('Year').agg({'Event': 'nunique', 'ID': 'nunique', 'Medal': 'count'})

# Line graph
plt.figure(figsize=(15, 10))
plt.plot(olympics.index, olympics['Event'], label='Events')
plt.plot(olympics.index, olympics['ID'], label='Participants')
plt.plot(olympics.index, olympics['Medal'], label='Medals')
plt.legend()
plt.title('Evolution of the Olympics Over Time')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()


# Bar chart
labels = olympics.index
events = olympics['Event']
participants = olympics['ID']
medals = olympics['Medal']

x = np.arange(len(labels))  # the label locations
width = 0.3  # the width of the bars

fig, ax = plt.subplots(figsize=(15, 10))  # Increase the size of the plot
rects1 = ax.bar(x - width, events, width, label='Events')
rects2 = ax.bar(x, participants, width, label='Participants')
rects3 = ax.bar(x + width, medals, width, label='Medals')

# Add some text for labels, title and custom x-axis tick labels to fix overlappings.
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.set_title('Comparison of the Last Two Olympics')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)  # Rotate the x-axis labels
ax.legend()

fig.tight_layout()
plt.show()

# Conclusion
print("\nAnd that's the end of our journey through the history of the Olympics. Thank you for joining me!")
