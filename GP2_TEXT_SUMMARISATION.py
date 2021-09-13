#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing model and tokenizer
from transformers import GPT2Tokenizer,GPT2LMHeadModel

# Instantiating the model and tokenizer with gpt-2
tokenizer=GPT2Tokenizer.from_pretrained('gpt2')
model=GPT2LMHeadModel.from_pretrained('gpt2')

original_text = 'published by cambridge university press and cambridge assessment english this recording is copyright test this is the belts listening test you will hear a number of different recordings and you will have to answer questions on what you hear there will be time for you to read me instructions and questions and you will have a chance to check your work all the recordings will be played once only the test is in parts at the end of the test you will be given minutes to transfer your answers to the answer sheet not turn to part part you will hear a woman showing a friend to get information about a job agency first you have some time to look at questions to now listen carefully and answer questions to hello william this is amber you said to phone if i wanted to get more information about the job agency you mentioned is now a good time hi amber yes fine so the agency i was talking about is called bankside are based in docklands i can tell you the address now eastside ok thanks so is there anyone in particular i should speak to you they are the agent i always deal with his cold beck james let me write that down beck james j a m i e s o n do you have her direct line yes its in my contacts somewhere right here we are i would not call her until the afternoon if i were you she is always really busy in the morning trying to fill last minute vacancies is really helpful and friendly so I am sure it would be worth getting in touch with her for an informal chat its mainly clerical and admin jobs they deal with is not it that is right i know you are hoping to find a full time job in a media eventually beck mostly recruits temporary staff for the finance sector which will look good on your cv and generally pays better too yeah I am just a bit worried because i do not have much office experience they will probably start you as a receptionist or something like that so what is important for that kind of job is not so much having business skills or knowing lots of different computer systems its communication that really matters so you would be fine though can you pick up office girls really quickly on the job its not that complicated ok good so how long do people generally need temporary staff for it would be great if i could get something lasting at least a month that should not be too difficult but you are more likely to be offered something for a week at first which might get extend its unusual to be sent somewhere for just a day or two I have heard the pay is not too bad better than working in a shop or a restaurant no yes definitely the hourly rate is about £ if you are lucky that is pretty good i was only expecting to get or pounds an hour before you hear the rest of the conversation you have some time to look at questions to listen and answer questions to do you want me to tell you anything about the registration process yes please i know you have to have an interview the interview usually takes about an hour and you should arrange that about a week in advance i suppose i should dress shortly if its for office work i can probably borrow a suit from mum good idea its better to look too smart than too casual will i need to bring copies of my exam certificates or anything like that no they do not need to see those i do not think what about my passport so yes they will ask to see that i would not get stressed about the interview there its just a chance for them to build a relationship with you so they can try and mate job which you will like so there are questions about personality but they always ask candidate le basic ones and they probably will not ask anything too difficult like what your plans are for the few hope not anyway there are lots of benefits to using an agency example the interview will be useful because they give you feedback on your performance so you can improve next time and ill have access to jump switch on advertised exactly most temporary jobs are not advertised and i expect finding a temporary job this way takes a lot less time its much easier than ringing up individual companies yes indeed well i think I have that is the end of part one you now have minute to check your answers to part'
# Encoding text to get input ids & pass them to model.generate()
inputs=tokenizer.batch_encode_plus([original_text],return_tensors='pt',max_length=512)
summary_ids=model.generate(inputs['input_ids'],early_stopping=True)


# In[2]:



GPT_summary=tokenizer.decode(summary_ids[0],skip_special_tokens=True)
print(GPT_summary)


# In[ ]:




