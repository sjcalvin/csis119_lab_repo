import sys

multiplier_amount = 1000000


def calculate_gains(amount_inv=0.0):
    """Calculating the return gains of an investment."""
    
    # base amount gain margin
    gain_margin = 0.001  # 0.1%

    # variables to store total gains and total amount
    total_gains = 0.0
    total_amount = 0.0

    # check if the amount is greater than the minimum value (1000)
    if amount_inv > 1000:
        # check whether the invested amount is greater than the multiplier amount
        if amount_inv > multiplier_amount:
            # calculate the number of times the multiplier is surpassed
            multiplier_mod = int((amount_inv - multiplier_amount) / multiplier_amount)
            
            # update the `gain_margin` by the multiplier mod
            gain_margin += multiplier_mod * 0.01
        
        # calculate the total amount of gains
        total_gains = amount_inv * gain_margin 
        
        # calculate the total amount plus the gain margin
        total_amount = amount_inv + total_gains

    # return the gains, the full amount, and the gain margin
    return total_gains, total_amount, round(gain_margin, 3)

def main():

    tg, ta, gm = calculate_gains(amount_inv = float(sys.argv[1]))

    print(tg, ta, gm)

if __name__ == '__main__':

    main()