import os
import sys
import time
import warnings
import logging

warnings.filterwarnings("ignore")
warnings.simplefilter('ignore')
#warnings.filterwarnings("ignore", category=NotFound)

def progress_bar(current, total, bar_length=20):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending)

userASK = input("Have you already done the setup for chappie? (y or n, yes or no) : ")

userinp = userASK.lower()

isSetup = False

if userinp == 'no':
    isSetup = False
elif userinp == 'yes':
    isSetup = True
elif userinp == 'y':
    isSetup = True
elif userinp == 'n':
    isSetup = False

if isSetup == False:
    os.system("cls")
    print("Setting up Python for Chappie (dependencies may not be on user's computer)")
    progress_bar(0, 100)
    os.system("python3 get_pip.py --user --no-warn-script-location --disable-pip-version-check>nul")
    progress_bar(25, 100)
    os.system("pip install -r requirements.txt --user --no-warn-script-location --disable-pip-version-check>null")
    progress_bar(50, 100)
    os.system("python3 updatejson.py && python3 train.py>nul")
    progress_bar(100, 100)
    time.sleep(1)
    os.system("cls")
    os.system("python3 updatejson.py && python3 train.py>nul")

userASK = input("Do you want to update the json file for chappie? (y or n, yes or no) : ")

userinp = userASK.lower()

isJSON = False

if userinp == 'no':
    isJSON = False
elif userinp == 'yes':
    isJSON = True
elif userinp == 'y':
    isJSON = True
elif userinp == 'n':
    isJSON = False

if isJSON == True:
    progress_bar(0, 100)
    os.system("py updatejson.py>nul")
    progress_bar(50, 100)
    os.system("py train.py>nul")
    progress_bar(100, 100)
    time.sleep(2)

import json
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

import colorama
colorama.init()
from colorama import Fore, Style, Back

import random
import pickle

with open("intents.json") as file:
    data = json.load(file)

#def writeinfile(n, filename):
    #text_file = open(filename, "w")
    #y = text_file.write(n)
    #text_file.close()

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
            os.system("cls")
            break

        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]), truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])
        print(" ", end="\r")
        for i in data['intents']:
            if i['tag'] == tag:

               print(Fore.GREEN + "Chappie :" + Style.RESET_ALL, np.random.choice(i['responses']))
            #else :
               #print(Fore.GREEN + "Chappie :" + Style.RESET_ALL, "I'm sorry I didn't get that.")
        # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,random.choice(responses))

chat()
