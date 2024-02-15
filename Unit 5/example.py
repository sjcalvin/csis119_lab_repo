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

def circle_area (radius, pi):
    '''
    Function calculates the area of a circle.

    params:
        radius: radius length
        pi: value of pi.
    '''

    # Calculate the area of the circle.
    area = pi * (radius ** 2)

    return area

def circle_area2 (radius, pi = 3.1415):
    '''
    Function calculates the area of a circle.

    params:
        radius: radius length
        pi: value of pi.
    '''

    # Calculate the area of the circle.
    area = pi * (radius ** 2)

    return area

def add_any_number_of_numbers (*args):
    '''
    Function addes any number of numbers together.
    '''

    # Define an iterator.
    n = 0

    # Loop through the arguments and add them together.
    for a in args:

        n += a

    return n

numbers = [3, 6, 9, 12, 15]

def cube(list):
    '''
    Function cubes the list of numbers.
    '''

    # Create an empty list.
    triples = []

    # Loop through the list and cube the numbers.
    for n in list:

        triples.append(n**3)

    return triples

def main():

    number = multiply_by_pi(6)
    print(number)

if __name__ == "__main__":

    main()

