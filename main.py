from typing import List
from POSTagger.Utility.Utils import readDictionary
from POSTagger.RDRPOSTagger.RDRPOSTagger import POSTagger
import nltk
from nltk import CFG
from nltk import EarleyChartParser
from nltk import word_tokenize
from nltk import Tree

import re

nltk.download('punkt')

POS_TAG_MODELS = {
    "en" : { 
      "dict" : "./POSTagger/Models/ud-treebanks-v2.4/UD_English-LinES/en_lines-ud-train.conllu.UPOS.DICT",
      "rdr" : "./POSTagger/Models/ud-treebanks-v2.4/UD_English-LinES/en_lines-ud-train.conllu.UPOS.RDR"
    },
    "it" : {
      "dict" : "./POSTagger/Models/ud-treebanks-v2.4/UD_Italian-ISDT/it_isdt-ud-train.conllu.UPOS.DICT",
      "rdr" : "./POSTagger/Models/ud-treebanks-v2.4/UD_Italian-ISDT/it_isdt-ud-train.conllu.UPOS.RDR" 
    },
    "fr" : {
      "dict" : "./POSTagger/Models/ud-treebanks-v2.4/UD_French-ParTUT/fr_partut-ud-train.conllu.UPOS.DICT",
      "rdr" : "./POSTagger/Models/ud-treebanks-v2.4/UD_French-ParTUT/fr_partut-ud-train.conllu.UPOS.RDR"
    },
    "ge" : {
      "dict" : "./POSTagger/Models/ud-treebanks-v2.4/UD_German-GSD/de_gsd-ud-train.conllu.UPOS.DICT",
      "rdr" : "./POSTagger/Models/ud-treebanks-v2.4/UD_German-GSD/de_gsd-ud-train.conllu.UPOS.RDR"
    }
}

LANGUAGE_EXTENDED = {
    "it" : "italian",
    "en" : "english",
    "ge" : "german",
    "fr" : "french"
}

def extract_pos_tags(text: str):
    rgr = re.compile(r'(\w+)/(\w+)')
    res = []
    for m in rgr.finditer(text):
        res.append((m.group(1), m.group(2)))
    return res

def pos_tag(text : str, lang : str):
    language = POS_TAG_MODELS[lang]
    
    pos_tagger = POSTagger()
    pos_tagger.constructSCRDRtreeFromRDRfile(language["rdr"]) 
    DICT = readDictionary(language["dict"])
    text_tagged = pos_tagger.tagRawSentence(DICT, text)
    
    return extract_pos_tags(text_tagged)
    
def load_grammar(terminals: List, lang: str):
    grammar = ""
    path = './grammars/' + lang + '.cfg'
    with open(path) as cfg:
        grammar = cfg.readlines()

        for (token, upos) in terminals:
            grammar.append("{lhs} -> '{rhs}'".format(lhs=upos, rhs=token))
            
    return CFG.fromstring(grammar)
    
def remove_empty_nodes(tree):
    if isinstance(tree, nltk.tree.Tree) and len(tree) == 0:
        return None
    if isinstance(tree, nltk.tree.Tree):
        children = [remove_empty_nodes(child) for child in tree]
        children = [child for child in children if child is not None]
        return Tree(tree.label(), children)
    return tree

# EDIT to test
lang = "en"
sentence = "The fox is on the table and a small turtle is on the floor of the building ."

langExtended = LANGUAGE_EXTENDED[lang]

# Run the RDR Pos tagger to obtain a pos tag for each word
pos_tags = pos_tag(sentence, lang)

print("\n>>>>> POS TAGAGGING: ")
print(">>>>> " + str(pos_tags))

# Load the grammar from a file and add the pos tags as terminals rules
grammar = load_grammar(pos_tags, lang)

# Initialize the parser with the corresponding grammar
parser = EarleyChartParser(grammar, trace=0)

# Use nltk to perform the word tokenization, accordingly to the language specified
text_tokenized = word_tokenize(sentence, langExtended)

print("\n>>>>> First admissible tree: ")
for tree in parser.parse(text_tokenized):
    # Tree with all the empty nodes removed
    print(remove_empty_nodes(tree))
    # Print only the first one, ambiguity blocked here
    break





