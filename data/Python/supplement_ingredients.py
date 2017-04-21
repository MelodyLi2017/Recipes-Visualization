import json
import copy
##load recipe to nutrition data
json_file='new_recipe_to_nutrition.json'
json_data=open(json_file)
recipe_data = json.load(json_data)
json_data.close()
##load reduced recipe with units data
json_file2='reduced_recipes_with_units.json'
json_data2=open(json_file2)
original_recipe_data = json.load(json_data2)
json_data2.close()
parseData = []
for row in recipe_data:
	# print (row)
	title = ""
	newRow = copy.deepcopy(row)
	for key in row.keys():
		title = key

	for recipe in original_recipe_data:
		# print(recipe['title'])
		# print (title)
		if title.strip()==recipe['title'].strip():
			# print ('found recipe matching')
			for ingredient in row[title]:
				# print(ingredient)
				no = row[title][ingredient]
				for full_ingredient in recipe['new ingredients']:
					# print(full_ingredient)
					toBePopped = ingredient
					
					if ingredient==full_ingredient['name']:
						
						newRow[title][ingredient]={}
						newRow[title][ingredient]['NDBNo'] = no
						newRow[title][ingredient]['unit']=full_ingredient['unit']
						newRow[title][ingredient]['magnitude']=full_ingredient['magnitude']
						# recipe_data[name][ingredient]['magnitude']=recipe['new ingredients'][full_ingredient]['magnitude']
						if '*' in ingredient.split()[0]:
							print ("Hey there's *")
							
							newRow[title].pop(toBePopped)
							# print(newRow[title])
	# print (newRow)
	parseData.append(newRow)
# print(parseData)

with open('recipe_to_nutrition_full_with_units.json', 'w') as outfile:
		json.dump(parseData, outfile)