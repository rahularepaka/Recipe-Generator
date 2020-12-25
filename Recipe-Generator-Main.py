# Import All Libraries
from urllib.request import urlopen
import urllib
import json
from datetime import datetime

# API Intialisation
def recipe_search(ingredient):
    api_key = '7a7cd9b85dd6e0d516903b7c2d582bfa'
    application_id = 'a720f909'
    url = 'https://api.edamam.com/search?app_id={}&app_key={}&q={}'.format(application_id, api_key, ingredient)
    # Opening the URL
    result = urllib.request.urlopen(url)
    # Converting the information to JSON File Format
    data = json.load(result)
    return data['hits']

# User Inputs the ingredient
ingredient = input('Enter an ingredient: ')

# Renaming the File to the ingredient 
opname = ingredient + '-recipes.txt'

# File Location 
intifile = "D:\\Python - Projects\\food_reciepe\\" #Please enter the file directory for the file to be saved
outFileName = intifile + str(opname) 

#Creating the File with Encoding
report = open(outFileName, "w", encoding="utf-8")

# Date and Time
now = datetime.now()
dt = now.strftime("%d/%m/%Y %H:%M:%S")

# API Call
hits = recipe_search(ingredient)

# Heading the Text File
report.write("--------------------------------------------Recipe Generated From " +ingredient+"---"+dt+"--------------------------" + '\n')
report.write('\n')

# Loop for Searching Recpies
for single_hit in hits:
    recipe_json = single_hit['recipe']
    report.write(str(recipe_json['label']) + '\n')
    report.write(str(recipe_json['ingredientLines']) + '\n')
    report.write(str(recipe_json['dietLabels']) + '\n')
    report.write('-'*150 + '\n')
    report.write('\n')

print('Please Find the Text File Saved in this directory')

#Closing the File Created
report.close()
