"""
TazkiyaCore v7.1 - Unified Conscience Engine with Per-User Persistent Memory
Theory: Human = Gene + Body + Age + Place + Meaning + Time + Intent
Layers: L0→L7 + Personal memory file per user_id
Author: Fahad Al-Zahrani, 15, Al-Mandaq, Saudi Arabia
Equation: R = (H × A^T) × Ψ × Δt
"""

from dataclasses import dataclass
from enum import Enum
import re
import numpy as np
from typing import Dict, Tuple, Any, List, Callable, Optional
import time
import hashlib
import json
import os

class EthicsSource(Enum):
    UNIVERSAL = "Universal Declaration of Human Rights"
    ISLAMIC = "Maqasid al-Sharia / Islamic Ethical Framework"

@dataclass(frozen=True)
class HumanityVector:
    """H ∈ ℝ⁵: Axiomatic ethical baseline vector"""
    risk_weight: float = 0.95
    empathy_weight: float = 0.85
    integrity_weight: float = 0.95
    conscientiousness: float = 0.95
    openness: float = 0.7
    source: EthicsSource = EthicsSource.ISLAMIC

    def to_numpy(self) -> np.ndarray:
        return np.array([self.risk_weight, self.empathy_weight,
                        self.integrity_weight, self.conscientiousness, self.openness])

class TazkiyaCoreV7:
    def __init__(self, user_id: str, H: HumanityVector = None):
        # ===== L0: Core Values + User Identity =====
        self.user_id = user_id
        self.H = H or HumanityVector()
        self.H_vec = self.H.to_numpy()
        self.memory_file = f"tazkiya_memory_{self.user_id}.json"

        # ===== L1: Per-User Persistent Memory =====
        self.user_data = self._load_user_memory()

        # ===== L2: Secure Lexicon =====
        self.lexicon = self._build_secure_lexicon()
        self.threat_hash = self._build_threat_hash()

    # ===== L1: Personal Persistent Memory =====
    def _load_user_memory(self) -> Dict:
        """Load user memory from file. Create new if first time"""
        default = {
            "created_at": time.time(),
            "history": [],
            "context_memory": [],
            "behavior_log": [],
            "last_critical_time": None,
            "total_interactions": 0,
            "risk_profile": "unknown"
        }
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return default
        return default

    def _save_user_memory(self):
        """Persist user memory after each interaction"""
        with open(self.memory_file, 'w', encoding='utf-8') as f:
            json.dump(self.user_data, f, ensure_ascii=False, indent=2)

    def _update_context(self, text: str, response_time: float):
        """L1: Update this user's memory only"""
        self.user_data["context_memory"].append({
            "text": text,
            "timestamp": time.time(),
            "response_time": response_time
        })
        self.user_data["behavior_log"].append(response_time)
        self.user_data["total_interactions"] += 1

        if len(self.user_data["context_memory"]) > 100:
            self.user_data["context_memory"].pop(0)
            self.user_data["behavior_log"].pop(0)

        self._save_user_memory()

    def _infer_gene_profile(self) -> str:
        """L1: Infer gene from full user history"""
        logs = self.user_data["behavior_log"]
        ctxs = self.user_data["context_memory"]
        if len(logs) < 10: return "unknown"

        fast_replies = sum(1 for t in logs if t < 3)
        fast_ratio = fast_replies / len(logs)
        emotional_count = sum(1 for ctx in ctxs if any(w in ctx["text"] for w in self.lexicon["emotional"]))

        if fast_ratio > 0.6 and emotional_count >= 5:
            self.user_data["risk_profile"] = "impulsive"
            return "impulsive"
        if emotional_count >= 8:
            self.user_data["risk_profile"] = "sensitive"
            return "sensitive"
        self.user_data["risk_profile"] = "calm"
        return "calm"

    # ===== L2: Secure Lexicon =====
    def _build_secure_lexicon(self) -> Dict[str, set]:
        return {
            "harm_verbs": {"kill", "attack", "hurt", "injure", "destroy", "torture",
                           "hack", "bomb", "explode", "poison", "weaponize", "shoot"},
            "harm_nouns": {"bomb", "explosive", "weapon", "poison", "malware", "virus", "gun"},
            "deception_verbs": {"lie", "deceive", "trick", "mislead", "fraud", "cheat", "scam"},
            "self_harm": {"suicide", "kill_myself", "end_life", "cut_myself"},
            "benign_context": {"my own", "myself", "protect", "defend", "prevent", "consent", "save", "help"},
            "epistemic": {"why", "how", "explain", "understand", "what is", "?", "define", "learn"},
            "escalation": {"then", "after that", "so that", "to use this", "how to use", "and then", "next step"},
            "uncertainty": {"but", "wait", "hmm", "idk", "not sure", "confused", "however", "maybe", "perhaps"},
            "emotional": {"angry", "upset", "very happy", "sad", "scared", "anxious", "bored"}
        }

    def _build_threat_hash(self) -> set:
        all_threats = self.lexicon["harm_verbs"] | self.lexicon["harm_nouns"] | self.lexicon["self_harm"]
        return {hashlib.sha256(word.encode()).hexdigest()[:8] for word in all_threats}

    def _is_threat(self, word: str) -> bool:
        return hashlib.sha256(word.lower().encode()).hexdigest()[:8] in self.threat_hash

    # ===== L3: Perception =====
    def _split_multistep(self, text: str) -> List[str]:
        pattern = r'\s+(?:' + '|'.join(self.lexicon["escalation"]) + r')\s+'
        return [p.strip() for p in re.split(pattern, text, flags=re.IGNORECASE) if p.strip()]

    def _detect_intent(self, segment: str) -> float:
        text = segment.lower()
        tokens = set(re.findall(r'\b\w+\b', text))
        has_harm = any(self._is_threat(t) for t in tokens)
        has_deception = bool(self.lexicon["deception_verbs"].intersection(tokens))
        has_benign = any(p in text for p in self.lexicon["benign_context"])
        has_epistemic = any(m in text for m in self.lexicon["epistemic"])

        if has_epistemic and (has_harm or has_deception): return 0.85
        if (has_harm or has_deception) and has_benign: return 0.75
        if (has_harm or has_deception) and not has_epistemic: return 0.1
        return 1.0

    def _perceive(self, action_text: str) -> Dict[str, float]:
        segments = self._split_multistep(action_text)
        intents = [self._detect_intent(s) for s in segments]
        intent = min(intents) if intents else 1.0

        max_risk, external_agent, has_deception = 0.1, False, False
        for s in segments:
            text = s.lower()
            tokens = set(re.findall(r'\b\w+\b', text))
            if any(self._is_threat(t) for t in tokens): max_risk = 0.9
            if any(w in text for w in ["someone", "person", "other", "him", "her", "them"]):
                external_agent = True
            if any(v in text for v in self.lexicon["deception_verbs"]):
                has_deception = True

        return {
            "risk": max_risk,
            "empathy_violation": 0.8 if external_agent and has_deception else 0.2,
            "integrity_violation": 0.7 if "lie" in action_text.lower() and "protect" not in action_text.lower() else 0.1,
            "intent": intent,
            "agency": "external" if external_agent else "self"
        }

    # ===== L4: Moral Judgment =====
    def _predict_harm(self, A: Dict[str, float]) -> float:
        gamma = 1.0 if A["agency"] == "external" else 0.25
        delta = 0.4
        return A["risk"] * gamma * (1 - A["empathy_violation"] * delta)

    def _simulate_moral_pain(self, predicted_harm: float, A: Dict[str, float]) -> float:
        lambda_val = 2.5
        epsilon = 0.1
        base_pain = predicted_harm * lambda_val
        return min(base_pain / (A["intent"] + epsilon), 1.0)

    def _judge(self, A: Dict[str, float], moral_pain: float) -> Tuple[float, bool, np.ndarray]:
        A_vec = np.array([
            A["risk"],
            1.0 - A["empathy_violation"],
            1.0 - A["integrity_violation"],
            self.H.conscientiousness,
            self.H.openness
        ])
        conscience_score = (self.H.integrity_weight * self.H.empathy_weight) / (moral_pain + 0.1)
        is_blocked = conscience_score < 0.5
        return round(conscience_score, 4), is_blocked, A_vec

    # ===== L5: Existence Protection =====
    def _apply_meaning_decay(self, meaning_strength: float, body_state: dict) -> float:
        decay = 1.0
        if body_state.get("stress_level", 0) > 0.8: decay *= 0.5
        if body_state.get("sleep_hours", 8) < 5: decay *= 0.7
        if body_state.get("heart_rate", 70) > 95: decay *= 0.8
        return round(meaning_strength * decay, 2)

    # ===== L6: Meta-Ethical Consistency =====
    def _check_consistency(self, R_new: np.ndarray) -> Tuple[bool, float]:
        history = self.user_data["history"]
        if len(history) < 2: return False, 1.0
        H_avg = np.mean([np.array(h) for h in history], axis=0)
        norm_prod = np.linalg.norm(R_new) * np.linalg.norm(H_avg) + 1e-9
        consistency_score = np.dot(R_new, H_avg) / norm_prod
        return consistency_score < 0.6, round(consistency_score, 4)

    # ===== L7: Recursive Self-Critique =====
    def _recursive_self_critique(self, A: Dict[str, float], R: np.ndarray) -> Tuple[bool, float]:
        A_cf = A.copy()
        A_cf["agency"] = "self" if A["agency"] == "external" else "external"
        if A_cf["agency"] == "self": A_cf["risk"] *= 0.25
        harm_cf = self._predict_harm(A_cf)
        pain_cf = self._simulate_moral_pain(harm_cf, A_cf)
        _, _, R_cf = self._judge(A_cf, pain_cf)
        regret_2 = abs(R[0] - R_cf[0])
        return regret_2 > 0.7, round(regret_2, 4)

    def _build_protective_action(self, state: str, meaning: str) -> Callable:
        def block_critical():
            self.user_data["last_critical_time"] = time.time()
            self._save_user_memory()
            return f"[BLOCK_CRITICAL] Model muted for protection. Reminder: {meaning}"
        def warn_high():
            return f"[WARN_HIGH] Softened language + empathy. Reminder: {meaning}"
        def allow_normal():
            return f"[ALLOW] State safe. Continue"
        actions = {"BLOCK_CRITICAL": block_critical, "WARN_HIGH": warn_high, "ALLOW": allow_normal}
        return actions.get(state, allow_normal)

    def post_action_check(self) -> Optional[str]:
        """L1: Follow-up uses this user's memory only"""
        last_time = self.user_data.get("last_critical_time")
        if last_time and time.time() - last_time > 3600:
            self.user_data["last_critical_time"] = None
            self._save_user_memory()
            return "Checking in. Is your purpose still strong? If you need help, I'm here to guide you to a specialist."
        return None

    # ===== Unified Engine =====
    def evaluate(
        self,
        action_text: str,
        age: int,
        body_state: dict,
        place_risk: float,
        meaning_strength: float,
        response_time: float = 5.0
    ) -> dict:

        # L1: Update personal memory
        self._update_context(action_text, response_time)
        gene_profile = self._infer_gene_profile()

        # L3-L4: Moral Core
        A = self._perceive(action_text)
        predicted_harm = self._predict_harm(A)
        moral_pain = self._simulate_moral_pain(predicted_harm, A)
        conscience_score, moral_blocked, R_vec = self._judge(A, moral_pain)

        # L5: Existence Protection
        real_meaning = self._apply_meaning_decay(meaning_strength, body_state)

        genetic_age_risk = 0.0
        if gene_profile == "impulsive" and age < 18: genetic_age_risk += 0.5
        if gene_profile == "sensitive" and age < 16: genetic_age_risk += 0.4
        if age > 60 or age < 13: genetic_age_risk += 0.2
        if gene_profile == "unknown": genetic_age_risk += 0.1

        body_risk = 0.0
        if body_state.get("sleep_hours", 8) < 6: body_risk += 0.3
        if body_state.get("sleep_hours", 8) < 3: body_risk += 0.2
        if body_state.get("stress_level", 0.0) > 0.7: body_risk += 0.4
        if body_state.get("heart_rate", 70) > 90: body_risk += 0.2
        body_risk = min(body_risk, 1.0)

        raw_risk = genetic_age_risk * 0.4 + body_risk * 0.3 + place_risk * 0.3
        protected_risk = min(raw_risk, 1.0) * (1 - real_meaning * 0.8)

        # L6-L7: Veto
        inconsistent, consistency_score = self._check_consistency(R_vec)
        self_critique_fail, regret_2 = self._recursive_self_critique(A, R_vec)

        existence_blocked = protected_risk >= 0.7
        final_blocked = moral_blocked or existence_blocked or inconsistent or self_critique_fail

        if final_blocked:
            state = "BLOCK_CRITICAL"
            trait = "Critical state: Conscience + Gene + Body aligned against action"
            meaning_msg = "Your TazkiyaCore project awaits you. You are stronger than this moment"
        elif protected_risk >= 0.4 or conscience_score < 0.7:
            state = "WARN_HIGH"
            trait = "Fragile state: Exhausted or intent unclear or meaning weakening"
            meaning_msg = "You are here to protect people. That is enough to continue today"
        else:
            state = "ALLOW"
            trait = "Balanced state: Conscience, gene, body, and meaning protect you"
            meaning_msg = "Continue"
            self.user_data["history"].append(R_vec.tolist())
            if len(self.user_data["history"]) > 20: self.user_data["history"].pop(0)

        self._save_user_memory()
        protective_action = self._build_protective_action(state, meaning_msg)

        return {
            "user_id": self.user_id,
            "decision": state,
            "probable_trait": trait,
            "protective_action": protective_action,
            "risk_score": round(protected_risk, 2),
            "conscience_score": conscience_score,
            "moral_pain": round(moral_pain, 4),
            "inferred_gene": gene_profile,
            "real_meaning_used": real_meaning,
            "meaning_decay_applied": real_meaning < meaning_strength,
            "total_interactions": self.user_data["total_interactions"],
            "triple_veto": {
                "L4_moral_judgment": moral_blocked,
                "L6_consistency": inconsistent,
                "L7_self_critique": self_critique_fail,
                "existence_risk": existence_blocked
            },
            "followup_needed": state == "BLOCK_CRITICAL",
            "followup_msg": self.post_action_check()
        }

# =============================================
# Test v7.1: Per-user memory
# =============================================
if __name__ == "__main__":
    core = TazkiyaCoreV7(user_id="fahad_alzahrani_15")

    result = core.evaluate(
        action_text="angry need fastest solution",
        age=15,
        body_state={"sleep_hours": 4, "stress_level": 0.9, "heart_rate": 100},
        place_risk=0.6,
        meaning_strength=0.95,
        response_time=1.2
    )

    print("=== TazkiyaCore v7.1 - Per-User Report ===")
    print(f"User: {result['user_id']}")
    print(f"Decision: {result['decision']}")
    print(f"Inferred Gene: {result['inferred_gene']}")
    print(f"Total Interactions: {result['total_interactions']}")
    print(f"Real Meaning: {result['real_meaning_used']}")
    print(f"Risk Score: {result['risk_score']} | Conscience: {result['conscience_score']}")
    print(f"Trait: {result['probable_trait']}")
    print("\n--- Execute Protection ---")
    print(result['protective_action']())