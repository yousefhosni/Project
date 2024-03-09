### app title
print('=======================================')
print('===  numbering system converter app ===')
print('=======================================\n\n')
### declare the variables
decimal = 1         #"0123456789"
binary = 2          #"01"
octal = 3           #"01234567"
hexadecimal = 4     #"0123456789ABCDEF"

main_menu = 1
while main_menu == 1:
    ### Ask the user what the base he wants to convert a number from
    limit = ['1','2','3','4']     # declare the numbers user can choose of them   
    print('Please select the base you want to convert a number from')
    from_what = input('Decimal = 1 \nBinary = 2 \noctal = 3 \nhexadecimal = 4 \n')
    i = 0
    while (len(from_what)) > i:                       ### checking number using while loop 
        while from_what[i] not in limit :             ### checking number using while loop
            print("\nit is not decimal number")
            from_what = input('please put a valid decimal number : ') ### get valid number from the user 
            i = 0
        i += 1
    
    while from_what == '1':  ### convert from decimal to any thing 
    ### ask the user what the base he want to convert a decimal number to    
        print('\nPlease select the base you want to convert a number to')
        from_decimal_to = int(input('Binary = 2 \noctal = 3 \nhexadecimal = 4 \n'))

        while from_decimal_to == 2:  ### convert from decimal to binary 
            limit = ['0','1','2','3','4','5','6','7','8','9']       ### make list to set the numbers of decimal
            decimal = input("\nEnter a decimal number : ")          ### get the decimal number from the user
            i = 0
            while (len(decimal)) > i:                       ### checking decimal number using while loop 
                while decimal[i] not in limit :             ### checking decimal number using while loop
                    print("\nit is not decimal number")
                    decimal = input('please put a valid decimal number : ') ### get valid decimal number from the user 
                    i = 0
                i += 1      
            binary = 0              ### declare new variable to save the result in
            power = 0               ### declare new variable to use it to know the result
            copy = int(decimal)     ### copy input decimal
            while(copy > 0):        ###find binary value using while loop
                binary = ((copy%2)*(10**power)) + binary
                copy = int(copy/2)
                power += 1

    ####### output the result       
            print("Binary of {x} is: {y}\n".format(x=decimal,y=binary))
    ####### make user choose if he wants make anether conversion or exit
            print('another number = 2 \nconvert to octal = 3')
            print('convert to hexadecimal = 4 \nanother chooice = 0')
            from_decimal_to = int(input())   

        while from_decimal_to == 3:  ### convert from decimal to octal 
            limit = ['0','1','2','3','4','5','6','7','8','9']       ### make list to set the numbers of decimal
            decimal = input("\nEnter a decimal number : ")          ### get the decimal number from the user
            i = 0
            while (len(decimal)) > i:                       ### checking decimal number using while loop 
                while decimal[i] not in limit :             ### checking decimal number using while loop
                    print("\nit is not decimal number")
                    decimal = input('please put a valid decimal number : ') ### get valid decimal number from the user 
                    i = 0
                i += 1     
            octal = 0               ### declare new variable to save the result in
            power = 0               ### declare new variable to use it to know the result
            copy = int(decimal)     ### copying number
            while(copy > 0):        ### computing octal using while loop
                octal += ((copy%8)*(10**power))     #Stacking remainders
                copy = int(copy/8)                  #updating dividend
                power += 1
           #output 
           # the result
            print("Octal of {x} is: {y}\n".format(x=decimal,y=octal))
    ####### make user choose if he wants make anether conversion or exit
            print('another number = 3 \nconvert to binary = 2')
            print('convert to hexadecimal = 4 \nanother chooice = 0')
            from_decimal_to = int(input())

        while from_decimal_to == 4:  ### convert from decimal to hexadecimal
    ####### make list to set the numbers of hexadecimal
            conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
            limit = ['0','1','2','3','4','5','6','7','8','9']       ### make list to set the numbers of decimal
            decimal = input("\nEnter a decimal number : ")          ### get the decimal number from the user
            i = 0
            while (len(decimal)) > i:                       ### checking decimal number using while loop 
                while decimal[i] not in limit :             ### checking decimal number using while loop
                    print("\nit is not decimal number")
                    decimal = input('please put a valid decimal number : ') ### get valid decimal number from the user 
                    i = 0
                i += 1     
            copy = int(decimal)         ### copying number
            hexadecimal = ''            ### declare new variable to save the result in
            while(copy>0):              ### computing hexadecimal using while loop
                remainder = copy%16
                hexadecimal = conversion_table[remainder]+ hexadecimal
                copy = copy//16
    ####### output the result    
            print("Hexadecimal of {y} : {x}\n ". format(y=decimal,x=hexadecimal))
    ####### make user choose if he wants make anether conversion or exit
            print('another number = 4 \nconvert to binary = 2')
            print('convert to octal = 3 \nanother chooice = 0')
            from_decimal_to = int(input())

        if from_decimal_to == 0 :    ### break the while loop
            break    

    while from_what == '2':  ### convert from binary to any thing 
    ### ask the user what the base he want to convert a binary number to         
        print('\nPlease select the base you want to convert a number to')
        from_binary_to = int(input('Decimal = 1 \noctal = 3 \nhexadecimal = 4 \n'))     
        while from_binary_to == 1:  ### convert from binary to decimal 
            limit = ['0','1']    ### make list to set the numbers of binary
            binary = input("\nEnter a binary number : ")    ### get the binary number from the user
            i = 0 
            while (len(binary)) > i:                       ### checking binary number using while loop 
                while binary[i] not in limit :             ### checking binary number using while loop
                    print("\nit is not binary number")
                    binary = input('please put a valid binary number : ') ### get valid binary number from the user 
                    i = 0
                i += 1    
            decimal = 0          ### declare new variable to save the result in
            power = len(binary)  ### declare new variable to use it to know the result
            for x in binary:     ### computing decimal using for loop 
                power -= 1 
                decimal = ((int(x))*(2**power))+decimal
    ####### output the result               
            print ("Decimal of {y} is : {x}\n".format(x=decimal,y=binary))
    ####### make user choose if he wants make anether conversion or exit        
            print('another number = 1 \nconvert to octal = 3')
            print('convert to hexadecimal = 4 \nanother chooice = 0')
            from_binary_to = int(input())

        while from_binary_to == 3:  ### convert from binary to octal         
            limit = ['0','1']    ### make list to set the numbers of binary
            binary = input("\nEnter a binary number : ")    ### get the binary number from the user
            i = 0 
            while (len(binary)) > i:                       ### checking binary number using while loop 
                while binary[i] not in limit :             ### checking binary number using while loop
                    print("\nit is not binary number")
                    binary = input('please put a valid binary number : ') ### get valid binary number from the user 
                    i = 0
                i += 1    
            decimal = 0             ### declare new variable to save the result in
            power = len(binary)     ### declare new variable to use it to know the result       
            for x in binary:        ### computing decimal using for loop 
                power -= 1 
                decimal = ((int(x))*(2**power))+decimal
    ### first step i convert to decimal now i convert from decimal to octal ###              
            octal = 0               ### declare new variable to save the result in
            power = 0               ### make the value of variable = 0
            while(decimal > 0):     ### computing octal using while loop
                octal += ((decimal%8)*(10**power))   #Stacking remainders
                decimal = int(decimal/8)             #updating dividend
                power += 1
    ####### output the result    
            print("Octal of {x} is: {y}\n".format(x=binary,y=octal))
    ####### make user choose if he wants make anether conversion or exit         
            print('another number = 3 \nconvert to decimal = 1')
            print('convert to hexadecimal = 4 \nanother chooice = 0')
            from_binary_to = int(input())

        while from_binary_to == 4:  ### convert from binary to hexadecimal     
            limit = ['0','1']    ### make list to set the numbers of binary
            binary = input("\nEnter a binary number : ")    ### get the binary number from the user
            i = 0 
            while (len(binary)) > i:                       ### checking binary number using while loop 
                while binary[i] not in limit :             ### checking binary number using while loop
                    print("\nit is not binary number")
                    binary = input('please put a valid binary number : ') ### get valid binary number from the user 
                    i = 0
                i += 1    
            decimal = 0             ### declare new variable to save the result in
            power = len(binary)     ### declare new variable to use it to know the result        
            for x in binary:        ### computing decimal using for loop
                power -= 1 
                decimal = ((int(x))*(2**power))+decimal
    ### first step i convert to decimal now i convert from decimal to hexadecimal ###             
    ####### make list to set the numbers of hexadecimal        
            conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
            hexadecimal = ''        ### declare new variable to save the result in         
            while(decimal>0):       ### computing hexadecimal using while loop
                remainder = decimal%16
                hexadecimal = conversion_table[remainder]+ hexadecimal
                decimal = decimal//16
    ####### output the result
            print("Hexadecimal of {y} : {x}\n ". format(y=binary,x=hexadecimal))
    ####### make user choose if he wants make anether conversion or exit         
            print('another number = 4 \nconvert to decimal = 1')
            print('convert to octal = 3 \nanother chooice = 0')
            from_binary_to = int(input())

        if from_binary_to == 0:     ### break the while loop
            break     

    while from_what == '3':  ### convert from octal to any thing 
    ### ask the user what the base he want to convert a octal number to    
        print('\nPlease select the base you want to convert a number to')
        from_octal_to = int(input('Decimal = 1 \nBinary = 2 \nhexadecimal = 4 \n'))   
        while from_octal_to == 1:   ### convert from octal to decimal         
            list = ['0','1','2','3','4','5','6','7']        ### make list to set the numbers of octal
            octal = input("\nEnter an octal number :")      ### get the octal number from the user
            i = 0
            while (len(octal)) > i:                          ### checking octal number using while loop 
                while octal[i] not in list :                 ### checking octal number using while loop 
                        print("\nit is not octal  number")
                        octal = input('please put a valid octal number : ') ### get valid octal number from the user
                        i = 0
                i += 1                
            decimal = 0         ### declare new variable to save the result in
            power = len(octal)  ### declare new variable to use it to know the result
            for x in octal:     ### computing decimal using for loop 
                power -= 1
                decimal = ((int(x))*(8**power))+decimal
            ###output the result            
            print ('Decimal of {y} : {x}\n '.format(y=octal,x=decimal)) 
    ####### output the result####### make user choose if he wants make anether conversion or exit             
            print('another number = 1 \nconvert to binary = 2')
            print('convert to hexadecimal = 4 \nanother chooice = 0')
            from_octal_to = int(input())    

        while from_octal_to == 2:   ### convert from octal to binary         
            list = ['0','1','2','3','4','5','6','7']        ### make list to set the numbers of octal
            octal = input("\nEnter an octal number :")      ### get the octal number from the user
            i = 0
            while (len(octal)) > i:                          ### checking octal number using while loop 
                while octal[i] not in list :                 ### checking octal number using while loop 
                        print("\nit is not octal  number")
                        octal = input('please put a valid octal number : ') ### get valid octal number from the user
                        i = 0
                i += 1                
            decimal = 0         ### declare new variable to save the result in
            power = len(octal)  ### declare new variable to use it to know the result
            for x in octal:     ### computing decimal using for loop
                power -= 1
                decimal = ((int(x))*(8**power))+decimal
            binary = 0              ### declare new variable to save the result in
            power = 0               ### make the value of variable = 0        
            while(decimal > 0):     ### find binary value using while loop
                binary = ((decimal%2)*(10**power)) + binary
                decimal = int(decimal/2)
                power += 1
    ####### output the result       
            print(f"Binary of {octal} is: {binary}\n")
    ####### make user choose if he wants make anether conversion or exit         
            print('another number = 2 \nconvert to decimal = 1')
            print('convert to hexadecimal = 4 \nanother chooice = 0')
            from_octal_to = int(input())

        while from_octal_to == 4:   ### convert from octal to hexadecimal
            list = ['0','1','2','3','4','5','6','7']        ### make list to set the numbers of octal
            octal = input("\nEnter an octal number :")      ### get the octal number from the user
            i = 0
            while (len(octal)) > i:                          ### checking octal number using while loop 
                while octal[i] not in list :                 ### checking octal number using while loop 
                        print("\nit is not octal  number")
                        octal = input('please put a valid octal number : ') ### get valid octal number from the user
                        i = 0
                i += 1                
            decimal = 0         ### declare new variable to save the result in
            power = len(octal)  ### declare new variable to use it to know the result
            for x in octal:     ### computing decimal using for loop
                power -= 1
                decimal = ((int(x))*(8**power))+decimal
    ####### make list to set the numbers of hexadecimal        
            conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
            hexadecimal = '' ### declare new variable to save the result in
    ### first step i convert to decimal now i convert from decimal to hexadecimal ### 
            while(decimal>0):  ### find hexadecimal value using while loop
                remainder = decimal%16
                hexadecimal = conversion_table[remainder]+ hexadecimal
                decimal = decimal//16
    ####### output the result    
            print("Hexadecimal of {y} : {x}\n ". format(y=octal,x=hexadecimal))
    ####### make user choose if he wants make anether conversion or exit 
            print('another number = 4 \nconvert to decimal = 1')
            print('convert to binary = 2 \nanother chooice = 0')
            from_octal_to = int(input())

        if from_octal_to == 0:      ### break the while loop
            break         

    while from_what == '4':  ### convert from hexadecimal to any thing
    ### ask the user what the base he want to convert a hexadecimal number to        
        print('\nPlease select the base you want to convert a number to')
        from_hexa_to = int(input("Decimal = 1 \nBinary = 2 \noctal = 3 \n")) 

        while from_hexa_to == 1:    ### convert from hexadecimal to decimal
    ####### make list to set the numbers of hexadecimal        
            list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            hexadecimal = input("\nEnter a hexadecimal number : ")    ### get the hexadecimal number from the user
            h = 0
            while (len(hexadecimal)) > h:                       ### checking hexadecimal number using while loop 
                while hexadecimal[h] not in list :      ### checking hexadecimal number using while loop
                    print("\nit is not hexadecimal number")
                    hexadecimal = input('please put a valid hexadecimal number : ') ### get valid hexadecimal number from the user
                    h = 0
                h += 1                    
            power = len(hexadecimal) - 1    ### declare new variable to use it to know the result
            decimal = 0                     ### declare new variable to save the result in
            for i in (hexadecimal):         ### computing decimal using for loop
                index = list.index(i)
                decimal = ((int(index))*(16**power))+decimal
                power -= 1
    ####### output the result        
            print("Decimal of {y} is : {x}\n".format(y=hexadecimal,x=decimal ))  
    ####### make user choose if he wants make anether conversion or exit 
            print('another number = 1 \nconvert to binary = 2')
            print('convert to octal = 3 \nanother chooice = 0')
            from_hexa_to = int(input())

        while from_hexa_to == 2:    ### convert from hexadecimal to binary
    ####### make list to set the numbers of hexadecimal        
            list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            hexadecimal = input("\nEnter a hexadecimal number : ")    ### get the hexadecimal number from the user
            h = 0
            while (len(hexadecimal)) > h:                       ### checking hexadecimal number using while loop 
                while hexadecimal[h] not in list :      ### checking hexadecimal number using while loop
                    print("\nit is not hexadecimal number")
                    hexadecimal = input('please put a valid hexadecimal number : ') ### get valid hexadecimal number from the user
                    h = 0
                h += 1                    
            power = len(hexadecimal) - 1    ### declare new variable to use it to know the result
            decimal = 0                     ### declare new variable to save the result in
            for i in (hexadecimal):         ### computing decimal using for loop
                index = list.index(i)
                decimal = ((int(index))*(16**power))+decimal
                power -= 1
            binary = 0           ### declare new variable to save the result in
            power = 0            ### make the value of variable = 0
    ### first step i convert to decimal now i convert from decimal to binary ### 
            while(decimal > 0):  ### find binary value using while loop
                binary = ((decimal%2)*(10**power)) + binary
                decimal = int(decimal/2)
                power += 1
    ####### output the result        
            print("Binary of {y} is : {x}\n".format(y=hexadecimal,x=binary ))  
    ####### make user choose if he wants make anether conversion or exit 
            print('another number = 2 \nconvert to decimal = 1')
            print('convert to octal = 3 \nanother chooice = 0')
            from_hexa_to = int(input())

        while from_hexa_to == 3:    ### convert from hexadecimal to octal
    ####### make list to set the numbers of hexadecimal        
            list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            hexadecimal = input("\nEnter a hexadecimal number : ")    ### get the hexadecimal number from the user
            h = 0
            while (len(hexadecimal)) > h:                       ### checking hexadecimal number using while loop 
                while hexadecimal[h] not in list :      ### checking hexadecimal number using while loop
                    print("\nit is not hexadecimal number")
                    hexadecimal = input('please put a valid hexadecimal number : ') ### get valid hexadecimal number from the user
                    h = 0
                h += 1                    
            power = len(hexadecimal) - 1    ### declare new variable to use it to know the result
            decimal = 0                     ### declare new variable to save the result in
            for i in (hexadecimal):         ### computing decimal using for loop
                index = list.index(i)
                decimal = ((int(index))*(16**power))+decimal
                power -= 1
            octal = 0           ### declare new variable to save the result in
            power = 0           ### make the value of variable = 0
    ### first step i convert to decimal now i convert from decimal to octal ###             
            while(decimal > 0): ### computing octal using while loop
                octal += ((decimal%8)*(10**power))  #Stacking remainders
                decimal = int(decimal/8)             #updating dividend
                power += 1
    ####### output the result        
            print("Octal of {y} is : {x}\n".format(y=hexadecimal,x=octal ))  
    ####### make user choose if he wants make anether conversion or exit 
            print('another number = 3 \nconvert to decimal = 1')
            print('convert to binary = 2 \nanother chooice = 0')
            from_hexa_to = int(input())

        if from_hexa_to == 0:       ### break the while loop 
            break
    
    print('\nback to main menu = 1 \nexit = 0')
    main_menu = int(input())
    if main_menu == 0:
        break    

# Yousef Hosni El-shiref    # 20231210
# Mohamed Hisham Gaber      # 20230359         