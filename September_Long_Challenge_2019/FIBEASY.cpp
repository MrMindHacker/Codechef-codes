#include "iostream"
#include "math.h"

int main(int argc, char const *argv[]) {
  int list[60];
  for (size_t i = 0; i < 60; i++) {
    if (i == 0)
      list[i] = 0;
    else if (i == 1)
      list[i] = 1;
    else {
      list[i] = (list[i-1] + list[i-2]) % 10;
    }
  }

  long long int t;
  std::cin >> t;

  for (size_t j = 0; j < t; j++) {

  long long int q;

  // a = 1000000000000000000;
  std::cin >> q;

  long long int p = (int)log2(q);
  p = ((long long int)pow(2, p))%60;

  int ans = list[p-1];
  std::cout << ans << '\n';
}
  return 0;
}
