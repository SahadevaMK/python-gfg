
int main()
{
  int  A[6] = {900, 940, 950, 1100, 1500, 1800};          ////minimum number of platforms
  int B[6] = {910, 1200, 1120, 1130, 1900, 2000};

// int A[3] = {900, 1100, 1235};
// int B[3] = {1000, 1200, 1240};
    int i=0;
     int j=0;
     int count=0;
   
    while(i<5  && j<6)
    {
          if(B[j]>A[i+1])
      {
        count++;
      }
      
      i++;
      j++;
        
    }
    
    cout<<count<<endl;
    
    return 0;
}
