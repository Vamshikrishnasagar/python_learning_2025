import os
import random
import logging
import datetime

# ---------- Setup ----------
today_date = datetime.datetime.today().strftime('%Y-%m-%d')
base_path = r"D:\PythonProjects\Python_Learning_Youtube_2025\LogicalPrograms\Dies_Game"
os.makedirs(base_path, exist_ok=True)

sponsor_name = input("Please enter the Sponsor Name: ").strip().replace(" ", "_")
file_name = os.path.join(base_path, f"{sponsor_name}_{today_date}.txt")

logging.basicConfig(
    level=logging.INFO,
    filemode='a',
    filename=file_name,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

logging.info("Dice game started")

# ---------- Game Init ----------
player_1 = 0
player_2 = 0
roll = 1

player_1_name = input("Please enter Player 1 Name: ")
player_2_name = input("Please enter Player 2 Name: ")

# ---------- Game Loop ----------
while True:

    input(f"{player_1_name}: press Enter to roll the die ")
    p1_die = random.randint(1, 6)
    player_1 += p1_die

    print(f"{player_1_name} | Roll {roll} | Die: {p1_die} | Total: {player_1}")
    logging.info(f"{player_1_name} rolled {p1_die}, total = {player_1}")

    if player_1 >= 20:
        break

    print("**" * 20)

    input(f"{player_2_name}: press Enter to roll the die ")
    p2_die = random.randint(1, 6)
    player_2 += p2_die

    print(f"{player_2_name} | Roll {roll} | Die: {p2_die} | Total: {player_2}")
    logging.info(f"{player_2_name} rolled {p2_die}, total = {player_2}")

    if player_2 >= 20:
        break

    print("--" * 20)
    print(f"Scores → {player_1_name}: {player_1}, {player_2_name}: {player_2}")
    print("--" * 20)

    roll += 1

# ---------- Result ----------
print("\n===== GAME OVER =====")

if player_1 > player_2:
    print(f"{player_1_name} is the winner!")
    logging.info(f"Winner: {player_1_name}")
elif player_2 > player_1:
    print(f"{player_2_name} is the winner!")
    logging.info(f"Winner: {player_2_name}")
else:
    print("Match Draw!")
    logging.info(f"Match draw between {player_1_name} and {player_2_name}")

logging.info("Dice game ended")
