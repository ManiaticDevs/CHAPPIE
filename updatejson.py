import json
from newspaper import Article
import nltk
nltk.download('punkt', quiet=True)

with open("intents.json") as file:
    data = json.load(file)

#-------------------------------------GREETINGS--------------------------------#
U1 = Article('https://chappie-webpages.werdimduly.repl.co/greetings/user/')
U1.download()
U1.parse()
U1.nlp()
corpusU1 = U1.text
textU1 = corpusU1
sentence_listU1 = nltk.sent_tokenize(textU1)

R1 = Article('https://chappie-webpages.werdimduly.repl.co/greetings/chappie/')
R1.download()
R1.parse()
R1.nlp()
corpusR1 = R1.text
textR1 = corpusR1
sentence_listR1 = nltk.sent_tokenize(textR1)

#-------------------------------------GOODBYE----------------------------------#
U2 = Article('https://chappie-webpages.werdimduly.repl.co/goodbye/user/')
U2.download()
U2.parse()
U2.nlp()
corpusU2 = U2.text
textU2 = corpusU2
sentence_listU2 = nltk.sent_tokenize(textU2)

R2 = Article('https://chappie-webpages.werdimduly.repl.co/goodbye/chappie/')
R2.download()
R2.parse()
R2.nlp()
corpusR2 = R2.text
textR2 = corpusR2
sentence_listR2 = nltk.sent_tokenize(textR2)

#-------------------------------------THANKS-----------------------------------#
U3 = Article('https://chappie-webpages.werdimduly.repl.co/thanks/user/')
U3.download()
U3.parse()
U3.nlp()
corpusU3 = U3.text
textU3 = corpusU3
sentence_listU3 = nltk.sent_tokenize(textU3)

R3 = Article('https://chappie-webpages.werdimduly.repl.co/thanks/chappie/')
R3.download()
R3.parse()
R3.nlp()
corpusR3 = R3.text
textR3 = corpusR3
sentence_listR3 = nltk.sent_tokenize(textR3)

#-------------------------------------ABOUT------------------------------------#
U4 = Article('https://chappie-webpages.werdimduly.repl.co/about/user/')
U4.download()
U4.parse()
U4.nlp()
corpusU4 = U4.text
textU4 = corpusU4
sentence_listU4 = nltk.sent_tokenize(textU4)

R4 = Article('https://chappie-webpages.werdimduly.repl.co/about/chappie/')
R4.download()
R4.parse()
R4.nlp()
corpusR4 = R4.text
textR4 = corpusR4
sentence_listR4 = nltk.sent_tokenize(textR4)
#--------------------------------------UPDATE----------------------------------#
intents= []

data['intents'][0]['patterns'] = sentence_listU1 #GREETINGS
data['intents'][0]['responses'] = sentence_listR1
data['intents'][1]['patterns'] = sentence_listU2 #GOODBYE
data['intents'][1]['responses'] = sentence_listR2
data['intents'][2]['patterns'] = sentence_listU3 #THANKS
data['intents'][2]['responses'] = sentence_listR3
data['intents'][3]['patterns'] = sentence_listU4 #ABOUT
data['intents'][3]['responses'] = sentence_listR4
#data['intents'][4]['patterns'] = sentence_listU5 #
#data['intents'][4]['responses'] = sentence_listR5

with open('intents.json', 'w') as file:
    json.dump(data, file, indent = 4)
