numlist=[0,2,3,7,11,12]
def count_odd(numlist):
    count=0
    for i in numlist:
        if i%2 !=0:
            count=count+1
    return count
    
def even_sum(numlist):
    even=0
    for i in numlist:
        if i%2 ==0:
            even=even+i
    return even

letterlist={"I", "name", "paper", "food"}

def odd_sum(numlist):
    odd=0
    for i in numlist:
        if i%2 !=0:
            odd=odd+i
    return odd

def fiveletter_words(letterlist):
    sum= 0
    for i in letterlist:
        if len(i) == 5:
            sum = sum+1
    return sum

def sumupto_even(numlist):
    sum = 0
    for i in numlist:
        if i % 2 == 0:
            break
        else:
            sum+=i
    return sum

namelist={"George", "James", "Sam"}
def upto_sam(namelist):
    sum= 0
    for i in namelist:
        if i == "sam":
            sum = sum+1
            break
        sum = sum+1
    return sum


def newtsqrt(n):
    approx = n/2
    while True:
        better = (approx + n/approx)/2
        if abs(better - approx) < .001:
            return better
        approx = better
        
        
        
def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return "not prime"
        else:
            return "prime"