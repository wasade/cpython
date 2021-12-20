#include <time.h>
#include <stdio.h>

int do_test() {
  struct tm tm_works = { .tm_year=117,
                         .tm_mon=4,
                         .tm_mday=26,
                         .tm_hour=15,
                         .tm_min=30,
                         .tm_sec=16,
                         .tm_wday=4,
                         .tm_yday=145,
                         .tm_isdst=-1 };
  
  struct tm tm_fails = { .tm_year=117,
                         .tm_mon=4,
                         .tm_mday=26,
                         .tm_hour=15,
                         .tm_min=30,
                         .tm_sec=16,
                         .tm_wday=4,
                         .tm_yday=145,
                         .tm_isdst=1 };

  time_t works = mktime(&tm_works);
  time_t fails = mktime(&tm_fails);

  if(works == -1) {
      printf("Unexpected failure\n");
  } else {
      if(works == fails) {
          printf("Test passed\n");
      } else {
          printf("Test failed: works=%d; fails=%d\n", (int)works, (int)fails);
          return 1;
      }
  }
  return 0;
}


int main(int argc, char **argv) {
    return do_test();
}
