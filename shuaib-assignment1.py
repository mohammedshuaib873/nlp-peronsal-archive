#

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example_sent = "can nltk remove the stopwords from this sample sentence-my name is shuaib"
stop_words = set(stopwords.words(example_sent)
word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w in stopwords]
filtered_sentence = []
for w in word_tokens:
      if w in word_tokens:
          filtered_sentence.append(w)
print(word_tokens)
print(filtered_sentence)