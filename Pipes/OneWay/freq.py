# Child sends a stream of numbers to parent and parent displays each numbers frequency

from os import fork, pipe, fdopen, close


def getFreq(s: str) -> str:
    # to interpret
    s = s.split()
    lis = []
    dic = {}
    for x in s:
        lis.append(int(x))
    for y in lis:
        if y in dic:
            dic[y] = dic[y]+1
        else:
            dic[y] = 1

    ans = ""
    for x in dic:
        ans = ans + str(x)+" : "+str(dic[x])+"\n"
    return ans


def main():

    # create pipes
    r, w = pipe()

    pid = fork()

    if pid > 0:
        close(w)
        r = fdopen(r)

        s = r.read()
        print(s)
        r.close()

        # solve the question:
        ans = getFreq(s)
        print("The numbers and their frequency are  : ")
        print(ans)

    else:
        close(r)

        w = fdopen(w, 'w')
        s = input("Enter the numbers separated by spaces: ")

        w.write(s)
        w.close()


if __name__ == "__main__":
    main()
