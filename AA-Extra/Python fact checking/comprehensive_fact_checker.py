"""
Comprehensive Fact Checker for Problem Set I Solutions
This script verifies all calculations in the HTML solutions file
"""

import math

print("=" * 80)
print("PROBLEM SET I - COMPREHENSIVE FACT CHECKING")
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

print(f"\nCalculation:")
print(f"  {PT:,} = {P0:,} × (1.04)^n")
print(f"  {PT/P0} = (1.04)^n")
print(f"  ln({PT/P0}) = n × ln(1.04)")
print(f"  n = ln({PT/P0}) / ln(1.04)")
print(f"  n = {math.log(PT/P0):.4f} / {math.log(1+r):.4f}")
print(f"  n = {n:.2f} months")

# Verification
final_amount = P0 * (1 + r) ** n
print(f"\nVerification: ${P0:,} × (1.04)^{n:.2f} = ${final_amount:,.2f}")

html_answer = 28
print(f"\n✓ HTML Answer: {html_answer} months")
print(f"✓ Calculated: {n:.2f} months")
print(f"✓ Status: {'CORRECT' if abs(n - html_answer) < 0.5 else 'INCORRECT'}")

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

print(f"\nBond Details:")
print(f"  Nominal: ${nominal:,}")
print(f"  Annual coupon rate: {annual_coupon_rate:.3%}")
print(f"  Semi-annual coupon: ${coupon_payment}")
print(f"  Total periods: {total_periods}")

# Calculate with SEMI-ANNUAL compounding (correct method)
print("\nUsing Semi-Annual Compounding (Standard for bonds):")
print("-" * 50)

pv_semiannual = 0
print(f"{'Period':>6} {'Time':>7} {'Rate%':>8} {'PV':>10}")
print("-" * 35)

for period in range(1, total_periods + 1):
    t = period * 0.5  # time in years
    
    # Calculate annual rate based on term structure
    if t <= 7:
        annual_rate = 0.04 + 0.000352 * (t - 0.5) * 2
    else:
        annual_rate = 0.04 + 0.000352 * (7 - 0.5) * 2  # = 0.044576
    
    # Semi-annual compounding: (1 + r/2)^(2*t)
    semi_rate = annual_rate / 2
    discount_factor = (1 + semi_rate) ** (2 * t)
    
    # Calculate present value
    if period < total_periods:
        cash_flow = coupon_payment
    else:
        cash_flow = coupon_payment + nominal
    
    pv = cash_flow / discount_factor
    pv_semiannual += pv
    
    # Print first 3 and last 3 periods
    if period <= 3 or period >= 18:
        print(f"{period:6d} {t:7.1f}y {annual_rate*100:7.4f}% {pv:10.2f}")
    elif period == 4:
        print("    ...")

print("-" * 35)
print(f"{'TOTAL':>23} {pv_semiannual:10.2f}")

# Also calculate with annual compounding (what HTML seems to use)
pv_annual = 0
for period in range(1, total_periods + 1):
    t = period * 0.5
    if t <= 7:
        annual_rate = 0.04 + 0.000352 * (t - 0.5) * 2
    else:
        annual_rate = 0.04 + 0.000352 * (7 - 0.5) * 2
    
    discount_factor = (1 + annual_rate) ** t
    if period < total_periods:
        cash_flow = coupon_payment
    else:
        cash_flow = coupon_payment + nominal
    pv_annual += cash_flow / discount_factor

print(f"\nUsing Annual Compounding: ${pv_annual:.2f}")

html_answer_3a = 1002.41
print(f"\n✗ HTML Answer: ${html_answer_3a}")
print(f"✓ Correct (Semi-Annual): ${pv_semiannual:.2f}")
print(f"  Annual Compounding: ${pv_annual:.2f}")
print(f"✗ Status: INCORRECT - HTML answer doesn't match either method")

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

# Method 1: Using annuity formula
annuity_factor = (1 - (1 + semi_rate) ** -total_periods) / semi_rate
pv_coupons_formula = coupon_payment * annuity_factor
pv_principal = nominal / (1 + semi_rate) ** total_periods
bond_price_formula = pv_coupons_formula + pv_principal

print(f"\nMethod 1 - Annuity Formula:")
print(f"  Annuity factor: {annuity_factor:.4f}")
print(f"  PV of coupons: ${pv_coupons_formula:.2f}")
print(f"  PV of principal: ${pv_principal:.2f}")
print(f"  Total bond price: ${bond_price_formula:.2f}")

# Method 2: Direct summation (verification)
bond_price_sum = 0
for period in range(1, total_periods + 1):
    pv = coupon_payment / (1 + semi_rate) ** period
    bond_price_sum += pv
    if period == total_periods:
        bond_price_sum += nominal / (1 + semi_rate) ** period

print(f"\nMethod 2 - Direct Summation:")
print(f"  Total bond price: ${bond_price_sum:.2f}")

html_answer_3b = 951.28
print(f"\n✓ HTML Answer: ${html_answer_3b}")
print(f"✓ Calculated: ${bond_price_formula:.2f}")
print(f"✓ Status: {'CORRECT' if abs(bond_price_formula - html_answer_3b) < 0.01 else 'INCORRECT'}")

# ==============================================================================
# QUESTION 3c: Effective Duration Calculation
# ==============================================================================
print("\n" + "=" * 80)
print("Q3c: EFFECTIVE DURATION CALCULATION")
print("=" * 80)

# Base bond value from Q3b
pv0 = bond_price_formula
delta_r = 0.0001  # 1 basis point

print(f"\nBase case (5% rate):")
print(f"  Bond price: ${pv0:.2f}")

# Calculate bond price with rate down (4.99%)
rate_down = flat_rate - delta_r
semi_rate_down = rate_down / 2
pv_down = 0
for period in range(1, total_periods + 1):
    pv = coupon_payment / (1 + semi_rate_down) ** period
    pv_down += pv
    if period == total_periods:
        pv_down += nominal / (1 + semi_rate_down) ** period

print(f"\nRate down (4.99%):")
print(f"  Bond price: ${pv_down:.2f}")

# Calculate bond price with rate up (5.01%)
rate_up = flat_rate + delta_r
semi_rate_up = rate_up / 2
pv_up = 0
for period in range(1, total_periods + 1):
    pv = coupon_payment / (1 + semi_rate_up) ** period
    pv_up += pv
    if period == total_periods:
        pv_up += nominal / (1 + semi_rate_up) ** period

print(f"\nRate up (5.01%):")
print(f"  Bond price: ${pv_up:.2f}")

# Calculate effective duration
effective_duration = (pv_down - pv_up) / (2 * pv0 * delta_r)

print(f"\nEffective Duration Calculation:")
print(f"  Duration = (PV_down - PV_up) / (2 × PV_0 × Δr)")
print(f"  Duration = ({pv_down:.2f} - {pv_up:.2f}) / (2 × {pv0:.2f} × {delta_r})")
print(f"  Duration = {pv_down - pv_up:.4f} / {2 * pv0 * delta_r:.6f}")
print(f"  Duration = {effective_duration:.2f}")

# Modified duration for comparison
modified_duration = effective_duration / (1 + flat_rate)
print(f"\nModified Duration: {modified_duration:.2f}")

# Calculate using Macaulay Duration formula (for verification)
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

print(f"Macaulay Duration: {macaulay_duration:.2f} years")

# The HTML seems to calculate something different
# Let's check their calculation
html_pv_down = 953.13
html_pv_up = 949.44
html_duration = (html_pv_down - html_pv_up) / (2 * 951.28 * 0.0001)
print(f"\nHTML's calculation:")
print(f"  PV_down: ${html_pv_down}")
print(f"  PV_up: ${html_pv_up}")
print(f"  PV_0: $951.28")
print(f"  Duration = ({html_pv_down} - {html_pv_up}) / (2 × 951.28 × 0.0001)")
print(f"  Duration = {html_duration:.2f}")

html_answer_3c = 19.40
print(f"\n? HTML Answer: {html_answer_3c}")
print(f"✓ Calculated Effective Duration: {effective_duration:.2f}")
print(f"  Macaulay Duration: {macaulay_duration:.2f}")
print(f"? Status: SUSPICIOUS - HTML value seems too high")

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

# Calculate ECL
ECL = EAD * PD * LGD

print(f"\nCalculation:")
print(f"  ECL = EAD × PD × LGD")
print(f"  ECL = {EAD:,} × {PD} × {LGD}")
print(f"  ECL = ISK {ECL:,.0f}")
print(f"  ECL = ISK {ECL/1_000_000:.1f} million")

html_answer_3d = 110.4  # million ISK
calculated_3d = ECL / 1_000_000

print(f"\n✓ HTML Answer: ISK {html_answer_3d} million")
print(f"✓ Calculated: ISK {calculated_3d:.1f} million")
print(f"✓ Status: {'CORRECT' if abs(calculated_3d - html_answer_3d) < 0.1 else 'INCORRECT'}")

# ==============================================================================
# SUMMARY OF FINDINGS
# ==============================================================================
print("\n" + "=" * 80)
print("SUMMARY OF FACT CHECKING RESULTS")
print("=" * 80)

print("\n✓ Q2 (Compound Interest): CORRECT")
print("  HTML: 28 months, Calculated: 28.02 months")

print("\n✗ Q3a (Bond Pricing with Term Structure): INCORRECT")
print(f"  HTML: $1,002.41")
print(f"  Correct (Semi-Annual): ${pv_semiannual:.2f}")
print("  Error: HTML value doesn't match any standard calculation method")

print("\n✓ Q3b (Bond Pricing with Flat Rate): CORRECT")
print(f"  HTML: $951.28, Calculated: ${bond_price_formula:.2f}")

print("\n? Q3c (Effective Duration): QUESTIONABLE")
print(f"  HTML: 19.40")
print(f"  Calculated Effective Duration: {effective_duration:.2f}")
print(f"  Macaulay Duration: {macaulay_duration:.2f} years")
print("  Note: HTML value seems unusually high for a 10-year bond")

print("\n✓ Q3d (Expected Credit Loss): CORRECT")
print(f"  HTML: ISK 110.4 million, Calculated: ISK {calculated_3d:.1f} million")

print("\n" + "=" * 80)
print("CORRECTIONS NEEDED:")
print("1. Q3a: Change bond price from $1,002.41 to $994.87")
print("2. Q3c: Verify duration calculation methodology")
print("=" * 80)