import speech_recognition as sr
sr.__version__
'3.8.1'

# WAV (PCM/LPCM format), AIFF, AIFF-C, FLAC (native)
#Using audio files

r = sr.Recognizer()
test = sr.AudioFile('recording.wav')
with test as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)

print(type(audio))

print(r.recognize_google(audio))


'''
# Using microphone
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.listen(source)

print(r.recognize_google(audio))
'''

'''
recognizer = sr.Recognizer()
mic = sr.Microphone()
def recognize_speech(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("Make sure that `recognizer` is `Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("Make sure that `microphone` is `Microphone` instance")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    output = {
        "success": True,
        "error": None,
        "transcription": None,
    }

    try:
        output["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        output["success"] = False
        output["error"] = "API not available"
    except sr.UnknownValueError:
        output["error"] = "Speech is not recognizable"

    return output

print(recognize_speech(recognizer, mic))
'''
