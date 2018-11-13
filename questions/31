#include <iostream>
using namespace std;

int main(void) {
  int count = 1;
  for (int one = 0; one <= 200; ++one) {
    for (int two = 0; two <=100; ++two) {
      for (int five = 0; five <= 40; ++five) {
        for (int ten = 0; ten <= 20; ++ten) {
          for (int twenty = 0; twenty <= 10; ++twenty) {
            for (int fifty = 0; fifty <= 4; ++fifty) {
              for (int hundred = 0; hundred <= 2; ++ hundred) {
                int sum = 1*one + 2*two + 5*five + 10*ten + 20*twenty + 50*fifty + 100*hundred;
                if (sum == 200) ++count;
              }
            }
          }
        }
      }
    }
  }
  cout << count << endl;
}
