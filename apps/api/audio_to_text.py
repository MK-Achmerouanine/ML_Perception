import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

r = sr.Recognizer()

def get_large_audio_transcription(path, lang):
    
    sound = AudioSegment.from_wav(path)
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    trash_audio_chunks = 'media/trash/audio_chunks'
    if not os.path.isdir(trash_audio_chunks):
        os.mkdir(trash_audio_chunks)
    whole_text = ""
 
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(trash_audio_chunks, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            try:
                text = r.recognize_google(audio_listened, language=lang)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    return whole_text
#make sure the audio file has format.wav
#path = "oneMinAudio.wav"
#print("\nFull text:", get_large_audio_transcription(path,'en'))