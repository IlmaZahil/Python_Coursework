#Author : F.Ilma Zahil
#Program: Course Work
#version: Horizontal Histogram(Staff Version)

import sys
pcount = 0
tcount = 0
rcount = 0
ecount = 0 
while True:
        print('\n''\n'"*****Student Version*****"'\n')                                                    
        try:
                pass_credit=int(input('\n'"Enter the Pass Credit : "))         #pass credits
                if pass_credit in range(0,121,20):
                        print("")
                else:
                        print("RANGE ERROR")
        except:
                print("Integers Required,Invalid format!,Try Again")


                #defers
        try:
                defer=int(input("Enter the Defer Credit : "))               #defer credits
                if defer in range(0,121,20):
                        print("")
                else:
                        print("RANGE ERROR")
        except:
                print("Integers Required,Invalid format!,Try Again")

                                    
                        #fails
        try:
                fail=int(input("Enter the Fail Credit : "))                #fail credits
                if fail in range(0,121,20):
                        print("")
                else:
                                print("RANGE ERROR")
        except:
                print("Integers Required,Invalid format!,Try Again")

         
                      
                
        total_cr = pass_credit+defer+fail                               # total credit
        if total_cr==120:                
                if (pass_credit==120) and (defer==0) and (fail==0):
                        print("Progress")
                        pcount +=1
                elif (pass_credit==100)and(defer==20 or fail==20):
                        print("Progress - Module Trailer")
                        tcount +=1
                elif (fail==80) and ((pass_credit==40) or (pass_credit==20 and defer==20)):
                        print("exclude")
                        ecount +=1
                elif ((pass_credit==20 and fail==100) or fail==120):
                        print("exclude")
                        ecount +=1
                elif ((defer==40 and fail==80) or (defer==20 and fail==100)):
                        print("exclude")
                        ecount+=1
                elif pass_credit in range(0,81,20) and (defer in range(0,121,20) and fail in range(0,81,20)):
                        print("Do Not Progress - Module Retriver")
                        rcount +=1
                        
                                       
        else:
                print("Total Incorrect")

        program_exit=str(input('\n'"Enter 'q' to exit, or Press any other key to continue : "))
        if program_exit == "q":                
                print('\n''\n'"***** Horizontal Histogram - Staff Version *****"'\n''\n')
                print("Progress",pcount," : ", end='')
                rows = 1                                    # Rows you want in your pattern
                for i in range(rows):
                        for column in range(0, pcount):
                                print("  *  ", end=' ')
                        print("")
                print("Trailing",tcount," : ", end='')
                rows = 1                                    # Rows you want in your pattern
                for i in range(rows):
                        for column in range(0, tcount):         
                                print("  *  ", end=' ')
                        print("")
                print("Retriver",rcount," : ", end='')
                rows = 1                                    # Rows you want in your pattern
                for i in range(rows):
                        for column in range(0, rcount):
                                print("  *  ", end=' ')
                        print("")
                print("Exclude ",ecount," : ", end='')
                rows = 1                                    # Rows you want in your pattern
                for i in range(rows):
                        for column in range(0, ecount):
                                print("  *  ", end=' ')
                        print("")
                print('\n',pcount+tcount+rcount+ecount,"outcomes in total")

                sys.exit(1)
                                           

                

                        


                
