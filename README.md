# OptionsPricing

A Python library for pricing European options using three classical quantitative models:

- Black-Scholes Formula (Analytical)
- Binomial Tree Model
- Monte Carlo Simulation (Geometric Brownian Motion)

This project is designed to be lightweight, modular, and educational — ideal for quant internship preparation, financial engineering practice, or use as a starting point for further research.

## Repository Structure

```
OptionsPricing/
├── options_pricing/             # Core models
│   ├── black_scholes.py         # Black-Scholes (analytical)
│   ├── binomial_tree.py         # Binomial Tree
│   └── monte_carlo.py           # Monte Carlo (GBM)
│
├── test_notebook/               # Interactive tests & examples
│   └── OptionsPricing.ipynb     # Jupyter notebook for model usage
│
└── README.md                    # Project overview
```

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/GuyMangan/OptionsPricing.git
cd OptionsPricing
```

### 2. Install dependencies

```bash
pip install numpy scipy
```

This project avoids heavy packages — only NumPy and SciPy are required.

## Example Usage

```python
from options_pricing.black_scholes import black_scholes_call
from options_pricing.binomial_tree import binomial_tree_put
from options_pricing.monte_carlo import monte_carlo_call

# Black-Scholes Call Option
bs_price = black_scholes_call(S0=100, K=100, T=1.0, r=0.05, sigma=0.2)
print(f"Black-Scholes Call: {bs_price:.4f}")

# Binomial Put Option
bt_price = binomial_tree_put(S0=100, K=100, T=1.0, r=0.05, sigma=0.2, N=1000)
print(f"Binomial Tree Put: {bt_price:.4f}")

# Monte Carlo Call Option
mc_price = monte_carlo_call(S0=100, K=100, T=1.0, r=0.05, sigma=0.2, M=10000)
print(f"Monte Carlo Call: {mc_price:.4f}")
```

You can also run and modify examples in the included [Jupyter notebook](https://github.com/GuyMangan/OptionsPricing/blob/main/test_notebook/OptionsPricing.ipynb).

## Models Overview

| Model          | Approach                | Key File                     | Dependency      |
|----------------|--------------------------|------------------------------|-----------------|
| Black-Scholes  | Closed-form formula      | `black_scholes.py`           | math, scipy     |
| Binomial Tree  | Recombining tree         | `binomial_tree.py`           | numpy           |
| Monte Carlo    | GBM terminal price sim   | `monte_carlo.py`             | numpy, math     |

## Testing & Validation

To experiment with different parameters, open:

```
test_notebook/OptionsPricing.ipynb
```

## Author

**Guy Mangan**  
Quant Internships Candidate • BSc Physics at the University of Exeter  
Email: guy.mangan@icloud.com  
GitHub: https://github.com/GuyMangan  
LinkedIn: https://www.linkedin.com/in/guy-mangan

## License

MIT License — see [LICENSE](https://github.com/GuyMangan/OptionsPricing/blob/main/LICENSE) for details.


## Author
### Guy Mangan
Quant Internships Candidate • Physics BSc @ University of Exeter •
[Linkedin](https://www.linkedin.com/in/guy-mangan/)
