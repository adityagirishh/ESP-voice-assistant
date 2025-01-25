import speech_recognition as sr
def transcribe_wav_to_text(wavFILE):
    recognizer = sr.Recognizer()

    with sr.AudioFile(wavFILE) as source:
        audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


# Replace 'your_wav_file.wav' with the path to your WAV file
wav_file = 'sample.wav'

# Transcribe the WAV file into text
transcribed_text = transcribe_wav_to_text(wav_file)


with open('output.txt', 'w+') as file:
    file.write(transcribed_text)

