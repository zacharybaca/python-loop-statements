# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

"""Task 1: The Selective DJ
Loop through a slice of the genres list from the previous question and print out the genres. Use slicing to create a sublist of genres from the second to the fourth track."""

sub_set = genres[1:]

for i in range(len(sub_set)):
    print(f'Track #: {i + 1} Genre: {sub_set[i]}')

"""Task 2: The One-Liner Band with List Comprehensions
Use a list comprehension to create a new list that contains each genre with the word "Music" appended to it. Print this new list."""

new_list = [genres[i] + ' Music' for i in range(len(genres))]
print(new_list)

"""Task 3: Numerical Beats with range
Write a loop using range() to print out a countdown from 10 to 1, followed by the message "The beat drops now!"."""

for i in range(10, -1, -1):
    if i >= 1:
        print(i)
    else:
        print("The beat drops now!")
