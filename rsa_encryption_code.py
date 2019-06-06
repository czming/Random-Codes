#code for RSA encryption and decryption after completing course on Number Theory and Crytography on Coursera
def string_to_dec(string): #convert string to ascii value in decimal form
    dec_string = ''
    string = str(string) #enforce this condition
    for char in string:
        curr = str(ord(char))
        if len(curr) < 3:
            curr = '0' + curr
        dec_string += curr
    return int(dec_string)

def dec_to_string(dec_value):
    dec_string = str(dec_value)  #if in int form, then change to str, if already in str, no change
    string = ''
    while len(dec_string) >= 3:
        curr = chr(int(dec_string[-3:]))
        string = curr + string
        dec_string = dec_string[:-3] #trim off the last part
    if dec_string: #anything left
        string = chr(int(dec_string)) + string
    return string

def FastModularExponentiation(b, e, m):
    mod_remainder = b % m
    current_remainder = 0
    while e > 0:
        if e % 2 == 1:
            if current_remainder == 0:
                current_remainder = mod_remainder
            else:
                current_remainder = (current_remainder * mod_remainder) % m #must remember to mod m
        mod_remainder = (mod_remainder ** 2) % m
        e = e // 2
    return current_remainder

def gcd(a, b):
    if a == 0:
        print (b, 0, 1, a, b)
        return b, 0, 1
    else:
        d, p, q = gcd(b%a, a)
        #need to swap the p and q in this case, because the q value is attached to the a, while p is attached to b % a
        #so d = ap + (b mod a)q, the values are mixed up already (just match them accordingly to see why)
        y = p
        x = q-p*(b//a)

        return d, x, y

def Encrypt(message, n, e):
    if type(message) != int:
        message = string_to_dec(message)
    return FastModularExponentiation(message, e, n)

def Decrypt(ciphertext, p, q, e):
    n = p * q
    p_q = (p-1) * (q-1)
    d = gcd(e, p_q)[1] % p_q #want the factor of e in the equation and a positive value mod p_q 
    #print (gcd(e, p_q))
    #print (d)
    message = FastModularExponentiation(ciphertext, d, n)
    print (dec_to_string(message))
    return message
