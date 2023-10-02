from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

import numpy as np

class Explainer(VoiceoverScene):
    def construct(self):
        text = self.speech_setup("attention.txt")
        self.text = text

        # example text and copy
        t_1, t_2 = setup_text_box()
        self.t = t_1.scale(0.4)
        self.tc = self.t.copy()

        # querys and keys
        self.bar = Rectangle(height=0.2, width=2)
        self.q = VGroup(*[self.bar.copy().set_fill(color=random_color(), opacity=0.8) for _ in range(len(self.t))]).arrange(DOWN, buff=0.2)
        self.k = VGroup(*[self.bar.copy().set_fill(color=random_color(), opacity=0.8) for _ in range(len(self.t))]).arrange(DOWN, buff=0.2)
        

        idx = 1

        self.intro(1)
        self.qk_vectors(5)


        

       
        # start communication
        tracker = self.add_voiceover_text(self.text[idx+11]); self.wait(tracker.get_remaining_duration(buff=0.5))    

        # communications
        temp_out = VGroup()
        for i in range(len(self.t)):
            temp_in = VGroup()
            for j in range(len(self.t)):
                l = Line(self.q[i].get_right(), self.k[j].get_left())
                temp_in.add(l)
            temp_out.add(temp_in)

        # matrix
        dots = dots_in_grid(len(self.q)).scale(0.5)
   
        for i in np.random.permutation(len(self.q)):
            for j in np.random.permutation(len(self.q)):
                self.play(Create(temp_out[i][j]), run_time=0.005)
            #self.play(Transform(temp_out[i], dots[i]))

        self.wait()

        tracker = self.add_voiceover_text(self.text[idx+12])  
        self.play(FadeOut(temp_out))
        self.wait(tracker.get_remaining_duration(buff=0.5))  

        # dot product 
        tracker = self.add_voiceover_text(text[idx+13]); self.wait(tracker.get_remaining_duration(buff=0.5))  

    def intro(self, idx):
        tmp = Tex("Attention")
        with self.voiceover(self.text[idx]) as tracker:
            self.play(FadeIn(tmp))
        self.play(FadeOut(tmp), run_time=0.5)

        with self.voiceover(self.text[idx+1]) as tracker: 
            self.play(Write(self.t))
        

        with self.voiceover(self.text[idx+2]) as tracker:
            self.wait_until_bookmark('a')
            self.play(Indicate(self.t[0]), Indicate(self.t[-1]))
        

        tmp = VGroup(self.bar.copy(), self.bar.copy(), self.bar.copy()).arrange(RIGHT).scale(0.5)
        with self.voiceover(self.text[idx+3]) as tracker:
            for i in range(len(self.t)):
                self.play(GrowFromPoint(tmp.next_to(self.t[i]), self.t[i].get_center()), run_time=tracker.duration/len(self.t))
        self.remove(tmp)
        self.wait()

    def qk_vectors(self, idx):

         # separate t and tc to each sides
        with self.voiceover(self.text[idx]) as tracker:
            self.play(self.t.animate.to_edge(LEFT), self.tc.animate.to_edge(RIGHT), run_time=tracker.duration)
        # Some explanations
        tracker = self.add_voiceover_text(self.text[idx+1]); self.wait(tracker.get_remaining_duration(buff=0.5))
        tracker = self.add_voiceover_text(self.text[idx+2]); self.wait(tracker.get_remaining_duration(buff=0.5))
        
        # Make querys
        with self.voiceover(self.text[idx+3]) as tracker:
            self.play(*[GrowFromPoint(self.q[i].next_to(self.t[i], RIGHT), self.t[i].get_center()) for i in range(len(self.q))], run_time=tracker.duration)
        # call it as q
        tracker = self.add_voiceover_text(self.text[idx+4]); self.wait(tracker.get_remaining_duration(buff=0.5))
        
        # Make keys
        with self.voiceover(self.text[idx+5]) as tracker:
            self.play(*[GrowFromPoint(self.k[i].next_to(self.tc[i], LEFT), self.tc[i].get_center()) for i in range(len(self.q))], run_time=tracker.duration)
        # call it as k    
        tracker = self.add_voiceover_text(self.text[idx+6]); self.wait(tracker.get_remaining_duration(buff=0.5))
        

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

        text = []
        for i in n:
            text.append("""<lang xml:lang="ko-KR">""" + i +"""</lang>""")

        return text
        


def dots_in_grid(n):
    v = VGroup()
    for i in range(n):
        vv = VGroup()
        for j in range(n):
            vv.add(Dot())
        vv.arrange(RIGHT)
        v.add(vv)
    v.arrange(DOWN)

    return v
                
        
def setup_text_box():
    vg_1 = VGroup()
    vg_2 = VGroup()
    box = Rectangle(height=1, width=3)

    # The animal did not cross the road because it was too tired. The animal did not cross the road because it was too wide.

    text_1 = "[START] The animal did not cross the road because it was too tired [END]".split()
    text_2 = "[START] The animal did not cross the road because it was too wide [END]".split()
    text_1 = [Tex(i).scale(1) for i in text_1]
    text_2 = [Tex(i).scale(1) for i in text_2]

    for i in text_1:
        temp = VGroup(i.copy(), box.copy())
        vg_1.add(temp)

    vg_1.arrange(DOWN, buff=0)

    for i in text_2:
        temp = VGroup(i.copy(), box.copy())
        vg_2.add(temp)

    vg_2.arrange(DOWN, buff=0)

    return vg_1, vg_2

