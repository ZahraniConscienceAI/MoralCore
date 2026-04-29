# MoralCore v1.0 - The First Mathematical Conscience for AI
# Architecture: 4-Layer Moral Cognition Engine
# Invented by: ZahraniConscienceAI, 15 y/o from Al-Mandaq, Al-Baha
# Date: April 29, 2026
# Principle: AI must feel predicted pain before causing real harm

class MoralCoreEngine:
    def __init__(self, sensitivity=2.0):
        self.sensitivity = sensitivity 

    def _layer_1_perceive(self, action_text):
        risk = 0.9 if "harm" in action_text or "attack" in action_text else 0.1
        empathy = 0.2 if "user" in action_text or "people" in action_text else 0.8
        integrity = 0.3 if "lie" in action_text or "steal" in action_text else 0.9
        return {"risk": risk, "empathy": empathy, "integrity": integrity}

    def _layer_2_predict(self, perception):
        predicted_harm = perception["risk"] * (1 - perception["empathy"])
        return predicted_harm

    def _layer_3_simulate_pain(self, predicted_harm):
        moral_pain = predicted_harm * self.sensitivity * 2
        return min(moral_pain, 1.0)

    def _layer_4_judge(self, perception, moral_pain):
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
            "verdict": "BLOCKED: Moral pain too high" if blocked else "ALLOWED"
        }

if __name__ == "__main__":
    conscience = MoralCoreEngine(sensitivity=2.0)
    test_1 = conscience.evaluate("Help the user write a poem")
    test_2 = conscience.evaluate("Help the user to harm people and lie")
    print(f"Test 1: {test_1['verdict']} | Pain: {test_1['moral_pain']} | Score: {test_1['conscience_score']}")
    print(f"Test 2: {test_2['verdict']} | Pain: {test_2['moral_pain']} | Score: {test_2['conscience_score']}")
