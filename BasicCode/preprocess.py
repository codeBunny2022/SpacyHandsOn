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
entities=list(doc.ents)


# print(entities,len(entities))
# characters=[]
# count=0
# for i in entities:
#     if(i.label_=="PERSON" and i.text not in characters):
#         count+=1
#         characters.append(i.text)
# print(*characters,"\n",count)


# for j in sent1:
#     print(j.text,"\t",j.pos_)


# for token in doc:
#     if(token.pos_=="NOUN"):
#         print(token)

# print(*(doc.noun_chunks))

patterns=[{"POS":"NOUN"},{"POS":"VERB"}]
gainedData=textacy.extract.matches(doc,pattern=patterns)