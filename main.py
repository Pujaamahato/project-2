#RULE BASED AI CHATBOT
import datetime
import time
name=input("Welcome!!,enter your name:")
presenthour= datetime.datetime.now().hour
if 5<= presenthour<=11:
       print(f"good morning!!{name}")
elif 11<= presenthour<=17:
        print(f"good afternoon!!{name}")
elif 17<= presenthour<=20:
         print(f"good evening!!{name}")
else:
      print(f"good night!!{name}")



print("Namaste!! Welcome to Rule based  AI Chatbot")
print("You can ask me basic question , Type bye to exit from the chatbot")
#chatbot memory creation {dictonary of response}


responses={
      "hello":"Hi,Welcome!! how can i help you",
       "how are you":"I am very fine,Thank You",
       "who are you":"I am Smart AI Chatbot",
       "motivate me":"Keep going!! Every Bugs of your projects makes you a better developer.",
       "functions":"i am not able to tell that yet!!, soon i learned about that",
        "happy":"Great to hear that!!",
        "thank you":"you're welcome! Happy to Help",
        "bye":"Goodbye! See you again Soon"
}
# method function to get response chat
def getresponseBot(userquestion):
    userquestion=userquestion.lower()
    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]
    return "I am not able to tell that yet, I am learn that soon" 
while True:
    userInput= input("Please ask your question:")
    reply= getresponseBot(userInput)
    print("Bot Response:",reply)

    if"bye"in userInput.lower():
        break