import os
r1, w1 = os.pipe()  # C TO P
r2, w2 = os.pipe()  # P TO C

pid = os.fork()


def checkPalindrome(word):
    i = 0
    j = len(word)-1
    while i <= j:
        if word[i] != word[j]:
            return False
        i = i+1
        j = j-1
    return True


if pid > 0:
    # PARENT HAS TO SEND THE STRING TO CHILD
    os.close(r2)
    w2 = os.fdopen(w2, 'w')
    test = input("Enter the String you want to check as palindrome  : ")
    print("Parent is sending String to Child")
    w2.write(test)
    w2.close()
    print("Parent has sent String to Child")

    # Receive from Pipe1
    os.close(w1)
    print("Parent will receive response from Child")
    r1 = os.fdopen(r1)
    answer = r1.read()
    print("Parent has received response from Child")
    print(answer)
else:
    os.close(w2)
    r2 = os.fdopen(r2)
    str = r2.read()
    print("String received from Parent is ", str)

    r2.close()
    # create a statement to send to parent back
    isPalindrome = checkPalindrome(str)

    answer = ""
    if isPalindrome == True:
        answer = "String is a Palindrome!"
    else:
        answer = "String is not a Palindrome!"

    # now use r1,w1 to handle back
    os.close(r1)
    print("Child is sending a response to Parent")
    w1 = os.fdopen(w1, 'w')
    w1.write(answer)
    print("Child has sent a response to Parent")
    w1.close()
