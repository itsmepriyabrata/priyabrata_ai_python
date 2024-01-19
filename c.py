import csv

def read_large_csv(TRANSFOMER.CSV):
    with open(TRANSFOMER.CSV, 'r') as TRANSFOMER.CSV:
        csv_reader = csv.reader(TRANSFOMER.CSV)
        
        for row in csv_reader:
            # Process each row as needed
            print(row)

# Replace 'your_large_file.csv' with the actual file path
read_large_csv('DUBLINAI.CSV')
