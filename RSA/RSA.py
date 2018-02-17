import random
import math

def euclid_GCD(a,b):
    if b==0:
        return a
    return euclid_GCD(b,a%b)


def extended_euclid(a,b):
    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    while r2 > 1:
        q = r1//r2
        r = r1 - q*r2
        r1 = r2
        r2 = r
        
        s = s1 - q*s2
        s1 = s2
        s2 = s
        
        t = t1 - q*t2
        t1 = t2
        t2 = t
    if t > a:
        t = t%a
    if t < 0:
        t = t + a
    return t


def modular_exponentiation(x,e,n):
    #Square and Multiply Method
    X = x
    E = e
    Y = 1
    while E:
        if E & 1:
            Y = Y * X % n
        E>>=1
        X = X*X % n
    return Y


def miller_rabin(n):
    s = n-1
    t = 0
    while s&1 == 0:
        s = s//2
        t +=1
    itr = 0
    while itr<128:
        a = random.randrange(2,n-1)
        v = modular_exponentiation(a,s,n)
        if v != 1:
            i=0
            while v != (n-1):
                if i == t-1:
                    return False
                else:
                    i = i+1
                    v = (v**2)%n
        itr+=2
    return True



def isPrime(n):
    trivial_Primes =   [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
                   ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
                   ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                   ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
                   ,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
                   ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
                   ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
                   ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
                   ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
                   ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
    if (n >= 3):
        if (n&1 != 0):
            for p in trivial_Primes:
                if (n == p):
                    return True
                if (n % p == 0):
                    return False
            return miller_rabin(n)
    return False



def generate_primes(k):
    
    r=1000*(math.log(k,2)+1)
    r_t = r
    while r>0:
        n = random.randrange(2**(k-1),2**(k))
        r-=1
        if isPrime(n) == True:
            return n
    return "Timeout after "+ str(r_t) + " tries."



def find_a_public_key():
    standard_key = [3, 5, 17, 257, 65537]
    return random.choice(standard_key)


def find_inverse(Phi,e):
    #Extended Euclidean Algorithm
    print("Applying extende euclid algo to find inverse ...\n")
    d = extended_euclid(Phi,e)
    return d



def RSA_Key_Generation(k = 1024):
    
    e = find_a_public_key()
    print("Executing Key Generation... \n")
    print("Generating Prime Numbers....")
    while True :
        p = generate_primes(k)
        q = generate_primes(k)
        while p == q:
            q = generate_primes(k)
        Phi_N = (p-1)*(q-1)
        if Phi_N%e != 0:
            break
    print("Prime Numbers Generated!\n" + "p = \n" + str(p) + "\nq = \n" + str(q))
    n = p*q
    print("\nPublic Key :\n" + "n = " + str(n) + "\n" + "e = " + str(e))
    
    d = find_inverse(Phi_N,e)
    print("Private key generated : \n" + str(d))
    
    Public_key = {'n':n,'e':e}
    Private_key = d
    return Public_key,Private_key



def RSA_Encryption(P,e,n):
    print("Encrypting ....\n")
    C = modular_exponentiation(P,e,n)
    print("Done Encrypting !")
    return C



def RSA_Decryption(C,d,n):
    print("Decrypting .... \n")
    P = modular_exponentiation(C,d,n)
    print("Done Decrypting !")
    return P



"""
P = 14256398852241562114894651321321654646232132164644651321321354654641313
public_key,private_key = RSA_Key_Generation()
print(public_key)
print(private_key)
C = RSA_Encryption(P,public_key['e'],public_key['n'])
D_C = RSA_Decryption(C,private_key,public_key['n'])
print('Plain Text : ' + str(P))
print('Cipher Text : ' + str(C))
print('Decrypted Text : ' + str(D_C))
"""


def main():
    P = int(input("\nEnter the Plain Text : "))
    public_key,private_key = RSA_Key_Generation()
    
    n = public_key['n']
    e = public_key['e']
    
    d =private_key
    
    C = RSA_Encryption(P,e,n)
    print("\nCipher Text Generated : \n" + str(C))
    choice = int(input("\nEnter 2 to check the encryption : "))
    if choice == 2:
        print("Entered Plain Text : \n" + str(P) + "\n")
        print("Generated Cipher Text : \n" + str(C) + "\n")
        D_Check = RSA_Decryption(C,d,n)
        print("Decrypted text : \n" + str(D_Check))


if __name__ == "__main__":
    main()

