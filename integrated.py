import speech_recognition as sr
import pyttsx
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    r.dynamic_energy_threshold=True
    #r.energy_threshold = 200
    r.adjust_for_ambient_noise(source, 0.5)     # listen for 0.5 second to calibrate the energy threshold for ambient noise levels
    r.pause_threshold = 0.5
    r.dynamic_energy_adjustment_ratio = 2.5     # speech is louder than ambedient noise by a factor of 2.5
    audio = r.listen(source)
    
    # write audio to a WAV file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())
ans = r.recognize_sphinx(audio)
# recognize speech using Sphinx
try:
    print("Sphinx thinks you said = " + ans)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


from chatterbot import ChatBot
from chatterbot.training.trainers import ListTrainer


# Create a new instance of a ChatBot
bot = ChatBot("Terminal",
    storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
    logic_adapters=[
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.TimeLogicAdapter",
        "chatterbot.adapters.logic.ClosestMatchAdapter"
    ],
    input_adapter="chatterbot.adapters.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.adapters.output.OutputFormatAdapter",
    format='text',
    database="../database.db"
)
bot.set_trainer(ListTrainer)
bot.train([
    "hello",
    "hi",
    "how are you",
    "i am fine",
    "that is good to hear",
    "thank you",
    "you are welcome",
    "sorry",
    "its okay", 
    "what is your name",
    "my name is HURO",
])
response= bot.get_response(ans)
engine=pyttsx.init()
engine.setProperty('rate', 120)
engine.say(response)
engine.runAndWait()

