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
    if intentName == "SocialMediaFact":
        return social_media(intent, session)
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
    speechOutput =  "Hello , Welcome to Social Media Fun! " \
                    "You can know interesting facts about scoial media like by saying Tell me social media facts! How can I help?"
    repromptText =  "You can know interesting facts about social media like by saying Tell me social media facts! How can I help?"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def social_media(intent, session):
    import random
    index = random.randint(0,len(social)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "One of the interesting fact related to social media is " + social[index] 
    repromptText = "You can know interesting facts about social media like by saying Tell me social media facts"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using social media facts Alexa Skills Kit. " \
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



social = [   "For context, as of April 2018, total worldwide population is 7.6 billion",
            "The internet has 4.2 billion users",
            "There are 3.03 billion active social media users",
            "On average, people have 5.54 social media accounts",
            "The average daily time spent on social is 116 minutes a day",
            "91% of retail brands use 2 or more social media channels",
            "81% of all small and medium businesses use some kind of social platform",
            "Internet users have an average of 7.6 social media accounts",
            "Social media users grew by 121 million between Q2 2017 and Q3 2017.",
            "That works out at a new social media user every 15 seconds.",
            "Facebook Messenger and Whatsapp handle 60 billion messages a day",
            "Social networks earned an estimated $8.3 billion from advertising in 2015",
            "$40bn was spent on social network advertising in 2016",
            "38% of organizations plan to spend more than 20% of their total advertising budgets on social media channels in 2015, up from 13% a year ago",
            "Only 20 Fortune 500 companies actually engage with their customers on Facebook, while 83% have a presence on Twitter",
            "People aged 55-64 are more than twice as likely to engage with branded content than those 28 or younger",
            "96% of the people that discuss brands online do not follow those brands’ owned profiles",
            "78 percent of people who complain to a brand via Twitter expect a response within an hour",
            "On WordPress alone, 91.8 million blog posts are published every month",
            "A 2011 study by AOL/Nielsen showed that 27 million pieces of content were shared every day, and today 3.2 billion images are shared each day",
            "The top 3 content marketing tactics are social media content (83%), blogs (80%), and email newsletters (77%)",
            "89% of B2B marketers use content marketing strategies",
            "Facebook now sees 8 billion average daily video views from 500 million users",
            "Snapchat users also sees 8 billion average daily video views",
            "US adults spend an average of 1 hour, 16 minutes each day watching video on digital devices",
            "Also in the US, there were 175.4m people watching digital video content",
            "78% of people watch online videos every week, 55% watch every day",
            "It’s estimated that video will account for 74% of all online traffic in 2017",
            "Google processes 100 billion searches a month",
            "That’s an average of 40,000 search queries every second",
            "91.47% of all internet searches are carried out by Google",
            "Those searches are carried out by 1.17 billion unique users",
            "Every day, 15% of that day’s queries have never been asked before",
            "Google has answered 450 billion unique queries since 2003",
            "60% of Google’s searches come from mobile devices",
            "By 2014, Google had indexed over 130,000,000,000,000 (130 trillion) web pages",
            "To carry out all these searches, Google’s data centre uses 0.01% of worldwide electricity, although it hopes to cut its energy use by 15% using AI",
            "300 hours of video are uploaded to Youtube every minute"
        ]