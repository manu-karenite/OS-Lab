# our process will be of form :
#[processnumber, arrivaltime,bursttime,waitingtime,completiontime,turnaroundtime]
from tabulate import tabulate


def wrtArrivalTime(process):
    return process[0]


def sjf(process):
    return process[1]


def main():
    # we need to take from user, inputs like arrival time, and burst times
    numProcess = int(input("Enter the number of processes: "))
    # we have the number of processes now
    # run a loop and read the inputs
    # processList=[["Process","Arrival Time","Burst Time","Waiting Time","Completion Time","Turnaround Time"]]
    processList = []
    i = 0
    while i < numProcess:
        arrivalTime = int(
            input("Enter the arrival time of process %d : " % (i+1)))
        burstTime = int(input("Enter the burst time of process %d : " % (i+1)))
        processList.append([arrivalTime, burstTime])
        i = i+1
        print("-------------------------------------------------------------------------------")

    # we sort the list wrt arrival time , that is index 1
    processList.sort(key=wrtArrivalTime)

    readyQ = [processList[0]]  # initialising the ready queue
    wait = 0
    burst = processList[0][0]
    j = 1
    i = 0
    while readyQ:
        current = readyQ.pop(0)
        # this process has to go on till, what time? burstTime
        endTime = burst+current[1]
        j = 0
        while j < numProcess:
            local = processList[j]
            if local[0] > current[0] and local[0] <= endTime and readyQ.count(local) == 0 and len(local) == 2:
                readyQ.append(local)
            elif local[0] > endTime:
                break
            j = j+1

        # ready queue established
        readyQ.sort(key=sjf)
        # work on the current queue now:
        completionTime = endTime
        waitingTime = completionTime-current[0]-current[1]
        turnaroundtime = completionTime-current[0]

        burst = endTime
        # now work on modifying the original array
        index = processList.index(current)
        current.append(waitingTime)
        current.append(completionTime)
        current.append(turnaroundtime)

        processList[index] = current

    # now prepare the list for table format
    k = 0
    while k < numProcess:
        processList[k].insert(0, k+1)
        k = k+1
    # Added Process Numbers
    processList.insert(0, ["Process", "Arrival Time", "Burst Time",
                       "Waiting Time", "Completion Time", "Turnaround Time"])

    avg_wt = 0
    avg_tt = 0

    k = 1
    while k <= numProcess:
        avg_wt += processList[k][3]
        avg_tt += processList[k][5]
        k = k+1

    print(tabulate(processList, headers='firstrow', tablefmt='fancy_grid'))
    print("The Average Waiting Time is : %f ms" % (avg_wt/numProcess))
    print("The Average Turn Around Time is : %f ms" % (avg_tt/numProcess))


main()
