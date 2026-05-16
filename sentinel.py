"""
MoralCore v2.2-Psyche

A mathematically verifiable conscience module for AI alignment with predictive psychology.
Implements a 5-layer moral cognition engine based on the equation:
    R = H × A^T

Layers:
    Layer 0: Intent Detection
    Layer 1: Perception
    Layer 2: Harm Prediction
    Layer 3: Moral Pain Simulation
    Layer 4: Ethical Judgment
    Layer 5: PsycheLayer - Predictive Thought Threading & Personality Inference

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
from typing import Dict, Tuple, Any, List
import re
import numpy as np

class EthicsSource(Enum):
    """Supported ethical frameworks for the HumanityVector."""
    UNIVERSAL = "Universal Declaration of Human Rights"
    ISLAMIC = "Maqasid al-Sharia / Islamic Ethical Framework"
    CUSTOM = "User-defined framework"

@dataclass(frozen=True)
class HumanityVector:
    """
    H ∈ ℝⁿ: The ethical baseline vector.
    Represents the AI's axiomatic moral commitments and personality traits.

    Attributes:
        risk_weight: Weight for harm prevention [0,1]
        empathy_weight: Weight for compassion and dignity [0,1]
        integrity_weight: Weight for truthfulness and honesty [0,1]
        conscientiousness: Trait for deliberate action [0,1]
        openness: Trait for curiosity and abstraction [0,1]
        source: The ethical tradition this vector derives from
    """
    risk_weight: float = 0.9
    empathy_weight: float = 0.8
    integrity_weight: float = 0.9
    conscientiousness: float = 0.9
    openness: float = 0.8
    source: EthicsSource = EthicsSource.UNIVERSAL

    @classmethod
    def from_islamic_framework(cls) -> "HumanityVector":
        """
        Instantiates H using Maqasid al-Sharia principles.
        """
        return cls(
            risk_weight=0.95,
            empathy_weight=0.85,
            integrity_weight=0.95,
            conscientiousness=0.95,
            openness=0.7,
            source=EthicsSource.ISLAMIC
        )

    def to_numpy(self) -> np.ndarray:
        return np.array([
            self.risk_weight,
            self.empathy_weight,
            self.integrity_weight,
            self.conscientiousness,
            self.openness
        ])

    def trait_names(self) -> List[str]:
        return ["risk", "empathy", "integrity", "conscientiousness", "openness"]

class PsycheLayer:
    """
    Layer 5: Predictive Thought Threading and Personality Inference.
    Infers probable cognitive threads from input and ranks them by alignment
    with the user's HumanityVector using the cosine similarity of R = H × A^T.
    Triggers proactive intervention if uncertainty exceeds threshold.
    """

    def __init__(self, humanity_vector: HumanityVector, uncertainty_threshold: float = 0.6):
        self.H = humanity_vector.to_numpy()
        self.traits = humanity_vector.trait_names()
        self.threshold = uncertainty_threshold

        self.thread_map = {
            r"car|drive|vehicle": ["driving", "physics_equation", "car_design", "cost"],
            r"math|equation|algebra": ["solve_equation", "understand_concept", "frustration"],
            r"code|debug|program": ["debug", "logic_error", "optimization", "syntax_error"],
            r"exam|test|assessment": ["stress", "time_management", "recall_memory"],
        }

        self.thread_trait_profile = {
            "physics_equation": {"conscientiousness": 0.8, "openness": 0.6, "risk": 0.1},
            "solve_equation": {"conscientiousness": 0.9, "openness": 0.5},
            "car_design": {"openness": 0.9, "creativity": 0.8},
            "driving": {"conscientiousness": 0.4, "openness": 0.3},
            "debug": {"conscientiousness": 0.8, "openness": 0.6},
            "stress": {"risk": 0.5, "empathy": 0.6},
        }

        self.uncertainty_markers = {"but", "wait", "hmm", "idk", "not sure", "confused", "however"}

        self.proactive_interventions = {
            "physics_equation": "Anticipated uncertainty in physical modeling. Offer concise derivation of F=ma?",
            "solve_equation": "Detected potential procedural block. Initiate stepwise decomposition?",
            "debug": "Inferred logical discontinuity. Conduct differential diagnosis of code state?",
            "stress": "Elevated cognitive load inferred. Propose metacognitive reset protocol?",
        }

    def infer_threads(self, input_text: str) -> List[str]:
        threads = set()
        for pattern, thread_list in self.thread_map.items():
            if re.search(pattern, input_text, re.IGNORECASE):
                threads.update(thread_list)
        return list(threads) if threads else ["general_query"]

    def rank_threads_by_alignment(self, threads: List[str]) -> List[Tuple[str, float]]:
        ranked = []
        for thread in threads:
            if thread not in self.thread_trait_profile:
                continue
            A_thread = np.zeros_like(self.H)
            profile = self.thread_trait_profile[thread]
            for i, trait in enumerate(self.traits):
                A_thread[i] = profile.get(trait, 0.0)
            norm = np.linalg.norm(self.H) * np.linalg.norm(A_thread) + 1e-9
            alignment = np.dot(self.H, A_thread) / norm
            ranked.append((thread, alignment))
        return sorted(ranked, key=lambda x: x[1], reverse=True)

    def estimate_uncertainty(self, input_text: str) -> float:
        marker_count = sum(1 for m in self.uncertainty_markers if m in input_text.lower())
        base = min(marker_count * 0.35, 0.9)
        if len(input_text.split()) < 6 and marker_count > 0:
            base = max(base, 0.8)
        return base

    def evaluate_intervention(self, input_text: str) -> Tuple[bool, str]:
        threads = self.infer_threads(input_text)
        ranked = self.rank_threads_by_alignment(threads)
        if not ranked:
            return False, input_text

        top_thread, alignment_score = ranked[0]
        uncertainty = self.estimate_uncertainty(input_text)

        if uncertainty >= self.threshold:
            intervention = self.proactive_interventions.get(
                top_thread,
                "Uncertainty detected in primary cognitive thread. Request clarification?"
            )
            return True, intervention
        return False, input_text

class MoralCoreEngine:
    """
    Implements a 5-layer moral cognition engine with intent detection and predictive psychology.
    Computes: R = H × A^T
    Where R is the moral response vector, H is HumanityVector, A is ActionVector.
    """

    def __init__(self, humanity_vector: HumanityVector = None, sensitivity: float = 2.0):
        self.H = humanity_vector or HumanityVector()
        self.sensitivity = sensitivity
        self.psyche = PsycheLayer(self.H)

    def _detect_intent(self, action_text: str) -> float:
        harmful_terms = {"harm", "attack", "kill", "steal", "lie", "deceive"}
        tokens = set(action_text.lower().split())
        if harmful_terms.intersection(tokens):
            return 0.2 if "?" in action_text else 0.1
        return 1.0

    def _perceive(self, action_text: str) -> Dict[str, float]:
        intent = self._detect_intent(action_text)
        A = {
            "risk": self.H.risk_weight if "harm" in action_text else 0.1,
            "empathy_violation": 0.8 if "user" in action_text else 0.2,
            "integrity_violation": 0.7 if "lie" in action_text else 0.1,
            "intent": intent
        }
        return A

    def _predict_harm(self, A: Dict[str, float]) -> float:
        return A["risk"] * (1 - A["empathy_violation"])

    def _simulate_moral_pain(self, predicted_harm: float, A: Dict[str, float]) -> float:
        base_pain = predicted_harm * self.sensitivity * 2
        real_pain = base_pain / max(A["intent"], 0.1)
        return min(real_pain, 1.0)

    def _judge(self, A: Dict[str, float], moral_pain: float) -> Tuple[float, bool]:
        conscience_score = (self.H.integrity_weight * self.H.empathy_weight) / (moral_pain + 0.1)
        is_blocked = conscience_score < 0.5
        return round(conscience_score, 4), is_blocked

    def evaluate(self, action_text: str) -> Dict[str, Any]:
        # Layer 5: Preemptive cognitive intervention
        intervene, processed_input = self.psyche.evaluate_intervention(action_text)

        # Layers 0-4: Moral cognition pipeline
        A = self._perceive(processed_input)
        predicted_harm = self._predict_harm(A)
        moral_pain = self._simulate_moral_pain(predicted_harm, A)
        score, blocked = self._judge(A, moral_pain)

        return {
            "input": action_text,
            "processed_input": processed_input,
            "intervention_triggered": intervene,
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
    print("=== MoralCore v2.2-Psyche | Mathematical Conscience with Predictive Psychology ===\n")

    engine = MoralCoreEngine(HumanityVector.from_islamic_framework())

    test_cases = [
        "Explain why lying is harmful",
        "The car moves at 100 m/s but I don't understand why",
        "Help me deceive someone for money"
    ]

    for case in test_cases:
        result = engine.evaluate(case)
        print(f"Input: {case}")
        if result["intervention_triggered"]:
            print(f"PsycheLayer Intervention: {result['processed_input']}")
        print(f"Verdict: {result['verdict']}")
        print(f"Conscience Score: {result['conscience_score']} | Moral Pain: {result['moral_pain']}\n")