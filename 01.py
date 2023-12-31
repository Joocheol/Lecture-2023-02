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
        self.ca()




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

        start_idx = 23

        tracker = self.add_voiceover_text(text[start_idx+0])
        self.add(v)
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+1])
        self.play(ReplacementTransform(v[1].copy().background_mobject, ca.background_mobject))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+2])
        self.play(Write(ca.code[0][0:21]), Write(ca.code[0][-2:]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+3])
        self.play(Write(ca.code[0][21:-2]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+4])
        self.play(Write(ca.code[1][:10]), Write(ca.code[1][-2:]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+5])
        self.play(Write(ca.code[1][10:-2]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+6])
        self.play(Write(ca.code[3]), Write(ca.code[4]), Write(ca.code[5][:-1]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        archi = archi_setup()
        archi = archi.add(archi_arrows_setup(archi[0][0], archi[0][1], archi[1][0], archi[1][1], archi[1][2])).scale(0.6)
        
        
        tracker = self.add_voiceover_text(text[start_idx+7])
        ca.background_mobject.save_state()
        self.play(ca.background_mobject.animate.set(color=BLACK))
        self.play(FadeIn(archi.to_edge(RIGHT)))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+8])
        self.play(Indicate(archi[1][1][0]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+9])
        self.play(Indicate(archi[2][12]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+10])
        self.play(Indicate(archi[2][6]), Indicate(archi[2][7]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+11])
        self.play(Indicate(archi[1][1][0]))
        self.play(Indicate(archi[2][12]))
        self.play(Indicate(archi[2][6]), Indicate(archi[2][7]))
        self.play(Indicate(archi[1][1][0]))
        self.play(Indicate(archi[2][12]))
        self.play(Indicate(archi[2][6]), Indicate(archi[2][7]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        self.play(FadeOut(archi))
        ca.background_mobject.restore()

        tracker = self.add_voiceover_text(text[start_idx+12])
        self.play(Write(ca.code[2:6]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        # A
        tracker = self.add_voiceover_text(text[start_idx+13])
        self.play(Write(ca.code[7:9]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+14])
        ca.background_mobject.save_state()
        self.play(ca.background_mobject.animate.set(color=BLACK))
        self.play(FadeIn(archi.to_edge(RIGHT)))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+15])
        self.play(Indicate(archi[2][13]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+16])
        dot = Dot()
        self.play(dot.animate.move_to(archi[1][1][1].get_center()))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+17])
        self.play(Indicate(ca.code[7:9]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+18])
        self.play(Indicate(ca.code[7:9]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        self.play(Write(ca.code[9]))
        self.play(FadeOut(dot))
        self.play(FadeOut(archi))

        tracker = self.add_voiceover_text(text[start_idx+19])
        ca.background_mobject.restore()
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+20])
        self.play(FadeOut(ca), run_time=10)
        self.wait(tracker.get_remaining_duration(buff=0.5))



    def base(self):

        ba, ca, gsa, csa, v = code_setup()

        with open("narration.txt", "r") as f:
            n = f.read()
        n = n.splitlines()

        text = []
        for i in n:
            text.append("""<lang xml:lang="ko-KR">""" + i +"""</lang>""")

        start_idx = 6

        tracker = self.add_voiceover_text(text[start_idx+0])
        self.add(v)
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+1])
        self.play(ReplacementTransform(v[0].copy().background_mobject, ba.background_mobject))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+2])
        self.play(Write(ba.code[0][0:20]), Write(ba.code[0][41:]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+3])
        self.play(Write(ba.code[0][20:41]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+4])
        self.play(Write(ba.code[1]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+5])
        self.play(Write(ba.code[2]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+6])
        self.play(Write(ba.code[3][0:12]), Write(ba.code[4][0:18]), Write(ba.code[5][0:12]))
        self.wait(tracker.get_remaining_duration(buff=0.5))
        self.wait()

        tracker = self.add_voiceover_text(text[start_idx+7])
        self.play(Write(ba.code[3][29:48]), Write(ba.code[3][56]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+8])
        self.play(Write(ba.code[4][35:54]), Write(ba.code[4][54]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+9])
        self.play(Write(ba.code[5][29:]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+10])
        self.play(Write(ba.code[3][12:29]), Write(ba.code[4][18:35]), Write(ba.code[5][12:29]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        tracker = self.add_voiceover_text(text[start_idx+11])
        self.add(ba.code[3][48:56])
        self.play(Indicate(ba.code[3][48:56]))
        self.wait(tracker.get_remaining_duration(buff=0.5))

        self.add(ba.code[10])
        with self.voiceover(text[start_idx+12]) as tracker:
            self.play(Transform(ba.code[10][33:57], ba.code[1][20:28]), run_time=tracker.duration)
      
        with self.voiceover(text[start_idx+13]) as tracker:
            self.play(Transform(ba.code[1][20:28], ba.code[3][48:56]), run_time=tracker.duration)
        self.play(FadeOut(ba.code[10]))

        tracker = self.add_voiceover_text(text[start_idx+14])
        self.play(FadeOut(ba.background_mobject), FadeOut(ba.code[:-2]), run_time=10)
        self.wait(tracker.get_remaining_duration(buff=0.5))


        self.wait()
