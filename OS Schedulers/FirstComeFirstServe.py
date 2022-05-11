#our process will be of form :
#[processnumber, arrivaltime,bursttime,waitingtime,completiontime,turnaroundtime]
from tabulate import tabulate
def main():
	#we need to take from user, inputs like arrival time, and burst time
	numProcess=int(input("Enter the number of processes: "))
	#we have the number of processes now
	#run a loop and read the inputs
	processList=[["Process","Arrival Time","Burst Time","Waiting Time","Completion Time","Turnaround Time"]]
	i=0
	while i<numProcess:
		arrivalTime=int(input("Enter the arrival time of process %d : " %(i+1)))
		burstTime=int(input("Enter the burst time of process %d : " %(i+1)))
		processList.append([i+1,arrivalTime,burstTime])
		i=i+1
		print("-------------------------------------------------------------------------------")
	waitingtime=0
	completiontime=0

	i=1;
	while i<=numProcess:
		currentProcess=processList[i];
		currentProcess.append(waitingtime-currentProcess[1])
		completiontime=completiontime+currentProcess[2]
		currentProcess.append(completiontime)
		currentProcess.append(currentProcess[4]-currentProcess[1])
		waitingtime=waitingtime+currentProcess[2]
		i=i+1
	print(tabulate(processList,headers='firstrow', tablefmt='fancy_grid'))
	
	#calculate the avg times
	avg_w_time=0
	i=1
	while i<=numProcess:
		avg_w_time=avg_w_time+processList[i][3]
		i=i+1

	avg_t_time=0
	i=1
	while i<=numProcess:
		avg_t_time=avg_t_time+processList[i][5]
		i=i+1

	print("The Average Waiting Time is : %f ms" %(avg_w_time/numProcess))
	print("The Average Turn Around Time is : %f ms" %(avg_t_time/numProcess))
	

main()