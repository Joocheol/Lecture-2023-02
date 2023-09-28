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
        a1, a2, a3, a4, a5, a6, a7, a8 = box_arrows_setup(boxes[0], boxes[1][0], boxes[1][1], boxes[1][2])

        self.explain_architecture( archi, a, boxes, a1, a2, a3, a4, a5, a6, a7, a8)
        # self.base(ba, ca, gsa, csa, v)
        # self.ca(ba, ca, gsa, csa, v)




    def explain_architecture(self, archi, a, boxes, a1, a2, a3, a4, a5, a6, a7, a8):

        self.play(Write(archi.scale(0.6)))
        self.play(Write(a.scale(0.6)))

        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            이것이 transformer 아키텍쳐입니다.
                            보기만 해도 어지럽습니다.
                            </lang>""") as tracker:
            self.wait()
        self.wait(0.5)

        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            우리의 목표는 여기에 보이는 모든 부분을, 하나도 남김없이 모두 이해하는 것입니다.
                            </lang>""") as tracker:
            self.wait()
        self.wait(1)

        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            이 그림을 다른 형식으로 표현해보겠습니다. 
                            </lang>""") as tracker:
            self.play(ReplacementTransform(VGroup(archi, a), boxes.add(a1, a2, a3, a4, a5, a6, a7, a8).scale(0.4)), run_time=tracker.duration)
        self.wait(1)

        self.play(FadeOut(boxes))
        self.play(FadeIn(VGroup(archi.copy(), a.copy())))

        

    def ca(self, ba, ca, gsa, csa, v):

        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            이번에는 cross attention 부분을 어떻게 구현하는가를 살펴보겠습니다.
                            앞에서 만들었던 base attetion을 이용할 것입니다.
                            </lang>""") as tracker:
            self.wait()
        self.wait(1)

        self.play(ReplacementTransform(v[1].copy().background_mobject, ca.background_mobject))
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            시작해보겠습니다.
                            </lang>""") as tracker:
            self.wait()
        self.wait(1)

        self.add(ca.code[0][0:20], ca.code[0][41:])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            이 클래스의 이름은 cross attention입니다. 
                            </lang>""") as tracker:
            self.wait()
        self.wait(1)
                
        self.add(ba.code[0][20:41])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            이 클래스는 앞에서 만들었던 base attention을 상속받습니다.
                            따라서 굳이 m h a, add 등을 설정하지 않아도 사용할 수 있습니다.
                            </lang>""") as tracker:
            self.wait(1)

        self.add(ba.code[1])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            이제 base attention class가 만들어질 때 초기화해야 하는 일을 정의하겠습니다.
                            </lang>""") as tracker:
            self.wait(2)

        self.add(ba.code[2])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            super는 나의 상위 클래스를 의미합니다. 즉, default라고 설명했던 keras layer를 초기화하는 것입니다. 이것도 default라고 생각하면 됩니다.
                            </lang>""") as tracker:
            self.wait()

        self.add(ba.code[3][0:12], ba.code[4][0:17], ba.code[5][0:11])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            이제 세개의 변수를 정의하겠습니다. 이 세가지 변수만 정의하면 base attention은 끝입니다. 일단, 이름을 보고 무엇을 만들지 짐작해보기 바랍니다.
                            </lang>""") as tracker:
            self.wait()
        self.wait(3)

        self.add(ba.code[3][28:47], ba.code[3][55])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            Multi head attention이라는 layer를 부르고, 그것을 m h a라는 변수에 넣습니다.
                            </lang>""") as tracker:
            self.wait()

        self.add(ba.code[4][34:])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            다음으로는 layer normalization이라는 layer를 부르고 그것을 layernorm에 넣습니다. 
                            이 layer의 구체적인 역할에 대해서는 다시 설명하겠지만, 기본적으로 모형이 더 빠르게 수렴하게 하는 역할을 합니다.
                            </lang>""") as tracker:
            self.wait()

        self.add(ba.code[5][28:])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            마지막 layer는 더하기 layer입니다. 
                            Transformer 아키텍쳐를 기억해 보면, Add and Norm 이라는 부분이 있었습니다. 
                            그 부분을 구현하기 위해서 필요한 layer입니다.
                            </lang>""") as tracker:
            self.wait()

        self.add(ba.code[3][12:28], ba.code[4][17:34], ba.code[5][11:38])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            지금까지 만든 모든 layer는 다 keras layer입니다. 따라서 앞에 tf keras layers 라고 붙여주어야 합니다.
                            </lang>""") as tracker:
            self.wait()

        self.add(ba.code[3][47:55])
        self.play(Indicate(ba.code[3][47:55]))
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            마지막으로 이 부분. keyword arguments 부분이 굉장히 신경쓰일텐데, 이것은 나중에 이 클래스를 부를 때 보내주는 인자를 받아오기 위한 것입니다.
                            </lang>""") as tracker:
            self.wait()

        self.add(ba.code[10])
        self.wait()
        
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            예를 들어, 이렇게 인자들을 보내면, 이것을 여기에서 받아옵니다.
                            </lang>""") as tracker:
            self.play(Transform(ba.code[10][33:57], ba.code[3][47:55]), run_time=tracker.duration)

        self.play(FadeOut(ba.code[10]))

        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            이상의 base attention class를 기반으로 세가지의 서로 다른 attention을 구현해 보겠습니다.
                            </lang>""") as tracker:
            self.wait()
        
        self.play(FadeOut(ba))
        self.wait()


    def base(self, ba, ca, gsa, csa, v):

        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            이번 시간에는 세가지의 서로 다른 어텐션을 코드로 어떻게 구현하는가를 살펴보도록 하겠습니다.
                            TensorFlow code를 기준으로 살펴보지만, pi torch에서도 거의 같은 방법으로 사용됩니다.
                            </lang>""") as tracker:
            self.wait()

        self.play(ReplacementTransform(v[0].copy().background_mobject, ba.background_mobject))
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            시작해보겠습니다.
                            </lang>""") as tracker:
            self.wait()

        self.add(ba.code[0][0:20], ba.code[0][41:])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            우선 base attention이라는 이름을 갖는 클래스를 정의하겠습니다. 
                            이 클래스의 목적은 세가지의 서로 다른 어텐션에서 공통적으로 사용될 layer들을 미리 정의해 놓는 것입니다.
                            </lang>""") as tracker:
            self.wait(2)
                
        self.add(ba.code[0][20:41])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            TensorFlow의 모든 layer는 tf keras layers layer라는 상위 class로부터 상속을 받아야 합니다. 그냥 default라고 생각하면 됩니다.
                            </lang>""") as tracker:
            self.wait(2)

        self.add(ba.code[1])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            이제 base attention class가 만들어질 때 초기화해야 하는 일을 정의하겠습니다.
                            </lang>""") as tracker:
            self.wait(2)

        self.add(ba.code[2])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            super는 나의 상위 클래스를 의미합니다. 즉, default라고 설명했던 keras layer를 초기화하는 것입니다. 이것도 default라고 생각하면 됩니다.
                            </lang>""") as tracker:
            self.wait()

        self.add(ba.code[3][0:12], ba.code[4][0:17], ba.code[5][0:11])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            이제 세개의 변수를 정의하겠습니다. 이 세가지 변수만 정의하면 base attention은 끝입니다. 일단, 이름을 보고 무엇을 만들지 짐작해보기 바랍니다.
                            </lang>""") as tracker:
            self.wait()
        self.wait(3)

        self.add(ba.code[3][28:47], ba.code[3][55])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            Multi head attention이라는 layer를 부르고, 그것을 m h a라는 변수에 넣습니다.
                            </lang>""") as tracker:
            self.wait()

        self.add(ba.code[4][34:])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            다음으로는 layer normalization이라는 layer를 부르고 그것을 layernorm에 넣습니다. 
                            이 layer의 구체적인 역할에 대해서는 다시 설명하겠지만, 기본적으로 모형이 더 빠르게 수렴하게 하는 역할을 합니다.
                            </lang>""") as tracker:
            self.wait()

        self.add(ba.code[5][28:])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            마지막 layer는 더하기 layer입니다. 
                            Transformer 아키텍쳐를 기억해 보면, Add and Norm 이라는 부분이 있었습니다. 
                            그 부분을 구현하기 위해서 필요한 layer입니다.
                            </lang>""") as tracker:
            self.wait()

        self.add(ba.code[3][12:28], ba.code[4][17:34], ba.code[5][11:38])
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            지금까지 만든 모든 layer는 다 keras layer입니다. 따라서 앞에 tf keras layers 라고 붙여주어야 합니다.
                            </lang>""") as tracker:
            self.wait()

        self.add(ba.code[3][47:55])
        self.play(Indicate(ba.code[3][47:55]))
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            마지막으로 이 부분. keyword arguments 부분이 굉장히 신경쓰일텐데, 이것은 나중에 이 클래스를 부를 때 보내주는 인자를 받아오기 위한 것입니다.
                            </lang>""") as tracker:
            self.wait()

        self.add(ba.code[10])
        self.wait()
        
        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            예를 들어, 이렇게 인자들을 보내면, 이것을 여기에서 받아옵니다.
                            </lang>""") as tracker:
            self.play(Transform(ba.code[10][33:57], ba.code[3][47:55]), run_time=tracker.duration)

        self.play(FadeOut(ba.code[10]))

        with self.voiceover(text="""<lang xml:lang="ko-KR">
                            이상의 base attention class를 기반으로 세가지의 서로 다른 attention을 구현해 보겠습니다.
                            </lang>""") as tracker:
            self.wait()
        
        self.play(FadeOut(ba))
        self.wait()


# class B(VoiceoverScene):
#     def construct(self):
        
#         ca = make_box(5,5)
#         m = make_box(1,5)
#         m1 = m.copy()
#         m2 = m.copy()
#         m3 = m.copy()
#         m4 = m.copy()
#         t1, t2, t3 = setup_text_box()

#         gsa = VGroup(VGroup(t1, m1).arrange(UP, buff=0.5), m2).arrange(UP, buff=1)
#         mmha = VGroup(VGroup(t2, m3).arrange(UP, buff=0.5), m4).arrange(UP, buff=1)
#         ff = VGroup(m, t3).arrange(UP, buff=0.5)
#         decoder = VGroup(mmha, ca, ff).arrange(UP, buff=1)
#         boxes = VGroup(gsa, decoder).arrange(RIGHT, buff=2)
#         gsa.align_to(decoder, DOWN)

#         a1 = arrows_setup_1(gsa[0][0], gsa[0][1])
#         a2 = arrows_setup_3(gsa[0][1], gsa[1])
#         a3 = arrows_setup_2(gsa[1], ca)
#         a4 = arrows_setup_1(mmha[0][0], mmha[0][1])
#         a5 = arrows_setup_4(mmha[0][1], mmha[1])
#         a6 = arrows_setup_1(mmha[1], ca)
#         a7 = arrows_setup_1(ca[:5], ff[0])
#         a8 = arrows_setup_1(ff[0], ff[1])
#         boxes.add(a1, a2, a3, a4, a5, a6, a7, a8)


#         self.play(Write(boxes.scale(0.4)))
#         self.wait(10)

# class Transformer(Scene):
#     def construct(self):

#         mmha, mha, ann, ff = setup()

#         block_1 = VGroup(mha.copy(), Line(ORIGIN, UP*small_buff), ann.copy()).arrange(UP, buff=0)
#         block_2 = VGroup(ff.copy(), Line(ORIGIN, UP*small_buff), ann.copy()).arrange(UP, buff=0)
#         block_3 = VGroup(mmha.copy(), Line(ORIGIN, UP*small_buff), ann.copy()).arrange(UP, buff=0)
#         block_4 = VGroup(mha.copy(), Line(ORIGIN, UP*small_buff), ann.copy()).arrange(UP, buff=0)
#         block_5 = VGroup(ff.copy(), Line(ORIGIN, UP*small_buff), ann.copy()).arrange(UP, buff=0)

#         encoder = VGroup(block_1, block_2).arrange(UP, buff=1)
#         decoder = VGroup(block_3, block_4, block_5).arrange(UP, buff=block_buff)

#         transformer = VGroup(encoder, decoder).arrange(RIGHT, buff=btn)
#         encoder.align_to(decoder, DOWN)

#         transformer.add(*arrows_setup(block_1, block_2, block_3, block_4, block_5))

#         self.play(Write(transformer.scale(0.66)))
#         self.wait(5)

# class TFCode(VoiceoverScene):
#     def construct(self):
#         # Initialize speech synthesis using Azure's TTS API
#         self.set_speech_service(
#             AzureService(
#                 voice="en-US-JennyMultilingualNeural",
#                 style="newscast-casual",
#             )
#         )

#         ba = Code(file_name="code_ba.py", tab_width=4, insert_line_no=False, background="window", language="python").rescale_to_fit(12,0)
#         ca = Code(file_name="code_ca.py", tab_width=4, insert_line_no=False, background="window", language="python").rescale_to_fit(12,0)
#         gsa = Code(file_name="code_gsa.py", tab_width=4, insert_line_no=False, background="window", language="python").rescale_to_fit(12,0)
#         csa = Code(file_name="code_csa.py", tab_width=4, insert_line_no=False, background="window", language="python").rescale_to_fit(12,0)

#         v = VGroup(ba.copy(), ca.copy(), gsa.copy(), csa.copy()).arrange(RIGHT).scale(0.2).to_edge(UP)
#         self.add(v)

#         self.base(ba, ca, gsa, csa, v)
#         self.ca(ba, ca, gsa, csa, v)
#         # self.gsa(ba, ca, gsa, csa, v)
#         # self.csa(ba, ca, gsa, csa, v)

#     def ca(self, ba, ca, gsa, csa, v):

#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             이번에는 cross attention 부분을 어떻게 구현하는가를 살펴보겠습니다.
#                             앞에서 만들었던 base attetion을 이용할 것입니다.
#                             </lang>""") as tracker:
#             self.wait()
#         self.wait(1)

#         self.play(ReplacementTransform(v[1].copy().background_mobject, ca.background_mobject))
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             시작해보겠습니다.
#                             </lang>""") as tracker:
#             self.wait()
#         self.wait(1)

#         self.add(ca.code[0][0:20], ca.code[0][41:])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             이 클래스의 이름은 cross attention입니다. 
#                             </lang>""") as tracker:
#             self.wait()
#         self.wait(1)
                
#         self.add(ba.code[0][20:41])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             이 클래스는 앞에서 만들었던 base attention을 상속받습니다.
#                             따라서 굳이 m h a, add 등을 설정하지 않아도 사용할 수 있습니다.
#                             </lang>""") as tracker:
#             self.wait(1)

#         self.add(ba.code[1])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             이제 base attention class가 만들어질 때 초기화해야 하는 일을 정의하겠습니다.
#                             </lang>""") as tracker:
#             self.wait(2)

#         self.add(ba.code[2])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             super는 나의 상위 클래스를 의미합니다. 즉, default라고 설명했던 keras layer를 초기화하는 것입니다. 이것도 default라고 생각하면 됩니다.
#                             </lang>""") as tracker:
#             self.wait()

#         self.add(ba.code[3][0:12], ba.code[4][0:17], ba.code[5][0:11])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             이제 세개의 변수를 정의하겠습니다. 이 세가지 변수만 정의하면 base attention은 끝입니다. 일단, 이름을 보고 무엇을 만들지 짐작해보기 바랍니다.
#                             </lang>""") as tracker:
#             self.wait()
#         self.wait(3)

#         self.add(ba.code[3][28:47], ba.code[3][55])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             Multi head attention이라는 layer를 부르고, 그것을 m h a라는 변수에 넣습니다.
#                             </lang>""") as tracker:
#             self.wait()

#         self.add(ba.code[4][34:])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             다음으로는 layer normalization이라는 layer를 부르고 그것을 layernorm에 넣습니다. 
#                             이 layer의 구체적인 역할에 대해서는 다시 설명하겠지만, 기본적으로 모형이 더 빠르게 수렴하게 하는 역할을 합니다.
#                             </lang>""") as tracker:
#             self.wait()

#         self.add(ba.code[5][28:])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             마지막 layer는 더하기 layer입니다. 
#                             Transformer 아키텍쳐를 기억해 보면, Add and Norm 이라는 부분이 있었습니다. 
#                             그 부분을 구현하기 위해서 필요한 layer입니다.
#                             </lang>""") as tracker:
#             self.wait()

#         self.add(ba.code[3][12:28], ba.code[4][17:34], ba.code[5][11:38])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             지금까지 만든 모든 layer는 다 keras layer입니다. 따라서 앞에 tf keras layers 라고 붙여주어야 합니다.
#                             </lang>""") as tracker:
#             self.wait()

#         self.add(ba.code[3][47:55])
#         self.play(Indicate(ba.code[3][47:55]))
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             마지막으로 이 부분. keyword arguments 부분이 굉장히 신경쓰일텐데, 이것은 나중에 이 클래스를 부를 때 보내주는 인자를 받아오기 위한 것입니다.
#                             </lang>""") as tracker:
#             self.wait()

#         self.add(ba.code[10])
#         self.wait()
        
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             예를 들어, 이렇게 인자들을 보내면, 이것을 여기에서 받아옵니다.
#                             </lang>""") as tracker:
#             self.play(Transform(ba.code[10][33:57], ba.code[3][47:55]), run_time=tracker.duration)

#         self.play(FadeOut(ba.code[10]))

#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             이상의 base attention class를 기반으로 세가지의 서로 다른 attention을 구현해 보겠습니다.
#                             </lang>""") as tracker:
#             self.wait()
        
#         self.play(FadeOut(ba))
#         self.wait()


#     def base(self, ba, ca, gsa, csa, v):

#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             이번 시간에는 세가지의 서로 다른 어텐션을 코드로 어떻게 구현하는가를 살펴보도록 하겠습니다.
#                             TensorFlow code를 기준으로 살펴보지만, pi torch에서도 거의 같은 방법으로 사용됩니다.
#                             </lang>""") as tracker:
#             self.wait()

#         self.play(ReplacementTransform(v[0].copy().background_mobject, ba.background_mobject))
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             시작해보겠습니다.
#                             </lang>""") as tracker:
#             self.wait()

#         self.add(ba.code[0][0:20], ba.code[0][41:])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             우선 base attention이라는 이름을 갖는 클래스를 정의하겠습니다. 
#                             이 클래스의 목적은 세가지의 서로 다른 어텐션에서 공통적으로 사용될 layer들을 미리 정의해 놓는 것입니다.
#                             </lang>""") as tracker:
#             self.wait(2)
                
#         self.add(ba.code[0][20:41])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             TensorFlow의 모든 layer는 tf keras layers layer라는 상위 class로부터 상속을 받아야 합니다. 그냥 default라고 생각하면 됩니다.
#                             </lang>""") as tracker:
#             self.wait(2)

#         self.add(ba.code[1])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             이제 base attention class가 만들어질 때 초기화해야 하는 일을 정의하겠습니다.
#                             </lang>""") as tracker:
#             self.wait(2)

#         self.add(ba.code[2])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             super는 나의 상위 클래스를 의미합니다. 즉, default라고 설명했던 keras layer를 초기화하는 것입니다. 이것도 default라고 생각하면 됩니다.
#                             </lang>""") as tracker:
#             self.wait()

#         self.add(ba.code[3][0:12], ba.code[4][0:17], ba.code[5][0:11])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             이제 세개의 변수를 정의하겠습니다. 이 세가지 변수만 정의하면 base attention은 끝입니다. 일단, 이름을 보고 무엇을 만들지 짐작해보기 바랍니다.
#                             </lang>""") as tracker:
#             self.wait()
#         self.wait(3)

#         self.add(ba.code[3][28:47], ba.code[3][55])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             Multi head attention이라는 layer를 부르고, 그것을 m h a라는 변수에 넣습니다.
#                             </lang>""") as tracker:
#             self.wait()

#         self.add(ba.code[4][34:])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             다음으로는 layer normalization이라는 layer를 부르고 그것을 layernorm에 넣습니다. 
#                             이 layer의 구체적인 역할에 대해서는 다시 설명하겠지만, 기본적으로 모형이 더 빠르게 수렴하게 하는 역할을 합니다.
#                             </lang>""") as tracker:
#             self.wait()

#         self.add(ba.code[5][28:])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             마지막 layer는 더하기 layer입니다. 
#                             Transformer 아키텍쳐를 기억해 보면, Add and Norm 이라는 부분이 있었습니다. 
#                             그 부분을 구현하기 위해서 필요한 layer입니다.
#                             </lang>""") as tracker:
#             self.wait()

#         self.add(ba.code[3][12:28], ba.code[4][17:34], ba.code[5][11:38])
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             지금까지 만든 모든 layer는 다 keras layer입니다. 따라서 앞에 tf keras layers 라고 붙여주어야 합니다.
#                             </lang>""") as tracker:
#             self.wait()

#         self.add(ba.code[3][47:55])
#         self.play(Indicate(ba.code[3][47:55]))
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             마지막으로 이 부분. keyword arguments 부분이 굉장히 신경쓰일텐데, 이것은 나중에 이 클래스를 부를 때 보내주는 인자를 받아오기 위한 것입니다.
#                             </lang>""") as tracker:
#             self.wait()

#         self.add(ba.code[10])
#         self.wait()
        
#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             예를 들어, 이렇게 인자들을 보내면, 이것을 여기에서 받아옵니다.
#                             </lang>""") as tracker:
#             self.play(Transform(ba.code[10][33:57], ba.code[3][47:55]), run_time=tracker.duration)

#         self.play(FadeOut(ba.code[10]))

#         with self.voiceover(text="""<lang xml:lang="ko-KR">
#                             이상의 base attention class를 기반으로 세가지의 서로 다른 attention을 구현해 보겠습니다.
#                             </lang>""") as tracker:
#             self.wait()
        
#         self.play(FadeOut(ba))
#         self.wait()



