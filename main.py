import pandas as pd

df = pd.read_csv('video_games_raw.csv')

print('\nVIDEO GAME CATALOG MANAGER\n')

while True:
    try:
        row_input = int(input("Enter a row number to inspect: "))

        if row_input in range(1, len(df) + 1):
            break

        print(f"\nEnter a number from 1 to {len(df)}.")

    except ValueError:
        print("Please enter a whole number.")

row_index = row_input - 1
choice = df.iloc[row_index]

print(f'\nSelected Game:')
print(f'Title: {choice["Title"]}')
print(f'Platform: {choice["Platform"]}')
print(f'Genre: {choice["Genre"]}')
print(f'Rating: {choice["Rating"]}')
print(f'Current Status: {choice["Status"]}\n')

valid_statuses = ["backlog", "playing", "completed", "dropped"]

while True:
    new_status = input("Enter a new status: ").lower()

    if new_status in valid_statuses:
        break

    print("\nInvalid Status. Status Options: Backlog, Playing, Completed, Dropped")

df.at[row_index, "Status"] = new_status.capitalize()

df["Recommended"] = "No"


df.loc[(df['Rating'] >= 8) & (df['Price'] <= 40), "Recommended"] = "Yes"

recommended_games = df.query('Recommended == "Yes"')

print("\nRecommended Games:")
print(recommended_games[["Title", "Platform", "Price", "Rating"]])

df.to_csv("video_games_cleaned.csv", index=False)

print('\nThe catalog has been updated.')
print('\nSaved as video_games_cleaned.csv.\n')
