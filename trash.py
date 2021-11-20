p=open("translated.txt","rt",encoding='utf8').read().replace("\n"," ")

from gtts import gTTS 

t=gTTS(text=txt, lang=la, slow=False)

t.save('try.wav')     

os.system('start try.wav')

import googletrans

langlist=googletrans.LANGUAGES

print(langlist)

from google_trans_new import google_translator

f=open('try.txt','rt',encoding="utf8")

translator=google_translator()

txt=translator.translate(text='hello python ...welcome', lang_tgt='tamil')

print(txt)

s=open("translated.txt","wt",encoding='utf8')

s.writelines(txt)

s.close

f.close()