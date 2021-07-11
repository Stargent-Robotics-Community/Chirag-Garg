import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
r=sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate') 
engine.setProperty('rate', 135) 
val=input("Enter your name"+"\n")
engine.say("Hello"+val+ "how can i help you")
engine.runAndWait()

with sr.Microphone() as Source:
 print("ask anything... :")
 audio = r.listen(Source)
 ans = r.recognize_google(audio)
 val1=ans.lower()
 print("you said "+val1)
 try:
  if val1 == "hello":
   print("Rio: hello"+val)
   engine.say("how can I help you ?")
   engine.runAndWait()

  elif val1 =="who created you":
   print("Rio: I an created by Chirag Garg")
   engine.say("I an created by Chirag Garg")
   engine.runAndWait()

  elif val1 == "introduce yourself":
   print("Rio: MY name is Rio. I have been created by Chirag Garg and I am here to help you.\n")
   engine.say("MY name is Rio. I have been created by Chirag Garg and I am here to help you")
   engine.runAndWait()

  elif val1 == "tell me quote for the day":
   print("Rio:A motivatonal quote for you")
   engine.say("Success is a journey not the destination")
   engine.runAndWait()

  elif val1 == "tell me a joke":
   print("Rio : The world tongue-twister champion just got arrested. I hear they're gonna give him a really tough sentence.")
   engine.say("The world tongue-twister champion just got arrested. I hear they're gonna give him a really tough sentence.")
   engine.runAndWait()

  elif val1 == "what time is it":
   print("Rio: time is")
   sTime = datetime.datetime.now().strftime("%H:%M:%S")
   engine.say(f"The current time is {sTime}")
   engine.runAndWait()

  elif val1=="open youtube":
   engine.say("wait a second i am opening youtube")
   webbrowser.open("youtube.com")
   engine.runAndWait()

  elif val1=="open google":
   print("opening google")
   engine.say("wait a second i am opening google")
   webbrowser.open("google.com")
   engine.runAndWait()

  elif val1=="suggest me series":
   print("you can watch Dark. It is a German science fiction thriller")
   engine.say("you can watch Dark. It is a German science fiction thriller")
   engine.runAndWait()

  elif val1 == "thanks for helping me":
   print("Rio: It's my pleasure")
   engine.say("It's my pleasure, Have a nice day")
   engine.runAndWait()

 except:
  engine.say("soory, could not recognise your voice")
  print(": sorry try again")

