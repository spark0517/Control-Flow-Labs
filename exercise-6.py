# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input("Enter the month of the year (Jan - Dec): ")
day = int(input("Enter the day of the month: "))
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

if len(month) != 3:
    print("Please type a 3 character abbrevation of a month")

if not (month in months):
    print ("Please type a 3 character abbreviation of a month")

def season (month, day):
    if month == "Dec":
        if (21 <= day <= 31):
            print (f"{month} {day} is in Winter")
        elif (1 <= day <= 20):
            print (f"{month} {day} is in Fall")
        else:
            print ("Invalid input received")
    if month == "Jan":
        if (1 <= day <= 31):
            print (f"{month} {day} is in Winter")
        else:
            print ("Invalid input received")
    if month == "Feb":
        if (1 <= day <= 29):
            print (f"{month} {day} is in Winter")
        else:
            print ("Invalid input received")
    if month == "Mar":
        if (1 <= day <= 19):
            print (f"{month} {day} is in Winter")
        elif (20 <= day <= 31):
            print (f"{month} {day} is in Spring")
        else:
            print ("Invalid input received")
    if month == "Apr":
        if (1 <= day <= 31):
            print (f"{month} {day} is in Spring")
        else:
            print ("Invalid input received")
    if month == "May":
        if (1 <= day <= 31):
            print (f"{month} {day} is in Spring") 
        else:
            print ("Invalid input received")       
    if month == "Jun":
        if (1 <= day <= 20):
            print (f"{month} {day} is in Spring")
        elif (21 <= day <=31):
            print (f"{month} {day} is in Summer")
        else:
            print ("Invalid input received")
    if month == "Jul":
        if (1 <= day <= 31):
            print (f"{month} {day} is in Summer")
        else:
            print ("Invalid input received")
    if month == "Aug":
        if (1 <= day <= 31):
            print (f"{month} {day} is in Summer")
        else:
            print ("Invalid input received")
    if month == "Sep":
        if (1 <= day <= 21):
            print (f"{month} {day} is in Summer")
        elif ( 22 <= day <= 31):
            print (f"{month} {day} is in Fall")
        else:
            print ("Invalid input received")
    if month == "Oct":
        if (1 <= day <= 31):
            print (f"{month} {day} is in Fall")
        else:
            print ("Invalid input received")
    if month == "Nov":
        if (1 <= day <= 31):
            print (f"{month} {day} is in Fall")
        else:
            print ("Invalid input received")

season(month, day)




