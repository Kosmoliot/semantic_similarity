#====Modules====#
import spacy

#====spaCy 'md' and 'sm' modules====#
nlp1 = spacy.load('en_core_web_md')
nlp2 = spacy.load('en_core_web_sm')

#====Function====#
def compare_word(word_list, nlp_mod):
    print(nlp_mod(word_list[0]).similarity(nlp_mod(word_list[1])))
    print(nlp_mod(word_list[0]).similarity(nlp_mod(word_list[2])))
    print(nlp_mod(word_list[1]).similarity(nlp_mod(word_list[2])))
    
#====Similarity====#
word1 = ['cat', 'monkey', 'banana']
word2 = ['spider', 'drain', 'rain']

compare_word(word1, nlp1)
compare_word(word2, nlp1)

"""
Cat and monkey are both animals, that's why the similarity is highest between
three comparisons that we did; Because monkeys eat banana, spaCy was able to
draw a connection there with the second highest similarity score; Well, cat and
banana has a lowest similarity score, which makes sense when tking in account
words we have used.
"""

compare_word(word1, nlp2)

"""
When running 'similarity' with 'sm' module user is warned that 'The model you are
using has no vectors loaded... so it will be based on the tagger, parsr and NER'
All combination scored much higher in similarity and with the minimum difference
between combinations: e.g. with 'sm' module (cat, monkey) and (cat, banana)
difference is 8%, and with 'sm' (cat, monkey) and (cat, banana) difference is
62%. With more vectors similarity prediction results will be more accurate, so
it would be beneficial to use larger modules.
"""