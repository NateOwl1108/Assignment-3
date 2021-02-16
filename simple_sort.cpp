# include <iostream>
# include <cassert>

int main()
{
    int array[5]{ 30, 50, 20, 10, 40 };

    // your code here
    bool sorted = false;
    while (sorted == false) 
    {
      sorted = true;
      for(int i=0; i < 5;i++)  
      {  
        int pos = array[i];  
        int next = array[i+1];
        if(pos > next)
        {
          array[i] = next;  
          array[i+1] = pos; 
          sorted = false;
        }       
      }  
    }

    std::cout << "Testing...\n";

    assert(array[0]==10);
    assert(array[1]==20);
    assert(array[2]==30);
    assert(array[3]==40);
    assert(array[4]==50);

    std::cout << "Succeeded";

    return 0;
}