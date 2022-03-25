# write your code here
import random

friends = {}
print('Enter the number of friends joining (including you):')
n = int(input())
if n <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(n):
        name = input()
        friends[name] = 0
    print('Enter the total bill value:')
    total_bill = float(input())
    print('Do you want to use the "Who is lucky?" feature? '
          'Write Yes/No:')
    answer = input()
    if answer == "Yes":
        lucky = random.choice(list(friends.keys()))
        print(f'{lucky} is the lucky one!')
    else:
        print('No one is going to be lucky')
    split_value = round(total_bill / n, 2)
    for name in friends:
        friends[name] = split_value
    # print(friends)
