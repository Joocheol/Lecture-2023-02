from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

import numpy as np

class Explainer(VoiceoverScene):
    def construct(self):
        text, start_idx = self.speech_setup()

        t_1, t_2 = setup_text_box()
        t = t_1.scale(0.4)
        tc = t.copy()

        tmp = Tex("Attention")
        self.add(tmp)
        tracker = self.add_voiceover_text(text[start_idx+0]); self.play(FadeOut(tmp, run_time=tracker.duration)); self.wait(tracker.get_remaining_duration(buff=0.5))
        tracker = self.add_voiceover_text(text[start_idx+1]); self.play(Write(t)); self.wait(tracker.get_remaining_duration(buff=0.5))
        tracker = self.add_voiceover_text(text[start_idx+2]); self.wait(tracker.get_remaining_duration(buff=0.5))
        tracker = self.add_voiceover_text(text[start_idx+3]); self.play(t.animate.to_edge(LEFT), tc.animate.to_edge(RIGHT)); self.wait(tracker.get_remaining_duration(buff=0.5))
        tracker = self.add_voiceover_text(text[start_idx+4]); self.wait(tracker.get_remaining_duration(buff=0.5))
        tracker = self.add_voiceover_text(text[start_idx+5]); self.wait(tracker.get_remaining_duration(buff=0.5))
        tracker = self.add_voiceover_text(text[start_idx+6]); self.wait(tracker.get_remaining_duration(buff=0.5))
        tracker = self.add_voiceover_text(text[start_idx+7]); self.wait(tracker.get_remaining_duration(buff=0.5))
        tracker = self.add_voiceover_text(text[start_idx+8]); self.wait(tracker.get_remaining_duration(buff=0.5))

        bar = Rectangle(height=0.2, width=2)

        q = VGroup(*[bar.copy().set_fill(color=random_color(), opacity=0.8) for _ in range(len(t))]).arrange(DOWN, buff=0.2).next_to(t, RIGHT)
        k = VGroup(*[bar.copy().set_fill(color=random_color(), opacity=0.8) for _ in range(len(t))]).arrange(DOWN, buff=0.2).next_to(tc, LEFT)

        tracker = self.add_voiceover_text(text[start_idx+4]); self.play(*[GrowFromPoint(q[i], t[i].get_center()) for i in range(len(q))], run_time=tracker.duration); self.wait(tracker.get_remaining_duration(buff=0.5))
        tracker = self.add_voiceover_text(text[start_idx+5]); self.play(*[GrowFromPoint(k[i], tc[i].get_center()) for i in range(len(q))], run_time=tracker.duration); self.wait(tracker.get_remaining_duration(buff=0.5))


        temp_out = VGroup()
        for i in range(len(t)):
            temp_in = VGroup()
            for j in range(len(t)):
                l = Line(q[i].get_right(), k[j].get_left())
                temp_in.add(l)
            temp_out.add(temp_in)

        self.wait()


        dots =dots_in_grid(len(q)).scale(0.5)
        
        

   
        for i in np.random.permutation(len(q)):
            if i == 0:
                tracker = self.add_voiceover_text(text[start_idx+5])
                for j in np.random.permutation(len(q)):
                    self.play(Create(temp_out[i][j]), run_time=0.1)
                self.wait(tracker.get_remaining_duration(buff=0.5))
            else:
                for j in np.random.permutation(len(q)):
                    self.play(Create(temp_out[i][j]), run_time=0.1)
            self.play(Transform(temp_out[i], dots[i]))


    def speech_setup(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-JennyMultilingualNeural",
                style="newscast-casual",
            )
        )

        with open("attention.txt", "r") as f:
            n = f.read()
        n = n.splitlines()

        text = []
        for i in n:
            text.append("""<lang xml:lang="ko-KR">""" + i +"""</lang>""")

        start_idx = 1

        return text, start_idx
        


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

