
number_set = {1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8}
for number in number_set:
    print(number)

name_set = {"Ghaith", "Anees", "Eyad", "Resan", "Ghaith", "Anees", "Eyad", "Resan", "Oday"}
for name in name_set:
    print(name)

for number in range(1, 12):
    if number == 11:
        continue
    print(number)

loop_condition = 5
while loop_condition >= 0:
    print("Do this for as many times as the loop condition")
    loop_condition -= 1
# This is the same as loop_condition = loop_condition - 1
# By the way, this is a comment
