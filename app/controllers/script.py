import spacy

from spacy import displacy
from spacy_streamlit import visualize_parser
import streamlit as st

text = "Verificado es el mejor grupo del mundo!!!. Con Robert, Dante, Azu y Lu estamos probando si displacy esto funciona"
texto2 = "Milei vs. gobernadores: ¿de qué provincias provienen los productos que la Argentina exporta al mundo?"

nlp = spacy.load("en_core_web_sm")
doc = nlp(texto2)

for token in doc:
    print(
        token.text,
        token.lemma_,
        token.pos_,
        token.tag_,
        token.dep_,
        token.shape_,
        token.is_alpha,
        token.is_stop,
    )
html = displacy.render([doc], style="dep", page=True)
visualize_parser(doc)
