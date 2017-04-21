import json
from fuzzywuzzy import fuzz
##load reduced recipe with units data
json_file='reduced_recipes_with_units.json'
json_data=open(json_file)
recipe_data = json.load(json_data)
json_data.close()
##load nutrition file
json_file2='nutrition_reduced.json'
json_data2=open(json_file2,'r')
nutrition_data = json.load(json_data2)
json_data2.close()
text_file = open("Output.txt", "w")
def strip(string):
	newstr = string.replace("(", "")##delete the '(),'
	newstr=newstr.replace(")", "")
	newstr=newstr.replace(",", "")
	return newstr

##Define a list of recognizatle units and frequent words that appear in recipes. 
relevantUnits = ['cup', 'cups', 'teaspoon', 'fresh', 'leaves', 
'unsweetened', 'sweetened', 'medium', 'diced' ,'large', 'small', 
'tbsps', 'tsps', 'teaspoons', 'pounds', 'ground', 'seed', 'tbsp', 
'tsp', 'pound', 'lb', 'tablespoon','tablespoons', 'ounces', 'oz', 
'chopped', 'canned', 'drained', 'cubes', 'brown', 'ripe', 'powdered', 
'sliced', 'slices', 'slice', 'preserves', 'minced', 'seeded', 
'toasted', 'quartered', 'minced', 'strips', 'with', 'crushed','cured', 
'thredded', 'powdered', 'grated', 'mixed', 'hard-cooked']
def strToFloat(string):
	try:
		return float(string)
	except:
		return False
###Function that modifies nutrition data to suit the quantity taken from recipe
def modifyNutrition(ingredient):
##TODO: if ingredient['magnitude']==0, use data from nutrition data. 
	if ingredient['magnitude']!='0' and ingredient['unit']=='NA':
		for k in ingredient['nutrition_data']:
			if k!='GmWt_1' and	k!='GmWt_Desc1' and k!='GmWt_2' and k!='GmWt_Desc2' and k!='Shrt_Desc' and k!='NDB_No':
				if(ingredient['nutrition_data']['GmWt_1']!=''):
					ingredient['nutrition_data'][k]=strToFloat(ingredient['nutrition_data']['GmWt_1'])/100*strToFloat(ingredient['magnitude'])
					# print('a')
				else:
					ingredient['nutrition_data'][k]=strToFloat(ingredient['nutrition_data']['GmWt_2'])/100*strToFloat(ingredient['magnitude'])
					# print('b')
	if ingredient['magnitude']!='0' and ingredient['unit']!='NA':
		for k in ingredient['nutrition_data']:
			if k!='GmWt_1' and	k!='GmWt_Desc1' and k!='NDB_No' and k!='GmWt_2' and k!='GmWt_Desc2' and k!='Shrt_Desc':
				ingredient['nutrition_data'][k]=strToFloat(ingredient['magnitude'])*strToFloat(ingredient['nutrition_data'][k])
				# print('c')
	return ingredient['nutrition_data']

totalscore = 0

parseData = []
data = nutrition_data['SUGARS,GRANULATED'] 

for recipe in recipe_data:
	newData = {}
	# print(recipe)
	listRecipe={}
	for ingredient in recipe['new ingredients']:

		maxRatio = 0
		matched = ''
		name = ingredient['name']
		isSugar = False
		listName = name.split(' ')
		for word in listName:
			if strip(word.strip()) in relevantUnits:
				# print (word)
				listName.remove(word)
				name = ' '.join(listName)
			# if strToFloat(word)!=False:
			if strip(word.strip())=='sugar':
				isSugar = True
				name = 'SUGARS,GRANULATED'
			if strip(word.strip())=='salt':
				isSalt = True
				name = 'SALT,TABLE'
			if strip(word.strip())==('eggs' or 'egg'):
				# isSalt = True
				name = 'EGG,WHL,RAW,FRSH'
			
		for k in name:
			# print (k)
			if strToFloat(k)!=False  or k=='/':
				name = name.replace(k,'')
		# print (name)
		##The 
		NDBno = ''
		datum = ''
		# for item in nutrition_data:
		# 	# print (nutrition_data[item])
			
		# 	description = nutrition_data[item]['Shrt_Desc'].lower()
		# 	description = description.split(',')
		# 	if len(description)>=2:
		# 		description = description[0] + ' ' + description[1]
		# 		# print(type(fuzz.ratio(name, item)))
		# 		##perform fuzzy search and calculate similarity
		# 	token_set_Ratio = fuzz.token_set_ratio(name, description)
		# 	ratio = fuzz.ratio(name, description)
		# 	partialRatio = fuzz.partial_ratio(name, description)
		# 	token_sort_Ratio = fuzz.token_sort_ratio(name, description)
		# 	ratios = [token_set_Ratio, partialRatio, token_sort_Ratio]
		# 	bestRatio = max(ratios)
		# 	if maxRatio ==0 or bestRatio>maxRatio:
		# 		maxRatio = bestRatio
		# 		totalscore+=maxRatio
		# 		matched = description
		# 		NDBno = nutrition_data[item]['NDB_No']
		# 		datum = item
		# newData[ingredient['name']] = NDBno
	listRecipe[recipe['title']] = newData
	print(listRecipe)
	parseData.append(listRecipe)

		
		# ingredient['nutrition_data'] = nutrition_data[datum]
		# 	# print(ingredient['nutrition_data'])
		# 	##TODO: if ingredient['magnitude']==0, use data from nutrition data. 
		# ingredient['nutrition_data']=modifyNutrition(ingredient)
		# print(ingredient['magnitude'])
		# print(ingredient['nutrition_data'])
		# print(ingredient['name'], ' ', datum)
		
		# print (nutrition_datum)
	
	# print(newData)
	# parseData.append(newData)	
	# parseData.append(newData)
		# print ("Name of ingredient: ", str(name))
		# print("Score of similarity: " ,str(maxRatio))
		# print( "Matched to: ", str(matched))
		# print("Matched number: ", str(NDBno))
print (parseData)
with open('reduced_recipes_with_nutrition.json', 'w') as outfile:
		json.dump(parseData, outfile)
# print("TOTAL SCORE: " ,totalscore)

##write final parsed data to the outfile


