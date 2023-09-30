from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

from transformer_functions import *
import numpy as np

# Multi head attention

class Explainer(VoiceoverScene):
    def construct(self):

        q = VGroup(*[Dot(color=RED) for _ in range(5)]).arrange(DOWN)
        k = VGroup(*[Dot(color=YELLOW) for _ in range(5)]).arrange(RIGHT)
        v = VGroup(*[Dot(color=BLUE) for _ in range(5)]).arrange(RIGHT)
        VGroup(q, k, v).arrange(RIGHT, buff=MED_SMALL_BUFF)
        v.next_to(k, RIGHT, buff=LARGE_BUFF)
        k.next_to(q, DR, buff=MED_SMALL_BUFF)
        
        qk = VGroup(*[VGroup(*[Dot() for _ in range(5)]).arrange(RIGHT) for _ in range(5)]).arrange(DOWN).next_to(q, RIGHT, buff=MED_SMALL_BUFF)
        kq = VGroup(*[VGroup(*[Dot() for _ in range(5)]).arrange(DOWN) for _ in range(5)]).arrange(RIGHT).next_to(q, RIGHT, buff=MED_SMALL_BUFF)

        # p = VGroup(*[VGroup(*[Rectangle(width=(qk[0][0].get_right()-qk[0][0].get_left()), height=np.random.uniform(0,0.08,1)) for _ in range(5)]).arrange(RIGHT) for _ in range(5)]).arrange(DOWN).next_to(q, RIGHT, buff=MED_SMALL_BUFF)
        p = VGroup(*[VGroup(*[Rectangle(width=0.16, height=np.random.uniform(0,0.16,1)) for _ in range(5)]).arrange(RIGHT) for _ in range(5)]).arrange(DOWN).next_to(q, RIGHT, buff=MED_SMALL_BUFF)

        dots = VGroup(*[Dot() for _ in range(5)]).arrange(RIGHT)
        dots.generate_target()
        dots.target.arrange(DOWN)

        self.play(MoveToTarget(dots))
        self.play(dots.animate.next_to(q, LEFT*2, buff=2*LARGE_BUFF))
        
        qkv = VGroup(*[VGroup(
                              Star(n=6, outer_radius=0.08, density=np.random.uniform(1,5/2,1), color=RED),
                              Star(n=7, outer_radius=0.08, density=np.random.uniform(1,6/2,1), color=YELLOW), 
                              Star(n=8, outer_radius=0.08, density=np.random.uniform(1,7/2,1), color=BLUE)
                              ).arrange(RIGHT) for _ in range(5)]
                    ).arrange(DOWN).next_to(dots, RIGHT)

        

        attn_out = VGroup(*[Dot(color=TEAL) for _ in range(5)]).arrange(DOWN).next_to(v, RIGHT, buff=2*LARGE_BUFF)
       

        
        

        self.play(Write(qkv))

        self.play(FadeIn(q))
        self.play(FadeIn(k))
        self.play(FadeIn(v))

        self.play(Indicate(q))
        self.play(FadeOut(q))
        self.play(*[qkv[i][0].animate.move_to(q[i]) for i in range(5)])
        self.wait()
        self.play(Indicate(k))
        self.play(FadeOut(k))
        self.play(*[qkv[i][1].animate.move_to(k[i]) for i in range(5)])
        self.wait()

        self.play(Indicate(qkv[0][0]))
        self.play(Write(qk), run_time=10)

        self.play(Transform(qk, p), run_time=3)
        
        
        self.play(Indicate(v))
        self.play(FadeOut(v))
        self.play(*[qkv[i][2].animate.move_to(v[i]) for i in range(5)])
        self.wait()


        
        

        self.play(Write(attn_out))


        self.wait()