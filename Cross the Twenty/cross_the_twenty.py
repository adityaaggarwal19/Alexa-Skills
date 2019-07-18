from __future__ import print_function
import random
import json

rulecount=0
start_game=0
# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, card_output,reprompt_text, should_end_session):
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


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Hello, Welcome to Cross The Twenty! <break/>" \
                    "For brief description and rules of the game, just say <emphasis level='moderate'>rules!</emphasis><break/> "\
                    "So, shall we start the game? Let's see who wins the game. Say, <emphasis level='moderate'>start game,</emphasis> to start the game!<break/> "
    card_output = "Hello, Welcome to Cross The Twenty! " \
                    "For brief description and rules of the game, just say rules! "\
                    "So, shall we start the game? Let's see who wins the game. Say start game to start the game! "
    reprompt_text = "Hi there say start game to start the game otherwise for rules say rules! "
    
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, card_output,reprompt_text, should_end_session))

def midintentfun(intent, session):
    
    global start_game
    session_attributes = {}
    card_title = "Game Home"
    if start_game==0:
        
        start_game=1
        speech_output = "<audio src='soundbank://soundlibrary/musical/amzn_sfx_drum_comedy_02'/>"\
                        "Let's begin the game! " \
                        "So, start with your turn! <break/>"\
                        "Say your number by saying,<break/> " \
                        "<emphasis level='moderate'>my number is one, or, two.</emphasis> "\
                        "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
        card_output = "Let's begin the game! " \
                        "So, start with your turn!"\
                        "Say your number by saying, " \
                        "my number is one, or, two. "
        reprompt_text = "Please tell me your number by saying, " \
                        "my option is your number like one."
    else:
        if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
        o1=str(int(comp_old_num)+1)
        o2=str(int(comp_old_num)+2)
        session_attributes = computer_number(comp_old_num)
        speech_output = "You are already playing a game. <break/>If you want to start new game then say <emphasis level='moderate'>play again,</emphasis> Otherwise<break/> "\
                        "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                        ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
        card_output = "You are already playing a game. If you want to start new game then say play again, Otherwise "\
                        "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
        reprompt_text = "Say your number by saying, " \
                        "my number is " + o1+ " or, " + o2 + "."
        
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, card_output,reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for playing Cross The Twenty! <break/>" \
                    "I hope you had fun. <break/>"\
                    "Come back to have more fun and to discover more tricks to win. <break/>"\
                    "Bye bye! Have a nice day! "
    card_output = "Thank you for playing Cross The Twenty! " \
                    "I hope you had fun. "\
                    "Come back to have more fun and to discover more tricks to win. "\
                    "Bye bye! Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, card_output,None, should_end_session))

def replay_func(intent, session):
    session_attributes={}
    global rulecount
    global start_game
    rulecount=0
    start_game=0
    return get_welcome_response()
    
def repeat_func(intent, session):
    card_title = "Repeat Number"
    session_attributes = {}
    if start_game==1:
        
        if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
        o1=str(int(comp_old_num)+1)
        o2=str(int(comp_old_num)+2)
        session_attributes = computer_number(comp_old_num)
        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                        "My number is " + \
                        comp_old_num + ". Your turn! <break/>" \
                        "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                        ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
        card_output = "My number is " + \
                        comp_old_num + ". Your turn! " \
                        "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
        reprompt_text = "Say your number by saying, " \
                        "my number is " + o1+ " or, " + o2 + "."
    else:
        speech_output = "First say start game to start the game. " 
                        
        card_output = "First say start game to start the game. " 
        reprompt_text = "First say start game to start the game. " 
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, card_output, reprompt_text, should_end_session))

def computer_number(comp_numb):
    return {"ComputerNumber": comp_numb}

def set_number(intent, session):

    card_title = "Number Select"
    session_attributes = {}
    should_end_session = False
    intNumber=0
    if start_game==1:
        
        if 'num' in intent['slots']:
            user_num = intent['slots']['num']['value']
            if user_num == "1":
                
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num== "2":
            
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num == "3":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num == "4":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num == "5":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
        
            elif user_num == "6":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num == "7":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num == "8":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num == "9":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num == "10":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num == "11":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num == "12":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num == "13":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num == "14":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num == "15":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num == "16":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num == "17":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    o1=str(int(comp_num)+1)
                    o2=str(int(comp_num)+2)
                    session_attributes = computer_number(comp_num)
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + ". Your turn! <break/>" \
                                    "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                    ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                    card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                    reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            elif user_num == "18":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num=random.randint(intNumber+1,intNumber+2)
                    comp_num=str(comp_num)
                    if comp_num== "20":
                        session_attributes = comp_num
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                        "My number is " + \
                                        comp_num + "<audio src='soundbank://soundlibrary/musical/amzn_sfx_buzz_electronic_01'/>. <emphasis level='moderate'>You lost the game!</emphasis> <break/>" \
                                        "To exit, say <emphasis level='moderate'>stop!</emphasis>"
                        card_output = "My number is " + \
                                        comp_num + ". You lost the game! " \
                                        "To exit say stop! "
                        reprompt_text = "You can exit by saying, " \
                                        "stop"
                    else:
                        o1=str(int(comp_num)+1)
                        o2=str(int(comp_num)+2)
                        session_attributes = computer_number(comp_num)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                        "My number is " + \
                                        comp_num + ". Your turn! <break/>" \
                                        "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                        ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "My number is " + \
                                    comp_num + ". Your turn! " \
                                   "Say your number by saying my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "You can say your number by saying, " \
                                    "my number is " + o1+ " or, " + o2 + "."
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                         "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                    "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            
            elif user_num == "19":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    intNumber=int(user_num)
                    comp_num= 20
                    comp_num=str(comp_num)
                    session_attributes = comp_num
                    speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player3_01'/>"\
                                    "My number is " + \
                                    comp_num + "<audio src='soundbank://soundlibrary/musical/amzn_sfx_buzz_electronic_01'/>. <emphasis level='moderate'>You lost the game!</emphasis> <break/>" \
                                    "To exit, say <emphasis level='moderate'>stop!</emphasis>"
                    card_output = "My number is " + \
                                    comp_num + ". You lost the game! " \
                                    "To exit say stop! "
                    reprompt_text = "You can exit by saying, " \
                                    "stop"
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                       "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
        
            elif user_num == "20":
                if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                    comp_old_num = session['attributes']['ComputerNumber']
                else:
                    comp_old_num="0"
                n1=int(user_num)
                c1=int(comp_old_num)
                if n1 == c1+1 or n1 == c1+2:
                
                    session_attributes = computer_number(user_num)
                    speech_output = "<audio src='https://s3.amazonaws.com/ask-soundlibrary/human/amzn_sfx_crowd_applause_03.mp3'/>"\
                                    "<say-as interpret-as='interjection'>Congratulations,</say-as> You have won the game! <break/>" \
                                    "You can exit by saying, " \
                                    "<emphasis level='moderate'>stop!</emphasis>"
                    card_output = "Congratulations, You have won the game! "\
                                    "You can exit by saying, " \
                                    "stop! "
                    reprompt_text = "You can exit by saying, " \
                                    "stop"
                else:
                    session_attributes = computer_number(comp_old_num)
                    if int(comp_old_num)<20:
                        o1=str(int(comp_old_num)+1)
                        o2=str(int(comp_old_num)+2)
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You said a wrong number. <break/>" \
                                       "Please try again. <break/>"\
                                       "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                                       ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
                        card_output = "Sorry, You said a wrong number. " \
                                       "Please try again. "\
                                       "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                        reprompt_text = "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
                    else:
                        speech_output = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_negative_response_01'/>"\
                                        "Sorry, You have already completed the game. <break/>" \
                                        "You can exit by saying stop"
                        card_output = "Sorry, You have already completed the game. <break/>" \
                                      "You can exit by saying stop"
                        reprompt_text = "Say stop to exit the skill."
            else:
                speech_output = "Say a valid number " \
                                "Please try again."
                card_output = "Say a valid number " \
                                "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                "You can tell me your number by saying, " \
                                "my number is one."
        else:
            speech_output = "Sorry, I'm not sure what your number is. <break/>" \
                            "Please try again."
            card_output = "Sorry, I'm not sure what your number is. " \
                            "Please try again."
            reprompt_text = "I'm not sure what your number is. " \
                                "You can tell me your number by saying, " \
                                "my number is one."
    else:
        speech_output = "First say start game to start the game. " 
        card_output = "First say start game to start the game. " 
        reprompt_text = "First say start game to start the game. "
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, card_output,reprompt_text, should_end_session))


def get_help_response(intent, session):
    
    global rulecount
    
    card_title = "Rules"
    session_attributes= {}
    comp_old_num="0"
    if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
    o1=str(int(comp_old_num)+1)
    o2=str(int(comp_old_num)+2)
    session_attributes = computer_number(comp_old_num)
    
    rulecount = rulecount + 1
    if rulecount == 1:
        speech_output = "This is a counting number game and the rules are simple. <break/>" \
                        "The objective of the game is to be the first one to say 20. <break/>"\
                        "I will play with you, and say the number one more than or two more than your number. "
        card_output = "This is a counting number game and the rules are simple. " \
                        "The objective of the game is to be the first one to say 20. "\
                        "I will play with you, and say the number one more than or two more than your number. "
    else:
        speech_output = "Hi! Welcome to Cross the Twenty! <break/>" \
                        "This is a counting number game and the rules are simple. <break/>" \
						"The game start at 1 when you say start game and you may say one or two. and the numbers must be in counting order. <break/>"\
						"Each person must say the number one more than or two more than the last one that the other person said. <break/>"\
						"For example, you say 1, then the alexa will say 2, or, 3. <break/>"\
						"If the Alexa say 2 then you need to say 3, or, 4. <break/>"\
						"If the you say 4 then Alexa will say 5, or, 6. <break/>"\
						"Whoever says 20 first wins the game. <break/>"\
						"You can say repeat number to ask Alexa repeat its number. <break/>"\
						"You can replay game by saying play again. <break/>"\
						"At any point of game to stop the game say stop. <break/>"\
						"Play this game many times and try to discover a winning strategy. "
        card_output = "Hi! Welcome to Cross the Twenty! " \
                        "This is a counting number game and the rules are simple. " \
						"The game start at 1 when you say start game and you may say one or two. and the numbers must be in counting order. "\
						"Each person must say the number one more than or two more than the last one that the other person said. "\
						"For example, you say 1, then the alexa will say 2, or, 3. "\
						"If the Alexa say 2 then you need to say 3, or, 4. "\
						"Whoever says 20 first wins the game. "\
						"You can say repeat number to ask Alexa repeat its number. "\
						"You can replay game by saying play again. "\
						"At any point of game to stop the game say stop. "\
						"Play this game many times and try to discover a winning strategy. "
        rulecount = 0                
    
    if comp_old_num == "0":
        speech_output = speech_output + "That's all! We're all set to begin! <break/>Say start game to get started!"
        card_output = card_output + "That's all! We're all set to begin! Say start game to get started!"
        
    else:
        speech_output = speech_output + "Alright! Shall we continue? <break/>"\
                        "Say your number by saying my number is "+ o1+ " ,or, " + o2 + "."
        card_output = card_output + "Alright! Shall we continue? "\
                        "Say your number by saying my number is "+ o1+ " ,or, " + o2 + "."       
    speech_output = speech_output + "<break/> For detailed rules, say rules again. "
    card_output = card_output + " For detailed rules, say rules again. "
    reprompt_text = "Hey there! What are you waiting for? " \
                    "Say start game to start the game!"
                    
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))


def fallBackIntent(intent, session):
    session_attributes = {}
    card_title = "Sorry!"
    if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
    else:
        comp_old_num="0"
    o1=str(int(comp_old_num)+1)
    o2=str(int(comp_old_num)+2)
    session_attributes = computer_number(comp_old_num)
    if int(comp_old_num)<20:
        
        speech_output = "You have spoken something different from utterances, Please try again! <break/>"\
                        "Say your number by saying my number is "+ o1+ " ,or, " + o2 +\
                        ".<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_player1_01'/>"
    
        card_output = "You have spoken something different from utterances, Please try again! "\
                        "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
        reprompt_text = "You have spoken something different from utterances, Please try again! "\
                        "Say your number by saying, my number is " + o1+ " or, " + o2 + "."
    else:
        speech_output = "You have spoken something different from utterances, Please try again! <break/>"
    
        card_output = "You have spoken something different from utterances, Please try again! "
    
        reprompt_text = "You have spoken something different from utterances, Please try again! "
    
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """
    global rulecount
    global start_game
    
    rulecount=0
    start_game=0
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "WhatIsNumber":
        return set_number(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response(intent, session)
    elif intent_name == "BeginIntent":
        return midintentfun(intent, session)
    elif intent_name == "RepeatIntent":
        return repeat_func(intent, session)
    elif intent_name == "ReplayIntent":
        return replay_func(intent, session)
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "AMAZON.FallbackIntent":
        return fallBackIntent(intent, session)
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])