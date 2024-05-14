"""Task 1: Your Mood Tracker
Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it.

Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"""

import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
times_of_day = ["Morning", "Afternoon", "Evening"]


for day in range(len(days_of_week)):
    for time in range(len(times_of_day)):
        print(f'On {days_of_week[day]} {times_of_day[time]} I was {random.choice(moods)}')