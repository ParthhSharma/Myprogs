// In this problem, you need to print the pattern of the following form containing the numbers from  to .
//
//                             4 4 4 4 4 4 4
//                             4 3 3 3 3 3 4
//                             4 3 2 2 2 3 4
//                             4 3 2 1 2 3 4
//                             4 3 2 2 2 3 4
//                             4 3 3 3 3 3 4
//                             4 4 4 4 4 4 4
// Input Format
//
// The input will contain a single integer .
//
// Constraints
//
//
// Output Format
//
// Print the pattern mentioned in the problem statement.
//
// Sample Input 0
//
// 2
// Sample Output 0
//
// 2 2 2
// 2 1 2
// 2 2 2
// Sample Input 1
//
// 5
// Sample Output 1
//
// 5 5 5 5 5 5 5 5 5
// 5 4 4 4 4 4 4 4 5
// 5 4 3 3 3 3 3 4 5
// 5 4 3 2 2 2 3 4 5
// 5 4 3 2 1 2 3 4 5
// 5 4 3 2 2 2 3 4 5
// 5 4 3 3 3 3 3 4 5
// 5 4 4 4 4 4 4 4 5
// 5 5 5 5 5 5 5 5 5
// Sample Input 2
//
// 7
// Sample Output 2
//
// 7 7 7 7 7 7 7 7 7 7 7 7 7
// 7 6 6 6 6 6 6 6 6 6 6 6 7
// 7 6 5 5 5 5 5 5 5 5 5 6 7
// 7 6 5 4 4 4 4 4 4 4 5 6 7
// 7 6 5 4 3 3 3 3 3 4 5 6 7
// 7 6 5 4 3 2 2 2 3 4 5 6 7
// 7 6 5 4 3 2 1 2 3 4 5 6 7
// 7 6 5 4 3 2 2 2 3 4 5 6 7
// 7 6 5 4 3 3 3 3 3 4 5 6 7
// 7 6 5 4 4 4 4 4 4 4 5 6 7
// 7 6 5 5 5 5 5 5 5 5 5 6 7
// 7 6 6 6 6 6 6 6 6 6 6 6 7
// 7 7 7 7 7 7 7 7 7 7 7 7 7
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    int n,i,j;
    scanf("%d", &n);
    int len = 2*n-1;
    int arr[len][len];
    int start = 0;
    int end = len-1;
      while(n!=0) {
          for(i=start;i<=end;i++) {
              for(j=start;j<=end;j++) {
                  if(i==start||j==start||i==end||j==end) {
                  arr[i][j] = n;
                  }
              }
          }
          start++;
          end--;
          n--;
      }
    for(i=0;i<len;i++) {
        for(j=0;j<len;j++) {
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}
