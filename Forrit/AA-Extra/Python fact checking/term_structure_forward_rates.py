#!/usr/bin/env python3
"""
Verification script for Term Structure and Forward Rate calculations
Based on French Government Bond data from Q12
"""

import math

def calculate_forward_rate(r1, t1, r2, t2):
    """
    Calculate forward rate from t1 to t2 given spot rates
    
    Formula: f(t1,t2) = [(1 + r2)^t2 / (1 + r1)^t1]^(1/(t2-t1)) - 1
    
    Args:
        r1: spot rate for period t1 (as decimal, not percentage)
        t1: first time period (years)
        r2: spot rate for period t2 (as decimal, not percentage)  
        t2: second time period (years)
    
    Returns:
        forward rate as decimal
    """
    numerator = (1 + r2) ** t2
    denominator = (1 + r1) ** t1
    power = 1 / (t2 - t1)
    forward_rate = (numerator / denominator) ** power - 1
    return forward_rate

def calculate_spot_from_forwards(initial_spot_rate, forward_rates):
    """
    Calculate spot rates by compounding forward rates
    
    Formula: (1 + r_n)^n = (1 + r_1) * product((1 + f_i)^delta_t_i)
    
    Args:
        initial_spot_rate: starting spot rate (as decimal)
        forward_rates: list of tuples (forward_rate, period_length)
    
    Returns:
        list of spot rates
    """
    spot_rates = [(1, initial_spot_rate)]
    compound_value = 1 + initial_spot_rate
    total_time = 1
    
    for forward_rate, period_length in forward_rates:
        total_time += period_length
        compound_value *= (1 + forward_rate) ** period_length
        spot_rate = compound_value ** (1 / total_time) - 1
        spot_rates.append((total_time, spot_rate))
    
    return spot_rates

def main():
    print("=" * 60)
    print("TERM STRUCTURE AND FORWARD RATE CALCULATIONS")
    print("French Government Bond Data Verification")
    print("=" * 60)
    
    # French government bond spot rates (from the image)
    french_bonds = [
        (10, 0.0014),  # 10Y: 0.14%
        (15, 0.0043),  # 15Y: 0.43%
        (20, 0.0063),  # 20Y: 0.63%
        (25, 0.0073),  # 25Y: 0.73%
        (50, 0.0104),  # 50Y: 1.04%
    ]
    
    print("\nInput Spot Rates:")
    print("-" * 40)
    for years, rate in french_bonds:
        print(f"{years:3d}Y: {rate*100:6.2f}%")
    
    # Question (a): Forward rate 20Y in 10Y time (i.e., from year 10 to year 30)
    # We need 10Y and 30Y spot rates
    # From data: 10Y = 0.14%, but we don't have 30Y
    # We'll use what we have: 10Y to 20Y
    
    print("\n" + "=" * 60)
    print("FORWARD RATE CALCULATIONS")
    print("=" * 60)
    
    # Calculate forward rates between consecutive periods
    print("\nForward Rates Between Consecutive Periods:")
    print("-" * 40)
    
    for i in range(len(french_bonds) - 1):
        t1, r1 = french_bonds[i]
        t2, r2 = french_bonds[i + 1]
        forward = calculate_forward_rate(r1, t1, r2, t2)
        print(f"f({t1:2d},{t2:2d}): {forward*100:6.4f}%")
    
    # Specific calculations for the questions
    print("\n" + "=" * 60)
    print("ANSWERS TO SPECIFIC QUESTIONS")
    print("=" * 60)
    
    # (a) Forward rate from 10Y to 20Y
    f_10_20 = calculate_forward_rate(0.0014, 10, 0.0063, 20)
    print(f"\n(a) Forward rate 20Y in 10Y time (10Y to 20Y):")
    print(f"    f(10,20) = {f_10_20*100:.4f}%")
    print(f"    Calculation: [(1.0063)^20 / (1.0014)^10]^(1/10) - 1")
    
    # (b) Forward rate from 15Y to 20Y  
    f_15_20 = calculate_forward_rate(0.0043, 15, 0.0063, 20)
    print(f"\n(b) Forward rate 20Y in 15Y time (15Y to 20Y):")
    print(f"    f(15,20) = {f_15_20*100:.4f}%")
    print(f"    Calculation: [(1.0063)^20 / (1.0043)^15]^(1/5) - 1")
    
    # Additional useful forward rates
    print("\n" + "=" * 60)
    print("ADDITIONAL FORWARD RATES")
    print("=" * 60)
    
    # 10Y to 15Y
    f_10_15 = calculate_forward_rate(0.0014, 10, 0.0043, 15)
    print(f"f(10,15) = {f_10_15*100:.4f}%")
    
    # 20Y to 25Y
    f_20_25 = calculate_forward_rate(0.0063, 20, 0.0073, 25)
    print(f"f(20,25) = {f_20_25*100:.4f}%")
    
    # 25Y to 50Y
    f_25_50 = calculate_forward_rate(0.0073, 25, 0.0104, 50)
    print(f"f(25,50) = {f_25_50*100:.4f}%")
    
    # Verification: Build spot rates from forward rates
    print("\n" + "=" * 60)
    print("VERIFICATION: SPOT RATES FROM FORWARD RATES")
    print("=" * 60)
    
    # Starting with 10Y spot rate, build up using forward rates
    initial_rate = 0.0014  # 10Y spot rate
    forwards = [
        (f_10_15, 5),   # 10Y to 15Y forward for 5 years
        (f_15_20, 5),   # 15Y to 20Y forward for 5 years
    ]
    
    reconstructed_spots = calculate_spot_from_forwards(initial_rate, forwards)
    
    print("\nReconstructed spot rates from forward rates:")
    print("-" * 40)
    # Skip the initial 1Y placeholder
    actual_periods = [(10, 0.0014), (15, 0.0043), (20, 0.0063)]
    
    for i, (period, rate) in enumerate(actual_periods):
        if i == 0:
            print(f"{period:3d}Y: {rate*100:6.4f}% (initial)")
        else:
            # Adjust index since reconstructed_spots starts with (1, initial_rate)
            if i < len(reconstructed_spots):
                _, reconstructed = reconstructed_spots[i-1] if i == 1 else reconstructed_spots[i]
                expected = rate
                error = abs(reconstructed - expected) * 100
                print(f"{period:3d}Y: {reconstructed*100:6.4f}% (reconstructed) vs {expected*100:6.4f}% (actual) - Error: {error:.6f}%")

if __name__ == "__main__":
    main()