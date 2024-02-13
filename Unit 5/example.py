#def sample_function (variable):
#    '''
#    This function prints the variable and then returns the variable plus 2.
#    '''
#
#    print(variable)
#
#    return variable

pi = 3.14


def multiply_by_pi (number):
    '''
    This function multiplies a number by the global variable pi.
    '''

    # Import global variable into function's scope
    global pi

    value = round(float(number) * pi, 2)

    return value

#number = multiply_by_pi(5)

#print(number)

def main():

    number = multiply_by_pi(6)
    print(number)

if __name__ == "__main__":

    main()