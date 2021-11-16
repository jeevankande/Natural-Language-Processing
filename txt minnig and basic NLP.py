'''Text Minnig and NLP'''

Sentence = 'We are Learning TextMining'

'TextMining' in Sentence

Sentence.index('Learning')

Sentence.split().index('TextMining')

Sentence.split()[2]

Sentence.split()[2][::-1]

word = Sentence.split()

first_word = word[0]

last_word = word[len(word)-1]

concat_word = first_word + last_word

print(concat_word)

[word[i] for i in range(len(word)) if i%2 == 0]

Sentence[-3:]

Sentence[::-1]

print(' '.join([word[::-1] for word in word]))

#word tokenization
import nltk

from nltk import word_tokenize

nlp_phrase = 'I am learning Natural Lanhuage Processing Fundamental for not only job interview'

print(nlp_phrase)

nltk.pos_tag(nlp_phrase) # Parts of Speech Tagging

#nltk.download('averaged_perceptron_tagger')

nltk.download('stopwords')  # Stop Words from nltk library

from nltk.corpus import stopwords

stop_words = stopwords.words('English')

sentence1 = "I am learning NLP. It is one of the most popular library in Python"

sentence1_words = word_tokenize(sentence1) # Tokenize the sentence

print(sentence1_words)
#nltk.download('punkt')
# Filtering stop words from the input string
sentence_no_stops = ' '.join([word for word in sentence1_words if word not in stop_words]) 
print(sentence_no_stops)

#replace words in string
sentence2 = "I will get MY job before  14-02-2022"

normalized_sentence = sentence2.replace('14-02-2022','31-01-2022')

print(normalized_sentence)

#pip install autocorrect

from autocorrect import Speller

spell = Speller(lang='en')

spell('Natureal') # Correct spelling is printed

sentence3 = word_tokenize("Ntural Luaguage Prcessin dealss with the art of extracting insightes from Natural Languaes")

sentence_corrected = ' '.join([spell(word) for word in sentence3])

#stemming

stemmer = nltk.stem.PorterStemmer()

stemmer.stem("Programming")

stemmer.stem("Jumping")
stemmer.stem("Jumper")

stemmer.stem("battling") # battl - stemming does not look into dictionary words
stemmer.stem("amazing")

# Lemmatization
# Lemmatization looks into dictionary words

#nltk.download('wordnet')

from nltk.stem.wordnet import WordNetLemmatizer

Lemmatization = WordNetLemmatizer()

Lemmatization.lemmatize('Programming')

Lemmatization.lemmatize('Programs')

Lemmatization.lemmatize('battling')

Lemmatization.lemmatize("amazing")

# Chunking (Shallow Parsing) - Identifying named entities
nltk.download('maxent_ne_chunker')
nltk.download('words')

sentence4 = 'We are learning nlp in Python by 360DigiTMG which is based out of India.'
a =nltk.pos_tag(word_tokenize(sentence4))
i = nltk.ne_chunk(a,binary = False)
#i = nltk.ne_chunk(nltk.pos_tag(word_tokenize(sentence4)), binary=True)
[a for a in i if len(a)==1]

[onj for onj in i if len(onj)==1]

#sentence tokenization
from nltk.tokenize import sent_tokenize

sent_tokenize("We are learning NLP in Python. Which enable me to help this society.")

from nltk.wsd import lesk #Word sense disambiguation
#In general, simple_lesk() from pywsd does better than lesk from NLTK

sentence5 = "Keep your savings in the bank"
print(lesk(word_tokenize(sentence1), 'bank'))

sentence6 = "It's so risky to drive over the banks of the river"
print(lesk(word_tokenize(sentence2), 'bank'))

# "bank" as multiple meanings. 
# The definitions for "bank" can be seen here:
from nltk.corpus import wordnet as wn
for ss in wn.synsets('bank'): print(ss, ss.definition())

###################################################################################
'''1.	CC	Coordinating conjunction
2.	CD	Cardinal number
3.	DT	Determiner
4.	EX	Existential there
5.	FW	Foreign word
6.	IN	Preposition or subordinating conjunction
7.	JJ	Adjective
8.	JJR	Adjective, comparative
9.	JJS	Adjective, superlative
10.	LS	List item marker
11.	MD	Modal
12.	NN	Noun, singular or mass
13.	NNS	Noun, plural
14.	NNP	Proper noun, singular
15.	NNPS	Proper noun, plural
16.	PDT	Predeterminer
17.	POS	Possessive ending
18.	PRP	Personal pronoun
19.	PRP$	Possessive pronoun
20.	RB	Adverb
21.	RBR	Adverb, comparative
22.	RBS	Adverb, superlative
23.	RP	Particle
24.	SYM	Symbol
25.	TO	to
26.	UH	Interjection
27.	VB	Verb, base form
28.	VBD	Verb, past tense
29.	VBG	Verb, gerund or present participle
30.	VBN	Verb, past participle
31.	VBP	Verb, non-3rd person singular present
32.	VBZ	Verb, 3rd person singular present
33.	WDT	Wh-determiner
34.	WP	Wh-pronoun
35.	WP$	Possessive wh-pronoun
36.	WRB	Wh-adverb'''
