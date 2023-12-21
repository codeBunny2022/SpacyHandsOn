#find quotes in data provided
'''we want to find narrator and color it!!'''
import spacy
from spacy import displacy
import re

with open("./DataAlice.txt") as f:
    text = f.read().replace("/n/n","")
    chapters = text.split("CHAPTER")[0:]

chap1=chapters[1]
# print(chap1)
nlp=spacy.load("en_core_web_sm")

doc=nlp(chap1)
sentences=list(doc.sents)


def get_quotes(text):
    # quotes=re.findall(r" '(.*?)'",text)
    quotes = re.findall(r"(?:(?<=\s)|^)['\"](.*?)['\"](?=\s|$)", text)      
    return quotes


for sent in sentences:
    found_quotes=get_quotes(str(sent))
    print(found_quotes)