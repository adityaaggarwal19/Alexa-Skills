/* eslint-disable  func-names */
/* eslint-disable  no-console */

const Alexa = require('ask-sdk');

const GetNewFactHandler = {
  canHandle(handlerInput) {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'LaunchRequest'
      || (request.type === 'IntentRequest'
        && request.intent.name === 'GetNewFactIntent');
  },
  handle(handlerInput) {
    const request = handlerInput.requestEnvelope.request;
    var animal = request.intent.slots.animalName.value;
    const factArr = data;
    const factIndex = Math.floor(Math.random() * factArr.length);
    console.log('fact index' + factIndex);
    const randomFact = factArr[factIndex];
    //const speechOutput = GET_FACT_MESSAGE + randomFact;
    const speechOutput = "Here is your fact about " + animal;

    return handlerInput.responseBuilder
      .speak(speechOutput)
      .withSimpleCard(SKILL_NAME, randomFact)
      .getResponse();
  },
};

const HelpHandler = {
  canHandle(handlerInput) {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'IntentRequest'
      && request.intent.name === 'AMAZON.HelpIntent';
  },
  handle(handlerInput) {
    return handlerInput.responseBuilder
      .speak(HELP_MESSAGE)
      .reprompt(HELP_REPROMPT)
      .getResponse();
  },
};

const ExitHandler = {
  canHandle(handlerInput) {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'IntentRequest'
      && (request.intent.name === 'AMAZON.CancelIntent'
        || request.intent.name === 'AMAZON.StopIntent');
  },
  handle(handlerInput) {
    return handlerInput.responseBuilder
      .speak(STOP_MESSAGE)
      .getResponse();
  },
};

const SessionEndedRequestHandler = {
  canHandle(handlerInput) {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'SessionEndedRequest';
  },
  handle(handlerInput) {
    console.log(`Session ended with reason: ${handlerInput.requestEnvelope.request.reason}`);

    return handlerInput.responseBuilder.getResponse();
  },
};

const ErrorHandler = {
  canHandle() {
    return true;
  },
  handle(handlerInput, error) {
    console.log(`Error handled: ${error.message}`);

    return handlerInput.responseBuilder
      .speak('Sorry, an error occurred.')
      .reprompt('Sorry, an error occurred.')
      .getResponse();
  },
};

const SKILL_NAME = 'Wildlife Facts';
const GET_FACT_MESSAGE = 'Here\'s your fact: ';
const HELP_MESSAGE = 'You can say tell me a wildlife fact, or, you can say exit... What can I help you with?';
const HELP_REPROMPT = 'What can I help you with?';
const STOP_MESSAGE = 'Goodbye!';

const data = [
  'Slugs have four noses.',
  'The fingerprints of a koala are so indistinguishable from humans that they have on occasion been confused at a crime scene.',
  'A snail can sleep for three years.',
  'The heart of a shrimp is located in its head.',
  'Elephants are the only animal that can\'t jump.',
  'A rhinoceros horn is made of hair.',
  'It is possible to hypnotize a frog by placing it on its back and gently stroking its stomach.',
  'It takes a sloth two weeks to digest its food.',
  'Nearly three percent of the ice in Antarctic glaciers is penguin urine.',
  'A cow gives nearly 200,000 glasses of milk in a lifetime.',
  'Bats always turn left when leaving a cave.',
  'Giraffes have no vocal chords.',
  'An ostrich eye is bigger than its brain.',
  'Kangaroos can\'t fart.',
];

const skillBuilder = Alexa.SkillBuilders.standard();

exports.handler = skillBuilder
  .addRequestHandlers(
    GetNewFactHandler,
    HelpHandler,
    ExitHandler,
    SessionEndedRequestHandler
  )
  .addErrorHandlers(ErrorHandler)
  .lambda();