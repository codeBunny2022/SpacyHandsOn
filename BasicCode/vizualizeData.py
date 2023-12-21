import spacy
from spacy import displacy


with open("./DataAlice.txt") as f:
    text = f.read().replace("/n/n","")
    chapters = text.split("CHAPTER")[1:]

nlp=spacy.load("en_core_web_sm")
chap1=chapters[1]
doc=nlp(chap1)

sentences=list(doc.sents)
sent1=sentences[1]

html=displacy.render(sent1, style="ent")

with open("data_vi.html", "w") as f:
    f.write(html)
