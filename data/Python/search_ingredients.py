import json
import copy
##load reduced recipe with units data
json_file='recipe_to_nutrition.json'
json_data=open(json_file)
recipe_data = json.load(json_data)
json_data.close()

json_file='nutrition_reduced.json'
json_data2=open(json_file)
nutrition_data = json.load(json_data2)
json_data2.close()

dictionary_ingredients={}
for row in recipe_data:
	for k in row.keys():
		recipe_name = k
	for ingredient in row[k].values():
	# print(k)
	# print(len(dictionary_ingredients[k]))
		if ingredient not in dictionary_ingredients.keys():
			dictionary_ingredients[ingredient]=[]

		dictionary_ingredients[ingredient].append(recipe_name)
dictionary_ingredients_new = []
for ingredientNo in dictionary_ingredients:
	matched=False
	datum = {}
	for r in nutrition_data:
		if int(r)==int(ingredientNo):
			# print('found')
			# print(nutrition_data[r]['Shrt_Desc'])
			# print(dictionary_ingredients[ingredientNo])
			datum[nutrition_data[r]['Shrt_Desc']]=dictionary_ingredients[ingredientNo]
			matched=True
	if matched ==False:
		print(ingredientNo)
	dictionary_ingredients_new.append(datum)
		
for dat in dictionary_ingredients_new:
	# dat['count'] = len(dat)
	length = 0
	for k in dat:
		length = len(dat[k])
	if(length>=5):
		print(dat.keys())
	dat['count']=length
	# print(length)

	
# print(dictionary_ingredients_new)
def sortCount(elem):
    return elem['count']
# with open('search_ingredients_counted.json', 'w') as outfile:
# 	newThing = json.dumps( sorted(dictionary_ingredients_new, key=lambda x: x['count'], reverse=True))
# 	json.dump(newThing, outfile)
	# print(newThing)
