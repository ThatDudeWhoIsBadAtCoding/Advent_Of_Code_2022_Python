import string

# upper_case_alphabet = string.ascii_uppercase nvm don't need this
lower_case_alphabet = string.ascii_lowercase
priority_sum = 0
group_ind = 1
curr_group = []


def find_common(group: list) -> int:
    grp_priority = 1
    for item in group[0]:
        if item in group[1] and item in group[2]:
            ind = lower_case_alphabet.index(item.lower())
            if item in lower_case_alphabet:
                grp_priority += ind
            else:
                grp_priority += ind + 26
            break
    return grp_priority


with open("Day 3/runsacks.txt", "r") as runsacks:
    for i, runsack in enumerate(runsacks.readlines()):
        # remove the \n at end
        runsack = runsack.removesuffix("\n")
        if group_ind > 3:
            priority = find_common(curr_group)
            curr_group = []
            curr_group.append(runsack)
            group_ind = 2
            priority_sum += priority
        else:
            curr_group.append(runsack)
            group_ind += 1
    # add the final group since it does not get added cuz loop ends
    priority = find_common(curr_group)
    priority_sum += priority


print(priority_sum)
