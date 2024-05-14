"""Task 1: Loop Condition Exploration
Write a while loop with a condition that will never be false (an infinite loop). Inside the loop, print a statement. Then, use a break statement to exit the loop after 5 iterations. """

i = 1
while 10 < 20:
    print(f'{i} iteration')
    i += 1
    if i == 6:
        break


"""Task 2: Conditional Exit
Modify the infinite loop from Task 1 to include a condition that will eventually be true and remove the break statement. The loop should terminate naturally once the condition is met. """


i = 1
while i <= 5:
    print(f'{i} iteration')
    i += 1
   