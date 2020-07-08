# If we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .
#
# Find the sum of all the multiples of  or  below .
#
# Input Format
#
# First line contains  that denotes the number of test cases. This is followed by  lines, each containing an integer, .
#
# Constraints
#
# Output Format
#
# For each test case, print an integer that denotes the sum of all the multiples of  or  below .
#
# Sample Input 0
#
# 2
# 10
# 100
# Sample Output 0
#
# 23
# 2318
# Explanation 0
#
# For , if we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .
#
# Similarly for , we get .
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())-1
    print((3*((n//3)*((n//3)+1)//2)+(5*((n//5)*((n//5)+1)//2)-(15*((n//15)*((n//15)+1)//2)))))
