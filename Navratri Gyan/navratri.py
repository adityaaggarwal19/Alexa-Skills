def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()

def onIntent(intentRequest, session):
             
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']
    if intentName == "NavratriMazaa":
        return nav_fact(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello"
    speechOutput =  "Hello , Welcome to Navratri Gyan! " \
                    "You can know interesting facts about navratri like by saying Tell me about navratri! How can I help?"
    repromptText =  "You can know interesting facts about navratri like by saying Tell me about navratri! Hoe can I help?"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def nav_fact(intent, session):
    import random
    index = random.randint(0,len(nav)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "One of the interesting fact related to navratri is " + nav[index] 
    repromptText = "You can know interesting facts about navratri like by saying Tell me about navratri"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using Navrati Gyan Alexa Skills Kit. " \
                    "Talk to you later" \
                    "Have a great time! " 
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }


def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }



nav = [ "Navratri festival is celebrated Five Times in a year, i.e. Sharad Navratri, Chaitra Navratri, Ashada Navratri, Paush Navratri and Magh Navratri.",
        "Navratri Dates have been set according to Hindu Lunar Calendar.",
        "The most popular Navratri is Sharad Navratri which is celebrated in the month of Ashwin (September or October). Sharad Navratri is also known as Maha Navratri.",
        "In Tamil Nadu, Navratri is known as Golu.",
        "Nine incarnations of goddess Shakti are worshipped during Navratri. Nine goddess names are, Durga, Bhadrakali, Jagadamba, Annapurna, Sarvamangala, Bhairavi, Chandika, Lalita, Bhavani, and Mookambika.",
        "In Sanskrit language, the meaning of Navratri is Nav means NINE and Ratri means NIGHT.",
        "Other than Goddess Durga, another legend of Navratri festival is Lord Rama who killed demon Ravana.",
        "Other festival linked with Navratri festival are Rama Navami and Dussehra. On the ninth day of Chaitra Navratri, Rama navami is celebrated while after the end of nine days of Sharad Navratri Vijayadashmi (Dussehra) is celebrated.",
        "During Navratri, in West Bengal, Durga Puja is a famous ritual, in Karnataka it is a Royal Festival while Mumbai and Gujarat are known for traditional dance forms of Dandiya and Garba.",
        "The months of celebration include March/April, June/July, September/October, December/January and January/February.",
        "Navratri also celebrates the welcoming of Spring and Autumn.",
        "Shakti or feminine power is celebrated or worshiped during the sacred time of Navratri. This includes, but is not limited to major Hindu goddesses, such as Durga and Kali.",
        "The end of Navratri, or the tenth day, marks Dusshera. Dusshera is celebrated as the day Lord Rama defeated the demon King Ravan in Lanka, which is described in detail in the holy Hindu epic, Ramayana.",
        "The tenth day is celebrated around the globe by setting extremely large “Ravanas” on fire, representing the conquering of good over evil.",
        "According to the epic, following this victory Lord Rama, Sita, Lakshman as well as Lord Hanuman traveled back to their kingdom of Ayodhya.”,"
        "Diwali is celebrated twenty days after, as the day Lord Rama returns to Ayodhya as the king.",
        "Diwali is known as the festival of lights, signified through diyas, which were lit to guide Lord Rama’s back to his kingdom, after  14 years of exile.",
        "Gujrat and Mumbai are especially known for their extravagant garba celebrations every night during the nine days of Navratri.",
        "In West Bengal, India, an elaborate Durga Puja is also celebrated during this time. Images of Durga slaying the demon buffalo Mahishasura are built and displayed in temples. They are worshiped for five days, and on the fifth day, the idols are then placed into the river. The Durga Puja performed during Navratri is the biggest festival of the year in Bengal."
        ]