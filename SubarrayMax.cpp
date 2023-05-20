 
    int A[9]={1, 2, 3, 1, 4, 5, 2, 3 ,6};
    int n=9;

    int i,j;
   
    int x=0, y=1, z=2;
   
    while(z<n)
    {
        cout<<A[x]<<A[y]<<A[z]<<endl;
       
       
if(A[x]>A[y])
{
    if(A[x]>A[z])
    {
        cout<<A[x]<<endl;
    }
    else
    {
        cout<<A[z]<<endl;
    }
   
}
else if(A[y]>A[z])
{
    cout<<A[y]<<endl;
}
else
cout<<A[z]<<endl;

        x++,y++,z++;
       
    }
      
