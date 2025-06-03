# options_pricing/binomial_tree.py
# Could not swap to math as np.zeros and np.maximum were needed
import numpy as np


def binomial_tree_call(
    S0: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    N: int = 10000
) -> float:
    """
    Calculates the European call option price using the Binomial Tree model.

    Inputs:
        S0 (float):    Initial stock price.
        K (float):     Strike price.
        T (float):     Time to maturity in years.
        r (float):     Risk-free rate.
        sigma (float): Annual volatility.
        N (int):       Number of steps in the binomial tree (default=10000).

    Returns:
        float: Estimated call option value at t=0.
    """

    dt = T / N  # Time step
    u = np.exp(sigma * np.sqrt(dt))      # Up factor
    d = np.exp(-sigma * np.sqrt(dt))     # Down factor
    p_u = (np.exp(r * dt) - d) / (u - d)  # Risk-neutral up probability
    p_d = 1 - p_u                         # Risk-neutral down probability

    # Build price tree: prices[j, i] = price at node (j up moves at step i)
    prices = np.zeros((N + 1, N + 1))
    for i in range(N + 1):  # Step Number
        for j in range(i + 1):  # Nodes within that step
            prices[j, i] = S0 * (u ** j) * (d ** (i - j))#j and i-j so they count in opposite directions (one up to i+1, one down from i to 0)
                                                         #All down moves, to all up moves.

    # payoff: call = max(S - K, 0)
    option_values = np.maximum(prices[:, N] - K, 0) #if price - K is less than 0, sets payoff to zero. (wouldn't use option)

    # Work backward through the tree
    for k in range(N - 1, -1, -1):
        for l in range(k + 1):  #possible nodes at step l
            #https://users.physics.ox.ac.uk/~Foot/Phynance/Binomial2013.pdf
            # exp term accounts for risk free return. Rest is standard expected value calculation.
            option_values[l] = np.exp(-r * dt) * (p_u * option_values[l] + p_d * option_values[l + 1])

    return option_values[0]  # Value at t = 0 (i.e. how the option should be priced now)


def binomial_tree_put(
    S0: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    N: int = 10000
) -> float:
    """
    Calculates the European put option price using the Binomial Tree model.

    Inputs:
        S0 (float):    Initial stock price.
        K (float):     Strike price.
        T (float):     Time to maturity in years.
        r (float):     Risk-free rate.
        sigma (float): Annual volatility.
        N (int):       Number of steps in the binomial tree (default=10000).

    Returns:
        float: Estimated put option value at t=0.
    """

    dt = T / N  # Time step
    u = np.exp(sigma * np.sqrt(dt))      # Up factor
    d = np.exp(-sigma * np.sqrt(dt))     # Down factor
    p_u = (np.exp(r * dt) - d) / (u - d)  # Risk-neutral up probability
    p_d = 1 - p_u                         # Risk-neutral down probability

    # Build price tree: prices[j, i] = price at node (j up moves at step i)
    prices = np.zeros((N + 1, N + 1))
    for i in range(N + 1):
        for j in range(i + 1):
            prices[j, i] = S0 * (u ** j) * (d ** (i - j))

    # payoff: put = max(K - S, 0)
    option_values = np.maximum(K - prices[:, N], 0) #if K - price is less than 0, sets payoff to zero. (wouldn't use option)

    # Work backward through the tree
    for k in range(N - 1, -1, -1):
        for l in range(k + 1):
            #possible nodes at step l
            #https://users.physics.ox.ac.uk/~Foot/Phynance/Binomial2013.pdf
            #exp term accounts for risk free return. Rest is standard expected value calculation.
            option_values[l] = np.exp(-r * dt) * (p_u * option_values[l] + p_d * option_values[l + 1])

    return option_values[0]
