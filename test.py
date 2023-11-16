from rasa_nlu.model import Trainer
from rasa_nlu import config

def train_rasa_nlu():
    training_data = "data.json"
    trainer = Trainer(config.load("config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist("./models/nlu", fixed_model_name="current")

def get_intent(user_input):
    from rasa_nlu.model import Interpreter
    interpreter = Interpreter.load("./models/nlu/current")
    intent = interpreter.parse(user_input)['intent']['name']
    return intent

# Example usage:

train_rasa_nlu()

while True:
    user_input = input("Type your command or say it: ")
    intent = get_intent(user_input)

    if intent == "greet":
        speak("Hi there! How can I assist you?")
    elif intent == "goodbye":
        speak("Goodbye! Have a great day.")
        break
    elif intent == "joke":
        speak("Why don't scientists trust atoms? Because they make up everything!")
    else:
        speak("I'm sorry, I don't understand that command. Please try again.")
