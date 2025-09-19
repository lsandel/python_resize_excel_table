import csv
import pandas as pd
import numpy as np

# Step 1: Load the CSV file
file_path = 'INSERT INPUT FILE PATH HERE'
df = pd.read_csv(file_path, skiprows=14)
print(df) # check csv file has all entries

# Convert CSV file to list
csv_data = df.values.tolist()
print(csv_data[0]) # check heading row is correct

# Flatten the original 2D list (575757 rows, 3 columns) to 1D list
flattened_data = [item for sublist in csv_data for item in sublist]

# Reshape the flattened list to 91 rows (one per logged message) and 6327 columns (oneper time entry)
#rows, cols = 91, 6327
rows, cols = 4, 4679
reshaped_list = [flattened_data[i * cols:(i + 1) * cols] for i in range(rows)]

transposed_list = list(map(list, zip(*reshaped_list)))
print((transposed_list[0])) # check headings are correct

# Write the data to a CSV file
file_path = 'INSERT OUTPUT FILE PATH HERE'
with open(file_path, mode='w', newline='') as file:
   writer = csv.writer(file)
   for row in transposed_list:
       writer.writerow(row)

print(f"Data has been written to {file_path}")

