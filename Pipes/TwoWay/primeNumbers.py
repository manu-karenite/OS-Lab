import os

r1,w1=os.pipe() #P TO C
r2,w2=os.pipe() #C TO P

pid=os.fork()

def extractPrime(listOfNumbers):
	splittedNumbers=listOfNumbers.split()

	#Now we have the numbers

	finalList=[]
	i=0
	while i<len(splittedNumbers):
		curr=int(splittedNumbers[i])
		check=False
		k=2
		while k<=curr-1:
			if curr%k==0:
				check=True
				break
			k=k+1
		if check==False: #means it is prime
			finalList.append(curr)
		i=i+1

	#create a string out of the numbers
	strin=""
	i=0
	while i<len(finalList):
		strin=strin+" "+str(finalList[i])
		i=i+1
	return strin

if pid>0:
	#Deal with Parent Process now, send n numbers
	#Use P1 to send data
	os.close(r1)
	n=int(input("Enter number of inputs : "))
	str1=""
	i=0
	while i<n:
		x=int(input("Enter the Term : "))
		str1=str1+" "+str(x)
		i=i+1

	w1=os.fdopen(w1,'w')
	w1.write(str1)
	w1.close()

	#Get the Values from The Child Process
	os.close(w2)
	r2=os.fdopen(r2)
	answer=r2.read()
	print("The Prime Numbers are : ",answer)
	r2.close()

else:
	#now read from Pipe 1
	os.close(w1)
	r1=os.fdopen(r1)
	listOfNumbers=r1.read()
	print("Numbers Received from Parent Process are  : ",listOfNumbers)

	primeList=extractPrime(listOfNumbers) #Returns a String Of Numbers

	#Send back via Pipe 2
	os.close(r2)
	w2=os.fdopen(w2,'w')
	w2.write(primeList)
	w2.close()
