// Objective
// This challenge will let you learn about bitwise operators in C.
//
// Inside the CPU, mathematical operations like addition, subtraction, multiplication and division are done in bit-level. To perform bit-level operations in C programming, bitwise operators are used which are explained below.
//
// Bitwise AND operator & The output of bitwise AND is 1 if the corresponding bits of two operands is 1. If either bit of an operand is 0, the result of corresponding bit is evaluated to 0. It is denoted by &.
//
// Bitwise OR operator | The output of bitwise OR is 1 if at least one corresponding bit of two operands is 1. It is denoted by |.
//
// Bitwise XOR (exclusive OR) operator ^ The result of bitwise XOR operator is 1 if the corresponding bits of two operands are opposite. It is denoted by .
//
// For example, for integers 3 and 5,
//
// 3 = 00000011 (In Binary)
// 5 = 00000101 (In Binary)
//
// AND operation        OR operation        XOR operation
//   00000011             00000011            00000011
// & 00000101           | 00000101          ^ 00000101
//   ________             ________            ________
//   00000001  = 1        00000111  = 7       00000110  = 6
// Task
// Given set , find:
//
// the maximum value of  which is less than a given integer , where  and  (where ) are two integers from set .
//
// the maximum value of  which is less than a given integer , where  and  (where ) are two integers from set .
//
// the maximum value of  which is less than a given integer , where  and  (where ) are two integers from set .
//
// Input Format
//
// The only line contains  space-separated integers,  and , respectively.
//
// Constraints
//
// Output Format
//
// The first line of output contains the maximum possible value of .
//
// The second line of output contains the maximum possible value of .
//
// The second line of output contains the maximum possible value of .
//
// Sample Input 0
//
// 5 4
// Sample Output 0
//
// 2
// 3
// 3
// Explanation 0
//
//
//
// All possible values of  and  are:
//
//
// The maximum possible value of  that is also  is , so we print  on first line.
//
// The maximum possible value of  that is also  is , so we print  on second line.
//
// The maximum possible value of  that is also  is , so we print  on third line.
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
    int maxAND = 0, maxOR = 0, maxXOR = 0,i,j,x,y,z;
    for(i=1;i<=n;i++) {
        for(j=i+1;j<=n;j++) {
            x=i&j;
            y=i|j;
            z=i^j;
            if(x>maxAND && x<k) {
                maxAND = x;
            }
            if(y>maxOR && y<k) {
                maxOR = y;
            }
            if(z>maxXOR && z<k) {
                maxXOR = z;
            }
        }
    }
    printf("%d\n",maxAND);
    printf("%d\n",maxOR);
    printf("%d",maxXOR);
}

int main() {
    int n, k;

    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
    return 0;
}
