
user_name = input("Enter your name: ")


def func_name(your_name):
    func_str = "Hey, This will print out next to your name " + your_name
    return func_str
# Now we call the function
print(func_name(user_name))

# Function with multiple parameters


def two_number_func(num1, num2):
    total = num1 + num2
    return total

num_var1 = 7
num_var2 = 14
print(two_number_func(num_var1, num_var2))

# Function with flexible parameters
# *args is for unknown number of parameters
# anything can be used like *para/ *unl but *args is more common between python developers


def numbers_func(*args):
    sum_ = 0
    for number_ in args:
        sum_ = sum_ + number_
    print(sum_)
num1 = 7
num2 = 7
num3 = 6
num4 = 5
numbers_func(num1, num2, num3, num4)
numbers_func(num3, num4)


def info(name ='', age ='', job=''):
    print("Your name is", name, "and you are", age, "years old and you work as a", job)

my_info = ['Ghaith', '20', 'Programmer']
info(*my_info)
