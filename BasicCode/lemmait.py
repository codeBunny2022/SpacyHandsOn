import spacy
import textacy
with open("./DataAlice.txt") as f:
    text = f.read().replace("/n/n","")
    chapters = text.split("CHAPTER")[1:]

nlp=spacy.load("en_core_web_sm")
chap1=chapters[1]
doc=nlp(chap1)

sentences=list(doc.sents)
sent1=sentences[1]

for word in sent1:
    if word.pos_ =="VERB":
        print(word,"\t",word.lemma_)