from cal_fun import do_addition,do_subtraction
from multiply import do_multiplication
from area import calculate_area_rectangle
def main():
    print("Welcome yo the calculator app")
    print("""
          /nselect the function
          1. Add
          2. Subtract
          3. mulptiply
          4. area
          """)

    user_input = input("select the function")

    a = int(input('value of A'))
    b = int(input('value of B'))


    if user_input == '1':
        result = do_addition(a,b)
    elif user_input == '2':
        result = do_subtraction(a,b)
    elif user_input == '3':
        result = do_multiplication(a,b)
    elif user_input == '4':
        result = calculate_area_rectangle(a,b)

    print('Result:',result)

if __name__ == '__main__':
    main()    