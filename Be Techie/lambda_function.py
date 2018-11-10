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

ques = ["The fathers of the Internet is ?",
        "The inventor of the World Wide Web is ?",
        "The first page of a website is called the ?",
        "Where was the first computer installed in India?",
        "Which company is nicknamed Big Blue ?",
        "The standard protocol of the Internet is ?",
        "The first web based e-mail sevice?",
        "Which was the first ever web server software?",
        "Full form of ALU is ?",
        "Full form of ANSI is ?",
        "Full form of API is ?",
        "Full form of ARP is ?",
        "1024 bits is equal to how many bytes?",
        "If a computer has more than one processor then it is known as ?",
        "Wikipedia was launched in 2001. ",
        "Full form of URL is ?",
        "In computer data is stored as ?",
        "Assembly language is a low level language?",
        "Full Form of GUI is ?",
        "Full form of VUI is ?",
        "Who was the Founder of Bluetooth ?",
        "Which Penguin is the mascot of Linux Operating system?",
        "i pad is manufactured by ?",
        "Which IT company got name from Sanfrancisco?",
        "Connecting people is the tagline of ?",
        "What is IMEI?",
        "Who developed first portable computer?",
        "What is NIC?",
        "Whose motto is wisdom of mass principle?",
        "Which Indian state implemented Cyber Grameen ?",
        "Tic-Tac-Toe is first graphical game.",
        "GPS was developed by?",
        "What is Blue Brain project?",
        "Which famous web site was found by Jeffry Bezos?",
        "In which year Microsoft Office was launched?",
        "In which year the first legalized personal computer sold in Cuba?",
        "A person who spends too much time in front of a computer is ?",
        "Who wrote Just for fun ?",
        "Which day is celebrated as world Computer Literacy Day?",
        "Who invented Compact Disc?",
        "Who invented Java?"
        ]

opA = ["Vint Cerf",
       "Brendan Eich",
       "Center Page",
       "Indian Statistical Institute, Kolkata",
       "Microsoft",
       "UDP",
       "Hot mail",
       "Apache",
       "Application Logic Unit",
       "American National Standards Institute",
       "Arithmetic Program Interface",
       "Address Resolution Protocol",
        "128 bytes",
        "Multiprocessor",
        "TRUE",
        "Uniform Resource Locator",
        "Binary",
        "FALSE",
        "Great User Interface",
        "Visual User Interface",
        "Anderson",
        "Adelie",
        "Nokia",
        "Infosys",
        "Micromax",
        "International Market Equipment Identifier",
        "Charles Babbage",
        "Network Interface Card",
        "Wikipedia",
        "Andhra Pradesh",
        "TRUE",
        "Roger Easton",
        "Inventing a brain",
        "Ebay",
        "1984",
        "2005",
        "Mouse User",
        "Jerry Ahern",
        "September 4",
        "Sergey Brin",
        "Bruce Arden"
       ]

opB = ["Barbara Liskov",
       "Larry Page",
       "Home page",
       "Indian Statistical Institute, Delhi",
       "IBM",
       "OSI",
       "Gmail",
       "CERN httpd",
       "Auto Lexical Unit",
       "African National State Institute",
       "Application Program Interface",
       "Arithmetic Resolution Program",
        "64 bytes",
        "Multiprogrammer",
        "FALSE",
        "Uniform Resource Link",
        "Decimal",
        "TRUE",
        "Graphical User Interface",
        "Voice User Interface",
        "Ericson",
        "TUX",
        "Intel",
        "TCS",
        "Samsung",
        "Indian Mobile Equipment Identity",
        "John Backus",
        "New Interface Card",
        "Google",
        "Bangalore",
        "FALSE",
        "Russian Army",
        "Cloning of human brain",
        "Amazon",
        "1989",
        "2008",
        "Mouse Potato",
        "John Agard",
        "December 24",
        "Alan Turing",
        "David F Bacon"
       ]

opC = ["Tim Berners Lee",
       "Tim Berners Lee ",
       "Navigation Page",
       "Indian Statistical Institute, Mumbai",
       "Google",
       "TCP | IP",
       "Yahoo",
       "nginx",
       "Arithmetic Logic Unit",
       "Asian National Status Institute",
       "Address Program Interface",
       "Application Rest Part",
        "256 bytes",
        "Uniprocessor",
        "",
        "Unique Resource Locator",
        "Hexadecimal",
        "",
        "Grand User Input",
        "Valid User Interface",
        "Windson",
        "Emperor",
        "Apple",
        "CISCO",
        "Nokia",
        "International Mobile Equipment Identity",
        "Adam Osborne",
        "Network Inter Control",
        "Bing",
        "Delhi",
        "",
        "China",
        "original human brain",
        "Flipkart",
        "1979",
        "1998",
        "Computer Geek",
        "Linus Torvalds",
        "December 2",
        "James T Russel",
        "James Gosling"
       ]

ans = ["A",
       "C",
       "B",
       "A",
       "B",
       "C",
       "A",
       "B",
       "C",
       "A",
       "B",
       "A",
       "A",
       "A",
       "A",
       "A",
       "A",
       "B",
       "B",
       "B",
       "B",
       "B",
       "C",
       "C",
       "C",
       "C",
       "C",
       "A",
       "A",
       "A",
       "A",
       "A",
       "B",
       "B",
       "B",
       "B",
       "B",
       "C",
       "C",
       "C",
       "C"
       ]

ansInfo = ["Vint Cerf is known as the father of internet.",
           "The first web browser was invented in 1990 by Sir Tim Berners Lee and called World Wide Web ",
           "Home page refers to the first page that appears upon opening a web browser, sometimes called the start page.",
           "The computer age in India began in 1955 with the installation of HEC-2M  at the Indian Statistical Institute at Kolkata",
           "IBM (International Business Machines Corporation) is known as Big Blue.",
           "The Internet protocol suite is the conceptual model and set of communications protocols used on the Internet and similar computer networks.",
           "Sabeer Bhatia of India and Jack Smith founded the first free web-based email service, Hotmail, in 1995.",
           "It was a web server (HTTP) daemon originally developed at CERN.",
           "ALU is the part of CPU that carries out arithmetic and logic operations on the operands in computer instruction words.",
           "ANSI is a voluntary organization composed of over 1,300 members that creates standards for the computer industry.",
           "API stands for application program interface. A programmer writing an application program can make a request to the Operating System using API",
           "ARP is a protocol for mapping an Internet Protocol address to a physical machine address that is recognized in the local network.",
            "1 byte is equal to 8 bits.",
            "Multiprocessor is a computer with more than one central processor.",
            "Wikipedia was launched on 15 January 2001, two days after the domain was registered by Jimmy Wales and Larry Sanger.",
            "A Uniform Resource Locator (URL), colloquially termed a web address, is a reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it.",
            "Binary data is data whose unit can take on only two possible states, traditionally labeled as 0 and 1 in accordance with the binary numeral system and Boolean algebra.",
            "An assembly language is any low-level programming language in which there is a very strong correspondence between the program\'s statements and the architecture's machine code instructions.",
            "The graphical user interface, is a type of user interface that allows users to interact with electronic devices through graphical icons and visual indicators.",
            "The voice user interface problem has long been the sticking point in automated support systems. Examples are Amazon Alexa, Google Assistant",
            "Bluetooth is a wireless technology standard for exchanging data over short distances from fixed and mobile devices, and building personal area networks.",
            "Tux was created by Larry Ewing in 1996 after an initial suggestion made by Alan Cox and further refined by Linus Torvalds on the Linux kernel mailing list.",
            "iPad is a line of tablet computers designed, developed and marketed by Apple Inc., which run the iOS mobile operating system.",
            "Cisco is an American multinational technology conglomerate headquartered in California that develops, manufactures and sells networking and other high-technology services and products.",
            "Nokia have a tagline of connecting people which is shown with a handshake.",
            "IMEI (International Mobile Equipment Identity) is a 15- or 17-digit code that uniquely identifies mobile phone sets.",
            "The first portable computer was created in April 1981 by a company called Osborne, led by a journalist turned entrepreneur named Adam Osborne.",
            "NIC is the premier science & technology organisation of India\'s Union Government in informatics services and information and communication technology (ICT) applications.",
            "Wisdom of mass principle is the motto of wikipedia.",
            "The native village of Andhra Pradesh became the country\'s first village to have a Cyber Grameen Centre, or rural cyber centre.",
            "Tic-tac-toe is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3 by 3 grid.",
            "Roger Easton was a key figure in the development of the Global Positioning System, GPS, a ubiquitous feature of modern life.",
            "Blue brain is the name given to the world\'s first virtual brain.",
            "Amazon is an American electronic commerce and cloud computing company based in Seattle, Washington, that was founded by Jeff Bezos on July 5, 1994.",
            "Microsoft is an American multinational technology company with headquarters in Washington.",
            "In 2008 the first legalized personal computer is sold in Cuba.",
            "Mouse potato is a person who spends large amounts of leisure or working time operating a computer.",
            "Just for Fun : The Story of an Accidental Revolutionary is a humorous autobiography of Linus Torvalds, the creator of the Linux kernel",
            "World Computer Literacy Day aims to curb the digital divide that exists in the world today.",
            "Compact disc is a digital optical disc data storage format.",
            "Java was originally developed by James Gosling at Sun Microsystems and released in 1995 as a core component of Sun Microsystems' Java platform."
           ]

# --------------------------- Global variables ---------------------------------

totalQues = 41
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
    speech_output = "<p>Hello! Welcome to tech quiz! For brief description and rules of the game, just say <emphasis level='moderate'>rules!</emphasis></p> "\
                    "So, Can we find out how well you know technology? Say <emphasis level='moderate'>start quiz</emphasis> to get started with the quiz! " 
    card_output = "Hello! Welcome to tech quiz! For brief description and rules of the game, just say rules! "\
                   "So, Can we find out how well you know technology? Say start quiz to get started with the quiz! "              
    reprompt_text = "Hi! I am waiting! " \
                    "Can we get started? Say begin to get started!" 

    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))

def result():
    
    init = "Awesome! You completed the quiz! " + " You got " + str(score) + " out of " + str(quesInOneSession) + " correct. "
    if score == quesInOneSession:
        init = init + " Well Done! Perfect score! You really know technology well! I am impressed! "
    elif score >= (quesInOneSession/1.5)+1:
        init = init + " Nice score! Keep playing, will definitely keep getting better! "
    elif score >= (quesInOneSession/2.5)+1:
        init = init + " Decent effort! You can do much better, I believe in you! "
    else:
        init = init + " You can do better! Way to go. Play again, get better!  "

    init = init + "  Wanna play again? Just say, Replay!"
    
    return (init)

def result1():
    
    init = "<audio src='soundbank://soundlibrary/human/amzn_sfx_crowd_applause_05'/>"\
            "<say-as interpret-as=\"interjection\">Awesome!</say-as> You completed the quiz!<break/> " + " You got " + str(score) + " out of " + str(quesInOneSession) + " correct. "
    if score == quesInOneSession:
        init = init + " <say-as interpret-as=\"interjection\">Well Done. Perfect Score!</say-as> <break/>You really know english phrases well! I am impressed! "
    elif score >= (quesInOneSession/1.5)+1:
        init = init + " Great score! Keep playing, will definitely keep getting better! "
    elif score >= (quesInOneSession/2.5)+1:
        init = init + " Decent effort! You can do much better, I believe in you! "
    else:
        init = init + " You can do better! <say-as interpret-as=\"interjection\">Way to go.</say-as> <break/> Play again, get better! "

    init = init + " Wanna play again? Just say, Replay!"
    
    return (init)

def ret_question():

    q = ques[currQues] + " . "
    return (q)

def ret_options():

    o3 = ""
    
    o1 = "Option 1 . " + opA[currQues] + ". "
    o2 = "Option 2 . " + opB[currQues] + ". "

    if opC[currQues] != "":
        o3 = "Option 3 . " + opC[currQues] + ". "

    o = o1+o2+o3
    return (o)
    

def quiz(intent, session):

    global askedQuesCount
    global currQues
    global askedQues
    global quesAnswered

    card_title = "Quiz"

    if askedQuesCount == 0:
        init = "Alright! Let us begin. "
    else:
        init = ""

    speech_output = ""
    card_output = ""
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
    options = "Your options are. " + ret_options()
    
    session_attributes['question'] = ques[x]
    session_attributes['options']= options
    
    question1 = "<audio src='soundbank://soundlibrary/musical/amzn_sfx_drum_comedy_02'/> Question " + str(quesNo) + ".  " + ret_question()
    quesAnswered = False
    
    speech_output = init +"<break/><emphasis level='moderate'>" + question1 +"</emphasis>"+ options
    card_output = init + question + options
    reprompt_text = "Hey! I am waiting for your answer. If you missed the question, say repeat question."

    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))    
    #print(b['response']['outputSpeech']['text'])
    

def convert(val):

    if val == '1':
        val = "A"
    elif val == '2':
        val = "B"
    elif val == '3':
        val = "C"
    else:
        val = "D"

    return val    
    
def convertRev(val):

    if val == "A":
        val = "1"
    elif val == "B":
        val = "2"
    elif val == "C":
        val = "3"
    else:
        val = "4"

    return val    

def get_answer(intent, session):

    global score
    global quesAnswered

    card_title = "Answer"

    if quesAnswered == True:
        speech_output = "<say-as interpret-as=\"interjection\">Haanji.</say-as> What you are trying to pull buddy?<break/> You have already answered the question."
        card_output = "Haanji! What you are trying to pull buddy? You have already answered the question."
        reprompt_text = "You can know more about this question's answer by saying, tell me more, or, you can move to the next question by saying, next question."

        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))    

        
    correctAns = ans[currQues]

    if 'value' not in intent['slots']['option']:
        speech_output = "You need to select an option! <emphasis level='moderate'>Select an option.</emphasis>"
        card_output = "You need to select an option! Select an option."
        reprompt_text = "If you missed the options, say repeat options."

        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))
        
    ans_input = intent['slots']['option']['value']
    ans_input = convert(ans_input)

    if ans_input == "D":
        speech_output = "You need to select a valid option! Select a valid option."
        card_output = "You need to select a valid option! <emphasis level-'moderate'>Select a valid option.</emphasis>"
        reprompt_text = "If you missed the options, say repeat options."

        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))

    if ans_input == correctAns:
        speak = "That is the correct answer!" + " Say next for the next question."
        speak1= "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_positive_response_01'/>"\
                "<say-as interpret-as=\"interjection\">Yay.</say-as> That is the correct answer!" + " Say <emphasis level='moderate'>next</emphasis> for the next question."
        score = score + 1
    else:
        speak = "That answer is incorrect. The correct answer is option " + convertRev(correctAns) + " . Say tell me more to know about the correct answer. " 
        speak1= "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                "<say-as interpret-as=\"interjection\">Oh no.</say-as>That answer is incorrect. <break/> The correct answer is <emphasis level='moderate'>" + convertRev(correctAns) + "</emphasis><break/> .Say <emphasis level='moderate'>tell me more</emphasis> to know about the correct answer.  "

    session_attributes['score'] = score
    
    quesAnswered = True
    speech_output = speak1
    card_output = speak
    reprompt_text = "You can know more about this question's answer by saying, tell me more. "
    
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
        
    return quiz(intent,session)

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

    speech_output = speak + ret_question() + " . Options.  " + ret_options()
    card_output = speak + ret_question() + " . Options.  " + ret_options()
    reprompt_text = re
    
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))    
    

def repeat_options(intent, session):

    card_title = "Option"

    if currQues == -1:
        speech_output = "The quiz has not started yet! Say <emphasis level='moderate'>begin</emphasis> to start the quiz"
        card_output = "The quiz has not started yet! Say begin to start the quiz"
        reprompt_text = "Say begin to start the quiz"
        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))    
    
    
    if quesAnswered == True:
        speak = "Your options were. "
        re = "Say, next question, to move to the next question!"
    else:
        speak = "Your options are. "
        re = "Hey, there! I am waiting for your answer."

    speech_output =  speak + ret_options()
    card_output =  speak + ret_options()
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
            speak = "Your score is " + sc + " because you have answered " + sc + " correctly, out of " + str(askedQuesCount) + " questions. Say, next question, to move to next question. "
            speak1= "Your score is <emphasis level='moderate'>" + sc + " </emphasis>because you have answered " + sc + " correctly, <break/>out of " + str(askedQuesCount) + " questions. Say, next question, to move to next question. "
            re = "Move to the next question by saying, next question."
        else:
            speak = "Your score is " + sc + " because you have answered " + sc + " correctly, out of " + str(askedQuesCount-1) + " questions. Say the answer now as option 1, or, option2, or, option3, or, option 4. "
            speak1= "Your score is <emphasis level='moderate'>" + sc + " </emphasis>because you have answered " + sc + " correctly, <break/>out of " + str(askedQuesCount-1) + " questions. Say the answer now as option 1, or, option2, or, option3, or, option 4. "
            re = "I am waiting for the answer! Say, repeat question, if you want me to repeat the question."

    speech_output = speak1
    card_output = speak
    reprompt_text = re
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))    

def tell_me_more(intent, session):

    card_title = "Tell Me More"

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


def replay_quiz(intent, session):
    
    global score
    global currQues
    global askedQuesCount
    global askedQues
    global quesAnswered
    
    score = 0
    currQues = -1
    askedQuesCount = 0
    askedQues = []
    session_attributes = {}
    quesAnswered = True
    
    return quiz(intent, session)    


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
                " If you want to answer a given question then just say, option 1, or option2, or, option 3, or, option 4."
    reprompt_text = "For rules, say rules!"
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))    

    
def get_help_response(intent, session):
    
    global rulecount
    
    card_title = "Rules"
    
    rulecount = rulecount + 1
    if rulecount == 1:
        '''
        s1 = "This is a technology quiz and the rules are very simple. <break/>" \
                        "I will ask you a question. <break/>You choose your answer by saying, <emphasis level = 'moderate'> Option 1, or Option 2, etc.</emphasis><break/>"\
                        "<break/> I will tell you, if you were correct. Move to the next question by saying <emphasis level='moderate' > Next! </emphasis>"
        '''
        s = "This is a technology quiz and the rules are very simple. " \
                        "I will ask you a question. You choose your answer by saying, Option 1, or Option 2, etc. "\
                        "I will tell you, if you were correct. Move to the next question by saying Next! "
    else:
        '''
        s1 ="Hi! Welcome to <emphasis level='moderate'>Be Techie!</emphasis><break/> "\
                        "This is a technology quiz and the rules are very simple. <break/>" \
                        "After you start the quiz, you will be prompted with a question. <break/>"\
                        "Options for the same will be provided. You have to choose one option, by saying, <emphasis level = 'moderate'> Option 1, or, Option 2, or, Option 3, or, Option 4. </emphasis> <break/>" \
                        "After you answer the question, I will tell you, whether you were right, or not. Then say, <emphasis level= 'moderate'> next question</emphasis>, to move to the next question. <break/>"\
                        "You can get a question repeated, by saying, <emphasis level='moderate'> Repeat question</emphasis>. You can also get the options for a question, repeated, by saying, <emphasis level= 'moderate'> repeat options. </emphasis><break/>"\
                        "You can also know more about the answer, of a question, by saying, <emphasis level='moderate' >tell me more. </emphasis><break/>"\
                        "You will be asked <emphasis level='moderate'>5 questions</emphasis>. You will get the final score after the game. To get your score between the game, you can ask, <emphasis level = 'moderate'>what is my score.</emphasis> "
        '''
        s = "Hi! Welcome to Be Techie! " \
                        "This is a technology quiz and the rules are very simple. " \
                        "After you start the quiz, you will be prompted with a question. "\
                        "Options for the same will be provided. You have to choose one option, by saying, Option 1, or, Option 2, or, Option 3, or, Option 4. " \
                        "After you answer the question, I will tell you, whether you were right, or not. Then say, next question, to move to the next question. "\
                        "You can get a question repeated, by saying, Repeat question. You can also get the options for a question, repeated, by saying, repeat options. "\
                        "You can also know more about the answer, of a question, by saying, tell me more. "\
                        "You will be asked 5 questions. You will get the final score after the game. To get your score between the game, you can ask, what is my score. "
        rulecount = 0                

    if askedQuesCount == 0:
        
        #s1 = s1 + "That's all! <break/>We're all set to begin! Say <emphasis level='moderate'>begin</emphasis> to get started!"
        s = s + "That's all! We're all set to begin! Say begin to get started!"
    else:
        
        #s1 = s1 + "Alright!<break/> Shall we continue? Say <emphasis level='moderate'>begin</emphasis> to continue!"
        s = s + "Alright! Shall we continue? Say begin to continue!"
                    
    speech_output = s + " For detailed rules, say rules again. "
    card_output = s + " For detailed rules, say rules again. "
    reprompt_text = "Hey there! What are you waiting for? " \
                    "Say begin!"
                    
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))

def handle_session_end_request():

    card_title = "Session Ended"
    speech_output = "<say-as interpret-as=\"interjection\">All for now folks.</say-as>"\
                    "I hope you had fun!<break/> " \
                    "Good day!<break/> Come back for more!<break/> Goodbye! "\
                    "<say-as interpret-as=\"interjection\">Ta ta! See you later.</say-as>"
    card_output = "All for now folks! "\
                    "I hope you had fun! " \
                    "Good day! Come back for more! Goodbye! "\
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
        return quiz(intent, session)
    elif intent_name == "AnswerIntent":
        return get_answer(intent, session)
    elif intent_name == "NextQuestionIntent":
        return get_next_question(intent, session)
    elif intent_name == "RepeatQuestionIntent":
        return repeat_question(intent, session)
    elif intent_name == "RepeatOptionsIntent":
        return repeat_options(intent, session)
    elif intent_name == "ReplayIntent":
        return replay_quiz(intent, session)
    elif intent_name == "WhatsMyScoreIntent":
        return current_score(intent, session)
    elif intent_name == "TellMeMoreIntent":
        return tell_me_more(intent, session)
    elif intent_name == "NoIntent":
        return no_response(intent, session)
    elif intent_name == "YesIntent":
        return yes_response()
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response(intent, session)
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
