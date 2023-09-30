from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

import numpy as np

class Explainer(VoiceoverScene):
    def construct(self):

        t = setup_text_box()
        t = t[-1].scale(0.4)
        tc = t.copy()

        self.play(Write(t))
        self.play(t.animate.to_edge(LEFT), tc.animate.to_edge(RIGHT))

        bar = Rectangle(height=0.2, width=2)

        q = VGroup(*[bar.copy().set_fill(color=random_color(), opacity=0.8) for _ in range(len(t))]).arrange(DOWN, buff=0.2).next_to(t, RIGHT)
        k = VGroup(*[bar.copy().set_fill(color=random_color(), opacity=0.8) for _ in range(len(t))]).arrange(DOWN, buff=0.2).next_to(tc, LEFT)


        self.play(Write(q))
        self.wait()
        self.play(Write(k))
        self.wait()

        for i in range(len(t)):
            for j in range(len(t)):
                self.play(Create(Line(q[i].get_right(), k[j].get_left())), run_time=0.05)

def setup_text_box():
    vg_1 = VGroup()
    vg_2 = VGroup()
    vg_3 = VGroup()

    box = Rectangle(height=1, width=3)

    # The animal did not cross the road because it was too tired. The animal did not cross the road because it was too wide.

    text = "[START] The animal did not cross the road because it was too tired [END]".split()
    text = [Tex(i).scale(1) for i in text]

    for i in [0,1,2,3,-1]:
        temp = VGroup(text[i].copy(), box.copy())
        vg_1.add(temp)

    for i in [0,4,5,6,7]:
        temp = VGroup(text[i].copy(), box.copy())
        vg_2.add(temp)

    for i in [4,5,6,7,8]:
        temp = VGroup(text[i].copy(), box.copy())
        vg_3.add(temp)

    vg_1.arrange(DOWN, buff=0)
    vg_2.arrange(DOWN, buff=0)
    vg_3.arrange(DOWN, buff=0)

    vg_4 = VGroup()
    for i in text:
        temp = VGroup(i.copy(), box.copy())
        vg_4.add(temp)

    vg_4.arrange(DOWN, buff=0)

    return vg_1, vg_2, vg_3, vg_4
