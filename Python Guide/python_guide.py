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
    if intentName == "PythonGuide":
        return py_fact(intent, session)
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
    speechOutput =  "<audio src='soundbank://soundlibrary/impacts/amzn_sfx_fireworks_firecrackers_01'/>"\
                    "Hello , Welcome to Python Guide! " \
                    "You can know interesting facts about python like by saying Tell me about python! How can I help?"
    repromptText =  "You can know interesting facts about python like by saying Tell me about python! How can I help?"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def py_fact(intent, session):
    import random
    index = random.randint(0,len(py)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "One of the interesting fact related to python is " + py[index] 
    repromptText = "You can know interesting facts about python like by saying Tell me about python"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using Python Guide Alexa Skills Kit. " \
                    "Talk to you later" \
                    "Have a great time! " 
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" + output + "</speak>"
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



py = ["Python was named after the comedy troupe Monty Python. That is why you will often see spam and eggs used as variables in examples (a little tip of the hat to Monty Python’s Flying Circus)",
        "Python was created in 1991 by Guido Van Rossum",
        "There are Java and C variants of Python called JPython and CPython",
        "Python is an interpretive language, meaning you don’t need to compile it. This is great for making programs on the fly, but does make the code rather slow compared to compiled languages",
        "Python is part of the open source community, meaning plenty of independent programmers are out there building libraries and adding functionality to Python.",
        "It is one of the official languages at Google",
        "One can use an else clause with a for loop in Python. It’s a special type of syntax that executes only if the for loop exits naturally, without any break statements. ",
        "In Python, everything is done by reference. It doesn’t support pointers.",
        "Python’s special Slice Operator. It is a way to get items from lists, as well as change them."
        ]