import os


def main():
    r1, w1 = os.pipe()  # p to c

    pid = os.fork()

    if pid > 0:
        # parent
        os.close(r1)
        s = input("Please Enter the String to test : ")
        w1 = os.fdopen(w1, 'w')
        w1.write(s)
        print("Parent has sent the string to child!")
        w1.close()

    else:
        # child process
        os.close(w1)
        r1 = os.fdopen(r1)
        s = r1.read()
        print(s, " has been received by the Child!")
        r1.close()


if __name__ == "__main__":
    main()
