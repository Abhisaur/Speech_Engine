import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    r.dynamic_energy_threshold=True
    r.adjust_for_ambient_noise(source, 0.5) 	# listen for 0.5 second to calibrate the energy threshold for ambient noise levels
    r.pause_threshold = 0.5
    audio = r.listen(source)

	# write audio to a WAV file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())
    
# recognize speech using Sphinx
try:
    print("Sphinx thinks you said = " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))