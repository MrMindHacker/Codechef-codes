
// A Dynamic Programming based solution for 0-1 Knapsack problem
#include<stdio.h>
#include "iostream"
#include "math.h"

// A utility function that returns maximum of two integers
int max(int a, int b, int &count){
  if (a > b)
    return a;
  else if (a == b){
    count++;
    return a;
  }
  else
    return b;
  }

// Returns the maximum value that can be put in a knapsack of capacity W
int knapSack(int W, int val[], int n, int &count)
{
   int i, w;
   int K[n+1][W+1];

   // Build table K[][] in bottom up manner
   for (i = 0; i <= n; i++)
   {
       for (w = 0; w <= W; w++)
       {
           if (i==0 || w==0)
               K[i][w] = 0;
           else
                 K[i][w] = max(val[i-1] + K[i-1][w-1],  K[i-1][w], count);
       }
   }

   return count;
}

int main()
{
    int t;
    std::cin >> t;

    for (size_t i = 0; i < t; i++) {
      int N, K, count = 0;
      std::cin >> N >> K;
      int val[N];

      for (size_t j = 0; j < N; j++) {
              std::cin >> val[j];
      }

      int  W = K;

      //int n = sizeof(val)/sizeof(val[0]);
      knapSack(W, val, N, count);
      std::cout << pow(2, count) << '\n';
      return 0;
    }
}
