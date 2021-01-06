import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen (source)
    print("Processing the Audio")
    try:
        print("Text: "+r.recognize_google(audio_text))
    except:
        print("There was a technical error")
