age = int(input("Enter your age: "))

if age >= 18:
    license = int(input("Do you have a license(1/0)? "))
    if(license == 1):
        print("You can drive")
    else:
        print("You cannot drive")
else:
    print("You cannot drive. Sorry!")