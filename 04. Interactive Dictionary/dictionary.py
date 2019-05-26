import json
from difflib import SequenceMatcher
from difflib import get_close_matches

dict = json.load(open("data.json"))

def search(w):
    if w in dict:
        return(dict.get(w))
    elif len(get_close_matches(w,dict.keys())) > 0:
        ans = input("Did you mean '%s'? [y/n] " % get_close_matches(w,dict.keys())[0])
        if ans == "y":
            return dict[get_close_matches(w,dict.keys())[0]]
        else:
            return "Sorry, we can't find your word"
    else:
        #SequenceMatcher(None,w,"rain").ratio()
        return("You word cannot be found, try a different word or spelling")

word = input("Enter Your Search Query: ").lower()
print(search(word))
