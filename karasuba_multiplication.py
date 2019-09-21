def karasuba(num1, num2):
    num1, num2 = str(num1), str(num2)
#num1 and num2 are strings, assuming they are same length
    if len(num1) == 1 or len(num2) == 1:
        #once one of them is len 1, cannot simplify any further
        #base case, return multiplication and 1 to denote one multiplication operation done
        return int(num1) * int(num2)

    else:
        if len(num1) < len(num2):
            #easier just to make num1 the longer one
            num1, num2 = num2, num1
        a = num1[:len(num1)//2] if len(num1[:len(num1)//2]) > 0 else 0
        b = num1[len(num1)//2:] if len(num1[len(num1)//2:]) > 0 else 0
        #take numbers from the back instead of the front, otherwise the code thinks that these front numbers actually have the behind numbers because of num1 length
        #but taking from the back first can lead to error, so just pad with zeroes
        while len(num2) < len(num1):
            num2 = '0' + num2
        #we leave len(num1)//2 in the d section and the rest in c
        c = num2[:len(num1)//2] if len(num2[:len(num2)-len(num1)//2]) > 0 else 0
        d = num2[len(num1)//2:] if len(num2[len(num2)-len(num1)//2:]) > 0 else 0
        n1 = len(num1)
        n2 = len(num2)
        ac = karasuba(a,c)
        bd = karasuba(b,d)
        #need n1-n1//2 in case of odd number of digits
        #to avoid below problem, enforce that we split based on num1 length, so the number of digit behind (and hence the power of 10, is constant throughout)
        #but what happens when n1 does not equal n2, which can happen due to a+b and c+d
        #the a*d will be 10 **(n1-n1//2) and b * c will be 10 ** (n2-n2//2)
        return ac * 10 ** (2*(n1 - n1 // 2)) + (karasuba(int(a)+int(b), int(c)+int(d)) - ac-bd) * 10 **(n1-n1//2) + bd
    

