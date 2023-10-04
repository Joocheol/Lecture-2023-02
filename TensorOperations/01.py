from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


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
    def voice(self, act, idx):
        if act == None:
            with self.voiceover(self.text[idx]) as tracker:
                self.wait(tracker.duration)
        elif isinstance(act, list):
            with self.voiceover(self.text[idx]) as tracker:
                self.play(*act, run_time=tracker.duration)
        else:
            with self.voiceover(self.text[idx]) as tracker:
                self.play(act, run_time=tracker.duration)

    def construct(self):
        self.text = self.speech_setup("01.txt")

        self.section_00()
        self.section_01()
        self.section_02()

        self.voice(None, 1)

    def section_00(self):
        pass

    def section_01(self):
        pass

    def section_02(self):
        pass
