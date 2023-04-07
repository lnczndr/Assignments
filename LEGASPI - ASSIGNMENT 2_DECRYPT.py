#LEGASPI, LANA CAZANDRA U. - BSCPE 1-5

moredata = "yes"
while moredata == "yes":
    user = input("Enter username: ")
    print ("\nWelcome to the program " + user, "!")

    print ("PROGRAM #2: DECRYPTION".center(50,("-")))

    #input
    inp_phrase = input("Enter the phrase you want to decode: ")
    final_output = ""
    #check each char
    for i in range (len(inp_phrase)):
    # a = *
        if inp_phrase[i] == "*":
            final_output += "a"
    # e = &
        elif inp_phrase[i] =="&":
            final_output +="e"
    # i = #
        elif inp_phrase[i] == "#":
            final_output += "i"
    # o = +
        elif inp_phrase[i] == "+":
            final_output += "o"
    # u = !
        elif inp_phrase[i] == "!":
            final_output += "u"
        else:
            final_output += inp_phrase[i]
    #output
    print ("\nOUTPUT: " + final_output)
    
    print ("\nNOTE: If you wanted to run the program again, strictly answer 'yes' in lowercase. Failure to do so will end the program.\n")
    moredata = str(input("Would you like to run the program again?: "))
