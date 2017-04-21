from collections import Counter
import numpy as np
import json
import csv
##initialize final merged data to be written into json file
parsedata={}
with open('nutrition.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    ##A list of truncated food names:
    food_names = []
    ##field names for each field
    field_names = []
    ##number of items belonging to each food name:
    food_names_counts=[]
    ## rawdata to be built
    tempdata={}
    ##start reading the original file
    length=0
    for row in reader:
        length+=1
        ##Shrt_Desc is the name for each food item.
        original_name = row['Shrt_Desc']
        if(len(field_names)==0):
            for key in row.keys():
                field_names.append(key)
        food_names.append(row['Shrt_Desc'].split(",")[0])
        ##modify the food names by matching the names against 
        ##the truncated names
        for name in food_names:
            if(name in row['Shrt_Desc']):
                food_names_counts.append(name)
                row['Shrt_Desc']=name
        tempdata[original_name]=row
        
    ##start merging the items with the same food name

    
    food_names_counts=Counter(food_names_counts)
    
    ##name of the food being combined
    desc = ''
    ##a list of rows of items with the same name to be combined
    group = []
    ##datum for merged food
    merged = {}
    for datum in tempdata:
        if(len(group)==0 or tempdata[datum]['Shrt_Desc']==desc):
            group.append(tempdata[datum])
        else:
            for field in field_names:
                merged[field] = 0
                for food in group:
                    # print(food[field])
                    ##if food[field] is a number,
                    ##take average over the number of items with the same name
                    try:
                        merged[field]+=(food[field]/food_names_counts[desc])
                    ##otherwise, if field is a string, use the first datum's info as default
                    except TypeError:
                        merged[field]=food[field]     
            ##write the merged data into parsedata
            parsedata[merged['Shrt_Desc']]=merged
            ##reset the groups to be re-populated
            desc = ''
            group=[]
            merged={}
            
##write final parsed data to the outfile
with open('parsed_nutrition.json', 'w') as outfile:
    json.dump(parsedata, outfile)
          
    