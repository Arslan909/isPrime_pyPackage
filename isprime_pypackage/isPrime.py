def isPrime(number):
    check = 0
    if number==2:
        return True
    if number <= 1 or  number%2==0:
    
        return False
    
    i=3
    while i*i<=number:
        if number % i == 0:
            check = 1
            return False
        i+=2
    return True