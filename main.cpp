#include <iostream>
#include <cassert>
#include <chrono>
#include <thread>

// RDTSC functions
extern "C" size_t RDTSCStart();
extern "C" size_t RDTSCStop();

int main() {
  auto before = RDTSCStart();
  std::this_thread::sleep_for(std::chrono::nanoseconds(10));
  auto after = RDTSCStop();
  assert(after > before &&
     "After RDTSC read value > than before RDTSC reading.");
  std::cout << "Difference of 10 ns in TSC: " << after - before << std::endl;
  return 0;
}

