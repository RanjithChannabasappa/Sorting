# Bubble Sort
# V1.0
"""
This Script will perform Bubble Sort for the User given sequence
"""

# Collect the user data
BUBBLE_LIST = []
USER_INPUT = input("Please enter the numbers to do bubble sort:\n").split()
ORDER = input("Please enter Yes for ascending order or No for descending order: ").lower()

# Converting STRING to INT
for i in USER_INPUT:
    BUBBLE_LIST.append(int(i))
# print("Int converted list:", bubble_list)

# Starting Bubble Sorting
RANGE_R = len(BUBBLE_LIST)

for i in range(RANGE_R-1):
    for j in range(RANGE_R-1):
        if ORDER == "yes" and BUBBLE_LIST[j] > BUBBLE_LIST[j+1]:
            BUBBLE_LIST[j], BUBBLE_LIST[j+1] = BUBBLE_LIST[j+1], BUBBLE_LIST[j]
        elif ORDER == "no" and BUBBLE_LIST[j] < BUBBLE_LIST[j+1]:
            BUBBLE_LIST[j], BUBBLE_LIST[j + 1] = BUBBLE_LIST[j + 1], BUBBLE_LIST[j]
print("Sorted Bubble List:", BUBBLE_LIST)
