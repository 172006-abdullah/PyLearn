import pyttsx3
engine= pyttsx3.init()
rate = engine.getProperty('rate')  
print (rate)                        
engine.setProperty('rate', 110)     
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[1].id)  

engine.say('''
Abdullah abu ha 
abdullah hassan ka abu ha 
abdullah eesa ka abu ha 
abdullah k teen betay hain 


''')
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        # printing current voice rate
# engine.setProperty('rate', 100)     # setting up new voice rate


# voices = engine.getProperty('voices')       # getting details of current voice
# engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female


engine.runAndWait()