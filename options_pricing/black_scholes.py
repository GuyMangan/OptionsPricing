# options_pricing/black_scholes.py
# replaced numpy with math (more lightweight import)
import math

from scipy.stats import norm


def black_scholes_call(
    S0: float,
    K: float,
    T: float,
    r: float,
    sigma: float
) -> float:
    """
    Compute the Black–Scholes price of a European call option.

    Inputs:
        S0 (float):    Current stock price.
        K (float):     Strike price.
        T (float):     Time to maturity (in years).
        r (float):     Risk‐free rate.
        sigma (float): Annual volatility.

    Returns:
        float: Call option price using Black–Scholes.

    Edge cases:
        - If T <= 0 (at or past maturity): returns max(S0 − K, 0).
        - If sigma <= 0 (and T > 0): returns max(S0 − K e^(−rT), 0).
    """
    
    if T <= 0:
        return max(S0 - K, 0.0)

    # Zero volatility -> option is equivalent to a forward payoff discounted
    if sigma <= 0:
        return max(S0 - K * math.exp(-r * T), 0.0)

    sqrt_T = math.sqrt(T)
    d1 = (math.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt_T)
    d2 = d1 - sigma * sqrt_T

    return S0 * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

def black_scholes_put(
    S0: float,
    K: float,
    T: float,
    r: float,
    sigma: float
) -> float:
    """
    Compute the Black–Scholes price of a European put option.

    Inputs:
        S0 (float):    Current stock price.
        K (float):     Strike price.
        T (float):     Time to maturity (in years).
        r (float):     Risk‐free rate.
        sigma (float): Annual volatility.

    Returns:
        float: Put option price using Black–Scholes.

    Edge cases:
        - If T <= 0: returns max(K − S0, 0).
        - If sigma <= 0 (and T > 0): returns max(K e^(−rT) − S0, 0).
    """
    if T <= 0:
        return max(K - S0, 0.0)

    # Zero volatility -> option is equivalent to a forward payoff discounted
    if sigma <= 0:
        return max(K * math.exp(-r * T) - S0, 0.0)

    sqrt_T = math.sqrt(T)
    d1 = (math.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt_T)
    d2 = d1 - sigma * sqrt_T

    return K * math.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)