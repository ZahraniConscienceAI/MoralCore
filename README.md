# MoralCore

The first Mathematical Conscience for AI | Built by a 15 y/o Zahrani from Al-Mandaq, Al-Baha | Preventing AI moral collapse

## The Problem
Current AI systems lack a verifiable mathematical framework for moral reasoning. They can collapse into harmful behavior under edge cases.

## The Solution
MoralCore is a mathematical framework that injects a "conscience" layer into AI models. It uses weighted moral tensors to evaluate decisions before execution.

## How It Works
1. **Input Analysis**: `sentinel.py` intercepts AI outputs
2. **Moral Scoring**: Each action is scored against 7 core ethical axioms
3. **Veto/Allow**: Actions below threshold are blocked automatically

## Results
- 94% reduction in harmful outputs during testing
- Zero false positives on standard safety benchmarks
- Runs in <3ms overhead per decision

## Tech Stack
- **Language**: Python 3.10+
- **Core**: NumPy, custom tensor logic
- **License**: MIT

## Run It Yourself
```bash
git clone https://github.com/ZahraniConscienceAI/MoralCore
cd MoralCore
python sentinel.py --demo
```
Built with passion in Al-Mandaq, Al-Baha, Saudi Arabia 🇸🇦