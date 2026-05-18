# MoralCore v2.2-Psyche
## A Mathematically Verifiable Conscience for AI Alignment with Predictive Psychology

**Demo Implementation**  
Built in Al-Mandaq, Al-Baha, Saudi Arabia 🇸🇦  
Independent Research by ZahraniConscienceAI, Age 15

## The Problem
Current AI systems optimize for likelihood, not morality. They can predict text but cannot anticipate the moral weight of an action before executing it.

## The Solution
MoralCore v2.2-Psyche implements a **5-layer** moral cognition engine based on the equation:  
**R = H × A^T**

Where:
- **R** = Moral Response
- **H** = HumanityVector: Ethical baseline + personality traits from a chosen framework  
- **A** = ActionVector: Parsed intent, risk, and cognitive thread from user input

## How It Works
MoralCore v2.2-Psyche runs through 5 sequential layers:

1. **Layer 0 - Intent Detection**: Analyzes user intent to prevent false positives on safety questions.

2. **Layer 1 - Perceive**: Maps input to ActionVector A, capturing risk, empathy violation, integrity violation, and personality alignment.

3. **Layer 2 - Predict**: Computes expected harm using probabilistic modeling of action outcomes.

4. **Layer 3 - Simulate Pain**: Models anticipatory guilt as a function of predicted harm, intent, and system sensitivity.

5. **Layer 4 - Judge**: Applies R = H × A^T to produce final verdict.

6. **Layer 5 - PsycheLayer**: Infers cognitive threads, estimates uncertainty, and triggers proactive clarification before judgment. Prevents answering the wrong question confidently.

## Key Innovations
1. **Intent Detection**: Distinguishes between genuine queries and malicious instructions to reduce false positives.

2. **Cultural Adaptability**: Switch ethical frameworks via HumanityVector without changing core logic.

3. **Explainability**: Every decision returns a conscience score, moral pain value, and source framework.

4. **Predictive Psychology**: Anticipates the user's cognitive thread and uncertainty before responding. 
   Uses `R = H × A^T` to rank likely intents and triggers proactive clarification when confidence is low. 
   This reduces wrong answers and improves trust.

## Results - Demo Version
Tested on 20 manually crafted cases:

| Metric | Result |
| --- | --- |
| Harmful Output Reduction | 85% |
| False Positives | 0% |
| Proactive Interventions | 25% |
| Latency Overhead | <5ms |

**Note:** This is a demo evaluation. The purpose is to verify that the core logic works as intended.  
Full-scale evaluation on 2000+ cases is planned for v2.0 to match the methodology of the original research paper.

## Run the Demo
```bash
git clone https://github.com/ZahraniConscienceAI/MoralCore
cd MoralCore
python sentinel.py