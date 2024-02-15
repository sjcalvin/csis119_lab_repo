# Initial parameter values.
serving_cost = 1.00
labor_rate = 7.50
shop_rental = 800
utilities = 150
advertising = 100
servings_per_month = 1000
selling_price = 4.00

# Function to display menu.
def display_menu():
    '''
    Function displays the menu with the current parameter values.
    '''
    
    # Print out the menu.
    print('Expenses:')
    print('1. Cost per serving:', serving_cost)
    print('2. Labor rate per hour:', labor_rate)
    print('3. Shop rental per month:', shop_rental)
    print('4. Utilities per month:', utilities)
    print('5. Advertising budget per month:', advertising)
    print()
    print('Income:')
    print('6. Selling price (each):', selling_price)
    print('7. Servings sold per month:', servings_per_month)
    print()
    print('Analysis:')
    print('8. Profit/Loss Calculation')
    print('9. "What If" analysis with 10% variance')
    print('10. Find Break-Even')
    print()
    print('Enter Selection (0 to Exit):')

# Function to update the values.
def update_values(selection):
    '''
    Function updates the values based on user input.
    '''

    # Import the global variables into the function's scope.
    global serving_cost, labor_rate, shop_rental, utilities, advertising, selling_price, servings_per_month

    # If the selection equals 1.
    if selection == 1:

        # Save the user input value for serving cost.
        serving_cost = float(input('Enter Serving Cost: '))

    # If the selection equals 2.
    elif selection == 2:

        # Save the user input value for labor rate.
        labor_rate = float(input('Enter Labor Rate: '))

    # If the selection equals 3.
    elif selection == 3:

        # Save the user input value for monthly shop rental.
        shop_rental = float(input('Enter Monthly Rent: '))

    # If the selection equals 4.
    elif selection == 4:
        
        # Save the user input value for monthly utilities.
        utilities = float(input('Enter Monthly Utilities: '))

    # If the selection equals 5.
    elif selection == 5:

        # Save the user input value for monthly advertising.
        advertising = float(input('Enter Monthly Advertising Budget: '))

    # If the Selection equals 6.
    elif selection == 6:

        # Save the user input value for the selling price.
        selling_price = float(input('Enter Selling Price: '))

    # If the selection equals 7.
    elif selection == 7:

        # Save the user input value for servings per month.
        servings_per_month = int(input('Enter Servings per month: '))

# Function to calculate expenses.
def calculate_expenses():
    '''
    Function calculates the expenses.
    '''

    # Total expenses equal the quantity of serving cost times the number of servings per month,
    #     plus the labor rate times 8 hours times 6 days times four weeks,
    #     plus monthly shop rental, plus monthly utilities, plus advertising.
    total_expenses = (serving_cost * servings_per_month) + (labor_rate * 8 * 6 * 4) + shop_rental + utilities + advertising

    # Return the total expenses.
    return total_expenses

# Function to calculate income.
def calculate_income(selling_price):
    '''
    Function calculates income.
    '''

    # Total income equals selling price times the servings per month.
    total_income = selling_price * servings_per_month

    return total_income

# Function to calculate profit / loss.
def calculate_profit_loss(income, expenses):
    '''
    Function calculates profit and loss.
    '''

    # Calculate the profit loss value
    profit_or_loss = income - expenses

    #return the result.
    return profit_or_loss

# Function to calculate Percent differential for task three.
def calculate_differential(income, expenses, transaction_type):
    '''
    Function calculates the percent differential.
    '''

    # Define a list of percents.
    percents = [
        -0.10, 
        -0.08,
        -0.06,
        -0.04,
        -0.02, 
         0.00, 
         0.02, 
         0.04, 
         0.06, 
         0.08, 
         0.10
    ]

    # Loop through the percents.
    for p in percents:

        # If transaction type equals expenses.
        if transaction_type == 'expenses':

            # Calculate the new expenses value.
            new_expenses = expenses + (expenses * p)

            # Calculate the new profit loss value.
            profit_loss = income - new_expenses

            # Format and pring the outcome.
            print(f'Percent: {int(p * 100)} Expenses: {round(new_expenses, 2)} Profit/Loss: {round(profit_loss, 2)}')

        # If transaction type equals income.
        elif transaction_type == 'income':

            # Calculate the new income value.
            new_income = income + (income * p)

            # Calculate the new profit loss value.
            profit_loss = new_income - expenses

            # Format and print the outcome.
            print(f'Percent: {int(p * 100)} Income: {round(new_income, 2)} Profit/Loss: {round(profit_loss, 2)}')

# Function to handle the what if analysis.
def what_if_analysis(income, expenses):
    '''
    Function calculates and prints variance of expenses and income 
        from -10% to 10%.
    '''

    print()
    print('Varying the Expenses From -10% to +10%:')
    
    # Expense Percent Differential
    calculate_differential(income, expenses, 'expenses')

    print()
    print('Varying the Income From -10% to +10%:')

    # Income Percent Differential
    calculate_differential(income, expenses, 'income')
    print()

# Function to find the break even point.
def calculate_break_even(income, expenses, selling_price):
    '''
    Function detects the "Break-even" point, where the sign of Profit/Loss changes.
    '''
    
    # Save the selling price and initial profit loss value.
    price  = selling_price
    profit_loss = calculate_profit_loss(income, expenses)

    # Check whether profit loss is positive.
    if profit_loss >= 0:

        # Loop decreases the selling price until profit loss becomes negative.
        while profit_loss >= 0:

            # Decrease the price by 10 cents per iteration.
            price -= 0.1

            # Then calculate a new income.
            new_income = calculate_income(price)

            # Lastly get a profit loss with the new income value.
            profit_loss = calculate_profit_loss(new_income, expenses)

    # If the profit loss is negative...
    elif profit_loss < 0:

        # Loop increaes the selling price until profit loss becomes positive.
        while profit_loss < 0:

            # Increase the price by 10 cents per iteration.
            price += 0.1

            # Then calculate a new income.
            new_income = calculate_income(price)

            #Lastly get a lrofit loss with the new income.
            profit_loss = calculate_profit_loss(new_income, expenses)

    # Finally print te result.
    print(f'Break-Even occurs when a selling price of: {round(price, 2)}')

# Main Program.
def main():
    '''
    Main program function.
    '''

    while True:
        '''
        While loop diplays current values of the parameters.
        It then takes input, and performs functionality accordingly.
        '''
        
        # Run the Menu Function
        display_menu()

        # Save the user entered value as a variable.
        selected_value = int(input())

        # Calculate income and expenses and round them to two decimal places.
        income = calculate_income(selling_price)
        income = round(income, 2)

        expenses = calculate_expenses()
        expenses = round(expenses, 2)

        # If the input is 0 exit the program.
        if selected_value == 0:

            # Stop the loop.
            break
        
        # Update the various values if the selection is 1 through 7.
        elif 1 <= selected_value <= 7:
            
            # Run the update values function with the  enetered value.
            update_values(selected_value)

        # If the selection is 8, calulate the profit loss.
        elif selected_value == 8:

            # Call the profit/loss function and then calculate the profit loss per serving.
            profit_loss = calculate_profit_loss(income, expenses)
            profit_loss_per_serving = profit_loss / servings_per_month

            # If the profit/loss it positive.
            if profit_loss >= 0:
                
                # Print out the message with positive.
                print(f'The shop will have a profit of {round(profit_loss, 2)}, or {round(profit_loss_per_serving, 2)} per serving.')

            else:
                
                # Print out the message with negative.
                print(f'The shop will have a loss of {profit_loss}, or {profit_loss_per_serving} per serving.')

        # If the selection is 9, perform the what if analysis.
        elif selected_value == 9:

            # Call the what-if analysis function.
            what_if_analysis(income, expenses)

        # If the selection is 10, find the break-even point.
        elif selected_value == 10:
            
            # Call the break even function.
            calculate_break_even(income, expenses, selling_price)

        # Otherwise...
        else:

            # Tell the user that they made an invalid selection.
            print('Invalid Selection. Please enter a value between 0 and 7...')

# Tell the interpreter to run this block first.
if __name__ == "__main__":

    main()
