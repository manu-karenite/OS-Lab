#[processnumber, arrivaltime,bursttime,waitingtime,completiontime,turnaroundtime]
from tabulate import tabulate
def wrtArrivalTime(process):
	return process[0]

def main():
	numProcess=int(input("Enter the number of processes: "))
	processList=[]
	i=0
	while i<numProcess:
		arrivalTime=int(input("Enter the arrival time of process %d : " %(i+1)))
		burstTime=int(input("Enter the burst time of process %d : " %(i+1)))
		processList.append([arrivalTime,burstTime,burstTime])
		#this second bursttIME WILL ACT AS REMAINING TIME
		i=i+1
		print("-------------------------------------------------------------------------------")

		processList.sort(key=wrtArrivalTime)

	#Inputs are Done

	quantum=int(input("Enter the quantum in ns : "))
	readyQ=[]
	i=0
	while i<numProcess:
		readyQ.append(processList[i])
		i=i+1

	time=0
	while readyQ:
		current=readyQ.pop(0)
		#print(current)
		#we have the currentProcess now
		
		if current[2]<=quantum:
			endTime=time+current[2]
			time=time+current[2]
			#work is done now
			waitingTime=endTime-current[0]-current[1]
			completionTime=endTime
			turnaroundTime=completionTime-current[0]

			index=processList.index(current)
			current.append(waitingTime)
			current.append(completionTime)
			current.append(turnaroundTime)
			processList[index]=current
		else:
			#process is still left
			endTime=time+quantum
			time=time+quantum
			current[2]=current[2]-quantum
			readyQ.append(current)

	#preparing for printing
	k=0
	while k<numProcess:
		processList[k].pop(2) #removing the remaining time from python
		processList[k].insert(0,k+1)
		k=k+1
	processList.insert(0,["Process","Arrival Time","Burst Time","Waiting Time","Completion Time","Turnaround Time"])
	avg_wt=0
	avg_tt=0

	k=1
	while k<=numProcess:
		avg_wt+=processList[k][3]
		avg_tt+=processList[k][5]
		k=k+1

	print(tabulate(processList,headers='firstrow', tablefmt='fancy_grid'))
	print("The Average Waiting Time is : %f ms" %(avg_wt/numProcess))
	print("The Average Turn Around Time is : %f ms" %(avg_tt/numProcess))


main()