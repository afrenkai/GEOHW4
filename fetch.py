import requests
import pandas as pd

starttime = '2010-01-04'
endtime = '2017-09-30T23:59:59.999999'
minmagnitude = 3
maxmagnitude = 10
minlatitude = 32.66
maxlatitude = 37.15
minlongitude = -105.35
maxlongitude = -90.9
mindepth = 0
maxdepth = 6371
limit = 99999999
output_format = 'text'
url = (
    f'https://service.iris.edu/fdsnws/event/1/query?starttime={starttime}'
    f'&endtime={endtime}'
    f'&minmagnitude={minmagnitude}&maxmagnitude={maxmagnitude}'
    f'&minlatitude={minlatitude}&maxlatitude={maxlatitude}'
    f'&minlongitude={minlongitude}&maxlongitude={maxlongitude}'
    f'&mindepth={mindepth}&maxdepth={maxdepth}'
    f'&limit={limit}&output={output_format}'
)

response = requests.get(url)
if response.status_code == 200:
    data = response.text
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    exit()

lines = data.split('\n')
columns = [col.strip() for col in lines[0].split('|')]
rows = [row.split('|') for row in lines[1:] if row]
df = pd.DataFrame(rows, columns=columns)

csv_file_path = 'earthquake_data_fetched.csv'
df.to_csv(csv_file_path, index=False)

print(f"Data saved to {csv_file_path}")
