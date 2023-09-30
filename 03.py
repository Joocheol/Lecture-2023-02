from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

import numpy as np

outer_radius = 0.16
class Explainer(VoiceoverScene):
    def construct(self):
        q = MobjectMatrix(
            [[Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=RED) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=RED) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=RED) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=RED) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=RED) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=RED) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=RED) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=RED) for i in [3,4,5,6,7]],]
            )
        
        k = MobjectMatrix(
            [[Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=YELLOW) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=YELLOW) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=YELLOW) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=YELLOW) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=YELLOW) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=YELLOW) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=YELLOW) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=YELLOW) for i in [3,4,5,6,7]],]
            )
        
        v = MobjectMatrix(
            [[Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=BLUE) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=BLUE) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=BLUE) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=BLUE) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=BLUE) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=BLUE) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=BLUE) for i in [3,4,5,6,7]],
             [Star(n=i, outer_radius=outer_radius, density=np.random.uniform(1,i/2,1), color=BLUE) for i in [3,4,5,6,7]],]
            )
        
        qc = q.copy()
        kc = k.copy()
        vc = v.copy()
        
        VGroup(q,k,v).arrange(RIGHT, buff=LARGE_BUFF*3).scale(0.4)
        
        self.play(Write(q))
        self.play(Write(k))
        self.play(Write(v))

       

        

        qt = MobjectMatrix([[qc[0][j + i] for i in range(0,40,5)] for j in range(5)])
        kt = MobjectMatrix([[kc[0][j + i] for i in range(0,40,5)] for j in range(5)])
        vt = MobjectMatrix([[vc[0][j + i] for i in range(0,40,5)] for j in range(5)])

        v = VGroup(qt,kt,vt).arrange(RIGHT).scale(0.4)

        self.play(Transform(q, qt))

        self.play(Indicate(qt.get_rows()[3]))