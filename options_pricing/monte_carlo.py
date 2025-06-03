def monte_carlo_call(
    S0: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    M: int = 10000
) -> float:
    """
    Calculates call price of an European Option using a Monte Carlo Simulation
    using the (risk-neutral) Black Scholes Options pricing model (risk-neutral Geometric Brownian Motion (analytic solution)).

    Inputs:
        S0 (float):    Initial stock price.
        K (float):     Strike price.
        T (float):     Time to maturity (in years).
        r (float):     Risk-free interest rate.
        sigma (float): Annual volatility.
        M (int):       Number of Monte Carlo simulations.

    Returns:
        float: Estimated call option value at t=0.
    """

    Z = np.random.standard_normal(M) #M random numbers (on a normal distribution)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * math.sqrt(T) * Z) #analytic solution of GBM (https://en.wikipedia.org/wiki/Geometric_Brownian_motion)
    payoffs = np.maximum(ST - K, 0.0)
    expected_payoff = np.mean(payoffs)
    return expected_payoff * math.exp(-r * T) #discounting by risk free rate

def analytic_monte_carlo_put(
    S0: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    M: int = 10000
) -> float:
    """
    Calculates put price of an European Option using a Monte Carlo Simulation
    using the (risk-neutral) Black Scholes Options pricing model (risk-neutral Geometric Brownian Motion (analytic solution)).

    Inputs:
        S0 (float):    Initial stock price.
        K (float):     Strike price.
        T (float):     Time to maturity (in years).
        r (float):     Risk-free interest rate.
        sigma (float): Annual volatility.
        M (int):       Number of Monte Carlo simulations.

    Returns:
        float: Estimated call option value at t=0.
    """

    Z = np.random.standard_normal(M) #M random numbers (on a normal distribution)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * math.sqrt(T) * Z) #analytic solution of GBM (https://en.wikipedia.org/wiki/Geometric_Brownian_motion)
    payoffs = np.maximum(K - ST, 0.0)
    expected_payoff = np.mean(payoffs)
    return expected_payoff * math.exp(-r * T) #discounting by risk free rate
