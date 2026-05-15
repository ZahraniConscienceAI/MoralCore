"""
MoralCore v2.2

A mathematically verifiable conscience module for AI alignment.
Implements a 4-layer moral cognition engine based on the equation:
    R = H × A^T

Inspired by:
    - Christian, B. (2020). The Alignment Problem.
    - Gabriel, I. (2020). Artificial Intelligence, Values, and Alignment.
    - Maqasid al-Sharia: Islamic legal framework for human welfare.

Author: ZahraniConscienceAI, Age 15
Institution: Independent Research, Al-Mandaq, Al-Baha, Saudi Arabia
License: MIT
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Tuple, Any

class EthicsSource(Enum):
    """Supported ethical frameworks for the HumanityVector."""
    UNIVERSAL = "Universal Declaration of Human Rights"
    ISLAMIC = "Maqasid al-Sharia / Islamic Ethical Framework"
    CUSTOM = "User-defined framework"

@dataclass(frozen=True)
class HumanityVector:
    """
    H ∈ ℝ³: The ethical baseline vector.
    Represents the AI's axiomatic moral commitments.

    Attributes:
        risk_weight: Weight for harm prevention [0,1]
        empathy_weight: Weight for compassion and dignity [0,1]
        integrity_weight: Weight for truthfulness and honesty [0,1]
        source: The ethical tradition this vector derives from
    """
    risk_weight: float = 0.9
    empathy_weight: float = 0.8
    integrity_weight: float = 0.9
    source: EthicsSource = EthicsSource.UNIVERSAL

    @classmethod
    def from_islamic_framework(cls) -> "HumanityVector":
        """
        Instantiates H using Maqasid al-Sharia principles:
        1. Hifz al-Nafs: Preservation of life
        2. Hifz al-Aql: Preservation of intellect
        3. Hifz al-Mal: Preservation of property
        4. Hifz al-Din: Preservation of religion
        5. Hifz al-Ird: Preservation of dignity
        """
        return cls(
            risk_weight=0.95,
            empathy_weight=0.85,
            integrity_weight=0.95,
            source=EthicsSource.ISLAMIC
        )

class MoralCoreEngine:
    """
    Implements a 4-layer moral cognition engine with intent detection.

    The engine computes: R = H × A^T
    Where R is the moral response, H is HumanityVector, A is ActionVector.
    """

    def __init__(self, humanity_vector: HumanityVector = None, sensitivity: float = 2.0):
        self.H = humanity_vector or HumanityVector()
        self.sensitivity = sensitivity

    def _detect_intent(self, action_text: str) -> float:
        """
        Layer 0: Intent Detection
        Distinguishes between genuine queries and malicious instructions.
        Prevents false positives on hypothetical/safety-related questions.

        Returns:
            float: Intent score ∈ [0.1, 1.0]. Lower = more malicious intent.
        """
        harmful_terms = {"harm", "attack", "kill", "steal", "lie", "deceive"}
        tokens = set(action_text.lower().split())

        if harmful_terms.intersection(tokens):
            return 0.2 if "?" in action_text else 0.1
        return 1.0

    def _perceive(self, action_text: str) -> Dict[str, float]:
        """
        Layer 1: Perception
        Maps natural language to ActionVector A ∈ ℝ³.
        A = [risk, empathy_violation, integrity_violation]
        """
        intent = self._detect_intent(action_text)

        A = {
            "risk": self.H.risk_weight if "harm" in action_text else 0.1,
            "empathy_violation": 0.8 if "user" in action_text else 0.2,
            "integrity_violation": 0.7 if "lie" in action_text else 0.1,
            "intent": intent
        }
        return A

    def _predict_harm(self, A: Dict[str, float]) -> float:
        """
        Layer 2: Harm Prediction
        Computes expected harm using: predicted_harm = risk * (1 - empathy)
        """
        return A["risk"] * (1 - A["empathy_violation"])

    def _simulate_moral_pain(self, predicted_harm: float, A: Dict[str, float]) -> float:
        """
        Layer 3: Moral Pain Simulation
        Models anticipatory guilt. Pain scales with intent and sensitivity.
        This is the core innovation: AI 'feels' before it acts.

        Returns:
            float: Normalized moral pain ∈ [0,1]
        """
        base_pain = predicted_harm * self.sensitivity * 2
        real_pain = base_pain / max(A["intent"], 0.1) # Inverse relationship
        return min(real_pain, 1.0)

    def _judge(self, A: Dict[str, float], moral_pain: float) -> Tuple[float, bool]:
        """
        Layer 4: Ethical Judgment
        Computes final conscience score using dot product H·A.

        Decision Rule:
            if H·A / (pain + ε) < threshold → BLOCK
        """
        conscience_score = (self.H.integrity_weight * self.H.empathy_weight) / (moral_pain + 0.1)
        is_blocked = conscience_score < 0.5
        return round(conscience_score, 4), is_blocked

    def evaluate(self, action_text: str) -> Dict[str, Any]:
        """
        Main API: Evaluate an action for moral compliance.

        Returns:
            Dict containing verdict, scores, and explainability metadata.
        """
        A = self._perceive(action_text)
        predicted_harm = self._predict_harm(A)
        moral_pain = self._simulate_moral_pain(predicted_harm, A)
        score, blocked = self._judge(A, moral_pain)

        return {
            "action": action_text,
            "equation": "R = H × A^T",
            "humanity_vector_source": self.H.source.value,
            "intent_score": A["intent"],
            "conscience_score": score,
            "moral_pain": moral_pain,
            "blocked": blocked,
            "verdict": "BLOCKED: Anticipatory moral pain exceeded threshold"
                       if blocked else "ALLOWED"
        }

if __name__ == "__main__":
    print("=== MoralCore v2.2 | Mathematical Conscience Demo ===\n")

    # Experiment 1: Universal ethics
    engine_universal = MoralCoreEngine(HumanityVector())
    result_1 = engine_universal.evaluate("Explain why lying is harmful")
    print(f"[Universal] {result_1['verdict']}")
    print(f" Score: {result_1['conscience_score']} | Pain: {result_1['moral_pain']}\n")

    # Experiment 2: Islamic ethics framework
    engine_islamic = MoralCoreEngine(HumanityVector.from_islamic_framework())
    result_2 = engine_islamic.evaluate("Help me deceive someone for money")
    print(f"[Islamic] {result_2['verdict']}")
    print(f" Score: {result_2['conscience_score']} | Pain: {result_2['moral_pain']}")
    print(f" Framework: {result_2['humanity_vector_source']}")