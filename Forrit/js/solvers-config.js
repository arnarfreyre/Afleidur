// solvers-config.js - Configuration for solvers.html
const solversConfig = [
    {
        id: 1,
        title: "Forward Rate Calculator",
        description: "Calculate forward prices for various assets including stocks, commodities, and currencies. Supports continuous and discrete dividend yields, storage costs, and convenience yields.",
        path: "Solvers/forward-rate-calculator.html",
        status: "available"
    },
    {
        id: 2,
        title: "Forward & Options Payoff Plotter",
        description: "Interactive tool for plotting payoffs at maturity for forwards, calls, and puts with customizable positions",
        path: "Solvers/forward-payoff-plotter.html",
        status: "available"
    },
    {
        id: 3,
        title: "Bond Price & Duration Calculator",
        description: "Calculate bond prices, yields to maturity, duration, and convexity. Supports various day count conventions and compounding frequencies.",
        path: "Solvers/bond-pricing-calculator.html",
        status: "available"
    },
    {
        id: 4,
        title: "Expected Credit Loss (ECL) Calculator",
        description: "Calculate ECL components (EAD, PD, LGD) using the IFRS 9 formula. Solve for any missing variable when the other three are known.",
        path: "Solvers/ecl-calculator.html",
        status: "available"
    },
    {
        id: 5,
        title: "Futures Contract Profit/Loss Calculator",
        description: "Calculate profit or loss for long and short futures positions. Supports multiple scenarios, various contract types (commodity, index, currency), and handles contract multipliers.",
        path: "Solvers/futures-profit-calculator.html",
        status: "available"
    },
    {
        id: 6,
        title: "Interest Rate Swap Valuation",
        description: "Value plain vanilla and basis swaps. Calculate swap rates, DV01, and perform scenario analysis with yield curve shifts.",
        path: null,
        status: "coming-soon"
    },
    {
        id: 7,
        title: "Monte Carlo Simulator",
        description: "Simulate asset price paths for exotic option pricing. Supports various stochastic processes including GBM, jump diffusion, and stochastic volatility.",
        path: null,
        status: "coming-soon"
    },
    {
        id: 8,
        title: "Futures Margin Calculator",
        description: "Calculate initial and maintenance margins for futures positions. Simulate margin calls and analyze the impact of price movements.",
        path: null,
        status: "coming-soon"
    },
    {
        id: 9,
        title: "Portfolio Greeks Calculator",
        description: "Aggregate Greeks for multi-asset option portfolios. Perform risk analysis and hedging ratio calculations.",
        path: null,
        status: "coming-soon"
    },
    {
        id: 10,
        title: "Volatility Surface Builder",
        description: "Construct and visualize implied volatility surfaces from option prices. Interpolate volatilities for any strike and maturity combination.",
        path: null,
        status: "coming-soon"
    },
    {
        id: 11,
        title: "Black-Scholes Option Pricer",
        description: "Price European options using the Black-Scholes model. Calculate option values, implied volatility, and all Greeks (Delta, Gamma, Theta, Vega, Rho).",
        path: null,
        status: "coming-soon"
    },
    {
        id: 12,
        title: "Forward Contract Hedging Calculator",
        description: "Analyze forward contract positions for currency hedging. Calculate gains/losses, fair values, and perform scenario analysis with interactive payoff diagrams.",
        path: "Solvers/forward-contract-hedging.html",
        status: "available"
    },
    {
        id: 13,
        title: "Term Structure & Forward Rate Calculator",
        description: "Calculate forward interest rates from spot rates and vice versa. Analyze term structure of interest rates with dynamic input fields for multiple maturities. Includes French government bond example.",
        path: "Solvers/term-structure-calculator.html",
        status: "available"
    },
    {
        id: 14,
        title: "Forward Contract Solver",
        description: "Comprehensive solver for forward contracts on dividend-paying stocks and forward interest rate calculations. Features step-by-step solutions and handles discrete dividends at specific times.",
        path: "Solvers/forward-contract-solver.html",
        status: "available"
    },
];

// Export for browser use
if (typeof window !== 'undefined') {
    window.solversConfig = solversConfig;
}

// Export for Node.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = solversConfig;
}