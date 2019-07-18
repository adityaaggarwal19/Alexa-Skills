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
    if intentName == "PlantFactIntent":
        return plant_fact(intent, session)
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
    speechOutput =  "Hello , Welcome to Green Facts! " \
                    "You can know interesting facts about plants like by saying Tell me plant facts! How can I help?"
    repromptText =  "You can know interesting facts about plants like by saying Tell me plant facts! Hoe can I help?"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def plant_fact(intent, session):
    import random
    index = random.randint(0,len(green)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "One of the interesting fact related to plants is " + green[index] 
    repromptText = "You can know interesting facts about plants like by saying Tell me plant fact"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using green facts Alexa Skills Kit. " \
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



green = [   "An average size tree can provide enough wood to make 170,100 pencils!",
            "The first type of aspirin, painkiller and fever reducer came from the tree bark of a willow tree!",
            "85% of plant life is found in the ocean!",
            "Bananas contain a natural chemical which can make people feel happy!",
            "Brazil is named after a tree!",
            "The Amazon rainforest produces half the world’s oxygen supply!",
            "Cricket bats are made of a tree called Willow and baseball bats are made out of the wood of Hickory tree!",
            "Dendrochronology is the science of calculating a tree’s age by its rings!",
            "Caffeine serves the function of a pesticide in a coffee plant! ",
            "Apple is 25% air, that is why it floats on water!",
            "Peaches, Pears, apricots, quinces, strawberries, and apples are members of the rose family!",
            "Apple, potatoes and onions have the same taste, to test this eat them with your nose closed!",
            "The tears during cutting an onion are caused by sulfuric acid present in them!",
            "The tallest tree ever was an Australian eucalyptus – In 1872 it was measured at 435 feet tall!",
            "The first potatoes were cultivated in Peru about 7,000 years ago!",
            "The evaporation from a large oak or beech tree is from ten to twenty-five gallons in twenty-four hours!",
            "Strawberry is the only fruit that bears its seeds on the outside. The average strawberry has 200 seeds!",
            "Leaving the skin on potatoes while cooking is healthier as all the vitamins are in the skin!",
            "Around 2000 different types of plants are used by humans to make food!",
            "Small pockets of air inside cranberries cause them to bounce and float in water!",
            "Bamboo is the fastest-growing woody plant in the world; it can grow 35 inches in a single day!",
            "A sunflower looks like one large flower, but each head is composed of hundreds of tiny flowers called florets, which ripen to become the seeds!",
            "Cabbage has 91% water content!",
            "Banana is an Arabic word for fingers!",
            "The California redwood (coast redwood and giant sequoia) are the tallest and largest living organism in the world!"
        ]