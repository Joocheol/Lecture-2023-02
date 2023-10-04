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

        self.section_01()
        self.section_02()
        self.section_36()

        #self.voice(None, 1)

    def section_01(self):
        t = Title(r"Tensor Operations")
        blist = BulletedList(
            "Element-wise operations",
            "Broadcasting",
            "Tensor product",
            "Tensor reshaping")
        
        self.wait(0.5)
        self.add(t)
        self.voice([Write(blist)], 1)
        self.play(FadeOut(blist), FadeOut(t))





    def section_02(self):
        code = Code(file_name="Dense.py", tab_width=4, insert_line_no=False, background="window", language="python").rescale_to_fit(12,0)
        self.play(FadeIn(code))


    def section_36(self):
        pass
