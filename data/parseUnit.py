import json
##load full recipe data
json_file='full_format_recipes.json'
json_data=open(json_file)
data = json.load(json_data)
json_data.close()
##
for row in data:
	try:
		print (row['ingredients'])

		##TO DO 1 : Define the units https://pint.readthedocs.io/en/0.7.2/defining.html
		##TODO 2: parse units and numerical value. e.g "3 cups of parsley" = "3", "cup"
	except KeyError:
		print ("no ingredients.")
