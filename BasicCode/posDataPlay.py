import spacy
import textacy
with open("./DataAlice.txt") as f:
    text = f.read().replace("/n/n","")
    chapters = text.split("CHAPTER")[1:]

nlp=spacy.load("en_core_web_sm")
chap1=chapters[1]
doc=nlp(chap1)

patterns=[{"POS":"ADV"},{"POS":"VERB"}]
verb_phrases=textacy.extract.matches(doc,patterns=patterns)

for verb_phrase in verb_phrases:
    print(verb_phrase)