
#download video using 

import pytube

import os

url = "http://youtu.be/v5MR5JnKcZI"

youtube=pytube.YouTube(url)

video = youtube.streams.first()
print('downloading video from youtube')
video.download()

x=video.default_filename

print("completed\n video path: ./videos/" + x )

print('converting into audio format')

import moviepy.editor

video = moviepy.editor.VideoFileClip(x)

audio=video.audio

audio.write_audiofile( x+".wav")

print('audio to audio segment')

import speech_recognition as sr 

r=sr.Recognizer()

from pydub import AudioSegment

from pydub.utils import make_chunks

import math

myaudio = AudioSegment.from_file(x+".wav" , "wav")

channel_count = myaudio.channels    #Get channels

sample_width = myaudio.sample_width #Get sample width

print(len(myaudio))

duration_in_sec = len(myaudio) / 1000#Length of audio in sec

sample_rate = myaudio.frame_rate

print ("sample_width=", sample_width )

print ("channel_count=", channel_count)

print ("duration_in_sec=", duration_in_sec) 

print ("frame_rate=", sample_rate)

bit_rate =16  #assumption , you can extract from mediainfo("test.wav") dynamically

wav_file_size = (sample_rate * bit_rate * channel_count * duration_in_sec) / 8

print ("wav_file_size = ",wav_file_size)  

file_split_size = 10000000  # 10Mb OR 10, 000, 000 bytes

total_chunks =  wav_file_size // file_split_size

chunk_length_in_sec = math.ceil((duration_in_sec * 10000000 ) /wav_file_size)   #in sec

chunk_length_ms = chunk_length_in_sec * 1000

chunks = make_chunks(myaudio, chunk_length_ms)

s=open("try.txt","wt",encoding="utf8")

 #converting audio chunks into text
  
for i, chunk in enumerate(chunks):

            chunk_name = f'chunk{i}.wav'

            print ("exporting", chunk_name)

            chunk.export(chunk_name, format="wav")

            path=chunk_name

            print(path)
with sr.AudioFile(path) as source:
                
              print('Fetching File')

              r.adjust_for_ambient_noise(source,duration=len(path))

              audio_text = r.listen(source)
                      
              print('Converting audio transcripts into text ...')
                      
              text = r.recognize_google(audio_text,language="en-IN")
                      
              print(text)

              s.writelines(text)
      
s.close()

#choosing language

import googletrans

langlist=googletrans.LANGUAGES

print(langlist.values())

keys=(langlist.values())

values=(langlist.keys())

langlist=dict(zip(keys,values))

i=1

while (i>0) :

    try:

      lang=input('enter the lanugage u want to covert\n')

      la=langlist[lang]

      i=-100

    except:

        print('invalid  language \n please')

        i+=1

#text translator
from googletrans import Translator, constants

from pprint import pprint

f=open('type.txt','rt',encoding="utf8")



translator = Translator()

txt = translator.translate(f.read(),dest=la)
print(txt)



#text to speak



from gtts import gTTS 


     

os.system('start try.wav')
