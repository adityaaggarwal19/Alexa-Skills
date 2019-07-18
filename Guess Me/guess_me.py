from __future__ import print_function
import random
import json

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, card_output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" + output + "</speak>"
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': card_output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# ---------------------------- Data for the skill ------------------------------

ques = [["centenarian","A person who is above hundred years"],
        ["posthumous","A book published after the death of its author"],
        ["anonymous","A book written by an unknown author"],
        ["matinee","A cinema show which is held in the afternoon"],
        ["cosmopolite","A citizen of the world"],
        ["epidemic","A contagious disease which spreads over a huge area"],
        ["soporific","A drug or other substance that induces sleep"],
        ["carnivorous","A flesh eating animal"],
        ["draw","A game in which neither party wins"],
        ["monarchy","A Government by a king or queen"],
        ["autocracy","A Government by one"],
        ["oligarchy","A Government by the few"],
        ["aristocracy","A Government by the Nobles"],
        ["bureaucracy","A Government by the officials"],
        ["democracy","A Government by the people"],
        ["plutocracy","A Government by the rich"],
        ["herbivorous","A grass eating animal"],
        ["illegible","A handwriting that cannot be read"],
        ["amphibian","A land animal that breeds in water"],
        ["autobiography","A life history written by oneself"],
        ["biography","A life history written by somebody else"],
        ["catalogue","A list of books"],
        ["irreparable","A loss or damage that cannot be compensated"],
        ["callous", "A man devoid of kind feeling and sympathy"],
        ["fanatic","A man who has too much enthusiasm for his own religion"],
        ["irritable","A man who is easily irritated"],
        ["germicide","A medicine that kills germs"],
        ["antiseptic","A medicine that prevents decomposing"],
        ["antidote","A medicine to counteract the effect of another medicine"],
        ["bourgeois","A member of the middle class"],
        ["inimitable","A method that cannot be imitated"],
        ["venial","	A pardonable offense"],
        ["arbitrator","	A person appointed by parties to settle the disputes between them"],
        ["fastidious","	A person difficult to please"],
        ["answerable","	A person liable to be called to account for his action"],
        ["parasite","A person supported by another and giving him/her nothing in return"],
        ["egotist",	"A person who always thinks of himself"],
        ["illiterate","	A person who cannot read or write"],
        ["misogynist","A person who hates women"],
        ["misogamist","A person who does not believe in the institution of marriage"]
        ]

ansInfo = ["Government has decided to give special allowances to all the Indian centerarian.",
           "Lt. Colonel Shergil was award posthumous gallanty award.",
           "The word Anonymous is used by the authors to conceal their identity from its readers.",
           "We are planning to go for a matinee show on next friday.",
           "The cosmopolite wandered in almost all the countries of the before finally settling in India.",
           "Epidemic in West Bengal took 7000 lives last year.",
           "Most of the cough syrups are soporific in nature.",
           "Lion is a carnivorous animals.",
           "World Cup Final ended in a draw.",
           "Monarchy is still prevalent in some countries.",
           "Democracy has proved much better than autocracy.",
            "There are very few countries with origarchy form of a country.",
        "aristocracy is still prevalent in some of the european countries.",
        "bureaucracy leds to red tapism thus delays in clearing the project files.",
        "democracy is best defined as government of the people, by the people and for the people.",
        "Plutocracy does not exist in any country of the world now.",
        "Herbivorous animals feed only on the plants and grass.",
        "Most of the doctors have illegible handwritting",
        "A frog is most commonly known amphibian.",
        "Autobiographies of National Leaders have become a precious treasure for their respective countries.",
        "Having a biography has become a trend in the upper class of the society.",
        "Catalogue is very essential to keep track of books in the library.",
        "Loss of life is always irreparable irrespective of any amount of financial help from the government.",
        "His callous behaviour helps him to do justice as a village head.",
        "People of a state should not choose a fanatic person as their Chief Minister.",
        "His irritable nature cost him his job.",
        "This germicide is quite effective for water born germs.",
        "Doctor prescribed me an antiseptic for my ear infection.",
        "Every medicine should have an antidote to negate its side effects.",
        "The young bourgeois had never entered a mall.",
        "The magnificent sheen and richness of the pure gold lacquer are wanting, but in their place we have inimitable tenderness and delicacy.",
        "No body expected such a harsh punishment for a seemingly venial offence.",
        "An arbitrator is the only person who can help to resolve the issue between two waring parties.",
        "I have got a fastidious boss in my new office.",
        "Parents should not be made answerable for the misdeeds of their spoilt children.",
        "Unemployment is just like a parasite on any economy.",
        "It is hard for an egotist to win friends.",
        "Regimental schools impart elementary education to illiterate soldiers.",
        "You cannot expect a miscogynist to marry and lead a peaceful married life.",
        "Present day youth feel proud be called as misogamist."
           ]
hint=["The word starts with a C and synonym is oldster and gloden ager.",
    "The word starts with a P and synonym is postmortem and postobit.",
    "The word starts with an A and synonym is nameless and unacknowledged.",
    "The word starts with a M and synonym is movie and entertainment.",
    "The word starts with a C and synonym is civilian and commoner.",
    "The word starts with an E and synonym is communicable and catching.",
    "The word starts with a S and synonym is narcotic and dull.",
    "The word starts with a C and synonym is flesh eating and predatory.",
    "The word starts with a D and synonym is tie and even steven.",
    "The word starts with a M and synonym is crown and kingdom.",
    "The word starts with an A and synonym is oppression and dictatorship.",
    "The word starts with an O and synonym is totality and fascism.",
    "The word starts with an A and synonym is upper class and elite.",
    "The word starts with a B and synonym is civil services and administration.",
    "The word starts with a D and synonym is representative government and liberal government.",
    "The word starts with a P and synonym is play to crown and put across.",
    "The word starts with a H and synonym is fruitarian and vegan.",
    "The word starts with an I and synonym is indistinct and unclear.",
    "The word starts with an A and synonym is caudate and frog.",
    "The word starts with an A and synonym is self portrayal and personal history.",
    "The word starts with a B and synonym is bio and life story.",
    "The word starts with a C and synonym is archive and bulletin.",
    "The word starts with an I and synonym is hopeless and impossible.",
    "The word starts with a C and synonym is unfeeling and heartless.",
    "The word starts with a F and synonym is addict and freek.",
    "The word starts with an I and synonym is hasty and annoyed.",
    "The word starts with a G and synonym is disinfectant and preventive.",
    "The word starts with an A and synonym is hygienic and germ free.",
    "The word starts with an A and synonym is neutralizer and medicine.",
    "The word starts with a B and synonym is common and traditional.",
    "The word starts with an I and synonym is matchless and unique.",
    "The word starts with a V and synonym is justifiable and forgivable.",
    "The word starts with an A and synonym is judge and fixer.",
    "The word starts with a F and synonym is critical and picky.",
    "The word starts with an A and synonym is accountable and to blame.",
    "The word starts with a P and synonym is dependable and stucker.",
    "The word starts with an E and synonym is braggart and boaster.",
    "The word starts with an I and synonym is unlearned and uneducated.",
    "The word starts with a M and synonym is anti feminist.",
    "The word starts with a M and synonym is unbeliever and pessimist."
    ]

# --------------------------- Global variables ---------------------------------

totalQues = 40
quesInOneSession = 5
maxScore = quesInOneSession

score = 0
currQues = -1
askedQuesCount = 0
askedQues = []
session_attributes = {}
rulecount = 0
quesAnswered = True

# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "<p>Hello! Welcome to one word phrase game! For brief description and rules of the game, just say <emphasis level='moderate'>rules!</emphasis></p> "\
                    "So, Can we find out how well you know english phrases? Say <emphasis level='moderate'>start quiz</emphasis> to get started with the quiz" 
    card_output = "Hello! Welcome to one word phrase game! For brief description and rules of the game, just say rules! "\
                   "So, Can we find out how well you know english phrases? Say start quiz to get started with the quiz"              
    reprompt_text = "Hi! I am waiting! " \
                    "Can we get started? Say begin to get started!" 

    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))

def result():
    
    init = "Awesome! You completed the phrase game! " + " You got " + str(score) + " out of " + str(quesInOneSession) + " correct. "
    if score == quesInOneSession:
        init = init + " Well done! Perfect score! You really know english phrases well! I am impressed! "
    elif score >= (quesInOneSession/1.5)+1:
        init = init + " Nice score! Keep playing, will definitely keep getting better! "
    elif score >= (quesInOneSession/2.5)+1:
        init = init + " Great effort! You can do much better, I believe in you! "
    else:
        init = init + " You can do better! Way to go! Play again, get better! "

    init = init + "  Wanna play again? Just say, Replay! Otherwise, say stop!"
    
    return (init)

def result1():
    
    init = "<audio src='soundbank://soundlibrary/human/amzn_sfx_crowd_applause_05'/>"\
            "<say-as interpret-as=\"interjection\">Awesome.</say-as> You completed the phrase game!<break/> " + " You got " + str(score) + " out of " + str(quesInOneSession) + " correct. "
    if score == quesInOneSession:
        init = init + " <say-as interpret-as=\"interjection\">Well Done. Perfect Score!</say-as> <break/>You really know english phrases well! I am impressed! "
    elif score >= (quesInOneSession/1.5)+1:
        init = init + " Nice score! Keep playing, will definitely keep getting better! "
    elif score >= (quesInOneSession/2.5)+1:
        init = init + " Decent effort! You can do much better, I believe in you! "
    else:
        init = init + " You can do better! <say-as interpret-as=\"interjection\">Way to go.</say-as> <break/> Play again, get better! "

    init = init + " Wanna play again? Just say, Replay! Otherwise, say stop! "
    
    return (init)

def ret_question():

    q = ques[currQues][1] + " . "
    return (q)

def phrase(intent, session):

    global askedQuesCount
    global currQues
    global askedQues
    global quesAnswered

    card_title = "Phrase"

    if askedQuesCount == 0:
        init = "Alright! Let's see how many phrases you can guess. "
    else:
        init = ""

    speech_output = ""
    card_output=""
    reprompt_text = ""
    
    if askedQuesCount == quesInOneSession:
         
                speech_output = result1()
                card_output = result()
                reprompt_text = " Hey! Let's play again! Say Replay to play again. Or Exit to stop playing "
                should_end_session = False

                return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))
            
    if quesAnswered == False:
        card_title = "Alert!"

        speech_output = "<say-as interpret-as=\"interjection\">Uh oh.</say-as> <break/>Answer the last question I asked you."
        card_output = "Answer the last question I asked you."
        reprompt_text = "Hey! I am waiting for your answer. If you missed the question, say repeat question."

        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))
             
    
    askedQuesCount = askedQuesCount+1   
    quesNo = askedQuesCount
    x =  random.randint(0,totalQues-1)
    while x in askedQues:
            x =  random.randint(0,totalQues-1)
        
    askedQues.append(x);
    currQues = x
    
    question = "Question " + str(quesNo) + ".  " + ret_question() 
    
    session_attributes['question'] = ques[x][1]
    
    quesAnswered = False
    ked= True
    
    question1 = "<audio src='soundbank://soundlibrary/musical/amzn_sfx_drum_comedy_02'/> Question " + str(quesNo) + ".  " + ret_question()
    
    speech_output = init+"<break/><emphasis level='moderate'>" + question1+"</emphasis>"
    card_output = init + question
    reprompt_text = "Hey! I am waiting for your answer. If you missed the question, say repeat question."\
                    "If you want hint then say give me hint"

    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))    
    #print(b['response']['outputSpeech']['text'])
    
def get_answer(intent, session):

    global score
    global quesAnswered

    card_title = "Answer"

    if quesAnswered == True:
        speech_output = "<say-as interpret-as=\"interjection\">Haanji.</say-as> What you are trying to pull buddy?<break/> You have already answered the question."
        card_output = "Haanji! What you are trying to pull buddy? You have already answered the question."
        reprompt_text = "You can know more about this question's answer by saying, tell me example, or, you can move to the next question by saying, next question."

        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))    


    if 'value' not in intent['slots']['answer']:
        speech_output = "<say-as interpret-as=\"interjection\">Hello.</say-as>You need to say an answer! Say an answer."
        card_output = "Hello! You need to say an answer! Say an answer."
        reprompt_text = "If you want hint, say hint."

        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))
        
    ans_input = intent['slots']['answer']['value']

    if ans_input.lower() == ques[currQues][0].lower():
        speak = "That is the correct answer!" + " Say next for the next question."
        speak1= "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_positive_response_01'/>"\
                "<say-as interpret-as=\"interjection\">Yay.</say-as> That is the correct answer!" + " Say <emphasis level='moderate'>next</emphasis> for the next question."
        score = score + 1
    else:
        speak = "Oh no! That answer is incorrect. The correct answer is " + ques[currQues][0] + ". Say tell me example to know about the correct answer. " 
        speak1= "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                "<say-as interpret-as=\"interjection\">Oh no.</say-as>That answer is incorrect. <break/> The correct answer is <emphasis level='moderate'>" + ques[currQues][0] + "</emphasis><break/> .Say <emphasis level='moderate'>tell me example</emphasis> to know about the correct answer.  "
    session_attributes['score'] = score
    
    quesAnswered = True
    speech_output = speak1 
    card_output = speak 
    reprompt_text = "You can know more about this question's answer by saying, tell me example. "
    
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))    


def get_next_question(intent, session):

    if quesAnswered == False:
        card_title = "Alert!"

        speech_output = "<say-as interpret-as=\"interjection\">Buddy.</say-as> You haven't answered the question yet.<break/> You can't move to the next question."
        card_output = "Buddy! You haven't answered the question yet. You can't move to the next question."
        reprompt_text = "Hey! I am waiting for your answer. If you missed the question, say repeat question."

        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))
        
    return phrase(intent,session)

def repeat_question(intent, session):

    card_title = "Question"

    if currQues == -1:
        speech_output = "<say-as interpret-as=\"interjection\">Buddy.</say-as>The quiz has not started yet!<break/> Say </emphasis level='moderate'>begin </emphasis>to get started with the quiz"
        card_output = "The quiz has not started yet! Say begin to get started with the quiz"
        reprompt_text = "Say begin to start the quiz"
        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))    
    
    if quesAnswered == True:
        speak = "Your question was. "
        re = "Say, next question, to move to the next question!"
    else:
        speak = "Your question is. "
        re = "Hey, there! I am waiting for your answer."

    speech_output = speak + ret_question()
    card_output = speak + ret_question()
    reprompt_text = re
    
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))    
    
    
def current_score(intent, session):

    card_title = "Score"

    sc = str(score)
    if askedQuesCount == quesInOneSession:
        speak = "Cool! You finished the quiz! Your final score is "+ sc + ". Say, replay to play again."
        speak1= "<say-as interpret-as=\"interjection\">Cool.</say-as> You finished the quiz! <break/> Your final score is <emphasis level='moderate'>"+sc + ".</emphasis><break/> Say,<emphasis level='moderate'>replay </emphasis> to play again."
        re = "Say replay to start the quiz again! Or say exit to exit the game"
    else:
        if quesAnswered == True:
            speak = "Your score is " + sc + " because you have answered " + sc + " correctly, out of " + str(askedQuesCount) + " questions. Say next question for the next question."
            speak1= "Your score is <emphasis level='moderate'>" + sc + " </emphasis>because you have answered " + sc + " correctly, <break/>out of " + str(askedQuesCount) + " questions. Say next question for the next question.."
            re = "Move to the next question by saying, next question."
        else:
            speak = "Your score is " + sc + " because you have answered " + sc + " correctly, out of " + str(askedQuesCount-1) + " questions. Say my answer is your answer to answer the question."
            speak1= "Your score is <emphasis level='moderate'>" + sc + " </emphasis>because you have answered " + sc + " correctly, <break/>out of " + str(askedQuesCount-1) + " questions. Say my answer is your answer to answer the question."
            re = "I am waiting for the answer! Say, repeat question, if you want me to repeat the question."

    speech_output = speak1
    card_output = speak
    reprompt_text = re
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))    

def tell_me_example(intent, session):

    card_title = "Tell Me Example"

    if quesAnswered == False:
        speak1 = "<say-as interpret-as=\"interjection\">Buddy.</say-as></break/>You can't know about the answer yet! <emphasis level='moderate'>Answer the question first.</emphasis>"
        speak = "Buddy, You can't know about the answer yet! Answer the question first. "
        re = "I am waiting for the answer! Say, repeat question, if you want me to repeat the question."
    else:
        speak = ansInfo[currQues] + " . Say begin to continue. "
        speak1 = ansInfo[currQues] + " . Say<emphasis level='moderate'> begin</emphasis> to continue. "
        re = "Move to the next question by saying, next question."

    speech_output = speak1
    card_output = speak
    reprompt_text = re
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))  

def give_me_hint(intent, session):

    card_title = "Give Me Hint"

    if quesAnswered == True:
        speak1 = "<say-as interpret-as=\"interjection\">Buddy.</say-as></break/>You can't hint about the question yet! <emphasis level='moderate'>Answer the question first.</emphasis>"
        speak = "You can't hint about the question yet! Let me ask the question first. "
        re = "I am waiting for asking you the question! Say, next question, if you want me to continue further to next question."
    else:
        speak = hint[currQues] + " . Answer the question now "
        speak1 = hint[currQues] + " .<break time='1s'/> Answer the question now "
        re = "Answer the question by saying, my answer is word."

    speech_output = speak1
    card_output = speak
    reprompt_text = re
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session)) 

def replay_quiz(intent, session):
    
    global score
    global currQues
    global askedQuesCount
    global askedQues
    global quesAnswered
    global quesAsked
    
    score = 0
    currQues = -1
    askedQuesCount = 0
    askedQues = []
    session_attributes = {}
    quesAnswered = True
    
    return phrase(intent, session)    


def no_response():

    card_title = "No!"
    
    speech_output = "<say-as interpret-as=\"interjection\">Sorry Buddy.</say-as></break/> I don't understand!"
    card_output = "Sorry buddy, I don't understand!"
    reprompt_text = "For rules, say rules!"
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))    
        
def yes_response():

    card_title = "Yes!"
    
    speech_output = "<say-as interpret-as=\"interjection\">Well well.</say-as> nice trying but I don't understand!"\
                    " If you want to answer the given question then just say,<emphasis level='moderate'> my answer is word.</emphasis>"
    card_output = "Well well! Nice trying but I don't understand!"\
                " If you want to answer a given question then just say, my answer is word."
    reprompt_text = "For rules, say rules!"
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))    

    
def get_help_response(intent, session):
    
    global rulecount
    
    card_title = "Rules"
    #session_attributes={}
    should_end_session = False
    
    rulecount = rulecount + 1
    if rulecount == 1:
        speech_output = "This is a one word english phrase quiz and the rules are very simple. " \
                        "I will ask you a question. You say one word by saying, my answer is word "\
                        "I will tell you, if you were correct. Move to the next question by saying next. "
        speech_output1 = "This is a one word english phrase quiz and the rules are very simple. <break/>" \
                        "I will ask you a question. You say one word by saying, <emphasis level = 'moderate'> my answer is word </emphasis>"\
                        "<break/>I will tell you, if you were correct. <break/> "\
                        "Move to the next question by saying <emphasis level='moderate' > next. </emphasis>"
        #rulecount=0
    else:
        speech_output = "Hello! Welcome to Guess Me! " \
                        "This is a one word elglish phrase quiz and the rules are very simple. " \
                        "After you start the game, you will be prompted with a question. "\
                        "You have to say one word answer, by saying, my answer is your answer like democracy " \
                        "After you answer the question, I will tell you, whether you were right, or not. Then say, next question, to move to the next question. "\
                        "You can get a question repeated, by saying, Repeat question."\
                        "You can also know more about the answer, of a question, by saying, tell me example. "\
                        "You can also get a hint for the question, by saying, hint "\
                        "You will be asked 5 questions. You will get the final score after the game. To get your score between the game, you can ask, what is my score. "\
                        "To exit the skill, say stop."
        
        speech_output1= "Hello! Welcome to <emphasis level='moderate'>Guess Me!</emphasis> <break/>"\
                        "This is a one word english phrase quiz and the rules are very simple. <break/>" \
                        "After you start the game, you will be prompted with a question. <break/>"\
                        "You have to say one word answer, by saying,<emphasis level = 'moderate'> my answer is your answer like democracy. </emphasis> <break/>" \
                        "After you answer the question, I will tell you, whether you were right, or not. Then say, <emphasis level= 'moderate'> next question</emphasis>, to move to the next question. <break/>"\
                        "You can get a question repeated, by saying, <emphasis level='moderate'> Repeat question</emphasis><break/>"\
                        "You can also know more about the answer, of a question, by saying, <emphasis level='moderate' >tell me example. </emphasis><break/>"\
                        "You can also get a hint for the question, by saying <emphasis level='moderate'> hint.</emphasis>"\
                        "You will be asked <emphasis level='strong'>5 questions</emphasis>. You will get the final score after the game. To get your score between the game, you can ask, <emphasis level = 'moderate' >what is my score.</emphasis> "\
                        "To exit the skill, say stop."
        rulecount = 0                
    #session_attributes['rulecount'] = rulecount
    if askedQuesCount == 0:
        speech_output = speech_output + "That's all! We're all set to begin! Say begin to get started!"
        speech_output1 = speech_output1 + "That's all! <break time='1s'/>We're all set to begin! Say <emphasis level='moderate'>begin</emphasis> to get started!"
    else:
        speech_output = speech_output + "Alright! Shall we continue? Say begin to continue!"
        speech_output1 = speech_output1 + "Alright!<break time='1s'/> Shall we continue? Say <emphasis level='moderate'>begin</emphasis> to continue!"
                    
    speech_output = speech_output1 + " For detailed rules, say <emphasis level='moderate'>rules</emphasis> again. "
    card_output = speech_output + " For detailed rules, say rules again. "
    reprompt_text = "Hey there! What are you waiting for? " \
                    "Say begin!"
                    
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))

def handle_session_end_request():

    card_title = "Session Ended"
    speech_output = "<say-as interpret-as=\"interjection\">All for now folks.</say-as>"\
                    "I hope you had fun!<break/> " \
                    "Good day!<break/> Come back for more!<break/> Goodbye!"\
                    "<say-as interpret-as=\"interjection\">Ta ta! See you later.</say-as>"
    card_output = "All for now folks! "\
                    "I hope you had fun! " \
                    "Good day! Come back for more! Goodbye!"\
                    " Ta ta! See you later!"
                    
    should_end_session = True
    
    return build_response({}, build_speechlet_response(card_title, speech_output, card_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):

    global score
    global currQues
    global askedQuesCount
    global askedQues
    global quesAnswered

    session_attributes = {}
    score = 0
    currQues = -1
    askedQuesCount = 0
    askedQues = []
    quesAnswered = True

def on_launch(launch_request, session):
    return get_welcome_response()


def on_intent(intent_request, session):
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    print(intent)
    
    if intent_name == "QuizIntent":
        return phrase(intent, session)
    elif intent_name == "AnswerIntent":
        return get_answer(intent, session)
    elif intent_name == "NextQuestionIntent":
        return get_next_question(intent, session)
    elif intent_name == "RepeatQuestionIntent":
        return repeat_question(intent, session)
    elif intent_name == "ReplayIntent":
        return replay_quiz(intent, session)
    elif intent_name == "WhatsMyScoreIntent":
        return current_score(intent, session)
    elif intent_name == "TellMeExampleIntent":
        return tell_me_example(intent, session)
    elif intent_name=="GiveMeHintIntent":
        return give_me_hint(intent,session)
    elif intent_name == "NoIntent":
        return no_response(intent, session)
    elif intent_name == "YesIntent":
        return yes_response()
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response(intent,session)
   # elif intent_name== "AMAZON.FallbackIntent":
    #    return fallbackfunction()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")
        
def on_session_ended(session_ended_request, session):
    session_attributes = {}

# --------------- Main handler ------------------

session_attributes = {}

def lambda_handler(event, context):
    
    if event['session']['new']:
	    on_session_started({'requestId': event['request']['requestId']},event['session'])
		
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])