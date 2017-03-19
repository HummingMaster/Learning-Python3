str_ = "This is a string"
another_str = 'This is also a string'

str_slice = str_[0]
print(str_slice)

another_str_slice = another_str[5:7]
print("\n" + another_str_slice + "\n")

this_is_list = ["0", "1", "2", "3"]
another_list = ['0', '1', '2', '3']
print(this_is_list[2] + another_list[1])

# This is another way using for loops
for str_loop_slice in another_str:
    print(str_loop_slice)

print('\n')
