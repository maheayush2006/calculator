print("Conversion : Decimal to Binary\n")
while True:
    start = int(input("Enter Start Point: ")) # Start Point 
    end = int(input("Enter End Point: ")) # End point 

    

    if (start > end):
        start,end = end , start
    # else:
    #     start ,end  = start ,end
    elif(start == end):
        binary = bin(start)[2:]
        print(f"\nDecimal number : {start}\nBinary number : {binary} \n")
        break
    choice = input("Enter your choice for bit (0 or 1) : ")
    repetition = int(input("Enter no.of repetion you want to search for: "))


    if choice in ["0", "1"]:
        num = choice

        data_array =[]
        binary_array = [] #store decimal numbers which have 4 time one in their binary

        binary_count = 0
        for i in range(start,end+1):
            binary = bin(i)[2:] # converts decimal to binary and removes 0b from the result
            data_array.append(binary) # add each binary to an array

        for k,i in enumerate(data_array,start = 1): # k return the index of the element and i stores the value of or the corresponding element from the array
            count = 0
            for j in i:
                if j == num:
                    count += 1

            if count == repetition:
                print(f"\nDecimal number : {k}\nBinary number : {i} \n")
                binary_array.append(k) #add decimal to binary_array

        print(f"Total number of such cases are: {len(binary_array)}\n")
        print(binary_array)  # optional.... if you want to see decimal number which 

    else:
        print("Enter 0 or 1 only !!!!!!")
    option = input("Do you want to continue? (Y/N)")
    print("\n")
    if option.lower() in ["yes","y"]:
        continue
    else:
        break