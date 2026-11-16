import pandas as pd

df = pd.read_csv('video_games_raw.csv')

print('\nVIDEO GAME CATALOG MANAGER\n')

# While loop that loops the row_input. The user can keep trying to input an integer that is in the range of 1 and len(df) + 1. If the value inputted is a number outside the range or another value, you are able to try again.
while True:
    try:
        row_input = int(input("Enter a row number to inspect: "))

        if row_input in range(1, len(df) + 1):
            break

        print(f"\nEnter a number from 1 to {len(df)}.")

    except ValueError:
        print("Please enter a whole number.")

# Locate Row that is being selected and display data.
row_index = row_input - 1
choice = df.iloc[row_index]

print(f'\nSelected Game:')
print(f'Title: {choice["Title"]}')
print(f'Platform: {choice["Platform"]}')
print(f'Genre: {choice["Genre"]}')
print(f'Rating: {choice["Rating"]}')
print(f'Current Status: {choice["Status"]}\n')

# List of valid statuses that can be entered as new_status
valid_statuses = ["backlog", "playing", "completed", "dropped"]

while True:
    new_status = input("Enter a new status: ").lower()

    if new_status in valid_statuses:
        break

    print("\nInvalid Status. Status Options: Backlog, Playing, Completed, Dropped")

df.at[row_index, "Status"] = new_status.capitalize()

# Set all columns to have new "Recommended" row. This row is initially given a value of "No" until using .loc we can set it to "Yes" if it meets proper conditions. Print those games that have "Yes".
df["Recommended"] = "No"

df.loc[(df['Rating'] >= 8) & (df['Price'] <= 40), "Recommended"] = "Yes"

recommended_games = df.query('Recommended == "Yes"')

print("\nRecommended Games:")
print(recommended_games[["Title", "Platform", "Price", "Rating"]])

# Created new csv called "video_games_cleaned"
df.to_csv("video_games_cleaned.csv", index=False)

print('\nThe catalog has been updated.')
print('\nSaved as video_games_cleaned.csv.\n')
