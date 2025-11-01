def calculate_bond_price(face_value, coupon_rate, yield_to_maturity, years_to_maturity):
    """
    Calculate the price of a coupon bond with semi-annual payments.

    Parameters:
    -----------
    face_value : float
        The face value (par value) of the bond
    coupon_rate : float
        Annual coupon rate (as a decimal, e.g., 0.05 for 5%)
    yield_to_maturity : float
        Annual yield to maturity (as a decimal, e.g., 0.04 for 4%)
    years_to_maturity : float
        Number of years until the bond matures

    Returns:
    --------
    float : The current price of the bond
    """

    # Convert annual rates to semi-annual
    coupon_payment = (coupon_rate * face_value) / 2  # Semi-annual coupon payment
    ytm_per_period = yield_to_maturity / 2  # Semi-annual yield
    num_periods = int(years_to_maturity * 2)  # Total number of semi-annual periods

    # Calculate present value of coupon payments
    pv_coupons = 0
    for period in range(1, num_periods + 1):
        pv_coupons += coupon_payment / ((1 + ytm_per_period) ** period)

    # Calculate present value of face value
    pv_face_value = face_value / ((1 + ytm_per_period) ** num_periods)

    # Total bond price
    bond_price = pv_coupons + pv_face_value

    return bond_price


def calculate_bond_price_formula(face_value, coupon_rate, yield_to_maturity, years_to_maturity):
    """
    Calculate bond price using the closed-form formula (more efficient).

    Formula:
    Bond Price = C × [(1 - (1 + y)^-n) / y] + FV × (1 + y)^-n

    Where:
    C = Semi-annual coupon payment
    y = Semi-annual yield
    n = Number of semi-annual periods
    FV = Face value
    """

    # Convert annual rates to semi-annual
    C = (coupon_rate * face_value) / 2  # Semi-annual coupon payment
    y = yield_to_maturity / 2  # Semi-annual yield
    n = int(years_to_maturity * 2)  # Total number of semi-annual periods
    FV = face_value

    # Apply the formula
    if y == 0:  # Special case: zero yield
        bond_price = C * n + FV
    else:
        # Present value of coupon payments (annuity)
        pv_coupons = C * ((1 - (1 + y) ** (-n)) / y)

        # Present value of face value
        pv_face_value = FV * ((1 + y) ** (-n))

        # Total bond price
        bond_price = pv_coupons + pv_face_value

    return bond_price


# Example usage
if __name__ == "__main__":
    # Define bond parameters
    face_value = 1000
    coupon_rate = 0.04375
    #yield_to_maturity = 0.04 + 0.000352*6.5*2
    yield_to_maturity = 0.05
    years_to_maturity = 10

    # Calculate bond price using both methods
    price_method1 = calculate_bond_price(face_value, coupon_rate, yield_to_maturity, years_to_maturity)
    price_method2 = calculate_bond_price_formula(face_value, coupon_rate, yield_to_maturity, years_to_maturity)

    print(f"Bond Parameters:")
    print(f"  Face Value: ${face_value:,.2f}")
    print(f"  Annual Coupon Rate: {coupon_rate * 100:.2f}%")
    print(f"  Annual Yield to Maturity: {yield_to_maturity * 100:.2f}%")
    print(f"  Years to Maturity: {years_to_maturity}")
    print(f"\nSemi-Annual Payment Details:")
    print(f"  Semi-Annual Coupon Payment: ${(coupon_rate * face_value) / 2:,.2f}")
    print(f"  Number of Periods: {int(years_to_maturity * 2)}")
    print(f"  Semi-Annual Yield: {yield_to_maturity / 2 * 100:.2f}%")
    print(f"\nBond Price (Method 1 - Loop): ${price_method1:,.2f}")
    print(f"Bond Price (Method 2 - Formula): ${price_method2:,.2f}")

    # Show that bond trades at premium when coupon rate > yield
    print(
        f"\nAnalysis: The bond trades at a {'premium' if price_method1 > face_value else 'discount' if price_method1 < face_value else 'par'}")
    print(f"Price/Par Ratio: {price_method1 / face_value:.4f}")