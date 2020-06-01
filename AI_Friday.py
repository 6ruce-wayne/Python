import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='th')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")

def recordAudio():
# Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
    # Uses the default API key
    # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio,language="th")
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return data
 
def dekdoydev(data):
    if "Friday" in data:
        speak("สวัสดีคะนายท่าน")

    if "สบายดีไหม" in data:
        speak("เป็น AI ก็ต้องสบายดีอยู่แล้วค่ะ")
    
    if "กี่โมงแล้ว" in data:
        speak(ctime())

    if "ร้องเพลงให้ฟังหน่อย" in data:
        speak("ลันลั่นลา ลันลั่นลา หนูชื่อโบว์มากับนุ่นแล้วก็มากับเจน ฮะฮะฮะฮะ")

    if "เปิดเพลงหน่อย" in data:
        speak("ได้เลยค่ะ นายท่าน")
        os.system("start Spotify")

    if "เล่าเรื่องตลกให้ฟังหน่อย" in data:
        speak("ไม่ได้เป็นคนตลกค่ะ ถ้าจะฟังเรื่องละ 20 บาทค่ะ")

    if "เปิด Excel หน่อย" in data:
        speak("ได้เลยค่ะ Excel นะคะ")
        os.system("start Excel")

    if "แผนที่ประเทศไทย" in data:
        data = data.split(" ")
        speak("รอสักครู่คะนายท่าน เดี๋ยวเปิดแผนที่ประเทศไทยให้ค่ะ")
        os.system("start https://www.google.co.th/maps/place/t...")

    if "ขอข่าวโควิทช์" in data:
        data = data.split(" ")
        speak("รอสักครู่คะนายท่าน เดี๋ยวเปิดข่าวโควิทช์ให้ค่ะ")
        os.system("start https://covid-19.kapook.com/")
    
# Starting Conversation

time.sleep(2)
speak("สวัสดีค่ะนายท่านมีอะไรให้ฉันช่วย")

while 1:
    data = recordAudio()
    dekdoydev(data)