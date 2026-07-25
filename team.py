# ================================
# Daneshjo: [Darya Behrooz]
# Shomareh Daneshjoii: [404130473]
# Onvan Proje: Shabihsaz Jam Jahani
# Tarikh Tahvil: [1405/05/01]
# ================================
#  team.py | Class Team | vabastegi: utils.py


from utils import poisson_random
import random


class Team:
    """
    Class Team - Negahdari etelaat va ammar har tim.
    """

    def __init__(self, name, attack, defense, rank):
        """
        Sakhtan object Team az rooye data file CSV.

        Args:
            name (str): Name tim.
            attack (float): Ghodrat hamle (1-100).
            defense (float): Ghodrat defa (1-100).
            rank (int): Rank FIFA (1 behtarin).
        """
        # Pak kardan fasele haye ezafe az name
        self.name = str(name).strip()
        # Tabdil be float baraye mohasebat
        self.attack = float(attack)
        self.defense = float(defense)
        self.rank = int(rank)
        # Name group (khali ta ghorekeshi)
        self.group = ""
        # Reset ammar baraye shoroe tournament
        self.reset_stats()

    def reset_stats(self):
        """Reset ammar tim baraye shoroe yek tournament jadid."""
        # Reset gol zade, gol khorde va emtiyaz
        self.for_goals = 0
        self.against_goals = 0
        self.points = 0
        self.group = ""  

    def goal_difference(self):
        """Bargardan tafazol gol (for_goals - against_goals)."""
        return self.for_goals - self.against_goals

    def simulate_match(self, opponent, is_knockout=False):
        """
        Shabihsazi yek bazi ba tim harif.

        Args:
            opponent (Team): Tim harif.
            is_knockout (bool): Hazfi boodan bazi.

        Returns:
            dict: Shamel goals1, goals2, winner, note, penalties.
        """
        # ---------- 1. Mohasebe lambda (miangin gol) baraye 90 daghighe ----------
        # Lambda tim khodi: attack khodi + defa harif
        lambda_self = (
            (self.attack / 100.0) * 1.5
            + (1.0 - opponent.defense / 100.0) * 0.8
        )
        # Lambda harif: attack harif + defa khodi
        lambda_opp = (
            (opponent.attack / 100.0) * 1.5
            + (1.0 - self.defense / 100.0) * 0.8
        )

        # ---------- 2. Shabihsazi 90 daghighe ba Poisson ----------
        goals_self = poisson_random(lambda_self)
        goals_opp = poisson_random(lambda_opp)

        # Motaghayer haye natije
        winner = None
        note = ""
        penalties = None

        # ---------- 3. Teyin barande pas az 90 daghighe ----------
        if goals_self > goals_opp:
            winner = self
        elif goals_opp > goals_self:
            winner = opponent

        # ---------- 4. Vaghte ezafe va penalti (faghat marhale hazfi) ----------
        # Baraye marhale hazfi, agar baz mosavi shod, vaghte ezafe va penalti
        if is_knockout and goals_self == goals_opp:
            # Shabihsazi 30 daghighe vaghte ezafe ba zarb 0.33
            extra_self = poisson_random(0.33 * lambda_self)
            extra_opp = poisson_random(0.33 * lambda_opp)

            # Ezafe kardan gol haye vaghte ezafe
            goals_self += extra_self
            goals_opp += extra_opp

            # Teyin barande pas az vaghte ezafe
            if goals_self > goals_opp:
                winner = self
            elif goals_opp > goals_self:
                winner = opponent
            else:
                # ---------- 5. Penalti (agar baz ham mosavi) ----------
                # Penalty success probability: base 75% + (attack - defense)/250
                # Clamped between 60% and 90%
                p_self = 0.75 + (self.attack - opponent.defense) / 250
                p_opp = 0.75 + (opponent.attack - self.defense) / 250

                # Mahdood kardan ehtemal beine 0.6 va 0.9
                p_self = max(0.6, min(0.9, p_self))
                p_opp = max(0.6, min(0.9, p_opp))

                # 5 penalti aval baraye har tim
                pen_self = sum(1 for _ in range(5) if random.random() < p_self)
                pen_opp = sum(1 for _ in range(5) if random.random() < p_opp)

                # Penalti nagahani (Sudden Death) dar sorate tasavi
                # Dar har round, har tim yek penalti mizanad ta barande mashakhas shavad
                while pen_self == pen_opp:
                    pen_self += 1 if random.random() < p_self else 0
                    pen_opp += 1 if random.random() < p_opp else 0

                # Sabt natije penalti
                penalties = (pen_self, pen_opp)
                note = f" (P: {pen_self}-{pen_opp})"
                winner = self if pen_self > pen_opp else opponent

        # ---------- 6. Bargashtane natije be surat dictionary ----------
        return {
            "goals1": goals_self,
            "goals2": goals_opp,
            "winner": winner,
            "note": note,
            "penalties": penalties,
        }