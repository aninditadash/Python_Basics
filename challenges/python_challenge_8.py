# Find out which prepositions have been used in the below quote as provided in the prepositions set

text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

text_in_words = text.split()
text_in_words_set = set(text_in_words)
print(text_in_words)
print(text_in_words_set)

preps_used = text_in_words_set & prepositions
print(preps_used)
