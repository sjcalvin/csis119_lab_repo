# Scenario

AppInvest is a mobile application that helps people save money and safely invest in a varied portfolio of investment vehicles. The app has helped thousands of people to accomplish their financial goals. To invest money in the app is simple: you open an account with at least $1,000 and you’re ready to go.

There are a number of investment apps currently available on the market, but AppInvest excels in some areas and offers a better service than its competitors. Some advantages of the app include setting a short-term financial goal to be achieved, as well as immediate access to the user’s funds. The company is planning on releasing a new feature that will enable investors to increase gains depending on the amount invested. In other words, the more money you put in the app, the greater your rate of return. You have been tasked with adding this functionality.

Initially, the investment engine has to be extended to allow for investors to increase their gain margin if they invest more money on the app.

The company has agreed internally that 1 million is a good starting point to trigger the increase of the gain margin. If the invested amount surpasses $1 million, then the gain margin will be increased by 1%. Similarly, if the invested amount is 5 million dollars, then the gain margin will be increased by 5% and so on, limited by a maximum of 100%.

The standard gain margin is 0.1% per month, plus 1% each time the amount surpasses increments of 1 million dollars. For example:

If the amount invested is $5,000,000 ($5 million), then the gain margin would be:
0.1% + 5% = 5.1%.

For this assessment, you will write a function that for a given invested amount will return that amount plus the calculated investment gains. If the given amount is greater than the $1 million threshold, the app will need to increase the rate of return 1% for every million dollars invested plus the original rate of 0.1%. Finally, you will implement the functionality to estimate (forecast) the return on investment over a time period.

In order for you to start this project, we will provide a function template that can be followed to solve this challenge. The code block below is a sample way that this project could be structured.

```python
# global variable


def calculate_gains(amount_inv=0.0):
    """ Calculating the return gains of an investment.


    # base amount gain margin


    if amount_inv > 1000:

        # check whether the invested amount is greater than the multiplier amount

            # gather the value of the division


            # update the `gain_margin` by the multiplier mod


        # calculate the total amount of gains


        # calculate the total amount plus the gain margin


        # return the gains, the full amount and the gain margin
```

Create a user-defined function called `calculate_gains()`, which receives the amount desired to be invested. Outside this function, create a global variable, `multiplier_amount` that would be accessible at any point in your code to store the "multiplier amount", which will be the amount that would trigger the increase on the gain margin in case the invested amount is greater than this value. In our case, this amount is set to 1 million.

Inside your function, create a variable to store the gain margin, which is **0.1**% by default. Also create variables for `total_gains` and `total_amount`, setting default values to **0**. After these declarations, the first thing to check is whether the amount invested is greater than 1000 (one thousand), which is the minimum application value to start using the app.

Next, check if the amount is greater than the multiplier value (1 million). If it is greater, then update the gain margin variable with the new gain margin and add the estimated amount to the original amount, otherwise just multiply the values to obtain the return on investment for the given amount.

Finally, you need to return the total gains amount, the amount invested updated with the return on investment added to it, as well as the gain margin (the ordering is important for testing purposes). To test your function, enter the following amount: **2000000** ($2 million).

To summarize:

• In the user-defined function declare a global variable inside the python file to store the multiplier amount.

• Declare a variable to store the gain margin.

• Declare variables to store the total gains and the total amount.

• Check if the amount is greater than the minimum value (which is 1000).

• Check if the amount is greater than the multiplier amount (which is 1000000).

• If so, update the gain margin.

• Calculate the total gains by multiplying the gain margin by the amount.

• Return the total gains, total updated amount, and gain margin.

Example:

```
Input :

calculate_gains(amount_inv=2000000)
```

```
Output:

(42000.0, 2042000.0, 0.021)

```

# Task #01

Create the function calculate_gains, which returns the total gains, total amount invested updated with the return on investment, and the gain margin.

Another functionality for the app is the ability to estimate the return on investment over a period of time. In order to implement this feature, you will have to update the investment calculator algorithm.

The base function to calculate the return on investment from Task 1 can be reutilized here to simplify our task. This feature will take into consideration a 12-month period by default.

To calculate the total amount earned over a period of time, you will have to loop through the n-months period, increase the amount for each period. The other rules from the previous task apply here as well.

For example: If you invest $3 million on the first month, and obtain a return of $93,000 dollars, then the amount to be invested in the second month is $3.093 million.

To summarize:

Loop over a period of 12 months to calculate the total for each period
Return the accumulated estimated value for a period of 12 months
Note that to calculate the accumulated value over a 12-month period do not just multiply the gain of every month by 12 (or n). In this case, the gain of every month is added to the original value, updating the amount to be invested in the subsequent month.

The following base code is given for you in the file calculate_gains_over_time.py:

def calculate_gains_over_time(amount_inv=0.0, period=12):
    """
    Calculating the return gains of a given amount invested based on a period of application.
    :param amount_inv: the money amount invested
    :param period: application period
    :return:
    """

    # call the base `calculate_gains` function to estimate the gains for the first period

    # calculate the first period before entering the loop

    # loop through the specified period to calculate the gain of each month

    # 1 to period-1 because the first period gains is already calculated above

        # call the function to update the value based on the period inside the loop and the updated amount

        new_amount = total_amount  # update the `new_amount` variable

    # return the final ammount
    return new_amount


print(calculate_gains_over_time(amount_inv=4000000, period=12))

# Task #02

Implement the calculate_gains_over_time function to calculate the total amount earned over a period of time.

## Make it your own

As the algorithm performs division of numbers with high precision, it is very common to see really big numbers after the period (for example: 1200.2300001), which is not desirable because of several reasons:

1. may cause confusion to some users when they see such big numbers;
2. uses more memory to store a bigger number;
3. it just does not make sense to display currency number in this format.

For this reason, you are going to implement a utility function to format any number into the appropriate currency format, using 2 decimal places.

For example:
The number 1200.2300001 would be became: 1200.23

> Take a look at the formatting options for python native.