import requests
import wget
import csv
from datetime import datetime, timedelta
from Utilities import create_folder
# =======================================

start_date = "2017-03-19"
# start_date = "2018-03-17"
stop_date = "2018-03-28"

stationsname = 'MaxBrauerAllee'

# sensor = [353, 1682, 4104, 7563]                                       # Habichtstr.
sensor = [413, 836, 2448, 2470, 2876, 3673, 4581, 4672, 9426, 10335]    # Max B.-Allee
# sensor = [543, 1573, 2448, 3539, 7140]                                 # Stresemannstr.
# sensor = [7140]                                                        # Kieler Str.

output_dir = '../LuftdatenInfo_Download/raw/'

#for item in sensor:
    # create_folder(output_dir,item)

# =======================================
# Define Start and Stop date
# =======================================

start = datetime.strptime(start_date, "%Y-%m-%d")
stop = datetime.strptime(stop_date, "%Y-%m-%d")

# =======================================
# download
# =======================================

temp = []
check_avail = []

while start <= stop:
    datum = start.date()        # extract only the date
    print(datum)
    temp.append(str(datum))

    # iterate over sensor
    for item in sensor:

        url = "https://archive.luftdaten.info/" + str(datum) + "/" + str(datum) + "_sds011_sensor_" + str(item) + ".csv"

        # check if website exists
        request = requests.get(url)
        if request.status_code == 200:
            print(str(item))
            filename = url.split('/')[-1].strip()
            #wget.download(url, output_dir + str(item) + '/' +str(filename))
            temp.append(1)
        else:
            temp.append(0)

    start = start + timedelta(days=1)
    check_avail.append(temp)
    temp = []
    print(' ')

# =======================================
# storage availability info in csv file
# =======================================

with open(output_dir + "check_availability_Luftdaten_"+str(stationsname) + ".csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(['time'] + sensor)
    writer.writerows(check_avail)



