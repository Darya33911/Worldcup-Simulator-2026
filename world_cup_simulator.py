# ================================
# Daneshjo: [Darya Behrooz]
# Shomareh Daneshjoii: [404130473]
# Onvan Proje: Shabihsaz Jam Jahani
# Tarikh Tahvil: [1405/05/01]
# ================================
#  world_cup_simulator.py | Class WorldCupSimulator
#  vabastegi: team.py, group.py, match.py, knockout_stage.py
#  in class asli va hame chiz ra modiriat mikonad

import csv
import os
import random
from team import Team
from group import Group
from match import Match
from knockout_stage import KnockoutStage


class WorldCupSimulator:
    """
    Class asli - Modiriat kamel shabihsazi Jam Jahani.
    """

    def __init__(self):
        # List 32 team
        self.teams = []
        # List 8 group
        self.groups = []
        # Marahale hazfi
        self.round_of_16 = None
        self.quarterfinals = None
        self.semifinals = None
        self.final = None
        self.champion = None
        # Zakhire khat haye bracket baraye namayesh
        self.bracket_lines = []
        # Flag haye vaziyat
        self.groups_drawn = False
        self.group_stage_completed = False
        self.knockout_ready = False

    def reset_tournament_state(self):
        """
        Reset vaziyat tournament baraye shoroe jadid.
        Hame ammar va structure ra pak mikonad.
        """
        # Reset ammar hame team ha
        for team in self.teams:
            team.reset_stats()

        # Reset structure tournament
        self.groups = []
        self.round_of_16 = None
        self.quarterfinals = None
        self.semifinals = None
        self.final = None
        self.champion = None
        self.bracket_lines = []
        self.groups_drawn = False
        self.group_stage_completed = False
        self.knockout_ready = False

    def load_teams_from_csv(self, filename):
        """
        Khandan team ha az file CSV.

        Args:
            filename (str): Name file.

        Returns:
            bool: True agar load success bud.
        """
        # Check kardane vojude file
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            return False

        try:
            # Baz kardane file ba encoding utf-8-sig baraye support Persian
            with open(filename, "r", encoding="utf-8-sig", newline="") as file:
                reader = csv.DictReader(file)

                # Check kardane header
                if reader.fieldnames is None:
                    print("Error: CSV file has no header row.")
                    return False

                # Check kardane sotun haye morede niyaz
                header_map = {h.strip().lower(): h for h in reader.fieldnames}
                required_cols = ["name", "attack", "defense", "rank"]

                for col in required_cols:
                    if col not in header_map:
                        print(
                            "Error: CSV must contain columns: "
                            "name, attack, defense, rank"
                        )
                        return False

                # Khandane team ha az file
                loaded_teams = []
                for row_number, row in enumerate(reader, start=2):
                    try:
                        name = row[header_map["name"]].strip()
                        attack = row[header_map["attack"]]
                        defense = row[header_map["defense"]]
                        rank = row[header_map["rank"]]

                        # Check kardane name khali
                        if not name:
                            print(
                                f"Warning: Row {row_number} skipped because "
                                f"team name is empty."
                            )
                            continue

                        # Sakhtan object Team
                        loaded_teams.append(Team(name, attack, defense, rank))
                    except (ValueError, KeyError):
                        print(
                            f"Warning: Row {row_number} skipped due to invalid data."
                        )

                # Check kardane tedad team ha (bayad 32 bashad)
                if len(loaded_teams) != 32:
                    print(f"Error: Expected 32 teams, but loaded {len(loaded_teams)}.")
                    return False

                # Check kardane unique bodane rank ha
                ranks = [team.rank for team in loaded_teams]
                if len(set(ranks)) != 32:
                    print("Error: Team ranks must be unique.")
                    return False

                # Zakhire team ha va reset tournament
                self.teams = loaded_teams
                self.reset_tournament_state()
                print(f"Success: {len(self.teams)} teams loaded from '{filename}'.")
                return True

        except Exception as error:
            print(f"Error while reading CSV: {error}")
            return False

    def seed_and_draw_groups(self, display=True):
        """
        Ghorekeshi va seed bandi group ha.
        Team ha bar asas rank be 4 seed taghsim va be 8 group tazei mishavand.

        Args:
            display (bool): Namayesh group ha.

        Returns:
            bool: True agar success bud.
        """
        # Check kardane tedad team ha
        if len(self.teams) != 32:
            print("Error: You must load exactly 32 teams first.")
            return False

        # Reset tournament baraye shoroe jadid
        self.reset_tournament_state()

        # Seed bandi: moratab bar asas rank va joda kardan be 4 seed
        sorted_teams = sorted(self.teams, key=lambda team: team.rank)
        # Taghsim be 4 seed (har seed 8 team)
        pots = [sorted_teams[i:i + 8] for i in range(0, 32, 8)]
        # Sakhtane 8 group (A ta H)
        self.groups = [Group(chr(65 + i), []) for i in range(8)]

        # Az har seed yek team be har group (ghorekeshi)
        for pot in pots:
            random.shuffle(pot)  # Random kardan tartib dar seed
            for i, team in enumerate(pot):
                self.groups[i].teams.append(team)
                team.group = self.groups[i].name

        self.groups_drawn = True

        # Namayesh natije dar sorate darkhast
        if display:
            print("Groups were drawn successfully.")
            for group in self.groups:
                print(f"\n===== Group {group.name} =====")
                for team in group.teams:
                    print(f"{team.name} (Rank {team.rank})")

        return True

    def run_group_stage(self, display=True):
        """
        Ejraye marhale groupi.
        Agar ghorekeshi anjam nashode, khodesh anjam midahad.

        Args:
            display (bool): Namayesh jadval group ha.

        Returns:
            bool: True agar success bud.
        """
        # Agar ghorekeshi anjam nashode, khodesh anjam bede
        if not self.groups_drawn or len(self.groups) != 8:
            if display:
                print("Groups not drawn yet. Drawing groups automatically...")
            self.seed_and_draw_groups(display=display)

        # Reset ammar hame team ha
        for group in self.groups:
            for team in group.teams:
                team.reset_stats()

        # Ejraye hame bazi haye group
        for group in self.groups:
            group.play_all_matches()

        self.group_stage_completed = True
        self.knockout_ready = False

        # Namayesh natayej dar sorate darkhast
        if display:
            for group in self.groups:
                print(f"\n===== Group {group.name} =====")
                ranked = group.ranking_get()
                for index, team in enumerate(ranked, start=1):
                    gd = team.goal_difference()
                    gd_text = f"+{gd}" if gd >= 0 else str(gd)
                    print(
                        f"{index}. {team.name}: {team.points} pts, "
                        f"GD {gd_text}, GF {team.for_goals}"
                    )

        return True

    def setup_knockout_bracket(self):
        """
        Sakhte bracket marhale hazfi bar asas ghanon FIFA:
        A1 vs B2, C1 vs D2, E1 vs F2, G1 vs H2,
        B1 vs A2, D1 vs C2, F1 vs E2, H1 vs G2

        Returns:
            bool: True agar success bud.
        """
        # Check kardane anjam shodane marhale groupi
        if not self.group_stage_completed:
            print("Error: Please run the group stage first.")
            return False

        # Gereftane team haye aval va dovom har group
        group_winners = []
        group_runners_up = []

        for group in self.groups:
            first, second = group.advance_teams()
            group_winners.append(first)
            group_runners_up.append(second)

        # Sakhte jadval bazi haye marhale hazfi bar asas ghanon FIFA
        pairings = [
            (group_winners[0], group_runners_up[1]),  # A1 vs B2
            (group_winners[2], group_runners_up[3]),  # C1 vs D2
            (group_winners[4], group_runners_up[5]),  # E1 vs F2
            (group_winners[6], group_runners_up[7]),  # G1 vs H2
            (group_winners[1], group_runners_up[0]),  # B1 vs A2
            (group_winners[3], group_runners_up[2]),  # D1 vs C2
            (group_winners[5], group_runners_up[4]),  # F1 vs E2
            (group_winners[7], group_runners_up[6]),  # H1 vs G2
        ]

        # Sakhtan marhale yek hesht
        self.round_of_16 = KnockoutStage(
            "Round of 16",
            [Match(team1, team2, is_knockout=True) for team1, team2 in pairings],
        )

        self.knockout_ready = True
        return True

    def run_knockout_stage(self, display=True):
        """
        Ejraye marahale hazfi: Round16 -> Quarter -> Semi -> Final.

        Args:
            display (bool): Namayesh natije final.

        Returns:
            bool: True agar success bud.
        """
        # Check kardane amade bodan marhale hazfi
        if not self.knockout_ready or self.round_of_16 is None:
            print("Error: Knockout stage is not ready.")
            return False

        # Reset zakhire bracket lines
        self.bracket_lines = []

        # ---------- Round of 16 (Marhale yek hesht) ----------
        self.round_of_16.play_round()
        round16_winners = self.round_of_16.winners_get()
        self.bracket_lines.append("===== Round of 16 =====")
        self.bracket_lines.extend(
            match.result_text() for match in self.round_of_16.matches
        )

        # ---------- Quarterfinals (Marhale yek chaharom) ----------
        # Joft kardan barande haye round16
        quarter_pairs = [
            (round16_winners[i], round16_winners[i + 1]) for i in range(0, 8, 2)
        ]
        self.quarterfinals = KnockoutStage(
            "Quarterfinals",
            [Match(team1, team2, is_knockout=True) for team1, team2 in quarter_pairs],
        )
        self.quarterfinals.play_round()
        quarter_winners = self.quarterfinals.winners_get()
        self.bracket_lines.append("")
        self.bracket_lines.append("===== Quarterfinals =====")
        self.bracket_lines.extend(
            match.result_text() for match in self.quarterfinals.matches
        )

        # ---------- Semifinals (Marhale nimhe nahayi) ----------
        semifinal_pairs = [
            (quarter_winners[i], quarter_winners[i + 1]) for i in range(0, 4, 2)
        ]
        self.semifinals = KnockoutStage(
            "Semifinals",
            [Match(team1, team2, is_knockout=True) for team1, team2 in semifinal_pairs],
        )
        self.semifinals.play_round()
        semifinal_winners = self.semifinals.winners_get()
        self.bracket_lines.append("")
        self.bracket_lines.append("===== Semifinals =====")
        self.bracket_lines.extend(
            match.result_text() for match in self.semifinals.matches
        )

        # ---------- Final (Marhale nahayi) ----------
        self.final = KnockoutStage(
            "Final",
            [Match(semifinal_winners[0], semifinal_winners[1], is_knockout=True)],
        )
        self.final.play_round()
        final_winners = self.final.winners_get()
        self.champion = final_winners[0]
        self.bracket_lines.append("")
        self.bracket_lines.append("===== Final =====")
        self.bracket_lines.extend(match.result_text() for match in self.final.matches)

        # Namayesh natije dar sorate darkhast
        if display:
            print("\n===== Final =====")
            final_match = self.final.matches[0]
            print(
                f"{final_match.team1.name} {final_match.goals1}-"
                f"{final_match.goals2} {final_match.team2.name}{final_match.note}"
            )
            print(f"Champion: {self.champion.name}")

        return True

    def run_full_simulation(self, display=True):
        """
        Ejraye kamel tournament (groupi + hazfi) dar yek call.
        Agar ghablan ghorekeshi va marhale groupi anjam shode bashe,
        az natijeye anha estefade mikonad.

        Args:
            display (bool): Namayesh natije.

        Returns:
            bool: True agar success bud.
        """
        # Check kardane team ha
        if len(self.teams) != 32:
            print("Error: Please load teams from CSV first.")
            return False

        # Agar ghorekeshi anjam nashode, anjam bede
        if not self.groups_drawn:
            if display:
                print("Groups not drawn yet. Drawing groups...")
            self.seed_and_draw_groups(display=display)
        else:
            if display:
                print("Using existing group draw.")

        # Agar marhale groupi anjam nashode, anjam bede
        if not self.group_stage_completed:
            if display:
                print("Group stage not completed yet. Running group stage...")
            self.run_group_stage(display=display)
        else:
            if display:
                print("Using existing group stage results.")

        # Ejraye marhale hazfi (age nabashe, jadid besaz)
        if not self.knockout_ready:
            self.setup_knockout_bracket()
        
        self.run_knockout_stage(display=display)
        return True

    def most_likely_champion(self, simulations_num=1000):
        """
        Ejraye simulations_num bar tournament va mohasebe darsad ghahremani.

        Args:
            simulations_num (int): Tedad shabihsazi.

        Returns:
            bool: True agar success bud.
        """
        # Check kardane team ha
        if len(self.teams) != 32:
            print("Error: Please load teams from CSV first.")
            return False

        # Check kardane tedad shabihsazi
        if simulations_num <= 0:
            print("Error: Number of simulations must be positive.")
            return False

        # Initial kardane dictionary baraye shomaresh ghahremani ha
        wins = {team.name: 0 for team in self.teams}

        # ---------- simulations_num bar shabihsazi ----------
        print(f"Starting {simulations_num} simulations...")

        for _ in range(simulations_num):
            self.seed_and_draw_groups(display=False)
            self.run_group_stage(display=False)
            self.setup_knockout_bracket()
            self.run_knockout_stage(display=False)
            wins[self.champion.name] += 1

        # Namayesh natayej
        print(f"\nSimulation completed {simulations_num} times.")
        print("Championship percentages:")
        print("-" * 40)
        
        zero_count = 0
        # Moratab kardan az bishtarin darsad
        for name, count in sorted(wins.items(), key=lambda item: item[1], reverse=True):
            percentage = (count / simulations_num) * 100.0
            if percentage > 0:
                print(f"{name:<20}: {percentage:>5.1f}%")
            else:
                zero_count += 1
        
        # Agar team haye ba darsad 0 vojoud dasht, tedad anha ra namayesh bede
        if zero_count > 0:
            print(f"\n{zero_count} teams had 0% championship probability.")
        print("-" * 40)

        return True

    def display_bracket(self):
        """
        Namayesh bracket akharin shabihsazi.
        Agar bracket vojoud nadarad, khodesh marahale groupi va hazfi ra anjam midahad.

        Returns:
            bool: True agar success bud.
        """
        # Agar bracket vojoud darad, an ra namayesh bede
        if self.bracket_lines:
            print("\n===== Knockout Bracket =====")
            for line in self.bracket_lines:
                print(line)
            return True
        
        # Agar bracket vojoud nadarad, khodesh marahale morede niyaz ra anjam bede
        print("No knockout bracket available. Running necessary stages...")
        
        # Agar team ha load nashode
        if len(self.teams) != 32:
            print("Error: Please load teams from CSV first (Option 1).")
            return False
        
        # Agar ghorekeshi anjam nashode, anjam bede
        if not self.groups_drawn:
            print("Groups not drawn yet. Drawing groups...")
            self.seed_and_draw_groups(display=True)
        
        # Agar marhale groupi anjam nashode, anjam bede
        if not self.group_stage_completed:
            print("Group stage not completed yet. Running group stage...")
            self.run_group_stage(display=True)
        
        # Agar marhale hazfi anjam nashode, anjam bede
        if not self.knockout_ready:
            print("Knockout stage not completed yet. Running knockout stage...")
            self.setup_knockout_bracket()
            self.run_knockout_stage(display=False)
        
        # Namayesh bracket
        print("\n===== Knockout Bracket =====")
        for line in self.bracket_lines:
            print(line)
        
        # Namayesh qahreman
        if self.champion:
            print(f"\nChampion: {self.champion.name}")
        
        return True

    def show_files_in_folder(self, folder_path="."):
        """
        Namayesh file haye folder baraye rahmati user dar entekhab CSV.

        Args:
            folder_path (str): Masir folder baraye namayesh.
        """
        print("\n===== Files in Folder =====")
        try:
            files = sorted(os.listdir(folder_path))
            if not files:
                print("Folder is empty.")
                return

            for file_name in files:
                # Faghat file haye CSV va py namayesh dade mishavand
                if file_name.endswith(('.csv', '.CSV', '.py')):
                    print(f"- {file_name}")
                else:
                    print(f"  {file_name}")
        except Exception as error:
            print(f"Error while listing files: {error}")