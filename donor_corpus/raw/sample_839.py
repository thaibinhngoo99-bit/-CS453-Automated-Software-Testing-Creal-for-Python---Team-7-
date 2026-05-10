# Import spacy
import spacy

# Instantiate the English model: nlp
nlp = spacy.load('en', tagger=False, parser= False, matcher = False)

# Create a new document: doc
doc = nlp(article)

# Print all of the found entities and their labels
for ent in doc.ents:
    print(ent.label_, ent.text)

""" <script.py> output:
    ORG Uber
    ORG Uber
    ORG Apple
    ORG Uber
    ORG Uber
    PERSON Travis Kalanick
    ORG Uber
    PERSON Tim Cook
    ORG Apple
    CARDINAL Millions
    ORG Uber
    GPE drivers’
    LOC Silicon Valley’s
    ORG Yahoo
    PERSON Marissa Mayer
    MONEY $186m """