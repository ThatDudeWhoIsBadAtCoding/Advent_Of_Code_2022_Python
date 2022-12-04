count = 0


def check_if_inside(list1, list2):
    for i in list1:
        if i not in list2:
            return False
    return True


with open("Day 4/sections.txt", "r") as pair_sections:
    for pair in pair_sections.readlines():
        sections = pair.split(",")
        nums1 = sections[0].split("-")
        nums1 = list(range(int(nums1[0]), int(nums1[1]) + 1))
        nums2 = sections[1].split("-")
        nums2 = list(range(int(nums2[0]), int(nums2[1]) + 1))
        if check_if_inside(nums1, nums2):
            count += 1
        elif check_if_inside(nums2, nums1):
            count += 1


print(count)
