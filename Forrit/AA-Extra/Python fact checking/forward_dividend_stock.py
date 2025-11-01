"""
Forward Contract on Dividend-Paying Stock Verification Script
T-503-AFLE Derivatives Course

Problem Q13: Allianz share forward contract with discrete dividend
"""

import math

def calculate_forward_price_with_dividend(spot_price, dividend, dividend_time, risk_free_rate_div, risk_free_rate_maturity, maturity):
    """
    Calculate forward price for a stock with a discrete dividend payment
    
    Formula: F = (S - PV(Dividend)) * e^(r*T)
    Where PV(Dividend) = Dividend * e^(-r_div * t_div)
    
    Parameters:
    - spot_price: Current stock price
    - dividend: Dividend amount to be paid
    - dividend_time: Time until dividend payment (years)
    - risk_free_rate_div: Interest rate for dividend period
    - risk_free_rate_maturity: Interest rate for full maturity period
    - maturity: Time to maturity of forward contract (years)
    """
    
    # Calculate present value of dividend
    pv_dividend = dividend * math.exp(-risk_free_rate_div * dividend_time)
    
    # Calculate forward price
    forward_price = (spot_price - pv_dividend) * math.exp(risk_free_rate_maturity * maturity)
    
    print(f"Forward Price Calculation with Discrete Dividend")
    print(f"=" * 60)
    print(f"Spot Price (S): €{spot_price:.2f}")
    print(f"Dividend: €{dividend:.2f} in {dividend_time*12:.1f} months")
    print(f"Risk-free rate (5 months): {risk_free_rate_div*100:.2f}%")
    print(f"Risk-free rate (1 year): {risk_free_rate_maturity*100:.2f}%")
    print(f"Maturity: {maturity} year")
    print()
    print(f"Step 1: Calculate PV of dividend")
    print(f"  PV(Dividend) = {dividend} × e^(-{risk_free_rate_div:.4f} × {dividend_time:.4f})")
    print(f"  PV(Dividend) = €{pv_dividend:.4f}")
    print()
    print(f"Step 2: Calculate forward price")
    print(f"  F = (S - PV(Dividend)) × e^(r × T)")
    print(f"  F = ({spot_price} - {pv_dividend:.4f}) × e^({risk_free_rate_maturity:.4f} × {maturity})")
    print(f"  F = {spot_price - pv_dividend:.4f} × {math.exp(risk_free_rate_maturity * maturity):.6f}")
    print(f"  F = €{forward_price:.4f}")
    print()
    
    return forward_price, pv_dividend

def calculate_forward_interest_rate(spot_rate_short, spot_rate_long, time_short, time_long):
    """
    Calculate forward interest rate F(t1, t2)
    
    Formula: F(t1, t2) = [(1 + r_long*t_long) / (1 + r_short*t_short) - 1] / (t_long - t_short)
    
    For continuous compounding:
    F(t1, t2) = [r_long*t_long - r_short*t_short] / (t_long - t_short)
    """
    
    # Using continuous compounding formula
    forward_rate = (spot_rate_long * time_long - spot_rate_short * time_short) / (time_long - time_short)
    
    print(f"Forward Interest Rate Calculation")
    print(f"=" * 60)
    print(f"Spot rate (0 to {time_short*12:.0f} months): {spot_rate_short*100:.2f}%")
    print(f"Spot rate (0 to {time_long*12:.0f} months): {spot_rate_long*100:.2f}%")
    print()
    print(f"Using continuous compounding formula:")
    print(f"F({time_short*12:.0f}m, {time_long*12:.0f}m) = [r_long×t_long - r_short×t_short] / (t_long - t_short)")
    print(f"F({time_short*12:.0f}m, {time_long*12:.0f}m) = [{spot_rate_long:.4f}×{time_long} - {spot_rate_short:.4f}×{time_short}] / {time_long - time_short}")
    print(f"F({time_short*12:.0f}m, {time_long*12:.0f}m) = [{spot_rate_long * time_long:.6f} - {spot_rate_short * time_short:.6f}] / {time_long - time_short:.4f}")
    print(f"F({time_short*12:.0f}m, {time_long*12:.0f}m) = {forward_rate:.6f} = {forward_rate*100:.4f}%")
    print()
    
    # Also calculate using discrete compounding for comparison
    forward_rate_discrete = ((1 + spot_rate_long * time_long) / (1 + spot_rate_short * time_short) - 1) / (time_long - time_short)
    print(f"Using discrete compounding formula (for comparison):")
    print(f"F({time_short*12:.0f}m, {time_long*12:.0f}m) = [(1 + r_long×t_long)/(1 + r_short×t_short) - 1] / (t_long - t_short)")
    print(f"F({time_short*12:.0f}m, {time_long*12:.0f}m) = {forward_rate_discrete:.6f} = {forward_rate_discrete*100:.4f}%")
    print()
    
    return forward_rate, forward_rate_discrete

def main():
    """
    Main verification for Problem Q13
    """
    print("\n" + "=" * 70)
    print("FORWARD CONTRACT ON DIVIDEND-PAYING STOCK VERIFICATION")
    print("Problem Q13 - T-503-AFLE Derivatives")
    print("=" * 70 + "\n")
    
    # Problem parameters
    spot_price = 217.1  # EUR
    dividend = 9.5  # EUR
    dividend_time = 5/12  # 5 months in years
    rate_5_months = 0.006  # 0.6%
    rate_1_year = 0.0085  # 0.85%
    maturity = 1  # 1 year
    
    print("Given Information:")
    print("-" * 60)
    print(f"Allianz share spot price: €{spot_price}")
    print(f"Expected dividend: €{dividend} in 5 months")
    print(f"5-month interest rate: {rate_5_months*100}%")
    print(f"1-year interest rate: {rate_1_year*100}%")
    print()
    
    # Part (a): Calculate forward price
    print("\nPART (a): Fair Price for 1-Year Forward Contract")
    print("-" * 60)
    forward_price, pv_dividend = calculate_forward_price_with_dividend(
        spot_price, 
        dividend, 
        dividend_time, 
        rate_5_months, 
        rate_1_year, 
        maturity
    )
    
    # Part (b): Calculate forward interest rate F(0, 5m, 1y)
    print("\nPART (b): Forward Interest Rate F(0, 5m, 1y)")
    print("-" * 60)
    forward_rate_cont, forward_rate_disc = calculate_forward_interest_rate(
        rate_5_months,
        rate_1_year,
        dividend_time,  # 5 months
        maturity  # 1 year
    )
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY OF RESULTS")
    print("=" * 70)
    print(f"\n(a) Fair price for 1-year forward contract: €{forward_price:.4f}")
    print(f"    Present value of dividend: €{pv_dividend:.4f}")
    print(f"    Adjusted spot price: €{spot_price - pv_dividend:.4f}")
    print()
    print(f"(b) Forward interest rate F(0, 5m, 1y):")
    print(f"    Continuous compounding: {forward_rate_cont*100:.4f}%")
    print(f"    Discrete compounding: {forward_rate_disc*100:.4f}%")
    print()
    print("Note: The forward rate represents the implied interest rate from")
    print("      month 5 to month 12 based on the given spot rates.")

if __name__ == "__main__":
    main()