import csv

data = [
    {"Date": "2024-01-01", "Distance": "41m", "Reading": "10°C"},
    {"Date": "2024-01-01", "Distance": "151ft", "Reading": "70°F"},
    {"Date": "2024-01-01", "Distance": "15m", "Reading": "15°C"},
    {"Date": "2024-01-01", "Distance": "100ft", "Reading": "62°F"},
    {"Date": "2024-01-01", "Distance": "31m", "Reading": "15°C"},
    {"Date": "2024-01-01", "Distance": "21m", "Reading": "17°C"},
    {"Date": "2024-01-01", "Distance": "10m", "Reading": "15°C"},
    {"Date": "2024-01-01", "Distance": "10ft", "Reading": "61°F"}
]

# Write data to CSV file
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Date', 'Distance', 'Reading']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)
