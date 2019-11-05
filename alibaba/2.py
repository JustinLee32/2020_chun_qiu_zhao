m=int(raw_input())
n=int(raw_input())
k=int(raw_input())
#def factorial function
def factorial(n):
	if n==0 or n==1:
		return 1
	else:
		return (n*factorial(n-1))
#record the number of ways		
ans=0
#record the factorial of 1 to max(m,n,k)
dic={}
for i in range(0,max(m,n,k)):
	dic[i]=factorial(i)

#how many bowls have wanzi 
for i in range(2,min(k+1,m+n+1)):
	#the number of bowls of rouwan C(m-1,j-1)
	for j in range(1,i):
		ans+=(dic[m-1]/(dic[m-j]*dic[j-1]))*(dic[n-1]/(dic[n-i+j]*dic[i-j-1]))

print(ans%10000)

