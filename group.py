# ================================
# Daneshjo: [Darya Behrooz]
# Shomareh Daneshjoii: [404130473]
# Onvan Proje: Shabihsaz Jam Jahani
# Tarikh Tahvil: [1405/05/01]
# ================================
#  group.py | Class Group | vabastegi: match.py


import random
from match import Match


class Group:
    """
    Class Group - Modiriat marhale groupi.
    """

    def __init__(self, name, teams):
        """
        Sakhtan yek group.
        
        Args:
            name (str): Name group (A, B, C, ...)
            teams (list): List Team objects dar in group
        """
        self.name = name
        self.teams = teams
        # Zakhire natije bazi baraye Head-to-Head
        self.match_results = {}

    def play_all_matches(self):
        """
        Ejraye tamame bazi haye group (har team 3 bazi).
        Har team faghat yek bar ba har team digar bazi mikonad.
        
        Returns:
            list: List Match objects
        """
        matches = []
        # Halghe baraye entekhab 2 team mokhtalef az group
        for i in range(len(self.teams)):
            for j in range(i + 1, len(self.teams)):
                match = Match(self.teams[i], self.teams[j], is_knockout=False)
                match.play()
                matches.append(match)
                
                # Zakhire natije baraye Head-to-Head
                key = (self.teams[i].name, self.teams[j].name)
                self.match_results[key] = (match.goals1, match.goals2)
                
        return matches

    def _head_to_head_sort(self, tied_teams):
        """
        Head-to-Head: Moratab kardan team haye barabar bar asas natije bazi ro be ro.
        
        Bar asas ghanon FIFA: vaghti team ha dar points, goal difference,
        va goals for barabar bashand, natije bazi ro be ro ra dar nazar migirad.
        
        Args:
            tied_teams (list): List team haye barabar
            
        Returns:
            list: List moratab shode team ha
        """
        # Agar faghat 2 team barabar bashand
        if len(tied_teams) == 2:
            team1, team2 = tied_teams[0], tied_teams[1]
            key1 = (team1.name, team2.name)
            key2 = (team2.name, team1.name)
            
            # Check kardane natije bazi ro be ro
            if key1 in self.match_results:
                g1, g2 = self.match_results[key1]
                if g1 > g2:
                    # team1 team2 ra zadeh
                    return [team1, team2]
                elif g2 > g1:
                    # team2 team1 ra zadeh
                    return [team2, team1]
                # Agar bazi mosavi shod, berim be ghorekeshi
            elif key2 in self.match_results:
                g1, g2 = self.match_results[key2]
                if g2 > g1:
                    # team1 team2 ra zadeh (az didgah team2)
                    return [team1, team2]
                elif g1 > g2:
                    # team2 team1 ra zadeh (az didgah team2)
                    return [team2, team1]
        
        # Agar bishtar az 2 team ya mosavi dar bazi ro be ro → ghorekeshi
        random.shuffle(tied_teams)
        return tied_teams

    def ranking_get(self):
        """
        Rتبه bandi team ha bar asas:
        1. Points (bishtar)
        2. Goal difference (bishtar)
        3. Goals for (bishtar)
        4. Head-to-Head (natije bazi ro be ro)
        5. Ghorekeshi (agar hanoz barabar bashand)
        
        Returns:
            list: List moratab shode Team objects (aval ta chaharom)
        """
        # Ghadam 1: Moratab kardan bar asas points, goal difference, goals for
        sorted_teams = sorted(
            self.teams,
            key=lambda t: (t.points, t.goal_difference(), t.for_goals),
            reverse=True
        )

        result = []
        i = 0
        
        # Ghadam 2: Peyda kardan team haye barabar
        while i < len(sorted_teams):
            j = i
            while (j < len(sorted_teams) and
                   sorted_teams[j].points == sorted_teams[i].points and
                   sorted_teams[j].goal_difference() == sorted_teams[i].goal_difference() and
                   sorted_teams[j].for_goals == sorted_teams[i].for_goals):
                j += 1

            # Gorohi az team haye barabar
            tied_group = sorted_teams[i:j]

            # Ghadam 3: Agar barabar bodand, Head-to-Head ra ejra kon
            if len(tied_group) > 1:
                tied_group = self._head_to_head_sort(tied_group)

            result.extend(tied_group)
            i = j

        return result

    def advance_teams(self):
        """
        Bargardan do team aval group baraye marhale hazfi.
        
        Returns:
            tuple: (team_aval, team_dovom)
        """
        ranked = self.ranking_get()
        return ranked[0], ranked[1]