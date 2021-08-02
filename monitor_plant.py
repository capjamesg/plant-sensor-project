import create_charts
from grow.moisture import Moisture
import datetime

m1 = 0
m2 = 0
m3 = 0

m1_interface = Moisture(1)
m2_interface = Moisture(2)
m3_interface = Moisture(3)

while m1 == 0:
    m1 = m1_interface.moisture

while m2 == 0:
    m2 = m2_interface.moisture

while m3 == 0:
    m3 = m3_interface.moisture

desired_saturation = 4.0

print(m1, m2, m3)

now = datetime.datetime.now()
    
with open("/home/james/plant-sensor/logging.csv", "a", newline="") as file
    row = [
       now.strftime("%Y-%m-%d"),
       now.strftime("%H:%M"),
       m1,
       m2,
       m3
    ]
    
     writer.writerow(row)

create_charts.create()
