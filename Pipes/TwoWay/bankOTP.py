from os import fdopen, close, pipe, fork
from random import random


def main():
    # create a pipe..
    # 6 digit itp means from 100000 to 999999
    OTP = str(int(random()*(999999-100000)+100000))

    r1, w1 = pipe()  # P TO C
    r2, w2 = pipe()  # C TO P
    pid = fork()

    if pid > 0:
        # BANK IS PARENT

        close(r1)

        # SEND THE OTP TO CLIENT..
        w1 = fdopen(w1, 'w')
        st = "The OTP Generated for your Transaction is : "+OTP
        print(st)
        w1.write(st)
        w1.close()

        close(w2)
        r2 = fdopen(r2)
        val = r2.read()
        r2.close()

        if val == OTP:
            print("OTP Validated! Transaction Success!")

        else:
            print("OTP Invalid! Transaction Failed!")

    else:
        # CUSTOMER IS CLIENT
        # CUSTOMER NOW HAS THE WORK TO RECEIVE AND ENTER THE OTP..
        # 1) RECEIVE THE OTP
        close(w1)
        r1 = fdopen(r1)
        target = r1.read()

        print("Waiting for the Customer to Enter the OTP !")

        # 2)) Read otp from cutsomer.....

        val = input("Enter the 6 Digit OTP for your transaction : ")

        # 3) sends back to bank for verification..

        close(r2)

        w2 = fdopen(w2, 'w')
        w2.write(val)
        w2.close()


if __name__ == "__main__":
    main()
