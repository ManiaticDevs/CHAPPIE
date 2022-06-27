import os
import sys
import time
import warnings
import logging

import colorama 
colorama.init()
from colorama import Fore, Style, Back

print(Fore.RED + "THE PROCESS YOU ARE ABOUT TO SEE IS THE TRAINING AND UPDATING PROCESS FOR CHAPPIE" + Style.RESET_ALL)

time.sleep(5)

warnings.filterwarnings("ignore")
warnings.simplefilter('ignore')
#warnings.filterwarnings("ignore", category=NotFound)

def progress_bar(current, total, bar_length=20):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending)

print("Setting up Python for Chappie (dependencies may not be on user's computer)")
progress_bar(00, 100)
os.system("py get_pip.py --user --no-warn-script-location --disable-pip-version-check>nul")
os.system("py updatejson.py && py train.py>nul")
progress_bar(50, 100)
os.system("pip install -r requirements.txt --user --no-warn-script-location --disable-pip-version-check>null")
progress_bar(100, 100)
time.sleep(1)
os.system("cls")

import json
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder



import random
import pickle

with open("intents.json") as file:
    data = json.load(file)


def chat():
    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20
    os.system('cls')
    print(Fore.YELLOW + "Start messaging with Chappie (type quit to stop)!" + Style.RESET_ALL)
    print(Fore.RED + "PROPERTY OF MANIATICDEVS" + Style.RESET_ALL)
    print(Fore.GREEN + "Chappie :" + Style.RESET_ALL + " Hello! I'm Chappie! Note that my responses are limited!")
    

    while True:

        print(Fore.LIGHTBLUE_EX + "User : " + Style.RESET_ALL, end="")
        inp = input()
        if inp.lower() == "quit":
            break

        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]), truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        for i in data['intents']:
            if i['tag'] == tag:
               print(Fore.GREEN + "Chappie :" + Style.RESET_ALL, np.random.choice(i['responses']))
            #else :
               #print(Fore.GREEN + "Chappie :" + Style.RESET_ALL, "I'm sorry I didn't get that.")
        # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,random.choice(responses))
        
chat()
