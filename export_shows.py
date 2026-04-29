import requests
import os

API_URL = "https://www.rundowncreator.com/davidrives/API.php"
API_KEY = "danielallen"
API_TOKEN = "FkdFM4Vr45vQaPdawH8LqeMRQCuIF7"

def run_export():
    print("Connecting to Rundown Creator...")
    params = {'APIKey': API_KEY, 'APIToken': API_TOKEN, 'Action': 'getRundowns'}

    try:
        response = requests.get(API_URL, params=params)
        rundowns = response.json()

        # Filter for March (03) and April (04)
        target_months = ["-03-", "-04-"]
        count = 0

        for item in rundowns:
            if any(month in item['Date'] for month in target_months):
                print(f"Downloading: {item['Date']} - {item['Title']}")

                # Fetch individual rundown data
                show_params = {
                    'APIKey': API_KEY,
                    'APIToken': API_TOKEN,
                    'Action': 'getRundown',
                    'RundownID': item['RundownID']
                }
                show_data = requests.get(API_URL, params=show_params)

                # Save as CSV
                filename = f"{item['Date']}_{item['Title'].replace(' ', '_')}.csv"
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(show_data.text)
                count += 1

        print(f"\nDone! Successfully exported {count} shows.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_export()
