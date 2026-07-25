# ================================
# Daneshjo: [Darya Behrooz]
# Shomareh Daneshjoii: [404130473]
# Onvan Proje: Shabihsaz Jam Jahani
# Tarikh Tahvil: [1405/05/01]
# ================================
#  main.py | entry point barname
#  vabastegi: world_cup_simulator.py


from world_cup_simulator import WorldCupSimulator

def main():
    """Tabe asli barname - menu va handle kardan vorudi."""
    # Sakhtan object az WorldCupSimulator
    simulator = WorldCupSimulator()

    # Halghe menu
    while True:
        print("\n===== World Cup Simulator Menu =====")
        print("1) Load teams from CSV")
        print("2) Draw groups (automatic seeding)")
        print("3) Run the group stage and display each group table")
        print("4) Run the complete World Cup and display the champion")
        print("5) Run simulations and report championship percentages")
        print("6) Display the knockout bracket from the last simulation")
        print("7) Exit")

        choice = input("Enter your choice: ").strip()

        # ---------- Gzine 1: Load CSV ----------
        if choice == "1":
            simulator.show_files_in_folder(".")
            filename = input("Enter CSV file name: ").strip()
            simulator.load_teams_from_csv(filename)

        # ---------- Gzine 2: Ghorekeshi ----------
        elif choice == "2":
            # Check kardane load shodane team ha
            if len(simulator.teams) != 32:
                print("Error: Please load teams from CSV first (Option 1).")
            else:
                simulator.seed_and_draw_groups(display=True)  

        # ---------- Gzine 3: Marhale Groupi ----------
        elif choice == "3":
            if len(simulator.teams) != 32:
                print("Error: Please load teams from CSV first (Option 1).")
            else:
                simulator.run_group_stage(display=True)  

        # ---------- Gzine 4: Ejraye Kamel ----------
        elif choice == "4":
            if len(simulator.teams) != 32:
                print("Error: Please load teams from CSV first (Option 1).")
            else:
                simulator.run_full_simulation(display=True)  

        # ---------- Gzine 5: 1000 bar Shabihsazi ----------
        elif choice == "5":
            if len(simulator.teams) != 32:
                print("Error: Please load teams from CSV first (Option 1).")
            else:
                value = input("Enter number of simulations (default 1000): ").strip()
                if value == "":
                    simulator.most_likely_champion(1000)  
                else:
                    try:
                        simulator.most_likely_champion(int(value))  
                    except ValueError:
                        print("Error: Please enter a valid integer.")

        # ---------- Gzine 6: Namayesh Bracket ----------
        elif choice == "6":
            if len(simulator.teams) != 32:
                print("Error: Please load teams from CSV first (Option 1).")
            else:
                simulator.display_bracket()  

        # ---------- Gzine 7: Exit ----------
        elif choice == "7":
            print("Goodbye.")
            break

        # ---------- Vorudi gheyr mojaz ----------
        else:
            print("Error: Invalid menu option.")


if __name__ == "__main__":
    main()
input()