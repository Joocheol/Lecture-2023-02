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

        # self.section_01()
        # self.section_02()
        self.section_15()

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
        self.voice(FadeIn(code), 2)
        self.wait()

        f = MarkupText(r"<tt>output = relu(dot(input, W) + b)</tt>").scale(0.5)
        self.voice(Write(f), 3)
        self.voice(None, 4)
        self.voice(f[12:24].animate.set_color(RED), 5)
        self.voice(None, 6)
        self.voice(f[12:26].animate.set_color(YELLOW), 7)
        self.voice(None, 8)
        self.voice(f[7:27].animate.set_color(BLUE), 9)
        self.voice(None, 10)

        f_2 = MarkupText(r"<tt>relu(x) = max(x, 0)</tt>").scale(0.5).next_to(f, DOWN)
        self.play(Write(f_2))

        self.play(FadeOut(code), FadeOut(f), FadeOut(f_2))
        
    def section_15(self):
        t = Tex(r"Element-wise operations")
        self.voice(Write(t), 15)
        self.voice(None, 16)
        self.voice(FadeOut(t), 17)
        

        code = Code(file_name="naive_relu.py", tab_width=4, insert_line_no=False, background="window", language="python").rescale_to_fit(12,0)
        self.voice(FadeIn(code), 18)
        self.wait()


