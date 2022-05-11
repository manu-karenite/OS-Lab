import os
import random

r,w=os.pipe()

pid=os.fork()

if pid>0:
	print("Parent is Sending the Numbers")
	os.close(r)
	w=os.fdopen(w,'w')

	#now we need to take numbers as input
	n=int(input("Enter the number of terms : "))
	i=0
	toSend=""
	while i<n:
		x=int(input("Enter the term number "))
		toSend=toSend+" "+str(x)
		i=i+1
	w.write(toSend)
	print("Parent has sent the numbers")
	w.close()
else:
	print("Child will receive the numbers now")
	os.close(w)
	r=os.fdopen(r)
	str=r.read()
	print("Child has received the numbers : ",str)
	r.close()



