from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

import numpy as np

# Multi head attention

tex_scale = 0.35

class Explainer(VoiceoverScene):
    def construct(self):

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

        q = VGroup(*[Dot() for _ in range(5)]).arrange(DOWN)
        k = VGroup(*[Dot() for _ in range(5)]).arrange(RIGHT)
        v = VGroup(*[Dot() for _ in range(5)]).arrange(RIGHT)
        VGroup(q, k, v).arrange(RIGHT, buff=MED_SMALL_BUFF)
        v.next_to(k, RIGHT, buff=LARGE_BUFF)
        k.next_to(q, DR, buff=MED_SMALL_BUFF)
        
        qk = VGroup(*[VGroup(*[Dot() for _ in range(5)]).arrange(RIGHT) for _ in range(5)]).arrange(DOWN).next_to(q, RIGHT, buff=MED_SMALL_BUFF)
        # kq = VGroup(*[VGroup(*[Dot() for _ in range(5)]).arrange(DOWN) for _ in range(5)]).arrange(RIGHT).next_to(q, RIGHT, buff=MED_SMALL_BUFF)

        # p = VGroup(*[VGroup(*[Rectangle(width=(qk[0][0].get_right()-qk[0][0].get_left()), height=np.random.uniform(0,0.08,1)) for _ in range(5)]).arrange(RIGHT) for _ in range(5)]).arrange(DOWN).next_to(q, RIGHT, buff=MED_SMALL_BUFF)
        p = VGroup(*[VGroup(*[Rectangle(width=0.16, height=np.random.uniform(0,0.16,1)) for _ in range(5)]).arrange(RIGHT) for _ in range(5)]).arrange(DOWN).next_to(q, RIGHT, buff=MED_SMALL_BUFF)

        dots = VGroup(*[bar() for _ in range(5)]).arrange(RIGHT)
        dots.generate_target()
        dots.target.arrange(DOWN)

        tracker = self.add_voiceover_text(text[start_idx+0])
        self.play(MoveToTarget(dots))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        self.play(MoveToTarget(dots))
        self.play(dots.animate.to_edge(LEFT))
        
        qkv = VGroup(*[VGroup(
                              Star(n=6, outer_radius=0.08, density=np.random.uniform(1,6/2,1), color=dots[i].get_color()),
                              Star(n=7, outer_radius=0.08, density=np.random.uniform(1,7/2,1), color=dots[i].get_color()), 
                              Star(n=8, outer_radius=0.08, density=np.random.uniform(1,8/2,1), color=dots[i].get_color())
                              ).arrange(RIGHT) for i in range(5)]
                    ).arrange(DOWN).next_to(dots, RIGHT)
        
        

        

        attn_out = VGroup(*[Dot(color=TEAL) for _ in range(5)]).arrange(DOWN).next_to(v, RIGHT, buff=2*LARGE_BUFF)
       

        
        

        self.play(Write(qkv))

        self.play(FadeIn(q))
        self.play(FadeIn(k))
        

        self.play(Indicate(q))
        self.play(FadeOut(q))
        self.play(*[qkv[i][0].animate.move_to(q[i]) for i in range(5)])

        qbar = VGroup(*[bar().set_fill(dots[i].get_color(), opacity=0.2) for i in range(5)]).arrange(DOWN).next_to(q, RIGHT)
        self.play(Write(qbar))
        

        self.wait()
        self.play(Indicate(k))
        self.play(FadeOut(k))
        self.play(*[qkv[i][1].animate.move_to(k[i]) for i in range(5)])
        
        vbar = VGroup(*[bar().set_fill(dots[i].get_color(), opacity=0.2).rotate(PI/2) for i in range(5)]).arrange(RIGHT).next_to(k, UP)
        self.play(Write(vbar))
        self.wait()

        self.play(Indicate(qkv[0][0]))
        self.play(Write(qk), run_time=10)

        self.play(Transform(qk, p), run_time=3)
        
        self.play(FadeIn(v))
        self.play(Indicate(v))
        self.play(FadeOut(v))
        self.play(*[qkv[i][2].animate.move_to(v[i]) for i in range(5)])
        self.wait()


        
        

        self.play(Write(attn_out))


        self.wait()

def bar():
    return Rectangle(height=0.16, width=1).set_fill(color=random_color(), opacity=0.8)