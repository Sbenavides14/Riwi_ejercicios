print("Welcome to the RIWI gym")


def age_validation():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Her age is invalid")
        elif  age < 13:
            print("You cannot enter the gym")
        elif age >= 13 and age <= 17:
            print("His class is youthful")
        elif age >= 18 and age <=  59:
            print("Its class is general")
        else:
            print("His class is senior")
    except ValueError:
        return age_validation()
    
age_validation()