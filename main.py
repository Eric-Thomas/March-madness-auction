import random
from typing import Dict
import traceback
from collections import defaultdict 


def main():
    teams = get_teams()
    users = get_users()
    while teams:
        try:
            ans = input("1. Next team\n2. See teams left\n3. See money left/teams selected\n4. Add or subract money\n>>")
            handle_input(ans, teams, users)
            with open("state.txt", "a") as fp:
                fp.write(f"{teams}\n")
                fp.write(f"{users}\n")
        except Exception:
            print(traceback.format_exc())

    print_users(users)

def handle_input(input, teams, users):
    if input is None:
        return

    if input != '1' and input != '2' and input != '3' and input != '4':
        print("Enter 1, 2, 3, or 4")
        return

    if input == '1':
        auction_off_team(teams, users)
    if input == '2':
        print_teams_left(teams)
    if input == '3':
        print_users(users)
    if input == "4":
        add_or_subtract_money(users)

def add_or_subtract_money(users):
    user = get_user_from_input(users)
    amount = get_amount_from_input()
    modify_amount(users, get_user_map()[user], amount)
    


def modify_amount(users, user, amount):
    users[user]["money"] += amount
    

def auction_off_team(teams, users):
    team = teams.pop()
    print("="*50)
    print(team)

    purchased = False
    while not purchased:
        user = get_user_from_input(users)
        amount = get_amount_from_input()
        if not amount > 0:
            print("Must buy for amount greater than 0")
            continue

        if not user_can_purchase(users, get_user_map()[user], amount):
            x = get_user_map()
            print(f"{get_user_map()[user]} cannot purchase for {amount}. They only have {users[get_user_map()[user]]['money']} left")
            print("="*50)
            print(team)
            user = None
            continue


        modify_amount(users, get_user_map()[user], amount * -1)
        add_team_to_user(users, get_user_map()[user], team)
        with open("rounds.txt", "a") as fp:
            fp.write(f"{get_user_map()[user]} buys {team} for {amount}\n")

        purchased = True

def add_team_to_user(users, user, team):
    users[user]["teams"].append(team)

def user_can_purchase(users, user, amount):
    if int(users[user]["money"]) < amount:        
        return False

    return True
    

def print_teams_left(teams):
    teams_by_seed = defaultdict(list)
    for team in teams:
        if "#1" in team[0:2] and not team[2].isdigit():
            teams_by_seed[1].append(team[2:])
        elif "#2" in team[0:2]:
            teams_by_seed[2].append(team[2:])
        elif "#3" in team[0:2]:
            teams_by_seed[3].append(team[2:])
        elif "#4" in team[0:2]:
            teams_by_seed[4].append(team[2:])
        elif "#5" in team[0:2]:
            teams_by_seed[5].append(team[2:])
        elif "#6" in team[0:2]:
            teams_by_seed[6].append(team[2:])
        elif "#7" in team[0:2]:
            teams_by_seed[7].append(team[2:])
        elif "#8" in team[0:2]:
            teams_by_seed[8].append(team[2:])
        elif "#9" in team[0:2]:
            teams_by_seed[9].append(team[2:])
        elif "#10" in team[0:3]:
            teams_by_seed[10].append(team[3:])
        elif "#11" in team[0:3]:
            teams_by_seed[11].append(team[3:])
        elif "#12" in team[0:3]:
            teams_by_seed[12].append(team[3:])
        elif "#13" in team[0:3]:
            teams_by_seed[13].append(team[3:])
        elif "#14" in team[0:3]:
            teams_by_seed[14].append(team[3:])
        elif team == "All #15 seeds":
            teams_by_seed[15].append(team)
        elif team == "All #16 seeds":
            teams_by_seed[16].append(team)

    for i in range(1, 17):
        print(f"{i} seeds - ", end='')
        for team in teams_by_seed[i][0:len(teams_by_seed[i]) - 1]:
            print(team, end=', ')

        if teams_by_seed[i]:
            print(teams_by_seed[i][-1])

        print('\n')
    random.shuffle(teams)

def print_users(users: Dict):
    for user, stats in users.items():
        print(user)
        print(f'${stats["money"]} left')
        print(f'teams - {stats["teams"]}')


def get_users():
    return {
        "Eric": {"money": 100, "teams": []},
        "Aaron": {"money": 100, "teams": []},
        "Cathcart": {"money": 100, "teams": []},
        "Julian": {"money": 100, "teams": []},
        "Harner": {"money": 100, "teams": []},
        "Daniy": {"money": 100, "teams": []},
        "Ryan": {"money": 100, "teams": []},
    }

def get_user_map():
    user_map = {}
    for i, user in enumerate(get_users()):
        user_map[str(i + 1)] = user

    return user_map

def get_user_from_input(users):
    user = None
    while not user:
        print("Select User")
        for i, user in enumerate(get_user_map().values()):
            print(f"{i+1}. {user}")
        user = input(">>")
        if user not in [str(i) for i in range (1, len(users) + 1)]:
            print(f"Enter number between 1 and {len(users)}")
            user = None

    return user

def get_amount_from_input():
    amount = None
    try:
        amount = int(input("Enter amount\n>>"))
    except ValueError:
        print("Must be an integer greater than 0")

    while not amount:
        try:
            amount = int(input("Enter amount greater than 0\n>>"))
        except ValueError:
            print("Must be an integer greater than 0")

    return amount
def get_teams():
    teams = """#1 Uconn
#8 Florida Atlantic
#9 Northwestern
#5 San Diego St.
#12 UAB
#4 Auburn
#13 Yale
#6 BYU
#11 Duquesne
#3 Illinois
#14 Morehead St.
#7 Washingston St.
#10 Drake
#2 Iowa St.
#1 North Carolina
#8 Mississippi St.
#9 Michigan St.
#5 Saint Mary's
#12 Grand Canyon
#4 Alabama
#13 Charleston
#6 Celmson
#11 New Mexico
#3 Baylor
#14 Colgate
#7 Dayton
#10 Nevada
#2 Arizona
#1 Houston
#8 Nebraska
#9 Texas A&M
#5 Wisconsin
#12 James Madison
#4 Duke
#13 Vermont
#6 Texas Tech
#11 NC State
#3 Kentucky
#14 Oakland
#7 Florida
#10 Boise St./Colorado
#2 Marquette
#1 Purdue
#8 Utah St.
#9 TCU
#5 Gonzaga
#12 McNeese
#4 Kansas
#13 Samford
#6 South Carolina
#11 Oregon
#3 Creighton
#14 Akron
#7 Texas
#10 Virginia/Colorado St.
#2 Tennessee
All #15 seeds
All #16 seeds
"""

    teams = teams.split("\n")
    random.shuffle(teams)
    return teams


if __name__ == "__main__":
    main()
