import csv

# Use 'newline=""' as recommended by the csv module documentation
with open("D:/movies.csv", 'r', newline='') as f:
    # Create a reader object
    reader = csv.reader(f)
    
    # Extract the first row as the header
    header = next(reader)
    
    # Convert the remaining rows into a list
    data = list(reader)

print("Header:", header)
print("First 2 rows of data:", data[:2])