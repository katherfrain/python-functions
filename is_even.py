def is_even(testnumber):
    if testnumber % 2 == 0:
        return True
    else:
        return False

def is_odd(testnumber):
    if not is_even(testnumber):
        return True
    else:
        return False

even_or_odd = int(input("Please enter an integer value so I can test if it is even or odd. "))
evenB = is_even(even_or_odd)
oddB = is_odd(even_or_odd)
print(f"It is {evenB} that the number is even, and {oddB} that the number is odd.")

def ask_for_list():
    firstlist = []
    while True:
        if not firstlist:
            firstlist.append(int(input("Alright, buttercup. Gimme the first integer on your list. ")))
        else:
            yn = input("Would you like to keep adding numbers? Yes or no: ")
            yn.lower()
            if yn == "yes":
                firstlist.append(int(input("Alright, hit me with another integer: ")))
            else:
                print("Done with the process? That's fine. Now we can test your integers for evenness or oddity.")
                break
    return firstlist

def only_evens(even_list):
    evenlist = []
    for x in even_list:
        if is_even(x) == True:
            evenlist.append(x)
    return evenlist

def only_odds(odd_list):
    oddlist = []
    for x in odd_list:
        if is_even == False:
            oddlist.append(x)
    return oddlist

#firstlist = []

print(f"Of the numbers you have entered, {only_evens(ask_for_list())} are even.")