def check_number(x):       
    limit = ['0','1']       ### make list to set the numbers         
    x = input()             ### get the number from the user   
    i = 0 
    while (len(x)) > i:                       ### checking number using while loop 
        while x[i] not in limit :             ### checking number using while loop
            print("\nit is not valid number")
            x = input('please choose a valid number : ') ### get valid number from the user 
            i = 0
        i += 1    
    return x

def check_choice(x):               
    limit = ['1','2','3','4']       ### make list to set the numbers         
    x = input()                     ### get the number from the user   
    i = 0 
    while (len(x)) > i:                       ### checking  number using while loop 
        while x[i] not in limit :             ### checking  number using while loop
            print("\nit is not valid number")
            x = input('please choose a valid number : ') ### get valid number from the user 
            i = 0
        i += 1    
    return x

def ones_complement(first_num):
    # Initialize the result string
    result = ''
    # Loop through each bit in the binary string
    for bit in first_num:
      # If the bit is 0, append 1 to the result
      if bit == '0':
        result += '1'
      # If the bit is 1, append 0 to the result
      else:
        result += '0'
    # Return the result string
    return result

def twos_complement(first_num):
  # Initialize the result and the carry bit
  result = ''
  carry = 1
  # Loop through the bits from right to left
  for bit in reversed(first_num):
    # Invert the current bit using bitwise NOT
    inverted = ~int(bit) & 1
    # Add the carry bit using bitwise XOR
    sum = inverted ^ carry
    # Update the carry bit using bitwise AND
    carry = inverted & carry
    # Prepend the sum bit to the result
    result = str(sum) + result
  # Return the result string
  return result

def binary_addition(frist_num, second_num):

    max_len = max(len(frist_num), len(second_num))
    frist_num = frist_num.zfill(max_len)
    second_num = second_num.zfill(max_len)

    carry = 0
    Binary_sum_result = ''
    for i in range(max_len - 1, -1, -1):
        bit_sum = carry + int(frist_num[i]) + int(second_num[i])
        Binary_sum_result = str(bit_sum % 2) + Binary_sum_result
        carry = bit_sum // 2
    if carry != 0:
        Binary_sum_result = str(carry) + Binary_sum_result
    return Binary_sum_result

def binary_subtraction(first_num, second_num):
  # Pad the shorter binary string with zeros
  maxlen = max(len(first_num), len(second_num))
  first_num = first_num.zfill(maxlen)
  second_num = second_num.zfill(maxlen)
  # Initialize the result and the carry
  result = ''
  carry = 0
  # Loop through the bits from right to left
  for i in range(maxlen - 1, -1, -1):
    # Get the current bits of a and b
    x = int(first_num[i])
    y = int(second_num[i])
    # Compute the difference and the new carry
    diff = x - y - carry
    if diff == -1:
      # If the difference is -1, set the result bit to 1 and the carry to -1
      result = '1' + result
      carry = -1
    elif diff == 0:
      # If the difference is 0, set the result bit to 0 and the carry to 0
      result = '0' + result
      carry = 0
    else:
      # If the difference is 1, set the result bit to 1 and the carry to 0
      result = '1' + result
      carry = 0
  # If there is a negative carry, prepend a minus sign to the result
  if carry == -1:
    result = '-' + result
  # Return the result
  return result
### main program ###
print('========================================')
print('=========   Binary calculator  =========')
print('========================================\n\n')

main_menu = 0
print('Insert new numbers = 1 \nExit = 0')
main_menu = int(check_number(main_menu))
while main_menu == 1:
    if main_menu == 0:
        break
    
    first_num = 0
    print('\nPlease insert the first binary number :')
    first_num = check_number(first_num)

    operation = 0
    ### Ask the user what operation he wants
    print('\nplease select the operation')
    print("Compute one's complement = 1 \nCompute two's complement = 2")
    print('addition = 3 \nsubtraction = 4')
    operation = check_choice(operation)
    while operation == '1':
        result = ones_complement(first_num)
        print(f"one's complement of {first_num} is : {result}")
        break
    while operation == '2':
        result = twos_complement(first_num)
        print(f"Two's complement of {first_num} is : {result}")
        break
    while operation == '3':
        second_num = 0
        print('\nPlease insert the second binary number :')
        second_num = check_number(second_num)
        result = binary_addition(first_num, second_num)
        print(f'Addition of {first_num} and {second_num} is : {result}')
        if len(result) > len(first_num) and len(result) > len(second_num) :
            print('The result is overflow')
        break
    while operation == '4':
        second_num = 0
        print('\nPlease insert the second binary number :')
        second_num = check_number(second_num)
        if len(first_num) != len(second_num) :
           first_edit = ones_complement(first_num)
           second_edit = ones_complement(second_num)
           result = binary_subtraction(first_edit, second_edit)
           print(f'Subtraction of {first_num} and {second_num} is : {result}')
        else:
           result = binary_subtraction(first_num, second_num)
           print(f'Subtraction of {first_num} and {second_num} is : {result}')    
        break
    print('\nInsert new numbers = 1 \nExit = 0')
    main_menu = int(input())

# Yousef Hosni El-shiref    # 20231210
# Mohamed Hisham Gaber      # 20230359  
