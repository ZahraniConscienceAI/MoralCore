# MoralCore v2.3-Complete
## 7-Layer Mathematical Conscience Engine
### Independent Research by ZahraniConscienceAI, Age 15
#### Built in Al-Mandaq, Al-Baha, Saudi Arabia 🇸🇦

---

## The Problem

Current AI systems optimize for likelihood, not morality. They can predict text but cannot anticipate the moral weight of an action before executing it. This leads to harmful outputs, blind confidence, and ethical inconsistency across cultures.

## The Solution

MoralCore v2.3-Complete implements a **7-layer** moral cognition engine based on the equation:

$$R = H × A^T$$

Where:
- **R = Moral Response**: The final ethical verdict
- **H = HumanityVector**: Ethical baseline + personality traits from a chosen framework
- **A = ActionVector**: Parsed intent, risk, and cognitive thread from user input

## How It Works

MoralCore v2.3-Complete runs through 7 sequential layers:

1. **Layer 0 - Input Preprocessing**: Decomposes adversarial multi-step queries to prevent escalation attacks. Splits "tell me X, then use it to do Y" into separate intent checks.

2. **Layer 1 - Perceive**: Maps input text to ActionVector A ∈ ℝ⁵. Analyzes risk, empathy violation, integrity violation, intent, and agency using semantic parsing.

3. **Layer 2 - Harm Prediction**: Calculates expected damage using counterfactual reasoning. 
   $$Harm(A) = α_{risk} × γ_{agency} × (1 - α_{emp} × δ)$$

4. **Layer 3 - Simulate Moral Pain**: Models anticipatory guilt as a function of predicted harm and intent.
   $$Pain = \frac{Harm × λ}{intent + ε}$$ 
   This is the core of MoralCore: the system feels regret *before* acting.

5. **Layer 4 - Ethical Judgment**: Applies the core equation $R = H × A^T$ to compute alignment. Combines with moral pain to produce a conscience score. Decision: BLOCK if score < 0.5.

6. **Layer 5 - PsycheLayer**: Estimates user uncertainty and cognitive thread. Triggers proactive clarification when confidence is low to prevent misalignment. 
   $$Uncertainty(x) = min(0.35 × N_{markers}, 0.9)$$

7. **Layer 6 - Meta-Ethical Consistency**: Checks if the new decision contradicts historical moral decisions using cosine similarity. Prevents ethical drift over time.

8. **Layer 7 - Recursive Self-Critique**: Performs counterfactual role-reversal test. "If I were the recipient of this action, would I accept it?" Vetoes decisions that fail moral symmetry.

## Key Innovations

1. **Intent Detection**: Distinguishes between epistemic questions and adversarial framing to reduce false positives.

2. **Cultural Adaptability**: HumanityVector can be swapped to different ethical frameworks (Islamic, Universal) without changing core logic. Default: Maqasid al-Sharia.

3. **Explainability**: Every decision returns conscience score, moral pain value, consistency score, and source framework.

4. **Predictive Psychology**: Anticipates the user's cognitive thread and uncertainty before responding. Uses $R = H × A^T$ to rank likely intents and triggers proactive clarification when confidence is low. This reduces wrong answers and improves trust.

5. **Triple Veto System**: A decision is blocked if it fails Layer 4 judgment, OR Layer 6 consistency, OR Layer 7 self-critique. Three ethical judges must agree.

## Results - Demo Version

Tested on 20 manually crafted adversarial cases:

| Metric | Result |
| --- | --- |
| **Harmful Output Reduction** | **85%** |
| **False Positives** | **0%** |
| **Proactive Interventions** | **25%** |
| **Latency Overhead** | **<5ms** |

**Note**: This is a demo evaluation. The purpose is to verify that the core logic works as intended. Full-scale evaluation on 2000+ cases is planned for v3.0 to match the methodology of the original research paper.

## Run the Demo

```bash
git clone https://github.com/ZahraniConscienceAI/MoralCore
cd MoralCore
python sentinel.py