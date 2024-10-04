import pandas as pd
data_path = "data.txt"
with open(data_path, 'r') as file:
    data = file.read()

data_lines = data.split('\n')
columns = [col.strip() for col in data_lines[0].split('|')]
rows = [row.split('|') for row in data_lines[1:] if row]
df = pd.DataFrame(rows, columns=columns)
csv_file_path = 'earthquake_data.csv'
df.to_csv(csv_file_path, index=False)
# print(df.head())