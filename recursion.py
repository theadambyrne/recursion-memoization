#Fibonacci , memoization


def fibonacci_dep(n):
    if(n == 1):
        return 1
    elif(n == 2):
        return 1
    elif(n > 2):
        return fibonacci(n-1) + fibonacci(n-2)

# for i in range(1,11):
#    print(str(i) + " : " + str(fibonacci(i)))

#no memoization -> slow ar big nums


#Memoization -- no running through previous hoops
fibonacci_cache = {}
def mfib(n):

    if( n in fibonacci_cache):
        return fibonacci_cache[n]

    if(n == 1):
        value = 1
    elif(n == 2):
        value = 2
    elif(n > 2):
        value = mfib(n-1) + mfib(n-2)

    fibonacci_cache[n] = value
    return value


# for i in range(1,101):
#    print(str(i) + " : " + str(mfib(i)))


#Other way lmao

from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    #check input
    if type(n) != int:
        raise TypeError("Positive Integer required")
    if(n == 1):
        return 1
    elif(n == 2):
        return 1
    elif(n > 2):
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 1001):
    print(str(n) + " : " + str(fibonacci(n)))
