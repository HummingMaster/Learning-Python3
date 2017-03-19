
while True:
    try:
        user = int(input("enter a number: "))
        print(18/user)
        break
    except ZeroDivisionError:
        print("You can't divide by zero")
    except ValueError:
        print("You should only enter numbers")
    finally:
        print("Don't use except without specification like except:")
