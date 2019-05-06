#include<iostream>
#include "unistd.h"
using namespace std;
int main()
{
  for(;;sleep(400),system("taskkill /f /im python.exe"));
  //for(;;sleep(4),system("taskkill /f /im python.exe"));
  return 0;
}