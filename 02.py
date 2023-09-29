from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

from transformer_functions import *

# Multi head attention

class Explainer(VoiceoverScene):
    def construct(self):

        dots = VGroup(*[Dot() for _ in range(5)]).arrange(RIGHT)
        dots.generate_target()
        dots.target.arrange(DOWN)
        
        self.play(MoveToTarget(dots))
        self.play(dots.animate.to_edge(LEFT))

        qkv = VGroup(*[VGroup(Dot(color=RED), Dot(color=YELLOW), Dot(color=BLUE)).arrange(RIGHT, buff=0) for _ in range(5)]).arrange(DOWN).next_to(dots, RIGHT)
        self.play(Write(qkv))

        self.play(Indicate(qkv[4][1]))

        q = VGroup(*[Dot(color=RED) for _ in range(5)]).arrange(DOWN).move_to(1.5*LEFT)
        k = VGroup(*[Dot(color=YELLOW) for _ in range(5)]).arrange(RIGHT).move_to(1.5*DOWN)
        v = VGroup(*[Dot(color=BLUE) for _ in range(5)]).arrange(RIGHT).next_to(k, 2*RIGHT)

        qk = VGroup(*[VGroup(*[Dot() for _ in range(5)]).arrange(RIGHT) for _ in range(5)]).arrange(DOWN)
        kq = VGroup(*[VGroup(*[Dot() for _ in range(5)]).arrange(DOWN) for _ in range(5)]).arrange(RIGHT)

        attn_out = VGroup(*[Dot(color=TEAL) for _ in range(5)]).arrange(DOWN).to_edge(RIGHT)
       

        self.add(q, k, v)

        self.play(Write(qk))
        self.play(FadeOut(qk))

        self.play(Write(kq))
        self.play(FadeOut(kq))

        self.play(Write(attn_out))


        self.wait()