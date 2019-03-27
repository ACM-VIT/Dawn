import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
sentence=input()
p="?;!.,;"
sentence_words= nltk.word_tokenize(sentence)
for word in sentence_words:
    if word in p:
        sentence_words.remove(word)
        
sentence_words
print("{0:20}{1:20}".format("Word","Lemma"))
for word in sentence_words:
    print("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word,pos="v")))
    