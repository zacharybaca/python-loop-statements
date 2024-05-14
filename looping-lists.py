# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']


"""Task 1: The for Loop DJ Set
Using the provided genres list, write a for loop that prints out each genre with a custom message. Extend this task by adding a counter that displays the number of the track before the genre."""

for i in range(len(genres)):
    print(f'Genre Number: {i + 1} Genre: {genres[i]}')

"""Task 2: The Remix Artist with while
Convert the for loop from Task 1 into a while loop. Ensure it performs the same function but also includes a condition to stop the loop if a certain genre is played for instance Hip-hop."""

i = 0

while i < len(genres):
    print(f'Genre Number: {i + 1} Genre: {genres[i]}')
    if genres[i] == 'Hip-hop':
        break
    i += 1

"""Task 3: Light Show Technician Loop
Using the range() function, loop through the genres list by index. For each genre, print out the track number and a message that the light show is ready. Modify the loop to skip a genre if it's not suitable for the light show, for instance Classical genre."""

for i in range(0, len(genres)):
    if genres[i] == 'Classical':
        continue
    print(f'Track #: {i} is playing, and the light show is ready')

