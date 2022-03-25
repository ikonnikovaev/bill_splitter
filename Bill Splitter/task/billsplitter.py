# write your code here
import random


print('Enter the number of friends joining (including you):')
n = int(input())
if n <= 0:
    print('No one is joining for the party')
else:
    names = []
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(n):
        names.append(input())
    friends = dict.fromkeys(names, 0)
    #print(friends)
    print('Enter the total bill value:')
    total_bill = float(input())
    lucky = None
    print('Do you want to use the "Who is lucky?" feature? '
          'Write Yes/No:')
    answer = input()
    if answer == "Yes":
        lucky = random.choice(names)
        print(f'{lucky} is the lucky one!')
        n -= 1
    else:
        print('No one is going to be lucky')
    split_value = round(total_bill / n, 2)
    for name in names:
        if name != lucky:
            friends[name] = split_value
    print(friends)
