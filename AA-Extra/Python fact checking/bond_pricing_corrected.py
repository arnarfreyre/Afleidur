''' Corrected Bond Pricing Calculation '''

nominal = 1000
annual_coupon_rate = 0.04375
coupon_amount = nominal * annual_coupon_rate / 2  # $21.875 semi-annual
time_to_maturity = 10  # years
total_periods = 20  # semi-annual periods

# Calculate present value using different approaches
print("=" * 60)
print("BOND PRICING COMPARISON")
print("=" * 60)

# Approach 1: Annual compounding (as in solutions.txt)
print("\nApproach 1: Annual Compounding")
print("-" * 40)
pv_annual = 0
for period in range(1, total_periods + 1):
    t = period * 0.5  # time in years
    
    # Calculate annual interest rate
    if t <= 7:
        annual_rate = 0.04 + 0.000352 * (t - 0.5) * 2
    else:
        annual_rate = 0.04 + 0.000352 * (7 - 0.5) * 2  # = 0.044576
    
    # Discount using annual compounding
    discount_factor = (1 + annual_rate) ** t
    
    # Add coupon PV
    pv_annual += coupon_amount / discount_factor
    
    # Add principal at maturity
    if period == total_periods:
        pv_annual += nominal / discount_factor
        
    if period <= 3 or period >= 19:
        print(f"Period {period:2d} (t={t:4.1f}y): Rate={annual_rate:.4%}, "
              f"DF={(1+annual_rate)**t:.6f}, PV=${coupon_amount/discount_factor:.3f}")

print(f"\nBond Price (Annual Compounding): ${pv_annual:.2f}")

# Approach 2: Semi-annual compounding (standard for bonds)
print("\nApproach 2: Semi-Annual Compounding")
print("-" * 40)
pv_semiannual = 0
for period in range(1, total_periods + 1):
    t = period * 0.5  # time in years
    
    # Calculate annual interest rate
    if t <= 7:
        annual_rate = 0.04 + 0.000352 * (t - 0.5) * 2
    else:
        annual_rate = 0.04 + 0.000352 * (7 - 0.5) * 2  # = 0.044576
    
    # Discount using semi-annual compounding
    # For semi-annual: (1 + r/2)^(2*t) where r is annual rate, t is years
    semi_rate = annual_rate / 2
    discount_factor = (1 + semi_rate) ** (2 * t)
    
    # Add coupon PV
    pv_semiannual += coupon_amount / discount_factor
    
    # Add principal at maturity
    if period == total_periods:
        pv_semiannual += nominal / discount_factor
        
    if period <= 3 or period >= 19:
        print(f"Period {period:2d} (t={t:4.1f}y): Rate={annual_rate:.4%}, "
              f"Semi-rate={semi_rate:.4%}, DF={(1+semi_rate)**(2*t):.6f}, "
              f"PV=${coupon_amount/discount_factor:.3f}")

print(f"\nBond Price (Semi-Annual Compounding): ${pv_semiannual:.2f}")

# Approach 3: Python solver's incorrect method (for comparison)
print("\nApproach 3: Python Solver Method (Incorrect)")
print("-" * 40)
pv_wrong = 0
for period in range(1, total_periods + 1):
    t = period * 0.5
    
    if t <= 7:
        rate = 0.04 + 0.000352 * (t - 0.5) * 2
    else:
        rate = 0.04 + 0.000352 * (7 - 0.5) * 2
    
    # This is the error: using period instead of 2*t
    discount_factor = (1 + rate/2) ** period
    
    pv_wrong += coupon_amount / discount_factor
    if period == total_periods:
        pv_wrong += nominal / discount_factor
        
    if period <= 3 or period >= 19:
        print(f"Period {period:2d}: DF={(1+rate/2)**period:.6f}, "
              f"PV=${coupon_amount/discount_factor:.3f}")

print(f"\nBond Price (Wrong Method): ${pv_wrong:.2f}")

print("\n" + "=" * 60)
print("SUMMARY:")
print("  Solutions.txt (Annual Compounding):     ${:.2f}".format(pv_annual))
print("  Semi-Annual Compounding (Standard):     ${:.2f}".format(pv_semiannual))
print("  Python Solver (Incorrect):              ${:.2f}".format(pv_wrong))
print("=" * 60)