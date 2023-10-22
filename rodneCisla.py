import sys #for exit
import datetime #for verifying age

today = datetime.date.today()
day = today.day
month = today.month
year = today.year

ageLimit = 100

calendar=  {
    'months': ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'],
    'days': [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    'century': [1801, 1901, 2001] #nerozumiem ako to funguje ked sa clovek narodi rok pred novym storocim, prepokladam ze pre datum narodenia v roku 2000 je kontrolna cislica pre storocie 2 (20. storocie)
    #no jako na tyhle kontrolni cislice se jeste kouknu
    #NOT CHECK CENTURY ABY SA PRVA CISLICA ZA LOMKOU NEKONTROLOVALA
}

def verify():
    global calendar
    notCheckCentury = True

    while True:
        userInput = input('please enter your birth number (rodni cislo jako): ')

        try:
            #if contains '/' checks for right position in birth number
            if '/' in userInput:
                if userInput.count('/') == 1 and userInput.rfind('/') == 6:
                    userInput = userInput.replace('/', '')

            #checks for valid format (only numbers)
            userInputInt = int(userInput)

            #checks for valid month nonation and assignes male/female
            if len(userInput) == 10:
                if userInput[2] == '0' or userInput[2] == '1' or userInput[2] == '5' or userInput[2] == '6':

                    if userInput[2] == '0' or userInput[2] == '1':
                        isMale = True
                        isFemale = False
                    elif userInput[2] == '5' or userInput[2] == '6':
                        isFemale = True
                        isMale = False
                    else:
                        print('fatal error; sys_exit initiated')
                        sys.exit(1)

                    #assignes month
                    userBirthMonth = userInput[2] + userInput[3]

                    #if female distract fifty
                    if isFemale:
                        userBirthMonth = int(userBirthMonth) - 50

                    #assignes age if century is valid
                    if int(userInput[6]) > 0 and int(userInput[6]) < 4 or notCheckCentury:

                        #userBirthCentury = calendar['century'][int(userInput[6]) -1]
                        userBirthYearTwoDigits = int(userInput[0] + userInput[1]) #only last two digits

                        if userBirthYearTwoDigits > int(str(year)[2:]):
                            userBirthCentury = 1901
                        else:
                            userBirthCentury = 2001
                        
                        #account for people born in (2000)
                        if userBirthYearTwoDigits == 0:
                            userBirthYearTwoDigits = 99
                            accountforDifference = 0
                        else:
                            accountforDifference = 1

                        userAge = year - (userBirthCentury + userBirthYearTwoDigits) # for people who already had a birthday in the current year the age value is their real age -1 at this point!!

                        userBirthYear = userBirthCentury + userBirthYearTwoDigits - accountforDifference #full birth year
                        
                        #checks if alive (max 100yo)
                        if userAge <= ageLimit:

                            #checs for valid day and assigns
                            userBirthDay = int(userInput[4] + userInput[5])

                            if userBirthDay > 0 and userBirthDay < 32:
                                userBirthDay = int(userInput[4] + userInput[5])

                                #account for leap year
                                if (userBirthYear % 4 == 0 and userBirthYear % 100 != 0) or (userBirthYear % 400 == 0):
                                    calendar['days'][1] = 29
                                else:
                                    calendar['days'][1] = 28

                                #check if day and month correspond to a valid date
                                if userBirthDay <= calendar['days'][int(userBirthMonth) -1]:

                                    #check control digit
                                    controlDigit = int(userInput[9])
                                    controlDigitExcluded = userInput[:9]

                                    if controlDigit == 0 and int(controlDigitExcluded) % 11 == 10:
                                        isValid = True
                                    
                                    elif int(controlDigitExcluded) % 11 == controlDigit:
                                        isValid = True

                                        # ALL VERIFICATIONS PASSED
                                        if isValid:

                                            #account for birthdays that already happened this year
                                            if month >= int(userBirthMonth) and day >= userBirthDay:
                                                userAge += 1

                                            #assign sex
                                            if isFemale:
                                                sex = 'Female'
                                            elif isMale:
                                                sex = 'Male'
                                            else:
                                                print('fatal error; sys_exit initiated')
                                                sys.exit(1)

                                            output(controlDigit, sex, userAge, userBirthDay, calendar['months'][int(userBirthMonth)-1], userBirthYear)

                                    else:
                                        print(' invalid control digit ')
                                        print()

                                else:
                                    print(' the combination of day and month you entered does not exist ')
                                    print()

                            else:
                                print(' invalid day - numbers from 0 to 31 allowed ')
                                print()

                        else:
                            print('you enter a birth number suggesting you are more than 100 years old')
                            print()
                    else:
                        print(' invalid century ')
                        print()
                else:
                    print(' invalid month (0-12 and 50-62 allowed)')
                    print()
            else:
                print(' length error - the length of a birth number should be ten characters or eleven with a slash')
                print()

        except ValueError:
            print(' format error ')

def output(controlDigit, sex, age, birtDay, birthMonth, birthYear):
    try:
        print() #empty line
        print('YAY! THE PROVIDED BIRTH NUMBER IS VALID AND FOLLOWING INFORMATION WAS FETCHED')
        print(f'control digit {controlDigit} is VALID')
        print(f'Sex: {sex}')
        print(f'Age: {age}')
        print(f'Date of Birth: {birtDay}. of {birthMonth} {birthYear}')
        print() #empty line
        sys.exit(0)
    except ValueError:
        print('internal error - function did not pass values correctly, please try again')
        sys.exit(1)

verify()