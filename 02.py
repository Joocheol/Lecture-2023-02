from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

from transformer_functions import *

# Multi head attention

class Explainer(VoiceoverScene):
    def construct(self):

        box = setup_text_box()
        
        self.play(box[0].rotate(-PI/2).animate.to_edge(LEFT))

        rect_1 = Rectangle(width=3, height=0.2).set_fill(YELLOW, opacity=0.5)
        rect_2 = Rectangle(width=3, height=0.2).set_fill(WHITE, opacity=0.5)
        rect_3 = Rectangle(width=3, height=0.2).set_fill(BLUE, opacity=0.5)

        rect = VGroup(rect_1, rect_2, rect_3).arrange(DOWN, buff=0.1)
        self.play(rect.animate.next_to(box[0][0], RIGHT))
        
        self.wait()