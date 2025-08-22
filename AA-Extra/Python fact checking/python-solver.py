"""
Problem Set I - Comprehensive Solutions and Fact Checker
This script solves and verifies all calculations for the problem set
"""

import math

print("=" * 80)
print("T-503-AFLE DERIVATIVES - PROBLEM SET I SOLUTIONS")
print("=" * 80)

# ==============================================================================
# QUESTION 2: Compound Interest Calculation
# ==============================================================================
print("\n" + "=" * 80)
print("Q2: COMPOUND INTEREST CALCULATION")
print("=" * 80)

# Given values
P0 = 100000  # Initial amount
PT = 300000  # Target amount
r = 0.04    # Monthly return (4%)

# Calculate months needed
n = math.log(PT / P0) / math.log(1 + r)

print(f"\nGiven:")
print(f"  Initial amount: ${P0:,}")
print(f"  Target amount: ${PT:,}")
print(f"  Monthly return: {r:.1%}")

print(f"\nFormula: P_T = P_0 × (1 + r)^n")
print(f"\nSolving for n:")
print(f"  {PT:,} = {P0:,} × (1.04)^n")
print(f"  {PT/P0} = (1.04)^n")
print(f"  ln({PT/P0}) = n × ln(1.04)")
print(f"  n = ln({PT/P0}) / ln(1.04)")
print(f"  n = {math.log(PT/P0):.4f} / {math.log(1+r):.4f}")

print(f"\n✓ ANSWER: n = {n:.2f} months (approximately 28 months)")

# Verification
final_amount = P0 * (1 + r) ** n
print(f"\nVerification: ${P0:,} × (1.04)^{n:.2f} = ${final_amount:,.2f} ✓")

# ==============================================================================
# QUESTION 3a: Bond Pricing with Given Term Structure
# ==============================================================================
print("\n" + "=" * 80)
print("Q3a: BOND PRICING WITH GIVEN TERM STRUCTURE")
print("=" * 80)

nominal = 1000
annual_coupon_rate = 0.04375
coupon_payment = nominal * annual_coupon_rate / 2  # Semi-annual
total_periods = 20
time_to_maturity = 10  # years

print(f"\nBond Details:")
print(f"  Nominal: ${nominal:,}")
print(f"  Annual coupon rate: {annual_coupon_rate:.3%}")
print(f"  Semi-annual coupon: ${coupon_payment}")
print(f"  Time to maturity: {time_to_maturity} years")
print(f"  Total periods: {total_periods} (semi-annual)")

print(f"\nTerm Structure:")
print(f"  For t ≤ 7 years: IR(t) = 4% + 0.000352 × (t - 0.5) × 2")
print(f"  For t > 7 years: IR(t) = 4.4576% (constant)")

# Calculate with SEMI-ANNUAL compounding (correct method for bonds)
print("\nPresent Value Calculation (Semi-Annual Compounding):")
print("-" * 60)
print(f"{'Period':>6} {'Time':>7} {'Rate':>8} {'Cash Flow':>12} {'PV':>12}")
print("-" * 60)

pv_total = 0

for period in range(1, total_periods + 1):
    t = period * 0.5  # time in years
    
    # Calculate annual rate based on term structure
    if t <= 7:
        annual_rate = 0.04 + 0.000352 * (t - 0.5) * 2
    else:
        annual_rate = 0.04 + 0.000352 * (7 - 0.5) * 2  # = 0.044576
    
    # Semi-annual compounding: (1 + r/2)^(2*t) where r is annual rate
    semi_rate = annual_rate / 2
    discount_factor = (1 + semi_rate) ** (2 * t)
    
    # Determine cash flow
    if period < total_periods:
        cash_flow = coupon_payment
    else:
        cash_flow = coupon_payment + nominal  # Final payment includes principal
    
    # Calculate present value
    pv = cash_flow / discount_factor
    pv_total += pv
    
    # Print first 3 and last 3 periods for display
    if period <= 3 or period >= 18:
        print(f"{period:6d} {t:7.1f}y {annual_rate*100:7.4f}% ${cash_flow:11.2f} ${pv:11.2f}")
    elif period == 4:
        print("    ...")

print("-" * 60)
print(f"{'TOTAL':>32} ${pv_total:11.2f}")

print(f"\n✓ ANSWER: Bond Price = ${pv_total:.2f}")

# ==============================================================================
# QUESTION 3b: Bond Pricing with Flat 5% Rate
# ==============================================================================
print("\n" + "=" * 80)
print("Q3b: BOND PRICING WITH FLAT 5% RATE")
print("=" * 80)

flat_rate = 0.05
semi_rate = flat_rate / 2  # 2.5% per semi-annual period

print(f"\nGiven:")
print(f"  Annual rate: {flat_rate:.1%}")
print(f"  Semi-annual rate: {semi_rate:.3%}")
print(f"  Coupon payment: ${coupon_payment}")
print(f"  Number of periods: {total_periods}")

# Method 1: Using annuity formula for coupons
print(f"\nMethod 1 - Annuity Formula:")
annuity_factor = (1 - (1 + semi_rate) ** -total_periods) / semi_rate
pv_coupons = coupon_payment * annuity_factor
pv_principal = nominal / (1 + semi_rate) ** total_periods
bond_price_flat = pv_coupons + pv_principal

print(f"  PV of coupons = C × [(1 - (1+r)^-n) / r]")
print(f"                = {coupon_payment} × {annuity_factor:.4f}")
print(f"                = ${pv_coupons:.2f}")
print(f"  PV of principal = {nominal} / (1.025)^{total_periods}")
print(f"                  = ${pv_principal:.2f}")

print(f"\n✓ ANSWER: Bond Price = ${bond_price_flat:.2f}")

# Method 2: Direct summation for verification
bond_price_sum = sum(coupon_payment / (1 + semi_rate) ** p for p in range(1, total_periods + 1))
bond_price_sum += nominal / (1 + semi_rate) ** total_periods
print(f"\nVerification (direct sum): ${bond_price_sum:.2f} ✓")

# ==============================================================================
# QUESTION 3c: Effective Duration Calculation
# ==============================================================================
print("\n" + "=" * 80)
print("Q3c: EFFECTIVE DURATION CALCULATION")
print("=" * 80)

# Function to calculate bond price
def calculate_bond_price(annual_rate, periods=20):
    semi_rate = annual_rate / 2
    price = sum(coupon_payment / (1 + semi_rate) ** p for p in range(1, periods + 1))
    price += nominal / (1 + semi_rate) ** periods
    return price

# Base case
pv0 = bond_price_flat
delta_r = 0.0001  # 1 basis point

print(f"\nGiven:")
print(f"  Base rate: {flat_rate:.2%}")
print(f"  Bond price at base rate: ${pv0:.2f}")
print(f"  Rate shock: ±{delta_r*10000:.0f} basis point")

# Calculate prices with rate changes
pv_down = calculate_bond_price(flat_rate - delta_r)
pv_up = calculate_bond_price(flat_rate + delta_r)

print(f"\nPrice Sensitivity Analysis:")
print(f"  Rate down ({(flat_rate-delta_r)*100:.2f}%): ${pv_down:.2f}")
print(f"  Base rate ({flat_rate*100:.2f}%): ${pv0:.2f}")
print(f"  Rate up ({(flat_rate+delta_r)*100:.2f}%): ${pv_up:.2f}")

# Calculate effective duration
effective_duration = (pv_down - pv_up) / (2 * pv0 * delta_r)

print(f"\nEffective Duration Calculation:")
print(f"  Duration = (PV_down - PV_up) / (2 × PV_0 × Δr)")
print(f"          = ({pv_down:.2f} - {pv_up:.2f}) / (2 × {pv0:.2f} × {delta_r})")
print(f"          = {pv_down - pv_up:.4f} / {2 * pv0 * delta_r:.6f}")

print(f"\n✓ ANSWER: Effective Duration = {effective_duration:.2f}")

# Additional duration measures for reference
# Modified duration
modified_duration = effective_duration / (1 + flat_rate/2)
print(f"\nAdditional Duration Measures:")
print(f"  Modified Duration: {modified_duration:.2f}")

# Macaulay duration
macaulay_duration = 0
for period in range(1, total_periods + 1):
    t = period * 0.5  # time in years
    if period < total_periods:
        cash_flow = coupon_payment
    else:
        cash_flow = coupon_payment + nominal
    pv = cash_flow / (1 + semi_rate) ** period
    weight = pv / pv0
    macaulay_duration += t * weight

print(f"  Macaulay Duration: {macaulay_duration:.2f} years")

print(f"\nInterpretation: The bond price will change by approximately {effective_duration:.2f}%")
print(f"for each 1% change in interest rates (inverse relationship).")

# ==============================================================================
# QUESTION 3d: Expected Credit Loss (ECL)
# ==============================================================================
print("\n" + "=" * 80)
print("Q3d: EXPECTED CREDIT LOSS (ECL) CALCULATION")
print("=" * 80)

# Given parameters
EAD = 8_000_000_000  # ISK 8 billion
PD = 0.023  # 2.3%
LGD = 0.60  # 60%

print(f"\nGiven:")
print(f"  EAD (Exposure at Default): ISK {EAD:,}")
print(f"  PD (Probability of Default): {PD:.1%}")
print(f"  LGD (Loss Given Default): {LGD:.0%}")

print(f"\nFormula: ECL = EAD × PD × LGD")

# Calculate ECL
ECL = EAD * PD * LGD

print(f"\nCalculation:")
print(f"  ECL = {EAD:,} × {PD} × {LGD}")
print(f"      = ISK {ECL:,.0f}")
print(f"      = ISK {ECL/1_000_000:.1f} million")

print(f"\n✓ ANSWER: Expected Credit Loss = ISK {ECL/1_000_000:.1f} million")

# ==============================================================================
# SUMMARY OF ALL ANSWERS
# ==============================================================================
print("\n" + "=" * 80)
print("SUMMARY OF ALL NUMERICAL ANSWERS")
print("=" * 80)

print(f"\nQ2: Compound Interest")
print(f"    Time to reach $300,000: {n:.2f} months")

print(f"\nQ3a: Bond Price (Term Structure)")
print(f"    Bond price: ${pv_total:.2f}")

print(f"\nQ3b: Bond Price (Flat 5% Rate)")
print(f"    Bond price: ${bond_price_flat:.2f}")

print(f"\nQ3c: Effective Duration")
print(f"    Duration: {effective_duration:.2f}")

print(f"\nQ3d: Expected Credit Loss")
print(f"    ECL: ISK {ECL/1_000_000:.1f} million")

print("\n" + "=" * 80)
print("FACT CHECK RESULTS VS HTML SOLUTIONS")
print("=" * 80)

# Compare with HTML answers
html_answers = {
    "Q2": 28,
    "Q3a": 1002.41,
    "Q3b": 951.28,
    "Q3c": 19.40,
    "Q3d": 110.4
}

calculated_answers = {
    "Q2": round(n, 2),
    "Q3a": round(pv_total, 2),
    "Q3b": round(bond_price_flat, 2),
    "Q3c": round(effective_duration, 2),
    "Q3d": round(ECL/1_000_000, 1)
}

print(f"\n{'Question':<10} {'HTML Answer':<15} {'Calculated':<15} {'Status':<10}")
print("-" * 50)
print(f"{'Q2':<10} {html_answers['Q2']:<15} {calculated_answers['Q2']:<15} {'✓ CORRECT' if abs(html_answers['Q2'] - calculated_answers['Q2']) < 0.5 else '✗ WRONG'}")
print(f"{'Q3a':<10} ${html_answers['Q3a']:<14} ${calculated_answers['Q3a']:<14} {'✓ CORRECT' if abs(html_answers['Q3a'] - calculated_answers['Q3a']) < 0.01 else '✗ WRONG'}")
print(f"{'Q3b':<10} ${html_answers['Q3b']:<14} ${calculated_answers['Q3b']:<14} {'✓ CORRECT' if abs(html_answers['Q3b'] - calculated_answers['Q3b']) < 0.01 else '✗ WRONG'}")
print(f"{'Q3c':<10} {html_answers['Q3c']:<15} {calculated_answers['Q3c']:<15} {'✓ CORRECT' if abs(html_answers['Q3c'] - calculated_answers['Q3c']) < 0.1 else '✗ WRONG'}")
print(f"{'Q3d':<10} {html_answers['Q3d']:<15} {calculated_answers['Q3d']:<15} {'✓ CORRECT' if abs(html_answers['Q3d'] - calculated_answers['Q3d']) < 0.1 else '✗ WRONG'}")

print("\n" + "=" * 80)
print("CORRECTIONS NEEDED IN HTML:")
print("=" * 80)
print("1. Q3a: Change bond price from $1,002.41 to $994.87")
print("2. Q3c: Change effective duration from 19.40 to 7.95")
print("=" * 80)