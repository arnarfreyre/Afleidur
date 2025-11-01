"""
Forward Contract Hedging Verification Script
T-503-AFLE Derivatives Course

Problem Q7: US company hedging EUR payment with forward contract
"""

def calculate_forward_contract_results(eur_amount, forward_rate, spot_rates):
    """
    Calculate gain/loss from forward contract position
    
    Parameters:
    - eur_amount: Amount of EUR to buy (millions)
    - forward_rate: Agreed forward exchange rate (USD per EUR)
    - spot_rates: List of spot rates to test
    
    Returns: Dictionary with results
    """
    results = {}
    
    # Cost using forward contract (locked in)
    forward_cost_usd = eur_amount * forward_rate
    
    print(f"Forward Contract Analysis")
    print(f"=" * 50)
    print(f"EUR Amount needed: €{eur_amount:.1f}m")
    print(f"Forward Rate: {forward_rate:.3f} USD/EUR")
    print(f"Cost locked in with forward: ${forward_cost_usd:.3f}m")
    print()
    
    # Calculate gain/loss for each spot rate
    for i, spot_rate in enumerate(spot_rates):
        spot_cost_usd = eur_amount * spot_rate
        
        # Gain/Loss from company's perspective
        # If spot > forward: company saves money (gain)
        # If spot < forward: company loses money (loss)
        gain_loss = spot_cost_usd - forward_cost_usd
        
        results[f'scenario_{i+1}'] = {
            'spot_rate': spot_rate,
            'spot_cost': spot_cost_usd,
            'forward_cost': forward_cost_usd,
            'gain_loss': gain_loss
        }
        
        print(f"Scenario {i+1}: Spot Rate = {spot_rate:.3f}")
        print(f"  Cost at spot: ${spot_cost_usd:.3f}m")
        print(f"  Cost with forward: ${forward_cost_usd:.3f}m")
        print(f"  Gain/Loss: ${gain_loss:.3f}m")
        
        if gain_loss > 0:
            print(f"  → Company LOSES ${abs(gain_loss):.3f}m by using forward")
        elif gain_loss < 0:
            print(f"  → Company SAVES ${abs(gain_loss):.3f}m by using forward")
        else:
            print(f"  → No gain or loss")
        print()
    
    return results

def calculate_fair_value_to_sell(eur_amount, forward_rate, spot_rate):
    """
    Calculate fair value to sell the forward contract
    
    When selling a long forward contract before expiry:
    - Fair value = (Spot Rate - Forward Rate) × EUR Amount
    
    This represents the value of the contract to another party
    """
    # Value of the contract (from buyer's perspective)
    contract_value = (spot_rate - forward_rate) * eur_amount
    
    print(f"Fair Value to Sell Forward Contract")
    print(f"=" * 50)
    print(f"EUR Amount: €{eur_amount:.1f}m")
    print(f"Original Forward Rate: {forward_rate:.3f} USD/EUR")
    print(f"Current Spot Rate: {spot_rate:.3f} USD/EUR")
    print(f"Rate Difference: {spot_rate - forward_rate:.3f} USD/EUR")
    print()
    print(f"Fair Value = (Spot - Forward) × Amount")
    print(f"Fair Value = ({spot_rate:.3f} - {forward_rate:.3f}) × {eur_amount:.1f}")
    print(f"Fair Value = ${contract_value:.3f}m")
    print()
    
    if contract_value > 0:
        print(f"→ The contract has POSITIVE value of ${contract_value:.3f}m")
        print(f"  (Buyer would pay more at current spot than forward rate)")
    elif contract_value < 0:
        print(f"→ The contract has NEGATIVE value of ${abs(contract_value):.3f}m")
        print(f"  (Buyer would pay less at current spot than forward rate)")
    else:
        print(f"→ The contract has ZERO value")
    
    return contract_value

def main():
    """
    Main verification for Problem Q7
    """
    print("\n" + "=" * 60)
    print("FORWARD CONTRACT HEDGING VERIFICATION")
    print("Problem Q7 - T-503-AFLE Derivatives")
    print("=" * 60 + "\n")
    
    # Problem parameters
    eur_amount = 6.4  # millions
    forward_rate = 1.22  # USD per EUR
    
    # Part 1: Calculate gain/loss at different spot rates
    print("\nPART 1: Gain/Loss Analysis")
    print("-" * 60)
    spot_rates = [1.195, 1.226]  # (a) and (b)
    results = calculate_forward_contract_results(eur_amount, forward_rate, spot_rates)
    
    # Part 2: Fair value to sell the contract
    print("\nPART 2: Fair Value to Sell Contract")
    print("-" * 60)
    spot_rate_at_expiry = 1.226
    fair_value = calculate_fair_value_to_sell(eur_amount, forward_rate, spot_rate_at_expiry)
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY OF RESULTS")
    print("=" * 60)
    print(f"\n1) Gain/Loss from company's perspective:")
    print(f"   a) At spot 1.195: Company SAVES ${abs(results['scenario_1']['gain_loss']):.3f}m")
    print(f"   b) At spot 1.226: Company LOSES ${abs(results['scenario_2']['gain_loss']):.3f}m")
    print(f"\n2) Fair value to sell contract at spot 1.226: ${fair_value:.3f}m")
    print("\nNote: A positive fair value means the buyer of the contract")
    print("      would receive value, as spot > forward rate.")

if __name__ == "__main__":
    main()