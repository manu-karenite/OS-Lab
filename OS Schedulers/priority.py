# assuming we can have multiple process with same priority, then sort according to fcfs
# assuming that we have arrived at 0
from tabulate import tabulate


def byP(lis):
    return (lis[1])


def main():
    n = int(input("Enter the number of processes : "))

    processList = []
    for i in range(0, n, 1):
        bt = int(input("Please enter the Burst Time of Process : "))

        p = int(input("Please enter the priority of Process : "))
        temp = [p, bt]
        processList.append(temp)
    k = 0
    while k < len(processList):
        processList[k].insert(0, k+1)
        k = k+1
    print(processList)

    processList.sort(key=byP)
    # Sorted by Priority

    # starting counter with burst time of 1st process because process reachs that time..
    clock = 0
    # assuming all arrived at 0 ms
    for item in processList:
        endtime = clock+item[2]
        wt = endtime-item[2]-0
        tat = endtime-0

        item.append(endtime)
        item.append(tat)
        item.append(wt)

        clock = endtime

    processList.insert(0, ["Process", "Priority", "Burst Time",
                       "Completion Time", "Turnaround Time", "Waiting Time"])
    print(tabulate(processList, headers='firstrow', tablefmt='fancy_grid'))


if __name__ == "__main__":
    main()
