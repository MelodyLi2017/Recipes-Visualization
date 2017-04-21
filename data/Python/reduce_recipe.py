import json
import fractions
###Reducing number of recipes in original dataset and store them

##load full recipe data
json_file='full_format_recipes.json'
json_data=open(json_file)
data = json.load(json_data)
json_data.close()
##check if a string that contains '/' is really a fraction. 
def checkFraction(string):
	try:
		round(float(fractions.Fraction(string)), 2)
		return True
	except ValueError:
		return False
print ('/' in 'g/2',  checkFraction ('g/2'))
##check if string contains numeric values besides the delimiter (hyphen in this case):
##returns 0 if does not contain numeric values.
def containsNumericValues(mystring, delimiter):
	listChar = mystring.split(delimiter)
	for word in listChar:
		# print(listChar[k])
		chars = list(word)
		# print (chars)
		for char in chars:
			if type(char)==int or char.isdigit():
				# print (mystring)
				return True
	return False
##Check using an example string. Should return True
print("Works?", '–' in '1–11/2', containsNumericValues('(1–11/2', '-'))
##to be stored
parsedata=[]

##number of recipes in the parsedata set
number = 0
# start parsing from the top
for row in data:
	try:
		noHyphen = True
		##reject recipes with hyphenated quantities
		for ingredient in row['ingredients']:
			for word in ingredient.split():
				
				if '-' in word and containsNumericValues(word, '-')==True or '–' in word:
					noHyphen = False
				if '/' in word and checkFraction(word)==False:
					noHyphen = False
				if '-' in word and '/' in word:
					noHyphen = False
				# else:
				# 	print(word)
		if noHyphen == True and len(row['ingredients'])<10:
			number+=1
			parsedata.append(row)
			# print (row['ingredients'])
				
	##Recipes with no ingredients will be discarded
	except KeyError:
		print ("no ingredients.")
print("Total number of simple recipes: ", number)	

# print(parsedata)
#write final parsed data to the outfile
with open('reduced_recipes.json', 'w') as outfile:
    json.dump(parsedata, outfile)