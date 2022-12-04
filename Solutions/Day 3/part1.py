import string

# upper_case_alphabet = string.ascii_uppercase nvm don't need this
lower_case_alphabet = string.ascii_lowercase
priority_sum = 0

with open("Day 3/runsacks.txt", "r") as runsacks:
    for runsack in runsacks.readlines():
        # remove the \n at end
        runsack = runsack.removesuffix("\n")
        compartment_1, compartment_2 = runsack[:len(
            runsack)//2], runsack[len(runsack)//2:]  # divide in half
        for item in compartment_1:
            if item in compartment_2:
                ind = lower_case_alphabet.index(item.lower())
                if item in lower_case_alphabet:
                    priority_sum += ind + 1
                else:
                    priority_sum += ind + 27
                break


print(priority_sum)
