# ================================
# Daneshjo: [Darya Behrooz]
# Shomareh Daneshjoii: [404130473]
# Onvan Proje: Shabihsaz Jam Jahani
# Tarikh Tahvil: [1405/05/01]
# =================================
#  knockout_stage.py | Class KnockoutStage | vabastegi: match.py

from match import Match


class KnockoutStage:
    """
    Class KnockoutStage - Modiriat yek marhale az hazfi.
    """

    def __init__(self, round_name, matches):
        self.round_name = round_name
        self.matches = matches

    def play_round(self):
        """Ejraye tamame bazi haye in marhale."""
        winners = []
        # Ejraye har match va sabt barande
        for match in self.matches:
            winners.append(match.play())
        return winners

    def winners_get(self):
        """Bargardan list team haye barande."""
        winners = []
        # Jam avari barande haye match ha
        for match in self.matches:
            if match.winner is not None:
                winners.append(match.winner)
        return winners

    def results_display(self):
        """Namayesh natayej marhale."""
        print(f"===== {self.round_name} =====")
        for match in self.matches:
            print(match.result_text())
