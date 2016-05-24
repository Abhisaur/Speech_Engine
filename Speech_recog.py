import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    r.energy_threshold = 200
    audio = r.listen(source)
    r.dynamic_energy_adjustment_ratio = 2		# speech is louder than ambedient noise by a factor of 2

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said = " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))