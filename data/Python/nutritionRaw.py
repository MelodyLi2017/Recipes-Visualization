from collections import Counter
import numpy as np
import json
import csv
##initialize final merged data to be written into json file
parsedata={}
with open('nutrition.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        parsedata[row['Shrt_Desc']] = row
            
##write final parsed data to the outfile
with open('nutritionRaw.json', 'w') as outfile:
    json.dump(parsedata, outfile)
          
    