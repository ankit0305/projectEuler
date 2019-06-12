low=1
high=2
third=0
sum=0
temp=0
while(third<4000000):
	third=low+high
	if(third%2==0):
		sum+=third
	low=high
	high=third

print(sum+2)
