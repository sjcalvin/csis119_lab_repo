# Global variable
multiplier_amount = 1000000

# Utility function to format number into currency format
def format_currency(number):
    return "{:.2f}".format(number)

# Function to calculate gains for a given amount
def calculate_gains(amount_inv=0.0):
    global multiplier_amount
    
    # Base amount gain margin
    gain_margin = 0.001  # 0.1%
    
    # Declare variables for total gains and total amount
    total_gains = 0.0
    total_amount = 0.0
    
    # Check if the amount is greater than the minimum value (1000)
    if amount_inv > 1000:
        
        # Check if the amount is greater than the multiplier amount
        if amount_inv > multiplier_amount:
            # Calculate the multiplier based on the amount invested
            multiplier = (amount_inv - 1000) // multiplier_amount
            
            # Update the gain margin by the multiplier mod
            gain_margin += multiplier * 0.01
        
        # Calculate the total amount of gains
        total_gains = amount_inv * gain_margin
        
        # Calculate the total amount plus the gain margin
        total_amount = amount_inv + total_gains
    
    # Return the gains, the full amount, and the gain margin
    return float(format_currency(total_gains)), float(format_currency(total_amount)), gain_margin

# Function to calculate gains over a period of time
def calculate_gains_over_time(amount_inv=0.0, period=12):
    # Call the base `calculate_gains` function to estimate the gains for the first period
    total_gains, total_amount, gain_margin = calculate_gains(amount_inv)

    # Loop through the specified period to calculate the gain of each month
    for _ in range(1, period):
        # Call the function to update the value based on the period inside the loop and the updated amount
        new_amount = calculate_gains(total_amount)[1]
        total_amount = float(new_amount)  # Update the `total_amount` variable
    
    # Return the final amount after the specified period
    return float(format_currency(total_amount))

# Main program.
def main():

    # Collect user input to determine how to proceed.
    proceed = input('Please enter (c) to calculate gains, or (q) to quit: ')

    # Infinite Loop to drive the menu.
    while True:
        
        # If the user wants to calculate...
        if proceed == 'c':

            # Get user input for initial investment amount.
            investment = input('Please enter an initial investment amount: ')
            time_frame = input('Please enter a time frame to calculate over: ')

            # Test if the input can be converted into a number format. If it can...
            if investment.isdigit() and time_frame.isdigit():

                # Convert it into a float.
                investment = float(investment)
                time_frame = int(time_frame)

            # If not...
            else:

                # Inform the user that they didn't enter a numerical value and try again.
                print('Some user input was not a numerical value.')
                continue

            gains_over_time = calculate_gains_over_time(investment, time_frame)

            print(f'The expected gains over these {str(time_frame)} months are, ${format_currency(gains_over_time - investment)},')
            print(f'leaving the invester with ${gains_over_time} at the end of the term.')

            proceed = input('Please indicate how you would like to proceed. Enter (c) for calculating a new investment, or (q) to quit: ')

        # Exit the menu if the user wants to quit.
        elif proceed == 'q':

            # Break out of the loop exiting the program.
            break
        
        # If the user enters anything else,
        else:
            
            # Get new instructions to proceed.
            proceed  = input('You have made an invalid entry. Please enter (c) to calculate gains, or (q) to quit: ')

if __name__ == "__main__":

    main()


        