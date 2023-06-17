let num=121
var count=0;
const num1=num.toString()
const c=num1.length
var b=num%10
for(let i=1;i<=c;i++)
{
    if(num%b==0)
    {
        count++;
    }
    b=num1[i-1+1]  
}
console.log(count);
