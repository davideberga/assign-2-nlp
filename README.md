# Assignment 2 NLP

## Introduction

This project contains a pipeline to produce the syntax tree of a sentence, given its language. The approach used is the pure symbolic one with a context free grammar as a base.

## Structure

- ```grammars/``` : here there are the grammars (*.cfg) used, one for each language
- ```POSTagger/``` : the PArt-of-Speech tagger used, downloaded from this [repository](https://github.com/datquocnguyen/RDRPOSTagger). It is the RDRPOSTagger, a rule base tagger with models for about 330 languages. This folder contains also the most recent models.
- ```main.py``` : the script to run the pipeline

## Usage

```python3 -m pip install -r requirements.txt```

Inside the ```main.py``` edit the language and the sentence:

```
lang = ["en" | "it" | "fr" | "ge"] : string
sentence = "A simple sentence" : string
```

then ```python3 main.py```.

## Examples

Input (en): 
```
lang = "en"
sentence = "The fox is on the table and a small turtle is on the floor of the building ."
```

Output: 
```
>>>>> First admissible tree: 
(S
  (S
    (S
      (NP (DET The) (NOUN fox))
      (VP (VERB is) (PP (ADP on) (NP (DET the))) (NP (NOUN table))))
    (CCONJ and)
    (S
      (NP (DET a) (ADJS (ADJ small) (ADJS (ADJ turtle))))
      (VP
        (VERB is)
        (PP
          (ADP on)
          (NP (DET the) (NOUN floor) (PP (ADP of) (NP (DET the)))))
        (NP (NOUN building)))))
  (PUNCT .))
```

Input (it): 
```
lang = "it"
sentence = "Il cane è salito improvvisamente su una mensola"
```

Output: 
```
>>>>> First admissible tree: 
(S
  (S (NP (DET Il) (NOUN cane)) (VP (VERB (AUX è))))
  (S
    (NP )
    (VP
      (VERB salito)
      (ADVS (ADV improvvisamente))
      (PP (ADP su) (NP (DET una)))
      (NP (NOUN mensola)))))
```

Input (fr): 
```
lang = "fr"
sentence = "Le chien a soudainement grimpé sur une étagère"
```

Output: 
```
>>>>> First admissible tree: 
(S
  (S
    (NP (DET Le) (NOUN chien))
    (VP (VERB (AUX a)) (ADVS (ADV soudainement))))
  (S
    (NP )
    (VP
      (VERB grimpé)
      (PP (ADP sur) (NP (DET une)))
      (NP (NOUN étagère)))))
```

Input (ge): 
```
lang = "ge"
sentence = "Die böse Hexe durchstreift den Wald"
```

Output: 
```
>>>>> First admissible tree: 
(S
  (NP (DET Die) (ADJS (ADJ böse)) (NOUN Hexe))
  (VP (VERB durchstreift) (NP (DET den) (NOUN Wald))))
```


