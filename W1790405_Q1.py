#Author : F.Ilma Zahil
#Program: Course Work
#Version: Student Version

#pass_credits

try:
        pass_credit=int(input("enter the credit:"))         #pass credits
        if pass_credit in range(0,121,20):
                print("")
        else:
                print("RANGE ERROR")
except:
        print("Integers Required,Invalid format!,Try Again")


#defer

try:
        defer=int(input("enter the credit:"))               #defer credits
        if defer in range(0,121,20):
                print("")
        else:
                print("RANGE ERROR")
except:
        print("Integers Required,Invalid format!,Try Again")

            
#fail

try:
        fail=int(input("enter the credit:"))                #fail credits
        if fail in range(0,121,20):
                print("")
        else:
                print("RANGE ERROR")
except:
        print("Integers Required,Invalid format!,Try Again")
           

total_cr = pass_credit+defer+fail

if total_cr==120:
        if (pass_credit==120) and (defer==0) and (fail==0):
                print("progress")
        elif (pass_credit==100)and(defer==20 or fail==20):
                print("progress-module trailer")
        elif pass_credit in range(0,81,20) and defer in range(20,121,20) and fail in range(0,81,20):
                print("Do not progress-module retriver")
        elif pass_credit in range(0,41,20) and defer in range(0,41,20) and fail in range(0,121,20):
                print("exclude")
else:
        print("Total Incorrect")






