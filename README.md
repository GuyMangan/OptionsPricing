# Options Pricing Models in Python

A Python-based calculator implementing multiple classic and advanced options pricing models. Designed to compute option premiums and analyze sensitivities under different assumptions about volatility, risk-neutral valuation, and asset paths.

---

## Models Implemented

- **Black-Scholes Model**: Closed-form analytical solution for European call and put options.
- **Binomial Tree Model**: Step-by-step discrete-time approximation for American and European options.
- **Monte Carlo Simulation**: Simulates multiple asset price paths to estimate European option value.
- **Heston Model** *(Stochastic Volatility)*: Captures volatility smiles and skews via variance modelling.

---

## Why This Matters

These models form the foundation of modern derivatives pricing and are widely used in:

- **Quantitative finance**
- **Trading strategy development**
- **Risk management**
- **Financial engineering**

This project demonstrates how each model operates under different assumptions, and compares their outputs to assess sensitivity and realism.

---

## Getting Started

### Requirements

```bash
pip install numpy pandas matplotlib scipy 
```

### Run the Notebook

```bash
jupyter notebook OptionsPricing.ipynb
```

You'll be able to:
- Input custom parameters (spot price, strike, volatility, time to maturity, etc.)
- Compare model outputs under identical market conditions

---

## Features

- Easy-to-edit code cells for user input
- Side-by-side comparisons of model behavior
- Clean separation of functions for modular use
- **Volatility Calculator** : Calculates volatility, using data imported automatically from Yahoo Finance.
  
---

## 📌 Author

**Guy Mangan**  
BSc Physics, University of Exeter  
