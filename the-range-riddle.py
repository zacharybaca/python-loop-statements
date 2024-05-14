"""Task 1: Your Mood Today
Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through the days of the week and for each day, randomly select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.

Example Outcome: An example output could be "On Wednesday, you were feeling happy." "On Thursday you were feeling sad." """

import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for day in range(len(days_of_week)):
    print(f'On {days_of_week[day]}, I was feeling {random.choice(moods)}')

