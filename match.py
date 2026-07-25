# ================================
# Daneshjo: [Darya Behrooz]
# Shomareh Daneshjoii: [404130473]
# Onvan Proje: Shabihsaz Jam Jahani
# Tarikh Tahvil: [1405/05/01]
# ================================
#  match.py | Class Match | vabastegi: team.py


from team import Team

class Match:
    """
    Class Match - Modiriat yek bazi beyn do tim.
    """

    def __init__(self, team1, team2, is_knockout=False):
        # Sabt etelaat bazi
        self.team1 = team1
        self.team2 = team2
        self.goals1 = 0
        self.goals2 = 0
        self.is_knockout = is_knockout
        self.winner = None
        self.note = ""

    def play(self):
        """
        Ejraye bazi va sabt natije.

        Returns:
            Team or None: Barande bazi.
        """
        # Shabihsazi bazi ba simulate_match az team1
        result = self.team1.simulate_match(self.team2, self.is_knockout)

        # Sabt natije
        self.goals1 = result["goals1"]
        self.goals2 = result["goals2"]
        self.winner = result["winner"]
        self.note = result["note"]

        # ---------- Agar marhale groupi bod, ammar ra be rooz kon ----------
        # Dar marhale groupi, gol ha va emtiyaz sabt mishavand
        if not self.is_knockout:
          
            self.team1.for_goals += self.goals1
            self.team1.against_goals += self.goals2
            self.team2.for_goals += self.goals2
            self.team2.against_goals += self.goals1

            # Be rooz kardane emtiyaz bar asas natije
            if self.goals1 > self.goals2:
                self.team1.points += 3   # Barande 3 emtiyaz
            elif self.goals2 > self.goals1:
                self.team2.points += 3
            else:
                self.team1.points += 1   # Mosavi 1 emtiyaz
                self.team2.points += 1

        return self.winner

    def result_text(self):
        """Sakht matn natije baraye namayesh."""
        # Baraye marhale hazfi: namayeshe barande ba penalti
        if self.is_knockout:
            return (
                f"{self.team1.name} {self.goals1}-{self.goals2} {self.team2.name}"
                f"{self.note} -> Winner: {self.winner.name}"
            )

        # Baraye marhale groupi: tasavi ya barande
        if self.goals1 == self.goals2:
            return (
                f"{self.team1.name} {self.goals1}-{self.goals2} "
                f"{self.team2.name} -> Draw"
            )

        return (
            f"{self.team1.name} {self.goals1}-{self.goals2} {self.team2.name}"
            f" -> Winner: {self.winner.name}"
        )