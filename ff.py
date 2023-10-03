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

        # self.intro()
        # self.linear_regression()
        # self.graphic_1()
        # self.graphic_2()
        # self.graphic_3() -> not finished yet

        self.mat_play()
        
        self.wait()


    def mat_play(self):
        sq = Square(0.2).set_fill(YELLOW, opacity=1)
        rect_h = Rectangle(height=0.2, width=1.1).set_fill(YELLOW, opacity=1)
        rect_v = Rectangle(height=1.1, width=0.2).set_fill(YELLOW, opacity=1)

        A = mat(sq, 7, 3)
        B = mat(sq, 3, 7)
        C = mat(rect_h, 7, 1)
        D = mat(rect_v, 1, 7)

        v = VGroup(A, B, D, C).arrange_in_grid(2,2)
        v = nn([3,4])
        self.play(Write(v))
        v1 = nn([3,3], arg=[Dot(), Circle(radius=0.1)])
        v1.next_to(v, LEFT, buff=-0.2)
        self.play(Write(v1))
        self.play(Create(v1[1][1][:]))


# TO DO
    def graphic_3(self):
        layer = mat(Circle(radius=0.1), 9, 1)
        ins = mat(Dot(), 5, 1)
        outs = mat(Dot(), 9, 1)
        v = VGroup(ins, layer, outs).arrange(RIGHT, buff=3)

        line_in = VGroup(*[VGroup(*[Line(ins[i], layer[j]) for i in range(len(ins))]) for j in range(len(layer))])

        self.play(Write(v))
        self.play(Write(line_in))



    def graphic_2(self):
        cir = Circle(radius=0.5)
        temp = MathTex(r"y = w_1 x_1 + \cdots + w_5 x_5 + b").shift(2*UP)
        ins = mat(Dot(), 5, 1).next_to(cir, 5*LEFT)
        outs = mat(Dot(), 5, 1).next_to(cir, 5*RIGHT)

        line_in = VGroup(*[Line(ins[i].get_center(), cir.get_left()) for i in range(len(ins))])
        line_out = VGroup(*[Line(cir.get_right(), outs[i].get_center()) for i in range(len(ins))])

        v = VGroup(cir, ins, outs[2], line_in, line_out[2])

        m = Write(v)
        self.voice(m, 31)

        m = Create(line_in)
        self.voice(m, 32)
        self.wait()

        m = Write(temp)
        self.voice(m, 33)
        self.voice(None, 34)

        m = Create(ins)
        self.voice(m, 35)

        m = Create(cir)
        self.voice(m, 36)

        m = [Create(line_out[2]), Create(outs[2])]
        self.voice(m, 37)

        m = [Create(line_out), Create(outs)]
        self.voice(m, 38)
        self.play(FadeOut(line_out), FadeOut(outs))

        m = [GrowFromPoint(line_out[2], cir.get_right()), Write(outs[2])]
        self.voice(m, 39)

        self.play(FadeOut(v), FadeOut(temp))
        

        pass

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