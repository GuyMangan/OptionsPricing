# greeks/bs_greeks

import numpy as np
from scipy.stats import norm

def bs_greeks(
    S: float, 
    K: float, 
    T: float, 
    r: float, 
    sigma: float, 
    option_type: str = "call"
) -> dict:
    
    """Calculates the Greeks for a European option using the Black-Scholes model.

    Inputs:
        S (float):     Stock Price.
        K (float):     Strike price.
        T (float):     Time to maturity (in years).
        r (float):     Risk-free rate.
        sigma (float): Volatility (annual).
        option_type (str): "call" or "put"

    Returns:
        dict: Dictionary of Greeks: delta, gamma, vega, theta, rho
        
    Source for formulae:
        https://www.macroption.com/black-scholes-formula/#delta
    
    Note: 252 in theta formula is number of trading days in a year. Makes theta = change in option price per one trading day"""
    
    d1 = (np.log(S0/K)+(r+((sigma**2)/2))*T)/(sigma*np.sqrt(T))
    d2 = d1 - (sigma*np.sqrt(T))
    
    pdf_d1 = np.exp(-0.5 * d1**2) / np.sqrt(2 * np.pi) #probability density function (1st derivative)
    
    #not including dividend yield (merton extension)
    if option_type == "call":
        delta = norm.cdf(d1)
        theta = (1/252)*(((-S*sigma*pdf_d1)/(2*np.sqrt(T))) - r*K*np.exp(-r*T)*norm.cdf(d2))
        rho = (1/100)*K*T*np.exp(-r*T)*norm.cdf(d2)
    
    elif option_type == "put":
        delta = norm.cdf(d1) - 1
        theta = (1/252)*(((-S*sigma*pdf_d1)/(2*np.sqrt(T))) + r*K*np.exp(-r*T)*norm.cdf(-d2))
        rho = -(1/100)*K*T*np.exp(-r*T)*norm.cdf(-d2)
    
    else:
        print("Option type must be 'put' or 'call'")
    
    vega = S*pdf_d1*np.sqrt(T)/100
    gamma = pdf_d1/(S*sigma*np.sqrt(T))
    
    return {
        "delta": delta,
        "gamma": gamma,
        "vega": vega,
        "theta": theta,
        "rho": rho
    }
        