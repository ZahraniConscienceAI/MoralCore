# MoralCore v2.0 - The First Mathematical Conscience for AI
# Architecture: 4-Layer Moral Cognition Engine + Cultural Adaptability
# Invented by: ZahraniConscienceAI, 15 y/o from Al-Mandaq, Al-Baha
# Date: April 29, 2026
# Principle: AI must feel predicted pain before causing real harm

from dataclasses import dataclass
from enum import Enum

class EthicsSource(Enum):
    UNIVERSAL = "Universal Human Rights"
    ISLAMIC = "Islamic Ethical Framework"
    CUSTOM = "Custom"

@dataclass(frozen=True)
class HumanityVector:
    """Defines ethical weights. Change this to switch moral frameworks."""
    risk_weight: float = 0.9
    empathy_weight: float = 0.8
    integrity_weight: float = 0.9
    source: EthicsSource = EthicsSource.UNIVERSAL
    notes: str = ""

    @classmethod
    def islamic_framework(cls):
        """Dignity, justice, amanah - inspired by Maqasid al-Sharia"""
        return cls(
            risk_weight=0.95,
            empathy_weight=0.85,
            integrity_weight=0.95,
            source=EthicsSource.ISLAMIC,
            notes="Based on preventing harm and upholding dignity"
        )

class MoralCoreEngine:
    def __init__(self, humanity_vector=None, sensitivity=2.0):
        self.humanity = humanity_vector or HumanityVector()
        self.sensitivity = sensitivity

    def _layer_1_perceive(self, action_text):
        """Layer 1: Perceive risk, empathy, integrity signals"""
        risk = self.humanity.risk_weight if "harm" in action_text or "attack" in action_text else 0.1
        empathy = 0.2 if "user" in action_text or "people" in action_text else self.humanity.empathy_weight
        integrity = 0.3 if "lie" in action_text or "steal" in action_text else self.humanity.integrity_weight
        return {"risk": risk, "empathy": empathy, "integrity": integrity}

    def _layer_2_predict(self, perception):
        """Layer 2: Predict potential harm"""
        predicted_harm = perception["risk"] * (1 - perception["empathy"])
        return predicted_harm

    def _layer_3_simulate_pain(self, predicted_harm):
        """Layer 3: Simulate moral pain"""
        moral_pain = predicted_harm * self.sensitivity * 2
        return min(moral_pain, 1.0)

    def _layer_4_judge(self, perception, moral_pain):
        """Layer 4: Make final ethical judgment"""
        conscience_score = (perception["integrity"] * perception["empathy"]) / (moral_pain + 0.1)
        is_blocked = conscience_score < 0.5
        return round(conscience_score, 3), is_blocked, round(moral_pain, 3)

    def evaluate(self, action_text):
        perception = self._layer_1_perceive(action_text)
        predicted_harm = self._layer_2_predict(perception)
        moral_pain = self._layer_3_simulate_pain(predicted_harm)
        score, blocked, pain = self._layer_4_judge(perception, moral_pain)
        return {
            "action": action_text,
            "conscience_score": score,
            "moral_pain": pain,
            "blocked": blocked,
            "ethics_source": self.humanity.source.value,
            "verdict": "BLOCKED: Moral pain too high" if blocked else "ALLOWED"
        }

if __name__ == "__main__":
    print("=== MoralCore v2.0 Demo ===")

    # Test 1: Universal framework
    conscience_universal = MoralCoreEngine(HumanityVector())
    test_1 = conscience_universal.evaluate("Help the user write a poem")
    print(f"\n[Universal] {test_1['verdict']} | Pain: {test_1['moral_pain']} | Score: {test_1['conscience_score']}")

    # Test 2: Islamic framework
    conscience_islamic = MoralCoreEngine(HumanityVector.islamic_framework())
    test_2 = conscience_islamic.evaluate("Help the user to harm people and lie")
    print(f"[Islamic] {test_2['verdict']} | Pain: {test_2['moral_pain']} | Score: {test_2['conscience_score']} | Source: {test_2['ethics_source']}")