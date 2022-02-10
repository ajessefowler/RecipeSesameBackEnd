import spacy

nlp = spacy.load('en_core_web_md')
text = ("I want some Greek food tonight.")
doc = nlp(text)

print("Nouns:", [token.lemma_ for token in doc if token.pos_ == "NOUN"])
print("Adjectives:", [token.lemma_ for token in doc if token.pos_ == "ADJ"])