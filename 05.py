from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

import numpy as np

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

        text = []
        for i in n:
            text.append("""<lang xml:lang="ko-KR">""" + i +"""</lang>""")

        return text
    
    def construct(self):
        text = self.speech_setup("05.txt")
        self.text = text

        self.function_1(1)

        self.wait()

    def function_1(self, idx):
        q = VGroup(*[Rectangle(width=8, height=1).set_fill(random_color(), opacity=0.8) for i in range(5)]).arrange(DOWN, buff=0.5).scale(0.3).to_edge(LEFT)
        k = VGroup(*[Rectangle(width=8, height=1).set_fill(random_color(), opacity=0.8) for i in range(5)]).arrange(DOWN, buff=0.5).scale(0.3).to_edge(RIGHT)
        dots = VGroup(*[VGroup(*[Dot() for i in range(5)]).arrange(RIGHT) for j in range(5)]).arrange(DOWN)
        Q = MathTex(r"Q").next_to(q.get_top(), UP)
        K = MathTex(r"K").add_updater(lambda m: m.next_to(k.get_top(), UP))
        KT = MathTex(r"K^T").add_updater(lambda m: m.next_to(k.get_top(), UP))

        with self.voiceover(self.text[idx]) as tracker:
            self.play(Write(q), Write(k), Write(Q), Write(K), run_time=tracker.duration)

        with self.voiceover(self.text[idx+1]) as tracker:
            self.play(k.animate.next_to(q), run_time=tracker.duration)

        with self.voiceover(self.text[idx+2]) as tracker:
            pass

        with self.voiceover(self.text[idx+3]) as tracker:
            pass

        with self.voiceover(self.text[idx+4]) as tracker:
            self.play(Transform(K, KT), Rotate(k, PI, axis=np.array([-1, 1, 0])), run_time=tracker.duration)
        K.clear_updaters()

        for i in range(5):
            for j in range(5):
                self.play(Indicate(q[i]), Indicate(k[j]), run_time=0.1)
                self.add(dots[i][j])

        with self.voiceover(self.text[idx+5]) as tracker:
            pass


