# parent sends n nuumbers to child, child sorts it and sends back to parent, which displays it
from os import fork, pipe, close, fdopen


def strtoint(s):
    ans = s.split()
    lis = []
    for x in ans:
        lis.append(int(x))
    return lis


def inttostr(lis):
    i = 0
    while i < len(lis):
        lis[i] = str(lis[i])
        i = i+1
    x = " ".join(lis)
    return x


def main():
    r1, w1 = pipe()  # p to c

    r2, w2 = pipe()  # c to p

    pid = fork()

    if pid > 0:
        lis = input("Enter the Numbers : ")

        # send to child
        close(r1)
        w1 = fdopen(w1, 'w')
        print("Parent Process has sent to Child Process")
        w1.write(lis)
        w1.close()

        # receive from Child
        close(w2)
        r2 = fdopen(r2)
        ans = r2.read()

        print("Child has received the answer as : ", ans)
        r2.close()

    else:

        close(w1)
        r1 = fdopen(r1)
        s = r1.read()
        print("Child has Received : ", s)

        nums = strtoint(s)
        nums.sort()
        s = inttostr(nums)

        # send to parent
        close(r2)
        w2 = fdopen(w2, 'w')
        w2.write(s)
        print("Child has sent the sorted numbers to parent")
        w2.close()


if __name__ == "__main__":
    main()
