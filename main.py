import csv
from Converter.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from Converter.distance import feet_to_meters, meters_to_feet

def convert_temperature_reading(reading):
    if 'C' in reading:
        celsius = float(reading.strip('°C'))
        return f"{celsius_to_fahrenheit(celsius):.2f}°F"
    elif 'F' in reading:
        fahrenheit = float(reading.strip('°F'))
        return f"{fahrenheit_to_celsius(fahrenheit):.2f}°C"
    else:
        return reading

def convert_distance_reading(reading):
    if 'm' in reading:
        meters = float(reading.strip('m'))
        return f"{meters_to_feet(meters):.2f}ft"
    elif 'ft' in reading:
        feet = float(reading.strip('ft'))
        return f"{feet_to_meters(feet):.2f}m"
    else:
        return reading

def process_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['Date', 'Converted Distance', 'Reading']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
              row['Reading'] = convert_temperature_reading(row['Reading'])
              if 'Distance' in row:
                  converted_distance = convert_distance_reading(row['Distance'])
                  row['Converted Distance'] = converted_distance
                  del row['Distance']  
              writer.writerow(row)
          
if __name__ == "__main__":
    input_file = "data.csv"
    output_file = "output.csv"
    process_data(input_file, output_file)
