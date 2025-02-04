import os
import tempfile
from TTS.api import TTS


class TTSTalker():
    def __init__(self) -> None:
        model_name = TTS().list_models()[31]
        #model_name = TTS("/root/.local/share/tts/tts_models--multilingual--multi-dataset--xtts_v1", gpu=True).list_models()[0]
        print(f'-------TTSTalker.model_name={model_name}--------')
        self.tts = TTS(model_name)

    def test(self, text, language='zh'):

        tempf  = tempfile.NamedTemporaryFile(
                delete = False,
                suffix = ('.'+'wav'),
            )
        print(f'-------speaker={self.tts.speakers},language={language},file_path={tempf.name}--------')
        self.tts.tts_to_file(text, file_path=tempf.name)

        return tempf.name
    

# if __name__=="__main__":
#     tts = TTSTalker()
#     tts.test(text= " hello ,nice to meet you ")


# [
# 'tts_models/multilingual/multi-dataset/your_tts', 
# 'tts_models/multilingual/multi-dataset/bark',
#  'tts_models/bg/cv/vits',
#  'tts_models/cs/cv/vits', 
#  'tts_models/da/cv/vits',
#  'tts_models/et/cv/vits', 
#  'tts_models/ga/cv/vits', 
#  'tts_models/en/ek1/tacotron2',
#  'tts_models/en/ljspeech/tacotron2-DDC',
#  'tts_models/en/ljspeech/tacotron2-DDC_ph',
#  'tts_models/en/ljspeech/glow-tts',
#  'tts_models/en/ljspeech/speedy-speech',
#  'tts_models/en/ljspeech/tacotron2-DCA',
#  'tts_models/en/ljspeech/vits', 
#  'tts_models/en/ljspeech/vits--neon', 
#  'tts_models/en/ljspeech/fast_pitch',
#  'tts_models/en/ljspeech/overflow', 
#  'tts_models/en/ljspeech/neural_hmm',
#  'tts_models/en/vctk/vits', 
#  'tts_models/en/vctk/fast_pitch', 
#  'tts_models/en/sam/tacotron-DDC',
#  'tts_models/en/blizzard2013/capacitron-t2-c50',
#  'tts_models/en/blizzard2013/capacitron-t2-c150_v2', 
#  'tts_models/en/multi-dataset/tortoise-v2', 
#  'tts_models/en/jenny/jenny', 
#  'tts_models/es/mai/tacotron2-DDC', 
#  'tts_models/es/css10/vits', 
#  'tts_models/fr/mai/tacotron2-DDC',
#  'tts_models/fr/css10/vits', 
#  'tts_models/uk/mai/glow-tts', 
#  'tts_models/uk/mai/vits',
#  'tts_models/zh-CN/baker/tacotron2-DDC-GST',
#  'tts_models/nl/mai/tacotron2-DDC', 
#  'tts_models/nl/css10/vits', 
#  'tts_models/de/thorsten/tacotron2-DCA', 
#  'tts_models/de/thorsten/vits',
#  'tts_models/de/thorsten/tacotron2-DDC',
#  'tts_models/de/css10/vits-neon', 
#  'tts_models/ja/kokoro/tacotron2-DDC', 
#  'tts_models/tr/common-voice/glow-tts',
#  'tts_models/it/mai_female/glow-tts', 
#  'tts_models/it/mai_female/vits', 
#  'tts_models/it/mai_male/glow-tts', 
#  'tts_models/it/mai_male/vits', 
#  'tts_models/ewe/openbible/vits', 
#  'tts_models/hau/openbible/vits',
#  'tts_models/lin/openbible/vits', 
#  'tts_models/tw_akuapem/openbible/vits',
#  'tts_models/tw_asante/openbible/vits', 
#  'tts_models/yor/openbible/vits', 
#  'tts_models/hu/css10/vits', 
#  'tts_models/el/cv/vits', 
#  'tts_models/fi/css10/vits',
#  'tts_models/hr/cv/vits', 
#  'tts_models/lt/cv/vits', 
#  'tts_models/lv/cv/vits', 
#  'tts_models/mt/cv/vits', 
#  'tts_models/pl/mai_female/vits', 
#  'tts_models/pt/cv/vits',
#  'tts_models/ro/cv/vits', 
#  'tts_models/sk/cv/vits',
#  'tts_models/sl/cv/vits', 
#  'tts_models/sv/cv/vits', 
#  'tts_models/ca/custom/vits', 
#  'tts_models/fa/custom/glow-tts', 
#  'tts_models/bn/custom/vits-male',
#  'tts_models/bn/custom/vits-female']