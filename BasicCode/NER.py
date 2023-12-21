import spacy
test="Harry Potter is a popular book series that tells the adventures of the young wizard Harry Potter and his friends Ron Wesley and Hermione Granger, who are all students of the Hogwarts School of Witchcraft and Wizardry. The series has sold more than 450 million copies worldwide, making it the best-selling book series in history. The first four books' film adaptations grossed more than $7 billion at box offices worldwide. The stories have been recognized for their themes of true friendship, courage, loyalty, and morality.1 In the book Harry Potter and the Sorcerer's Stone, Harry finds out that when Lily Potter died, an ancient magical protection from Voldemort's lethal spells was transferred to her son. This protection allowed Harry as an infant to survive Voldemort's attack and help him keep Voldemort from possessing the Stone, which Dumbledore agrees to destroy"
nlp=spacy.load("en_core_web_sm")
doc=nlp(test)
for ent in doc.ents:
    print(ent.text," ",ent.label_)