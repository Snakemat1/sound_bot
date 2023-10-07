from gtts import gTTS
def sound(text):
    tts = gTTS(text,lang='ru')
    return tts.save(f'{text}.mp3')