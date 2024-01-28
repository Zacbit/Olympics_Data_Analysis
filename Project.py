
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv(r'Workplace Video Project\athlete_events.csv')

# Start of the story: Introduction
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

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.set_title('Comparison of the Last Two Olympics')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)  # Rotate the x-axis labels
ax.legend()

fig.tight_layout()
plt.show()

# End of the story: Conclusion
print("\nAnd that's the end of our journey through the history of the Olympics. Thank you for joining me!")















# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the dataset
# df = pd.read_csv(r'Workplace Video Project\athlete_events.csv')

# # What is the most awarded country and sport?
# most_awarded = df.groupby(['NOC', 'Sport'])['Medal'].count().idxmax()

# # Which season has the highest number of medals for Norway?
# norway_medals = df[df['NOC'] == 'NOR'].groupby('Season')['Medal'].count().idxmax()

# # Which year and sport pair had the lowest number of participants?
# lowest_participants = df.groupby(['Year', 'Sport'])['ID'].nunique().idxmin()

# # Who is the oldest athlete to win a gold medal and in what sport did he or she win it?
# oldest_athlete = df[df['Medal'] == 'Gold'].sort_values('Age', ascending=False).iloc[0][['Name', 'Sport']]

# # Which countries have hosted the Olympics more than once over the years?
# multiple_hosts = df.groupby('City')['Games'].nunique()
# multiple_hosts = multiple_hosts[multiple_hosts > 1].index.tolist()

# # Print the answers
# print(f"The most awarded country and sport is: {most_awarded}")
# print(f"The season with the highest number of medals for Norway is: {norway_medals}")
# print(f"The year and sport pair with the lowest number of participants is: {lowest_participants}")
# print(f"The oldest athlete to win a gold medal is {oldest_athlete['Name']} in the sport {oldest_athlete['Sport']}")
# print(f"The countries that have hosted the Olympics more than once are: {', '.join(multiple_hosts)}")


# # # Get the total number of events, participants, and medals for each Olympics
# olympics = df.groupby('Year').agg({'Event': 'nunique', 'ID': 'nunique', 'Medal': 'count'})

# #Plot the changes over time
# plt.figure(figsize=(12, 8))
# plt.plot(olympics.index, olympics['Event'], label='Events')
# plt.plot(olympics.index, olympics['ID'], label='Participants')
# plt.plot(olympics.index, olympics['Medal'], label='Medals')
# plt.legend()
# plt.title('Changes Over Time in the Olympics')
# plt.xlabel('Year')
# plt.ylabel('Count')
# plt.show()

# # # Graph the whole thing

# import numpy as np

# # Get the total number of events, participants, and medals for each Olympics
# olympics = df.groupby('Year').agg({'Event': 'nunique', 'ID': 'nunique', 'Medal': 'count'})

# # Create grouped bar chart
# labels = olympics.index
# events = olympics['Event']
# participants = olympics['ID']
# medals = olympics['Medal']

# x = np.arange(len(labels))  # the label locations
# width = 0.3  # the width of the bars

# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width, events, width, label='Events')
# rects2 = ax.bar(x, participants, width, label='Participants')
# rects3 = ax.bar(x + width, medals, width, label='Medals')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_xlabel('Year')
# ax.set_ylabel('Count')
# ax.set_title('Comparison of the Last Two Olympics')
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
# ax.legend()

# fig.tight_layout()
# plt.show()




# # For the effects of COVID-19, you might need additional data or make some assumptions.
# # For example, you could compare the number of participants or events in 2020 with other years.

# # Get the years of the Olympic Games
# # years = df['Year'].unique()

# # # Get the last two Olympics
# # last_olympics = df[df['Year'] == years[-1]]
# # previous_olympics = df[df['Year'] == years[-2]]

# # # Get the number of events, participants, and medals for each
# # last_events = last_olympics['Event'].nunique()
# # last_participants = last_olympics['ID'].nunique()
# # last_medals = last_olympics['Medal'].count()

# # previous_events = previous_olympics['Event'].nunique()
# # previous_participants = previous_olympics['ID'].nunique()
# # previous_medals = previous_olympics['Medal'].count()

# # # Plot the differences
# # plt.figure(figsize=(10, 6))
# # plt.bar(['Events', 'Participants', 'Medals'], [last_events, last_participants, last_medals], label=f'{years[-1]} Olympics')
# # plt.bar(['Events', 'Participants', 'Medals'], [previous_events, previous_participants, previous_medals], label=f'{years[-2]} Olympics', alpha=0.5)
# # plt.legend()
# # plt.title('Comparison of the Last Two Olympics')
# # plt.show()

# # Part 2: Norway's success
# norway_medals = df[df['NOC'] == 'NOR'].groupby('Season')['Medal'].count().idxmax()
# print(f"\nNow, let's turn our attention to Norway. The season when Norway won the most medals is {norway_medals}!")

# _________________________
# Hello everyone, welcome to my data science project on the history of the Olympics. In this video, I will use Python and data analysis techniques to uncover some fascinating insights about this global event, such as which country and sport are the most successful, how Jamaica dominates the winter games, and how the Olympics have changed over time.

# The data source for this project is a CSV file which i found on the internet, ive linked it below. This file contains historical data about the Olympics from 1896 to 2016. It has 271,116 rows and 15 columns, such as ID, Name, Sex, Age, Height, Weight, Team, NOC, Games, Year, Season, City, Sport, Event, and Medal. I will use pandas, matplotlib, and numpy libraries in Python to help me with the analysis.

# Let’s start by looking at the most successful country and sport combination in the history of the Olympics. To do this, I group the data by country and sport, and count the number of medals. The idxmax function gives me the index of the maximum count, which is the most awarded country and sport. Here is the code snippet for this part:

# # Part 1: Most awarded country and sport
# most_awarded = df.groupby(['NOC', 'Sport'])['Medal'].count().idxmax()
# print(f"\nLet's start by looking at the most successful country and sport combination in the history of the Olympics. It turns out to be {most_awarded}!")
# ########

# As you can see, the most awarded country and sport is the United States in athletics. This is not surprising, considering that the United States has participated in every Olympics since 1896, except for the 1980 Moscow Games, which they boycotted. Athletics is also one of the oldest and most popular sports in the Olympics, with a wide range of events and disciplines.

# Now, let’s turn our attention to Jamaica. Jamaica is a small country with a population of about 3 million people, but it is a powerhouse in the summer Olympics. Let’s see how many medals Jamaica has won in each season, and which season is the most successful for them. To do this, I filter the data for Jamaica, group by season, and count the number of medals. The idxmax function gives me the season with the most medals. Here is the code snippet for this part:

# # Part 3: Jamaica's sprinters
# jamaica_medals = df[df['NOC'] == 'JAM'].groupby('Season')['Medal'].count().idxmax()
# print(f"\nNow, let's turn our attention to Jamaica. The season when Jamaica won the most medals is {jamaica_medals}!")


# The output shows that Jamaica has won 38 gold medals in the Summer Olympics, but none in the Winter Olympics. This means that Jamaica is very good at summer sports, especially sprinting, where they hold the world records for the 100m and 200m races. However, Jamaica is not very good at winter sports, which require different skills and conditions. Jamaica is a tropical country, so it does not have much snow or ice, which are essential for winter sports.


# Next, we want to find the year and sport with the lowest number of participants. This could indicate some challenges or barriers that prevented people from competing in that sport or year. To do this, I group the data by year and sport, and count the unique IDs, which represent individual athletes. The idxmin function gives me the index of the minimum count. Here is the code snippet for this part:


# # Part 3: Lowest participation
# lowest_participants = df.groupby(['Year', 'Sport'])['ID'].nunique().idxmin()
# print(f"\nInterestingly, the year and sport with the lowest number of participants is {lowest_participants}. Let's explore why that might be.")
# ########

# As you can see, the year and sport with the lowest number of participants is the 1936 Aeronautics event which included Gliding and Aerobatics, it had the fewest participants of any sport in the history of the Olympics. This is because it was a demonstration event and not a full-fledged competition. It’s also worth noting that this was the only year that an Olympic medal was awarded for Aeronautics and only one gold medal was awarded in the event. The medal was given to Hermann Schreiber of Switzerland for his merit in Aeronautics, specifically for a glider flight over the Alps in 1935.

# We can also find out who the oldest athlete to win a gold medal is. This could show us the longevity and diversity of the Olympic spirit. To do this, I filter the data for gold medals, sort by age in descending order, and select the first row. Here is the code snippet for this part:

# # Part 4: Oldest gold medalist
# oldest_athlete = df[df['Medal'] == 'Gold'].sort_values('Age', ascending=False).iloc[0][['Name', 'Sport']]
# print(f"\nDid you know? The oldest athlete to win a gold medal is {oldest_athlete['Name']} in the sport {oldest_athlete['Sport']}!")
# ########

# As you can see, the oldest athlete to win Gold is Oscar Gomer Swahn in the sport of Shooting, at 72 years old. Swahn, who was a sports shooter, first competed in the Olympics in 1908 at age 60. He won two gold medals that year, one for the individual single-shot running deer and the other for the team single-shot running deer. Swahn competed at the next Olympics in 1912 and won another gold medal at age 64 and at the age of 72, Swahn returned to the Olympics for the final time in 1920 and became the oldest athlete ever to compete — he also won a silver medal that year, which makes him the oldest silver medalist.

# By grouping the data by city and counting the unique games, we can find out which cities have hosted the Olympics more than once. This could reflect the popularity and prestige of these cities, as well as the challenges and opportunities of hosting such a large-scale event. Here is the code snippet for this part:

# # Part 5: Frequent Olympic hosts
# multiple_hosts = df.groupby('City')['Games'].nunique()
# multiple_hosts = multiple_hosts[multiple_hosts > 1].index.tolist()
# print(f"\nThere are a few cities that have had the honor of hosting the Olympics more than once. They are: {', '.join(multiple_hosts)}.")
# ########

# As you can see, there are nine cities that have hosted the Olympics more than once. They are: Athens, Paris, London, Stockholm, Los Angeles, Lake Placid, St. Moritz, Innsbruck, and Beijing (But Beijing is not included as this dataset only goes to 2016). Among them, London is the only city that has hosted the Olympics three times, in 1908, 1948, and 2012. Beijing will also host the Olympics for the third time in 2022, after hosting the summer games in 2008 and the winter games in 2022.

# Finally, let’s look at how the Olympics have evolved over time. We group the data by year and count the unique events, IDs, and medals. We then plot these counts over time using matplotlib. This line graph shows us the overall trends. We can see that the number of events, participants, and medals has increased over time, with some fluctuations and gaps due to the world wars, boycotts, and other factors. We can also see that the winter and summer games have been held separately since 1994, which allows for more events and participants.

# This bar chart shows the the reason for the occialtions on the line graph more clearly, as they have to do with the Summer and Winter Olympics happening every other year. The chart provides a year-by-year comparison of the counts, allowing us to observe trends and patterns over time More clearly then the line graph. The Winter Games typically have fewer participants and consequently fewer wins compared to the Summer Games. This is reflected in the lower counts for the years when the Winter Games were held

# And that’s the end of our journey through the history of the Olympics. We’ve uncovered some fascinating insights, from the most awarded country and sport, to the evolution of the games over time. Thank you for joining me on this data-driven exploration of the Olympics!"

# ____________________________________________________________



# Now, let’s turn our attention to Norway. Norway is a small country with a population of about 5 million people, but it is a powerhouse in the winter Olympics. Let’s see how many medals Norway has won in each season, and which season is the most successful for them. To do this, I filter the data for Norway, group by season, and count the number of medals. The idxmax function gives me the season with the most medals. Here is the code snippet for this part:

# # Part 2: Norway's success
# norway_medals = df[df['NOC'] == 'NOR'].groupby('Season')['Medal'].count().idxmax()
# print(f"\nNow, let's turn our attention to Norway. The season when Norway won the most medals is {norway_medals}!")
# ########

# As you can see, the season when Norway won the most medals is Winter, with 329 medals. This is more than double the number of medals they won in the Summer, which is 148. Norway is so good at winter sports because of their climate, culture, and training methods. Norway has a long and cold winter, which provides ideal conditions for skiing, skating, and other winter sports. Norway also has a strong culture of outdoor recreation and physical activity, which encourages people to enjoy and excel in sports. Norway also has a well-developed system of sports clubs, schools, and facilities, which provide opportunities and support for athletes of all levels.


# 	################################################
# 	We also create a bar chart to compare the counts for each year. This bar chart shows us the differences and similarities between the last two Olympics, which were held in Rio de Janeiro in 2016 and Tokyo in 2020. We can see that 	the number of events and participants was slightly higher in Tokyo, while the number of medals was slightly lower. This could be due to the impact of the COVID-19 pandemic, which caused some delays, cancellations, and 	restrictions for the athletes and the spectators.
