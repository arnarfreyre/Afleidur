"""
Investigation of Q3c Duration Calculation Discrepancy
"""

import math

# Bond parameters
nominal = 1000
coupon_rate = 0.04375
coupon_payment = nominal * coupon_rate / 2
total_periods = 20
base_rate = 0.05

print("=" * 80)
print("Q3c DURATION CALCULATION INVESTIGATION")
print("=" * 80)

# Function to calculate bond price
def calculate_bond_price(annual_rate, periods=20):
    semi_rate = annual_rate / 2
    price = 0
    for period in range(1, periods + 1):
        pv = coupon_payment / (1 + semi_rate) ** period
        price += pv
        if period == periods:
            price += nominal / (1 + semi_rate) ** period
    return price

# Base price
pv0 = calculate_bond_price(base_rate)
print(f"\nBase bond price (5% rate): ${pv0:.2f}")

# Test different delta values
print("\n" + "=" * 60)
print("Testing Different Delta Values")
print("=" * 60)

deltas = [0.0001, 0.001, 0.01, 0.10]  # 1bp, 10bp, 100bp, 1000bp
delta_names = ["1 basis point", "10 basis points", "100 basis points", "1000 basis points"]

for delta, name in zip(deltas, delta_names):
    print(f"\nDelta = {delta} ({name}):")
    print("-" * 40)
    
    # Calculate prices
    pv_down = calculate_bond_price(base_rate - delta)
    pv_up = calculate_bond_price(base_rate + delta)
    
    print(f"  Rate down ({(base_rate-delta)*100:.2f}%): ${pv_down:.2f}")
    print(f"  Rate up ({(base_rate+delta)*100:.2f}%): ${pv_up:.2f}")
    
    # Calculate effective duration
    duration = (pv_down - pv_up) / (2 * pv0 * delta)
    
    print(f"  Price difference: ${pv_down - pv_up:.2f}")
    print(f"  Effective Duration: {duration:.2f}")
    
    # Check if this matches HTML values
    if abs(pv_down - 953.13) < 0.01 and abs(pv_up - 949.44) < 0.01:
        print(f"  *** MATCHES HTML VALUES! ***")

# Now let's reverse-engineer what the HTML might be doing
print("\n" + "=" * 60)
print("Reverse Engineering HTML Calculation")
print("=" * 60)

# HTML shows: PV_down = 953.13, PV_up = 949.44, PV_0 = 951.28
html_pv_down = 953.13
html_pv_up = 949.44
html_pv0 = 951.28

# What interest rates would give these prices?
print("\nFinding rates that produce HTML prices...")

# Binary search for the rates
def find_rate_for_price(target_price, low=0.01, high=0.10, tolerance=0.01):
    while high - low > 0.000001:
        mid = (low + high) / 2
        price = calculate_bond_price(mid)
        if abs(price - target_price) < tolerance:
            return mid
        elif price > target_price:
            low = mid
        else:
            high = mid
    return (low + high) / 2

rate_for_pv0 = find_rate_for_price(html_pv0)
rate_for_pv_down = find_rate_for_price(html_pv_down)
rate_for_pv_up = find_rate_for_price(html_pv_up)

print(f"\nRates that produce HTML prices:")
print(f"  For PV_0 = ${html_pv0:.2f}: Rate = {rate_for_pv0*100:.4f}%")
print(f"  For PV_down = ${html_pv_down:.2f}: Rate = {rate_for_pv_down*100:.4f}%")
print(f"  For PV_up = ${html_pv_up:.2f}: Rate = {rate_for_pv_up*100:.4f}%")

implied_delta = (rate_for_pv0 - rate_for_pv_down)
print(f"\nImplied delta: {implied_delta*100:.4f}% or {implied_delta*10000:.2f} basis points")

# Calculate duration with HTML values and stated delta
html_delta = 0.0001  # They claim to use 1 basis point
html_duration = (html_pv_down - html_pv_up) / (2 * html_pv0 * html_delta)
print(f"\nHTML's stated calculation:")
print(f"  Duration = ({html_pv_down} - {html_pv_up}) / (2 × {html_pv0} × {html_delta})")
print(f"  Duration = {html_duration:.2f}")

# Recalculate with proper values
print("\n" + "=" * 60)
print("CORRECT CALCULATION")
print("=" * 60)

# Standard effective duration with 1 basis point
delta_correct = 0.0001
pv_down_correct = calculate_bond_price(base_rate - delta_correct)
pv_up_correct = calculate_bond_price(base_rate + delta_correct)
duration_correct = (pv_down_correct - pv_up_correct) / (2 * pv0 * delta_correct)

print(f"\nUsing 1 basis point (0.01%) shock:")
print(f"  Base rate: {base_rate*100:.2f}%")
print(f"  PV_0: ${pv0:.2f}")
print(f"  PV_down (4.99%): ${pv_down_correct:.2f}")
print(f"  PV_up (5.01%): ${pv_up_correct:.2f}")
print(f"  Effective Duration: {duration_correct:.2f}")

# Also calculate Macaulay and Modified Duration for reference
macaulay_duration = 0
for period in range(1, total_periods + 1):
    t = period * 0.5  # time in years
    semi_rate = base_rate / 2
    if period < total_periods:
        cash_flow = coupon_payment
    else:
        cash_flow = coupon_payment + nominal
    pv = cash_flow / (1 + semi_rate) ** period
    weight = pv / pv0
    macaulay_duration += t * weight

modified_duration = macaulay_duration / (1 + base_rate/2)

print(f"\nOther Duration Measures:")
print(f"  Macaulay Duration: {macaulay_duration:.2f} years")
print(f"  Modified Duration: {modified_duration:.2f}")

print("\n" + "=" * 60)
print("CONCLUSION")
print("=" * 60)
print(f"The HTML's duration value of 19.40 appears to be an error.")
print(f"The correct effective duration is approximately {duration_correct:.2f}")
print(f"The HTML's PV values don't correspond to 1 basis point changes.")