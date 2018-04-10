import json
from difflib import get_close_matches

data=json.load(open('data.json'))
def translate(word):
    if word in data :
        return data[word]
    elif word.title() in data.keys():
        return data[word.title()]
    elif word.upper() in data.keys():
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8)) > 0:
         yn = input("Did you mean %s instead? Enter 'Y' for yes or 'N' for No. " % get_close_matches(word, data.keys())[0])
         if yn == 'Y' or yn == 'y':
             return data[get_close_matches(word, data.keys())[0]]
         elif yn == 'N' or yn == 'n':
            return "The word doesn't exit. Duble check it."
         else:
            return "Couldn't understand your entry."

    else:
            return "Try Again"

word = input("Enter Word: ")
output = translate(word.lower())
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
