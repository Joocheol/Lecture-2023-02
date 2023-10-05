from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
from helper import *

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

        # self.section_01()
        self.section_02()
        self.wait()

 
    def section_01(self):
        self.text = self.speech_setup("intro.txt")
        
        # tracker = self.add_voiceover_text(self.text[1])
        # self.tensor_animation_1()
        # self.wait(tracker.get_remaining_duration())

        tracker = self.add_voiceover_text(self.text[2])
        self.tensor_animation_2()
        self.wait(tracker.get_remaining_duration())
        
    def section_02(self):
        self.text = self.speech_setup("np.txt")
        t = MarkupText(
            """
            <tt>np.array(3)</tt>\r
            <tt>np.array([3])</tt>\r
            <tt>np.array((3))</tt>
            """, font_size=24).scale(1)
        

        self.play(Create(t.to_corner(UL, buff=LARGE_BUFF)))
        
        a = Arrow().rotate(PI).move_to([t.get_right()[0]+1.0, t.get_top()[1]-0.1445, 0.0])
        print(t.get_top()-t.get_bottom())
        for i in range(10):
            self.play(a.animate.shift(DOWN*0.335))
        self.wait()

        
        
        
        

    def tensor_animation_1(self):
        sq = Square(0.16).set_fill(random_color(), opacity=0.5)
        t1 = VGroup(*[sq.copy() for i in range(np.random.randint(2,10))]).arrange(RIGHT).set_color(random_color())
        t2 = VGroup(*[t1.copy() for i in range(np.random.randint(2,10))]).arrange(DOWN).set_color(random_color())
        t3 = VGroup(*[t2.copy() for i in range(np.random.randint(5,10))]).set_color(random_color())

        for i in range(len(t3)):
            t3[i].shift(UR*0.23*i).set_color(random_color()).set_z(-i)

        self.play(ReplacementTransform(sq, t1), run_time=2)
        self.play(ReplacementTransform(t1, t2), run_time=3)
        self.play(ReplacementTransform(t2, t3), run_time=4)
        self.play(FadeOut(t3))
        
    def tensor_animation_2(self):
        sq = Square(0.16).set_fill(random_color(), opacity=0.5)
        t1 = VGroup(*[sq.copy() for i in range(np.random.randint(2,10))]).arrange(RIGHT).set_color(random_color())
        t2 = VGroup(*[t1.copy() for i in range(np.random.randint(2,10))]).arrange(DOWN).set_color(random_color())
        t3 = VGroup(*[t2.copy() for i in range(np.random.randint(5,10))]).set_color(random_color())

        for i in range(len(t3)):
            t3[i].shift(UR*0.23*i).set_color(random_color()).set_z(-i)

        self.play(ReplacementTransform(t3, t2), run_time=4)
        self.play(ReplacementTransform(t2, t1), run_time=3)
        self.play(ReplacementTransform(t1, sq), run_time=2)
        self.play(FadeOut(sq))



        


