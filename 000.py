from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

from my_transformer import *

class Explainer(VoiceoverScene):
    def speech_setup(self, file):
        self.set_speech_service(
            AzureService(
                voice="en-US-JennyMultilingualNeural",
                style="newscast-casual",
            )
        )

        with open(file, "r") as f:
            n = f.read()
        n = n.splitlines()

        text = ["""<lang xml:lang="ko-KR">""" + "줄 번호를 확인하기 바랍니다." +"""</lang>"""]
        for i in n:
            text.append("""<lang xml:lang="ko-KR">""" + i +"""</lang>""")

        return text[:]
    
    def construct(self):
        self.text = self.speech_setup("000.txt")

        act = Write(Circle())
        self.voice(act, 1)

        tracker = self.add_voiceover_text(self.text[2])
        self.wait()
        self.wait(tracker.get_remaining_duration(buff=0.5))


        
        self.wait()

    def voice(self, act, idx):
        with self.voiceover(self.text[idx]) as tracker:
            self.play(act, run_time=tracker.duration)
            
     

