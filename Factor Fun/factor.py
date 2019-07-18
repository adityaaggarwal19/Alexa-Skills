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
    if intentName == "whatisnumbergame":
        return factor(intent, session)
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
    speechOutput =  "Hello , Welcome to factors fun! " \
                    "You can know interesting facts about numbers by saying Tell me number game"
    repromptText =  "You can know interesting facts about numbers by saying Tell me number game"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def factor(intent, session):
    import random
    index = random.randint(0,len(prime)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Factors fun that is actually facts obout factors is that " + prime[index] 
    repromptText = "You can know interesting facts about numbers by saying Tell me number game"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using factors fun Alexa Skills Kit. " \
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



prime = [ "Factors of a number N refers to all the numbers which divide N completely. These are also called divisors of a number." ,
          "Factors are what we can multiply to get the number" ,
          "Multiples are what we get after multiplying the number by an integer (not a fraction)",
          "Factors are the numbers we can multiply together to get another number" ,
          "A number can have many factors" ,
          "Multiplying negatives makes a positive, −1, −2, −3, −4, −6 and −12 are also factors of 12." ,
          "Factors of 12 are 1,2,3,4,6,12.",
          "A multiple is the result of multiplying a number by an integer (not a fraction)." ,
          "The terms factor and multiple are sometimes confused with each other. Factors of 15 include 3 and 5; multiples of 15 include 30, 45, 60 (and more)." ,
          "To factor a number is to express it as a product of (other) whole numbers, called its factors. For example, we can factor 12 as 3 x 4, or as 2 x 6, or as 2 x 2 x 3. So 2, 3, 4, and 6 are all factors of 12." ,
          "Zero is the only number that can't be represented in Roman numerals.",
          "A factor of a number -- let's name that number N -- is a number that can be multiplied by something to make N as a product." ,
          "Another way of saying it: a number's factors are divisors of that number; that is, they can divide that number without leaving a remainder." ,
          "The factors of a number include the number, itself, and 1. But these are pretty trivial factors, and so when we talk about factoring a number, we don't generally include factorizations that include 1 or the number itself." ,
          "In the context of numbers, the terms factor (and multiple and divisibility) are used only in connection with whole numbers. So, for example, even though 12 can be expressed as a product using fractions -- for example,  or -- these are not factorizations of 12.",
          "Prime numbers have two factors, themselves and 1, but those are the trivial factors that every number has. Because they cannot be factored in any other way, we say that they cannot be factored. For example, 7 ",
          "Composite numbers (counting numbers that are neither prime nor 1) can often be factored (expressed as a product of whole numbers) in more than one way. For example, 12 can be factored as 3 x 4, or as 2 x 6, or as 2 x 2 x 3. Not all composite numbers can be factored in more than one way, though. For example, 25 can be factored only as 5 x 5.",
          "The order in which numbers are listed in a factorization does not matter: 3 x 4 and 4 x 3 are the same factorization of 12.",
          "A prime factor of a number is just a factor of that number that is also prime. So, 12 has six factors -- 1, 2, 3, 4, 6, and 12 -- but only two of them (2 and 3) are prime, so it has only two prime factors.",
          "The prime factorization of a number is a factorization -- a way of expressing that number as a product -- consisting only of primes.",
          "So, 12 can be expressed as a product many ways -- 1 x 2 x 2 x 3, or 3 x 4, 2 x 2 x 3, or or 2 x 6 -- but only one of those consists solely of primes: 2 x 2 x 3." 
        ]