import speech_recognition as sr
import pyttsx3
import webbrowser
import requests


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def listen(text_input=None):
    recognizer = sr.Recognizer()
    # print(sr.Microphone.list_microphone_names())

    device_index = 1
    if text_input:
        return text_input.lower()
    try:
        with sr.Microphone(device_index=device_index) as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5)

        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""


def open_website(url):
    webbrowser.open(url)


# def get_weather(city):
#     api_key = "YOUR_OPENWEATHERMAP_API_KEY"
#     base_url = "http://api.openweathermap.org/data/2.5/weather"
#     params = {"q": city, "appid": api_key}

#     try:
#         response = requests.get(base_url, params=params)
#         data = response.json()

#         if data["cod"] == "404":
#             return "City not found. Please try again."
        
#         temperature = data["main"]["temp"]
#         description = data["weather"][0]["description"]
#         return f"The weather in {city} is {description} with a temperature of {temperature} Kelvin."

#     except Exception as e:
#         return f"An error occurred: {e}"


def main():
    speak("Hello! I am your assistant. How can I help you today?")
    
    while True:
        user_input = input("Type your command or say it: ")
        command = listen(text_input=user_input)

        if "hello" in command:
            speak("Hi there! How can I assist you?")
        elif "goodbye" in command:
            speak("Goodbye! Have a great day.")
            break
        elif "tell me a joke" in command:
            speak("Why don't scientists trust atoms? Because they make up everything!")
        elif "open website" in command:
            speak("Sure, which website would you like me to open?")
            website = listen()
            open_website("http://" + website)
        elif "search" in command:
            speak("What do you want to search for?")
            search_query = listen()
            webbrowser.open("https://www.google.com/search?q=" + search_query)
        # elif "weather" in command:
        #     speak("Sure, which city would you like the weather for?")
        #     city = listen()
        #     weather_info = get_weather(city)
        #     speak(weather_info)
        else:
            speak("I'm sorry, I don't understand that command. Please try again.")


if __name__ == "__main__":
    main()





