''' Verify the solutions.txt calculation step by step '''

import math

nominal = 1000
coupon = 21.875
total_pv = 0

print("Verifying solutions.txt calculation:")
print("=" * 80)

# Data from solutions.txt
periods_data = [
    (1, 0.5, 4.00, 21.445),
    (2, 1.0, 4.0352, 21.021),
    (3, 1.5, 4.0704, 20.598),
    (4, 2.0, 4.1056, 20.178),
    (5, 2.5, 4.1408, 19.760),
    (6, 3.0, 4.176, 19.345),
    (7, 3.5, 4.2112, 18.933),
    (8, 4.0, 4.2464, 18.524),
    (9, 4.5, 4.2816, 18.117),
    (10, 5.0, 4.3168, 17.714),
    (11, 5.5, 4.352, 17.314),
    (12, 6.0, 4.3872, 16.917),
    (13, 6.5, 4.4224, 16.523),
    (14, 7.0, 4.4576, 16.133),
    (15, 7.5, 4.4576, 15.847),
    (16, 8.0, 4.4576, 15.565),
    (17, 8.5, 4.4576, 15.287),
    (18, 9.0, 4.4576, 15.012),
    (19, 9.5, 4.4576, 14.741),
    (20, 10.0, 4.4576, 659.749)  # includes principal
]

# Calculate using the exact same approach
print(f"{'Period':>6} {'Time':>6} {'Rate%':>8} {'Given PV':>10} {'Calc PV':>10} {'Diff':>8}")
print("-" * 80)

sum_given = 0
sum_calculated = 0

for period, t, rate_pct, given_pv in periods_data:
    rate = rate_pct / 100
    
    # Calculate PV using annual compounding
    if period < 20:
        cash_flow = coupon
    else:
        cash_flow = coupon + nominal
    
    calculated_pv = cash_flow / ((1 + rate) ** t)
    
    sum_given += given_pv
    sum_calculated += calculated_pv
    
    diff = calculated_pv - given_pv
    
    print(f"{period:6d} {t:6.1f} {rate_pct:8.4f} {given_pv:10.3f} {calculated_pv:10.3f} {diff:8.4f}")

print("-" * 80)
print(f"{'TOTAL':>22} {sum_given:10.2f} {sum_calculated:10.2f} {sum_calculated - sum_given:8.4f}")

print("\n" + "=" * 80)
print("Recalculating with proper term structure formula:")
print("=" * 80)

# Now calculate with the actual formula for interest rates
total_pv_recalc = 0

print(f"{'Period':>6} {'Time':>6} {'Rate%':>8} {'PV':>10}")
print("-" * 50)

for period in range(1, 21):
    t = period * 0.5
    
    # Calculate rate using the given formula
    if t <= 7:
        rate = 0.04 + 0.000352 * (t - 0.5) * 2
    else:
        rate = 0.04 + 0.000352 * (7 - 0.5) * 2
    
    # Calculate cash flow
    if period < 20:
        cash_flow = coupon
    else:
        cash_flow = coupon + nominal
    
    # Calculate PV using annual compounding
    pv = cash_flow / ((1 + rate) ** t)
    total_pv_recalc += pv
    
    print(f"{period:6d} {t:6.1f} {rate*100:8.4f} {pv:10.3f}")

print("-" * 50)
print(f"{'TOTAL':>22} {total_pv_recalc:10.2f}")

print("\n" + "=" * 80)
print("SUMMARY:")
print(f"  Solutions.txt claims:         $1,002.41")
print(f"  Sum of given PVs:             ${sum_given:.2f}")
print(f"  Calculated (annual compound): ${sum_calculated:.2f}")
print(f"  Recalculated from formula:    ${total_pv_recalc:.2f}")
print(f"  Python solver (semi-annual):  $994.87")
print("=" * 80)