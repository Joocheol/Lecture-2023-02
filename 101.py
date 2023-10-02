from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

from my_transformer import *

import numpy as np

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
        self.text = self.speech_setup("05.txt")
        
        s = skeleton()
        a = skeleton_connect()

        b = setup_boxes()
       
        #self.play(Write(VGroup(s,a).scale(0.66)))
        self.play(Write(b.scale(0.4)))
        
