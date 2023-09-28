from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

from transformer_functions import *
from constants import *

class Explainer(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-JennyMultilingualNeural",
                style="newscast-casual",
            )
        )

        archi = archi_setup()
        boxes = boxes_setup()
        ba, ca, gsa, csa, v = code_setup()

        a = archi_arrows_setup(archi[0][0], archi[0][1], archi[1][0], archi[1][1], archi[1][2])
        aa = box_arrows_setup(boxes[0], boxes[1][0], boxes[1][1], boxes[1][2])

        # self.explain_architecture()
        self.base()
        # self.ca()




    def explain_architecture(self):

        with open("narration.txt", "r") as f:
            n = f.read()
        n = n.splitlines()

        text = []
        for i in n:
            text.append("""<lang xml:lang="ko-KR">""" + i +"""</lang>""")

        archi = archi_setup()
        archi = archi.add(archi_arrows_setup(archi[0][0], archi[0][1], archi[1][0], archi[1][1], archi[1][2])).scale(0.6)
        boxes = boxes_setup()
        boxes = boxes.add(box_arrows_setup(boxes[0], boxes[1][0], boxes[1][1], boxes[1][2])).scale(0.3)
        
        # self.play(Write(archi))
        # self.wait()
        
        # self.play(FadeOut(archi))
        # self.wait()

        # self.play(Write(archi[0]))
        # self.wait()

        # self.play(FadeOut(archi[0]))
        # self.wait()

        # self.play(Write(archi[1]))
        # self.wait()

        # self.play(FadeOut(archi[1]))
        # self.wait()

        # self.play(Write(archi[0][0])) # gsa
        # self.wait()
        # self.play(FadeOut(archi[0][0]))
        # self.wait()

        # self.play(Write(archi[0][1])) # encoder ff
        # self.wait()
        # self.play(FadeOut(archi[0][1]))
        # self.wait()

        # self.play(Write(archi[1][0])) # mmha
        # self.wait()
        # self.play(FadeOut(archi[1][0]))
        # self.wait()

        # self.play(Write(archi[1][1])) # ca
        # self.wait()
        # self.play(FadeOut(archi[1][1]))
        # self.wait()

        # self.play(Write(archi[1][2])) # decoder ff
        # self.wait()
        # self.play(FadeOut(archi[1][2]))
        # self.wait()

        # # archi connetions
        # self.play(Write(archi[2]))
        # self.wait()
        # self.play(FadeOut(archi[2]))
        # self.wait()

        # self.play(Write(archi[2][0])) # 2/3
        # self.wait()
        # self.play(FadeOut(archi[2][0]))
        # self.wait()

        # self.play(Write(archi[2][1])) # 1/3
        # self.wait()
        # self.play(FadeOut(archi[2][1]))
        # self.wait()

        # self.play(Write(archi[2][2])) # 3/3
        # self.wait()
        # self.play(FadeOut(archi[2][2]))
        # self.wait()

        # self.play(Write(archi[2][3])) # to add and norm
        # self.wait()
        # self.play(FadeOut(archi[2][3]))
        # self.wait()

        # self.play(Write(archi[2][4])) # gsa -> ff
        # self.wait()
        # self.play(FadeOut(archi[2][4]))
        # self.wait()

        # self.play(Write(archi[2][5])) # to add and norm
        # self.wait()
        # self.play(FadeOut(archi[2][5]))
        # self.wait()

        # self.play(Write(archi[2][6])) # important 1/3
        # self.wait()
        # self.play(FadeOut(archi[2][6]))
        # self.wait()

        # self.play(Write(archi[2][7])) # important 2/3
        # self.wait()
        # self.play(FadeOut(archi[2][7]))
        # self.wait()

        # self.play(Write(archi[2][8])) # decoder part start 2/3
        # self.wait()
        # self.play(FadeOut(archi[2][8]))
        # self.wait()

        # self.play(Write(archi[2][9])) # 1/3
        # self.wait()
        # self.play(FadeOut(archi[2][9]))
        # self.wait()

        # self.play(Write(archi[2][10])) # 3/3
        # self.wait()
        # self.play(FadeOut(archi[2][10]))
        # self.wait()

        # self.play(Write(archi[2][11])) ## to add & norm
        # self.wait()
        # self.play(FadeOut(archi[2][11]))
        # self.wait()

        # self.play(Write(archi[2][12])) # important 3/3
        # self.wait()
        # self.play(FadeOut(archi[2][12]))
        # self.wait()

        # self.play(Write(archi[2][13])) # to add and norm
        # self.wait()
        # self.play(FadeOut(archi[2][13]))
        # self.wait()

        # self.play(Write(archi[2][14])) # straight
        # self.wait()
        # self.play(FadeOut(archi[2][14]))
        # self.wait()

        # self.play(Write(archi[2][15])) # to add & norm
        # self.wait()
        # self.play(FadeOut(archi[2][15]))
        # self.wait()

        # self.play(Write(archi[2][16])) # to output
        # self.wait()
        # self.play(FadeOut(archi[2][16]))
        # self.wait()




        # self.play(Write(archi))
        # self.wait()
        # self.play(FadeOut(archi))
        # self.wait()
        # self.play(Write(boxes[0:2]))
        # self.wait()
        # self.play(FadeOut(boxes[0:2]))
        # self.play(Write(boxes[2]))
        # self.wait()
        # self.play(FadeOut(boxes[2]))
        # self.wait()

        # self.play(Write(boxes[2][0]))
        # self.wait()
        # self.play(FadeOut(boxes[2][0]))
        # self.wait()

        # self.play(Write(boxes[2][1])) # polygon
        # self.wait()
        # self.play(FadeOut(boxes[2][1]))
        # self.wait()

        # self.play(Write(boxes[2][7])) # last
        # self.wait()
        # self.play(FadeOut(boxes[2][7]))
        # self.wait()

        # self.play(Write(boxes))
        # self.wait()
        # self.play(FadeOut(boxes))
        # self.wait()

        
        with self.voiceover(text=text[0]) as tracker:
            self.play(Write(archi.scale(0.6)), run_time=tracker.duration)

        with self.voiceover(text=text[1]) as tracker:
            pass

        with self.voiceover(text=text[2]) as tracker:
            pass
        self.wait(1)

        # with self.voiceover(text="""<lang xml:lang="ko-KR">
        #                     이 그림을 다른 형식으로 표현해보겠습니다. 
        #                     </lang>""") as tracker:
        #     self.play(ReplacementTransform(VGroup(archi, a), boxes.add(aa).scale(0.4)), run_time=tracker.duration)
        # self.wait(1)

        # with self.voiceover(text="""<lang xml:lang="ko-KR">
        #                     여전히 복잡하지만, 아까보다는 좀 나아진 것 같습니다.
        #                     </lang>""") as tracker:
        #     pass
        # self.wait(1)

        # with self.voiceover(text="""<lang xml:lang="ko-KR">
        #                     이 모형의 입력 부분은 어디일까요?
        #                     </lang>""") as tracker:
        #     pass
        # self.wait(1)

        # with self.voiceover(text="""<lang xml:lang="ko-KR">
        #                     여기가 입력 부분입니다.
        #                     </lang>""") as tracker:
        #     self.play(Indicate(boxes[0][0][0]), run_time=tracker.duration)
    
        # self.play(boxes[0][0][0].animate.set(color=YELLOW)) 

        # with self.voiceover(text="""<lang xml:lang="ko-KR">
        #                     프랑스어로 나는 학생입니다 라는 문장이 적혀 있습니다. 
        #                     또한 문장의 제일 앞에 start 라는 표시가 있고,
        #                     제일 마지막에는 end 라는 표시가 있습니다.
        #                     </lang>""") as tracker:
        #     pass
        # self.wait(1)

        # with self.voiceover(text="""<lang xml:lang="ko-KR">
        #                     그러면 이 모형의 출력 부분은 어디에 있을까요?
        #                     </lang>""") as tracker:
        #     pass
        # self.wait(1)

        # with self.voiceover(text="""<lang xml:lang="ko-KR">
        #                     여기가 출력 부분입니다.
        #                     </lang>""") as tracker:
        #     self.play(Indicate(boxes[1][2][1]), run_time=tracker.duration)
    
        # self.play(boxes[1][2][1].animate.set(color=YELLOW)) 

        # with self.voiceover(text="""<lang xml:lang="ko-KR">
        #                     프랑스어에 대한 번역으로 I am a student 가 나오기를 바라는 것입니다.
        #                     제일 마지막에 end 라는 표시가 있다는 것을 기억하기 바랍니다.
        #                     </lang>""") as tracker:
        #     pass
        # self.wait(1)

        # with self.voiceover(text="""<lang xml:lang="ko-KR">
        #                     그러면 이 곳은 어떠한 역할을 하는 것일까요?
        #                     </lang>""") as tracker:
        #     self.play(Indicate(boxes[1][0][0][0]), run_time=tracker.duration)
        # self.wait(1)



        # self.play(FadeOut(boxes))
        

        

    def ca(self):

        ba, ca, gsa, csa, v = code_setup()

        with open("narration.txt", "r") as f:
            n = f.read()
        n = n.splitlines()

        text = []
        for i in n:
            text.append("""<lang xml:lang="ko-KR">""" + i +"""</lang>""")

        start_idx = 6

        with self.voiceover(text=text[start_idx+0]) as tracker:
            pass

        with self.voiceover(text=text[start_idx+1]) as tracker:
            pass

        with self.voiceover(text=text[start_idx+2]) as tracker:
            pass

        with self.voiceover(text=text[start_idx+3]) as tracker:
            pass

        with self.voiceover(text=text[start_idx+4]) as tracker:
            pass

        with self.voiceover(text=text[start_idx+5]) as tracker:
            pass

        with self.voiceover(text=text[start_idx+6]) as tracker:
            pass


        # with self.voiceover(text="""<lang xml:lang="ko-KR">
                            
        #                     </lang>""") as tracker:
        #     self.wait()
        # self.wait(1)

        # self.play(ReplacementTransform(v[1].copy().background_mobject, ca.background_mobject))
        # with self.voiceover(text="""<lang xml:lang="ko-KR">
                            
        #                     </lang>""") as tracker:
        #     self.wait()
        # self.wait(1)

        # self.add(ca.code[0][0:20], ca.code[0][41:])
        # with self.voiceover(text="""<lang xml:lang="ko-KR">
                            
        #                     </lang>""") as tracker:
        #     self.wait()
        # self.wait(1)
                
        # self.add(ba.code[0][20:41])
        # with self.voiceover(text="""<lang xml:lang="ko-KR">
                            
        #                     </lang>""") as tracker:
        #     self.wait(1)

        # self.add(ba.code[1])
        # with self.voiceover(text="""<lang xml:lang="ko-KR">
                           
        #                     </lang>""") as tracker:
        #     self.wait(2)

        # self.add(ba.code[2])
        # with self.voiceover(text="""<lang xml:lang="ko-KR">
                           
        #                     </lang>""") as tracker:
        #     self.wait()

        # self.add(ba.code[3][0:12], ba.code[4][0:17], ba.code[5][0:11])
        # with self.voiceover(text="""<lang xml:lang="ko-KR">
                            
        #                     </lang>""") as tracker:
        #     self.wait()
        # self.wait(3)

        # self.add(ba.code[3][28:47], ba.code[3][55])
        # with self.voiceover(text="""<lang xml:lang="ko-KR">
                            
        #                     </lang>""") as tracker:
        #     self.wait()

        # self.add(ba.code[4][34:])
        # with self.voiceover(text="""<lang xml:lang="ko-KR">
                            
        #                     </lang>""") as tracker:
        #     self.wait()

        # self.add(ba.code[5][28:])
        # with self.voiceover(text="""<lang xml:lang="ko-KR">
                            
        #                     </lang>""") as tracker:
        #     self.wait()

        # self.add(ba.code[3][12:28], ba.code[4][17:34], ba.code[5][11:38])
        # with self.voiceover(text="""<lang xml:lang="ko-KR">
                            
        #                     </lang>""") as tracker:
        #     self.wait()

        # self.add(ba.code[3][47:55])
        # self.play(Indicate(ba.code[3][47:55]))
        # with self.voiceover(text="""<lang xml:lang="ko-KR">
                            
        #                     </lang>""") as tracker:
        #     self.wait()

        # self.add(ba.code[10])
        # self.wait()
        
        # with self.voiceover(text="""<lang xml:lang="ko-KR">
                            
        #                     </lang>""") as tracker:
        #     self.play(Transform(ba.code[10][33:57], ba.code[3][47:55]), run_time=tracker.duration)

        # self.play(FadeOut(ba.code[10]))

        # with self.voiceover(text="""<lang xml:lang="ko-KR">
                            
        #                     </lang>""") as tracker:
        #     self.wait()
        
        # self.play(FadeOut(ba))
        # self.wait()


    def base(self):

        ba, ca, gsa, csa, v = code_setup()

        with open("narration.txt", "r") as f:
            n = f.read()
        n = n.splitlines()

        text = []
        for i in n:
            text.append("""<lang xml:lang="ko-KR">""" + i +"""</lang>""")

        start_idx = 6

        self.play(ReplacementTransform(v[0].copy().background_mobject, ba.background_mobject))
        with self.voiceover(text=text[start_idx+0]) as tracker:
            pass

        self.add(ba.code[0][0:20], ba.code[0][41:])
        with self.voiceover(text=text[start_idx+1]) as tracker:
            pass
 
        self.add(ba.code[0][20:41])
        with self.voiceover(text=text[start_idx+2]) as tracker:
            pass

        self.add(ba.code[1])
        with self.voiceover(text=text[start_idx+3]) as tracker:
            pass

        self.add(ba.code[2])
        with self.voiceover(text=text[start_idx+4]) as tracker:
            pass

        self.add(ba.code[3][0:12], ba.code[4][0:17], ba.code[5][0:11])
        with self.voiceover(text=text[start_idx+5]) as tracker:
            pass

        self.add(ba.code[3][28:47], ba.code[3][55])
        with self.voiceover(text=text[start_idx+6]) as tracker:
            pass





 












        self.add(ba.code[5][28:])


        self.add(ba.code[3][12:28], ba.code[4][17:34], ba.code[5][11:38])


        self.add(ba.code[3][47:55])
        self.play(Indicate(ba.code[3][47:55]))


        self.add(ba.code[10])

        
        # special
        self.play(Transform(ba.code[10][33:57], ba.code[3][47:55]), run_time=tracker.duration)

        self.play(FadeOut(ba.code[10]))

        
        self.play(FadeOut(ba))
        self.wait()
