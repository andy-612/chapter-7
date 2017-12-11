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

def odd_sum(numlist):
    odd=0
    for i in numlist:
        if i%2 !=0:
            odd=odd+i
    return odd