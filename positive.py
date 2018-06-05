num=int(input("enter the num"))
if(num<=10000):
	if(num<0):
		print("the num is -ve")
	elif(num==0):
		print("the num is zero")
	else:
		print("the num is +ve")
else:
	print("the num is valid")
