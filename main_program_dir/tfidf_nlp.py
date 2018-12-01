import nltk, math
import re, string
from nltk import tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.snowball import SnowballStemmer

def tokenize_stem(text):
    tokens = [word for sentence in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sentence)]
    filtered_token = []

    for token in tokens:
        if(re.search('[a-zA-Z]', token)):
            filtered_token.append(token)
    
    stemmer = SnowballStemmer('english')
    stems = [stemmer.stem(t) for t in filtered_token]
    return stems

token_d = ["""Nature refers to the natural resources and natural surroundings. The life species in nature are
 interrelated and create balance in nature. They form a natural food chain through which energy is passed
 to all the species. The series of organisms in which each organism feeds on the one below it in the sequence 
 is called the food chain in natural ecosystem. Food chain includes several plants, organisms, animals and
  other living species. This natural food chain is the source of energy for the forest species. The energy 
  is passed from one creature to the other which helps them grow and survive.
For example in forest deer feeds on the grass and green plants and the tiger feeds on the deer. Plants get
 their energy form sunlight and nutrients from soil. Deer is herbivores animal. Herbivores animals depend
  on plants for energy and are vegetarians. Tiger is carnivorous animal. Carnivorous animals eat herbivores 
  and sometimes other carnivorous for energy. So there is a whole chain that includes plants,
   herbivores, carnivorous and plants consume energy from sunlight. And there are lots of animals that eat
    plants and meat both. These are called omnivorous animals. For instance, black beer is an 
    omnivorous animal. Some omnivorous also eat dead animals and those are called scavengers. Thus, 
    the chain goes on.
All the species on earth are important for the survival of entire series of organisms and to balance the
 natural cycle."""]

# token = open("/home/madhavane/workplace/geek ai-mania tcs/chatbot/bbc/business/001.txt")
# token_d = token.readlines()
# token.close()

tokens = tokenize.sent_tokenize(str(token_d))

# token_d = r"%s"%token_d

tfidf = TfidfVectorizer(tokenize_stem, stop_words='english',decode_error='ignore')
td_matrix = tfidf.fit_transform(token_d)
feature = tfidf.get_feature_names()

# print(td_matrix[0,21])

sent_score = []
for sent in nltk.sent_tokenize(str(token_d)):
    score = 0
    sent_token = tokenize_stem(sent)
    for token in (t for t in sent_token if t in feature):
        score += td_matrix[0,feature.index(token)]
    sent_score.append((score/len(sent_token), sent))

summary_length = int(math.ceil(len(sent_score)/3.5))
sent_score.sort(key=lambda sent:sent[0])
# print(sent_score)

extract = [sents[1] for sents in sent_score[:summary_length]]

# for summary_sent in sent_score[:summary_length]:
#     print(summary_sent[1])

# print(extract)

sort_sum = sorted(extract,key = lambda x:tokens.index(x))

print(sort_sum)

# print("\n",sort_sum)