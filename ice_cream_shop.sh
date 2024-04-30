#!/bin/bash

# Initial parameter values.
serving_cost=1.00
labor_rate=7.50
shop_rental=800.00
utilities=150.00
servings_per_month=1000
selling_price=4.00

# Main program.
function main() {
    # Funciton displays the menu with the current parameter values.

    breaker=true

    while $breaker; do
        
        menu="Expenses:
1. Cost per serving: $serving_cost
2. Labor rate per hour: $labor_rate
3. Shop rental per month: $shop_rental
4: Utilities per month: $utilities
5. Advertising budget per month: $advertising

Income:
6. Selling price: $selling_price
7. Servings sold per month: $servings_per_month

Analysis:
8. Profit/Loss Calculation
9. "What-If" analysis with 10% variance
10. Find break-even

Enter Selection (0 to Exit)"

    # Display menu and get user input.
    echo "$menu"
    
    read -p "Enter your selection: " selection

    income=$(calculate_income $selling_price)

    expenses=$(calculate_expenses)

    # Case statement for actions.
    case $selection in

        # If the selected value is zero, then break the loop.
        0)
            breaker=false
            echo "Exiting program..."
            ;;

        # Update the various values if the selection is 1 through 7.
        [1-7])

            update_values $selection
            ;;

        # If the selection is 8, calculate the profit loss.
        8)
            profit_loss=$(calculate_profit_loss $income $expenses)
            echo "The profit/loss is $profit_loss"
            ;;

        # If the selection is 9, perform the what if analysis.
        9)
            what_if_analysis $income $expenses
            ;;

        # If the selection is 10, find the break-even point.
        10)
            break_even $income $expenses $selling_price
            ;;

        *)
            echo "Invalid selection. Please try again."
            ;;

    esac
    done
}

# function to update the values.
function update_values() {
    # Function updates the values based on user input.

    # If selection equals 1...
    if [ $1 -eq 1 ]; then

        read -p "Enter the new serving cost: " serving_cost

    elif [ $1 -eq 2 ]; then

        read -p "Enter the new labor rate: " labor_rate

    elif [ $1 -eq 3 ]; then

        read -p "Enter the new shop rental: " shop_rental

    elif [ $1 -eq 4 ]; then

        read -p "Enter the new utilities: " utilities

    elif [ $1 -eq 5 ]; then

        read -p "Enter the new advertising budget: " advertising

    elif [ $1 -eq 6 ]; then

        read -p "Enter the new selling price: " selling_price

    elif [ $1 -eq 7 ]; then

        read -p "Enter the new servings per month: " servings_per_month

    fi

}

# Function to calculate income.
function calculate_income() {
    # Function calculates income.

    total_income=$(echo "$1 * $servings_per_month" | bc)

    echo $total_income

}

# Funciton to calculate expenses.
function calculate_expenses() {
    # Function calculates expenses.

    total_expenses=$(echo "($serving_cost * $servings_per_month) + ($labor_rate * 8 * 6 * 4) + $shop_rental + $utilities + $advertising" | bc)

    echo $total_expenses

}

function calculate_profit_loss() {
    # Function calculates profit or loss.

    profit_loss=$(echo "$1 - $2" | bc)

    echo $profit_loss

}

# Function to calculate percent differential.
function calculate_differential() {
    # Function calculates the percent differential.

    percents=(-0.10 -0.08 -0.06 -0.04 -0.02 0.00 0.02 0.04 0.06 0.08 0.10)

    for percent in "${percents[@]}"; do

        # If transaction type is expenses...
        if [ "$3" == "expenses" ]; then

            new_expenses=$(echo "$2 * (1 + $percent)" | bc)

            new_profit_loss=$(calculate_profit_loss $1 $new_expenses)

            echo "With a $percent change in expenses, the new profit/loss is $new_profit_loss"

        else

            new_income=$(echo "$1 * (1 + $percent)" | bc)

            new_profit_loss=$(calculate_profit_loss $new_income $2)

            echo "With a $percent change in income, the new profit/loss is $new_profit_loss"

        fi
    done
}

# Function to handle the what if analysis.
function what_if_analysis() {
    # Function calculates and prints the variance or expenses and income from -10% to 10%.

    message="Varying the Expenses from -10% to 10%"

    echo "$message"

    # Expense Percent Differential.
    calculate_differential $1 $2 expenses

    message="Varying the Income from -10% to 10%:"

    echo "$message"

    # Income Percent Differential.
    calculate_differential $1 $2 income

}

function break_even() {
    # Function determines the break-even point, where the sign of the profit/loss changes.

    # Save the selling price and initial profit/loss value.
    price=$3
    profit_loss=$(calculate_profit_loss $1 $2)

    # Check whether the profit-loss value is positive.
    if [ $(echo "$profit_loss >= 0" | bc) -eq 1 ]; then
    
        # While the profit-loss value is positive...
        while [ $(echo "$profit_loss >= 0" | bc) -eq 1 ]; do
    
            # Decrease the selling price by 0.01.
            price=$(echo "$price - 0.01" | bc)
    
            # Calculate the new income.
            new_income=$(calculate_income $price)
    
            # Calculate the new profit/loss.
            profit_loss=$(calculate_profit_loss $new_income $2)
    
        done
    
    else
    
        # While the profit-loss value is negative...
        while [ $(echo "$profit_loss < 0" | bc) -eq 1 ]; do
    
            # Increase the selling price by 0.01.
            price=$(echo "$price + 0.01" | bc)
    
            # Calculate the new income.
            new_income=$(calculate_income $price)
    
            # Calculate the new profit/loss.
            profit_loss=$(calculate_profit_loss $new_income $2)
    
        done

        message="The break-even point is at a selling price of $price per serving."

        echo $message
    
    fi
}

# Call the main function.
main
