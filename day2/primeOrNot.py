flag = 0
number = int(input("Enter a number: "))
factors_list = []

def checkPrime(number):
    if number == 0 or number == 1:
        flag = 1
    else:
        for i in range(2, number):
            if number % i == 0:
                flag = 1
                factors_list.append(i)
                return factors_list
output=checkPrime(number)

def primeFactors(numbers):
    for i in numbers:
        return (checkPrime(i))



if flag == 1:
    print(f"{number} is not prime")
    print(primeFactors(output))
else:
    print(f"{number} is prime")


    
