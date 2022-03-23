# write your code here
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
    print(friends)
