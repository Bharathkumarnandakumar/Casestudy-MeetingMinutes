#!/usr/bin/env python
# coding: utf-8

# In[1]:



# In[42]:


#import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable

with sr.AudioFile("C:/Users/bhara/Downloads/IELTS15_test1_audio1.wav") as source:
    
    audio_text = r.listen(source)
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print(text)
     
    except:
         print('Sorry.. run again...')


# In[48]:


# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

# create a speech recognition object
r = sr.Recognizer()

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text


# In[2]:


data=get_large_audio_transcription("C:/Users/bhara/Downloads/IELTS15_test1_audio1.wav")


# In[3]:


def preprocessing(data):
    import json 
    text=str(data)
    
    # Normalization
    # converting the lower case 
    text1 = text.lower()
    

# removing numbers 
    import re 
    text2 = re.sub(r'\d+','', text1)
    

# remove punctuation in this case only fullstop using maketrans
#  the built-in functions provided in the String class to strip punctuation from a string in Python.
# str.maketrans creates a translation table containing the mapping between two characters.
# In this case, we want to remove all the punctuations, hence str.maketrans('', '', string.punctuation) creates mapping from empty string to empty string, and punctuations to None.
    import string 
# The translate method applies these mappings to the given string thereby removing the punctuations.
    text3 = text2.translate(str.maketrans("","",string.punctuation))
    

# remove whitespaces To remove leading and ending spaces, you can use the strip() function
    text4 = text3.strip()
    

# using contractions by dropping letters and replacing them by apostrophe.
#!pip install contractions

    import contractions

    expanded_words = []
    for word in text4.split():
        expanded_words.append(contractions.fix(word))
    text5 = ' '.join(expanded_words)
  

    import nltk 
    nltk.download('punkt')

# the process of splitting the given text into smaller pieces called tokens. Words, numbers, 
# punctuation marks, 
# and others can be considered as tokens

    import nltk 
    from nltk.tokenize import sent_tokenize, word_tokenize
    sent_token = sent_tokenize(text5)
    sent_token

    word_token = word_tokenize(text5)
    word_token

# for stop words importing libraries
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    import nltk
    nltk.download('stopwords')

# removal of stopwords 
# A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine 
# has been programmed to ignore, both when indexing entries for searching and 
# when retrieving them as the result of a search query. 

    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text5)
    text6 = [i for i in tokens if not i in stop_words]
    

# remove parse terms and particular words 
# Stemming and Lemmatization
# Stemming is a process of reducing the words to its original/base/root form 
# import libraries for stemming 
    from nltk.stem import PorterStemmer
    from nltk.tokenize import word_tokenize

# The Porter stemming algorithm (or 'Porter stemmer') is a process for removing 
# the commoner morphological and inflexional endings from words in English. 
# Its main use is as part of a term normalisation process that is 
# usually done when setting up Information Retrieval systems.
    stemmer = PorterStemmer()
    text7 = word_tokenize(text5)
    

# Lemmatization 
# is to reduce inflectional forms to a common base form. As opposed to stemming, lemmatization does not simply chop off inflections.
# Instead it uses lexical knowledge bases to get the correct base forms of words.
# import libraries
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize
    import nltk
    nltk.download('wordnet')

# creating an object for lemmatization 
    lemmatizer = WordNetLemmatizer()
    text8 = word_tokenize(text5)
    

# spelling correction 
#!pip install textblob

   

    from textblob import TextBlob
    text9 = TextBlob(text5)
    

    from autocorrect import Speller
    check=Speller(lang='en')  
    print(check(str(text9))) # 'does this sentence have misspelled words?'


# In[4]:


preprocessed_data=preprocessing(data)


# In[5]:



import pymongo
from pymongo import MongoClient


client = pymongo.MongoClient("mongodb+srv://bharath_23:nanda8189N23@cluster0.l5wpk.mongodb.net/test?retryWrites=true&w=majority")


# In[6]:



# In[9]:


mydb = client["casestudytwo"]
colec = mydb["discussions"]



# In[7]:



doc = {"file_name":preprocessed_data }
colec.insert_one(doc)


# In[8]:




xa = colec.find() 


# In[9]:



for data in xa: 
    print(data)


# In[ ]:




