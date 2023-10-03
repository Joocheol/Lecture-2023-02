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
    def voice(self, act, idx):
        if act == None:
            with self.voiceover(self.text[idx]) as tracker:
                self.wait()
        elif isinstance(act, list):
            with self.voiceover(self.text[idx]) as tracker:
                self.play(*act, run_time=tracker.duration)
        else:
            with self.voiceover(self.text[idx]) as tracker:
                self.play(act, run_time=tracker.duration)

    def construct(self):
        self.text = self.speech_setup("ff.txt")

        self.intro()
        self.linear_regression()
        self.graphic_1()
        
        self.wait()

    def graphic_1(self):
        cir = Circle(radius=0.5)
        temp = MathTex(r"y = wx + b").shift(2*UP)
        line_in = Line().next_to(cir, LEFT, buff=0)
        line_out = Line().next_to(cir, RIGHT, buff=0)
        v = VGroup(cir, line_in, line_out)

        m = Write(temp)
        self.voice(m, 21)

        m = Write(v)
        self.voice(m, 22)

        m = temp[0][3].copy().animate.move_to(line_in.get_left() + LEFT/2)
        self.voice(m, 23)

        m = temp[0][0].copy().animate.move_to(line_out.get_right() + RIGHT/2)
        self.voice(m, 24)

        m = [temp[0][2].copy().animate.move_to(cir.get_left() + RIGHT/3), temp[0][5].copy().animate.move_to(cir.get_right() + LEFT/3)]
        self.voice(m, 25)

        self.voice(None, 26)









    def linear_regression(self):
        temp = MathTex(r"y = \beta_0 + \beta_1 x")
        
        m = Write(temp)
        self.voice(m, 3)

        m = Indicate(temp[0][7])
        self.voice(m, 4)
        
        m = Indicate(temp[0][0])
        self.voice(m, 5)

        m = [Indicate(temp[0][2:4]), Indicate(temp[0][5:7])]
        self.voice(m, 6)

        m = None
        self.voice(m, 7)

        temp2 = MathTex(r"y = wx + b")
        m = Transform(temp, temp2)
        self.voice(m, 8)

        m = None
        self.voice(m, 9)

        m = Indicate(temp[0][4])
        self.voice(m, 10)
        
        m = Indicate(temp[0][0])
        self.voice(m, 11)

        m = Indicate(temp[0][3])
        self.voice(m, 12)

        m = Indicate(temp[0][7])
        self.voice(m, 13)

        m = None
        self.voice(m, 14)

        blist = BulletedList("example", "label", "weight", "bias").next_to(temp, RIGHT, buff=LARGE_BUFF)
        
        self.add(blist[0])
        m = Indicate(temp[0][4])
        self.voice(m, 15)
        
        self.add(blist[1])
        m = Indicate(temp[0][0])
        self.voice(m, 16)
        
        self.add(blist[2])
        m = Indicate(temp[0][3])
        self.voice(m, 17)
        
        self.add(blist[3])
        m = Indicate(temp[0][7])
        self.voice(m, 18)
        
        self.play(FadeOut(temp), FadeOut(blist))

    def intro(self):
        temp = Tex("Feed-Forward Neural Network")
        m = FadeIn(temp)
        self.voice(m, 1)

        temp2 = Tex("Linear Regression")
        m = Transform(temp, temp2)
        self.voice(m, 2)
        
        self.play(FadeOut(temp))

    
























    def unused(self):
        act = Write(Circle())
        self.voice(act, 1)

        tracker = self.add_voiceover_text(self.text[2])
        self.wait()
        self.wait(tracker.get_remaining_duration(buff=0.5))