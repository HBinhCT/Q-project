"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
test_cases = int(input())
for _ in range(test_cases):
    nx2, k = map(int, input().strip().split())
    lists = list(map(int, input().strip().split()))
    if nx2 == 2:
        print(0)
        print('Chick magnet Jhool!')
    else:
        lists.sort()
        pairs = [lists[i] + lists[nx2 - i - 1] for i in range(0, nx2 // 2)]
        ans = max(pairs) - min(pairs)
        print(ans)
        if ans > k:
            print('No more girlfriends!')
        elif ans == k:
            print('Lucky chap!')
        else:
            print('Chick magnet Jhool!')
