
count=0
result=0

while(count<1000):
	if(count%3==0):
		result+=count
	elif(count%5==0):
		result+=count
	count+=1

print(result)
