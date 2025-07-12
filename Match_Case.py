print("Enter Day and Month:",end="")

def prnt(data): # Function to print anything without by default next line
    print(data + " ",end="")

day,month=map(int,(input().split()))
match day:
    case 1:
        prnt("Monday")
    case 2:
        prnt("Tuesday")
    case 3:
        prnt("Wednesday")
    case 4:
        prnt("Thursday")
    case 5:
        prnt("Friday")
    case 6:
        prnt("Saturday")
    case 7:
        prnt("Sunday")
    
# Use of default value and combining values using (|)

match month:
    case 1:
        prnt("January")
    case 2:
        prnt("February")
    case 3:
        prnt("March")
    case 4:
        prnt("April")
    case 5:
        prnt("May")
    case 6:
        prnt("June")
    case 7:
        prnt("July")
    case 8:
        prnt("August")
    case 9:
        prnt("September")
    case 10:
        prnt("October")
    case 11:
        prnt("November")
    case 12:
        prnt("December")
    case _:
        prnt("Wrong Month No. Entered")


match day:
    case 1 | 2 | 3 | 4 | 5 :
        prnt("It's a Weekday")
    case 6 | 7:
        prnt("It's Weekend")
    case _:
        prnt("Wrong Day No. Entered")



# O/P 1 :
# Enter Day and Month:6 7
# Saturday July It's Weekend 

# O/P 2 :
# Enter Day and Month:7 8
# Sunday August It's Weekend 