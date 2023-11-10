import nltk
from nltk.corpus import brown
from nltk.corpus import wordnet
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

# Step 1: Retrieve the Brown corpus.
nltk.download('brown')
nltk.download('wordnet')

print(len(brown.sents()))  # Print the number of sentences in the corpus

# Step 3: Create short and long sentence corpora.
short_sentences = [s for s in brown.sents() if len(s) <= 20]
long_sentences = [s for s in brown.sents() if len(s) > 20]

print(len(short_sentences))
print(len(long_sentences))

with open('lexicon.tff', 'r') as tff_file:
    tff_data = tff_file.read().split('\n')

lexicon = []  # Initialize an empty list to store lexicon data

for line in tff_data:
    # Split the line into key-value pairs
    if line != " ":
        pairs = line.strip().split(" ")

        word_data = {}
        for pair in pairs:
            key, value = pair.split('=')
            word_data[key] = value
            lexicon.append(word_data)

long_tokens = []

for sentence in long_sentences:
    for token in sentence:
        long_tokens.append(token)

short_tokens = []

for sentence in short_sentences:
    for token in sentence:
        short_tokens.append(token)

positive_words = 0
negative_words = 0

for i, token in enumerate(long_tokens):
    print(i, "/", len(long_tokens))
    for word_data in lexicon:
        if word_data["word1"] == token:
            print(token)
            if word_data["priorpolarity"] == "negative":
                negative_words += 1
            else:
                positive_words += 1
                
# Print the positive and negative words
print("Positive Words:", positive_words)
print("Negative Words:", negative_words)
