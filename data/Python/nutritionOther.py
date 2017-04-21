from collections import Counter
import numpy as np
import json
import csv
##initialize final merged data to be written into json file
parsedata={}
with open('nutrition.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
    	# print (row.keys())
        parsedata[row['NDB_No']] = row
            
##write final parsed data to the outfile
with open('nutrition_reduced.json', 'w') as outfile:
    json.dump(parsedata, outfile)
          
    