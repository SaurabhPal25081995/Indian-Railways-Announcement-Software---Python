import os 
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToHindiSpeech(text, filename):
    mytext = str(text)
    language = "hi"
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

def textToEnglishSpeech(text, filename):
    mytext = str(text)
    language = "en"
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

# This function returns pydubs audio segment
def mergeAudios(audios1, audios2):
    combined = AudioSegment.empty()
    for audio in audios1:
        combined += AudioSegment.from_mp3(audio)
    
    for audio in audios2:
        combined += AudioSegment.from_mp3(audio)

    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    #1- Generate kripaya dhayan digiye
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")

    #3- Generate se chalkar
    start = 91000
    finish = 92000
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3",format="mp3")

    #5- Generate ke raste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3",format="mp3")

    #7- Generate ko jane wali sankhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3",format="mp3")

    #9- Generate kuch hi samya me platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3",format="mp3")

    #11- Generate par aa rhi h
    start = 109000
    finish = 112100
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3",format="mp3")

    #12- Generate May I have your attention please train number
    start = 66000
    finish = 69800
    audioProcessed = audio[start:finish]
    audioProcessed.export("12_english.mp3",format="mp3")

    #14- generate - from
    start = 76500
    finish = 77000
    audioProcessed = audio[start:finish]
    audioProcessed.export("14_english.mp3",format="mp3")

    #16- generate- to
    start = 78000
    finish = 78500
    audioProcessed = audio[start:finish]
    audioProcessed.export("16_english.mp3",format="mp3")

    #18- generate- via
    start = 80000
    finish = 80900
    audioProcessed = audio[start:finish]
    audioProcessed.export("18_english.mp3",format="mp3")

    #20- Generate- is arriving shortly on platform number
    start = 82600
    finish = 86500
    audioProcessed = audio[start:finish]
    audioProcessed.export("20_english.mp3",format="mp3")



def generateAnnocement(filename):
    df = pd.read_excel(filename)
    print(df)

    for index, item in df.iterrows():
        #2- Generate from city
        textToHindiSpeech(item['from'], '2_hindi.mp3')

        #4- Generate via-city
        textToHindiSpeech(item['via'], '4_hindi.mp3')

        #6- Generate to city
        textToHindiSpeech(item['to'], '6_hindi.mp3')

        #8- Generate train no and name
        textToHindiSpeech(item['train_no'] + " "+item['train_name'], '8_hindi.mp3')

        #10- Generate platform no
        textToHindiSpeech(item['platform'], '10_hindi.mp3')

        #13- No of train no
        textToEnglishSpeech(item['train_no']+ " "+item['train_name'], '13_english.mp3')

        #15- Generate from city
        textToEnglishSpeech(item['from'], '15_english.mp3')

        #17- Generate to city
        textToEnglishSpeech(item['to'], '17_english.mp3')

        #19- Generate via city name
        textToEnglishSpeech(item['via'], '19_english.mp3')
    
        #21- Generate platform no
        textToEnglishSpeech(item['platform'], '21_english.mp3')

        audios1 = [f"{i}_hindi.mp3" or f"{i}_english.mp3" for i in range(1,12)]
        audios2 = [f"{i}_english.mp3" for i in range(12,22)]
        annoucement = mergeAudios(audios1,audios2)
        # This line will create a file having full audio with combining small clips
        annoucement.export(f"annoucement_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now generating annoucement...")
    generateAnnocement("announce_hindi.xlsx")
