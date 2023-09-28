from manim import *
from constants import *



def setup():
    # Masked MHA
    text = Tex(r"Masked\\ Multi-Head\\ Attention")
    box = RoundedRectangle(width=width, height=height*3, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=opacity)
    mmha = VGroup(box, text)

    # MHA
    text = Tex(r"Multi-Head \\ Attention")
    box = RoundedRectangle(width=width, height=height*2, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=opacity)
    mha = VGroup(box, text)

    # Add & Norm
    text = Tex(r"Add \& Norm")
    box = RoundedRectangle(width=width, height=height, corner_radius=0.1, color=RED).set_fill(RED, opacity=opacity)
    ann = VGroup(box, text)

    # Feed Forward
    text = Tex(r"Feed \\ Forward")
    box = RoundedRectangle(width=width, height=height*2, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=opacity)
    ff = VGroup(box, text)

    return mmha, mha, ann, ff

def arrows(start, arg1, arg2):
    temp = VGroup()
    temp.add(Dot().move_to(start))
    end = start

    for i, j in zip(arg1, arg2):
        end = start + i * j
        temp.add(Line(start, end))
        start = end

    temp.add(Dot().move_to(end))

    return temp

def make_box(rows, cols, is_causal=False, is_emph=False, is_long=False):
    width = 1
    height = 2 if is_long else 1
    vg = VGroup()

    if is_causal:
        for i in range(rows):
            for j in range(cols):
                if i > j:
                    vg.add(Rectangle(width=width, height=height).set(stroke_width=1))
                else:
                    vg.add(Rectangle(width=width, height=height))
    else:
        for i in range(rows):
            for j in range(cols):
                vg.add(Rectangle(width=width, height=height))

    vg.arrange_in_grid(rows=rows, cols=cols, buff=0)

    if is_emph:
        for j in range(cols):
            if is_causal:
                vg.add(Rectangle(width=width, height=height*min(j+1,rows)).align_to(vg[j], UL).set(color=BLUE))
            else:
                vg.add(Rectangle(width=height, height=height*rows).align_to(vg[j], UL).set(color=BLUE))

    return vg

def setup_text_box():
    vg_1 = VGroup()
    vg_2 = VGroup()
    vg_3 = VGroup()

    box = Rectangle(height=1, width=3)

    text = "[START] je suis etudiant I am a student [END]".split()
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

    vg_1.arrange(DOWN, buff=0).rotate(PI/2)
    vg_2.arrange(DOWN, buff=0).rotate(PI/2)
    vg_3.arrange(DOWN, buff=0).rotate(PI/2)

    return vg_1, vg_2, vg_3

def arrows_setup_simple(m, m1):
    vg = VGroup()

    dist = sum(m1.get_bottom() - m.get_top())

    for i, j in enumerate(m):
        vg.add(arrows(j.get_top(), [UP], [dist]))

    return vg

def arrows_setup_mid(m, m1):
    vg = VGroup()

    for i, j in enumerate(m):
        vg.add(arrows(j.get_top(), [UP, RIGHT], [5.5-i, 6.5-i]))

    return vg

def arrows_setup_gsa(m, m1):
    vg = VGroup()

    for i in range(len(m)):
        vg.add(Polygon(m[0].get_corner(UL), m1[i].get_bottom(), m[-1].get_corner(UR), stroke_width=1))

    return vg

def arrows_setup_mmsa(m, m1):
    vg = VGroup()

    for i in range(len(m)):
        vg.add(Polygon(m[0].get_corner(UL), m1[i].get_bottom(), m[i].get_corner(UR), stroke_width=1))

    return vg

def archi_setup():

    mmha, mha, ann, ff = setup()

    block_1 = VGroup(mha.copy(), Line(ORIGIN, UP*small_buff), ann.copy()).arrange(UP, buff=0)
    block_2 = VGroup(ff.copy(), Line(ORIGIN, UP*small_buff), ann.copy()).arrange(UP, buff=0)
    block_3 = VGroup(mmha.copy(), Line(ORIGIN, UP*small_buff), ann.copy()).arrange(UP, buff=0)
    block_4 = VGroup(mha.copy(), Line(ORIGIN, UP*small_buff), ann.copy()).arrange(UP, buff=0)
    block_5 = VGroup(ff.copy(), Line(ORIGIN, UP*small_buff), ann.copy()).arrange(UP, buff=0)

    encoder = VGroup(block_1, block_2).arrange(UP, buff=1)
    decoder = VGroup(block_3, block_4, block_5).arrange(UP, buff=block_buff)

    transformer = VGroup(encoder, decoder).arrange(RIGHT, buff=btn)
    encoder.align_to(decoder, DOWN)
    
    return transformer

def archi_arrows_setup(block_1, block_2, block_3, block_4, block_5):

    temp = VGroup()
    # -> block_1
    temp.add(arrows(block_1[0].get_bottom() + DOWN, [UP], [block_buff]))
    temp.add(arrows(block_1[0].get_bottom() + DOWN, [UP, LEFT, UP], [2*block_buff/3, width/4, block_buff/3]))
    temp.add(arrows(block_1[0].get_bottom() + DOWN, [UP, RIGHT, UP], [2*block_buff/3, width/4, block_buff/3]))
    temp.add(arrows(block_1[0].get_bottom() + DOWN, [UP, LEFT, UP, RIGHT], [block_buff/2, width/2 + btn/2, height*3 + block_buff/2, btn/2]))
    # block_1 -> block_2
    temp.add(arrows(block_1[2].get_top(), [UP], [block_buff]))
    temp.add(arrows(block_1[2].get_top(), [UP, LEFT, UP, RIGHT], [block_buff/2, width/2 + btn/2, height*3 + block_buff/2, btn/2]))
    # block_2 -> block_3
    temp.add(arrows(block_2[2].get_top(), [UP, RIGHT, DOWN, RIGHT, UP], [small_buff, width/2 + btn/2, height*3 + block_buff/3, btn/2 + width/4, block_buff/3]))
    temp.add(arrows(block_2[2].get_top(), [UP, RIGHT, DOWN, RIGHT, UP], [small_buff, width/2 + btn/2, height*3 + block_buff/3, btn/2 + 2*width/4, block_buff/3]))
    # -> block_3
    temp.add(arrows(block_3[0].get_bottom() + DOWN, [UP], [block_buff]))
    temp.add(arrows(block_3[0].get_bottom() + DOWN, [UP, LEFT, UP], [2*block_buff/3, width/4, block_buff/3]))
    temp.add(arrows(block_3[0].get_bottom() + DOWN, [UP, RIGHT, UP], [2*block_buff/3, width/4, block_buff/3]))
    temp.add(arrows(block_3[0].get_bottom() + DOWN, [UP, RIGHT, UP, LEFT], [block_buff/2, width/2 + btn/2, height*4 + block_buff/2, btn/2]))
    # block_3 -> block_4
    temp.add(arrows(block_3[2].get_top(), [UP, RIGHT, UP], [block_buff/2, width/4, block_buff/2]))
    temp.add(arrows(block_3[2].get_top(), [UP, RIGHT, UP, LEFT], [block_buff/3, width/2 + btn/2, height*3 + 2*block_buff/3, btn/2]))
    # block_4 -> block_5
    temp.add(arrows(block_4[2].get_top(), [UP], [block_buff]))
    temp.add(arrows(block_4[2].get_top(), [UP, RIGHT, UP, LEFT], [block_buff/2, width/2 + btn/2, height*3 + block_buff/2, btn/2]))
    # block_5 ->
    temp.add(arrows(block_5[2].get_top(), [UP], [block_buff]))

    return temp

def boxes_setup():

    ca = make_box(5,5)
    m = make_box(1,5)
    m1 = m.copy()
    m2 = m.copy()
    m3 = m.copy()
    m4 = m.copy()
    t1, t2, t3 = setup_text_box()

    gsa = VGroup(VGroup(t1, m1).arrange(UP, buff=0.5), m2).arrange(UP, buff=1)
    mmha = VGroup(VGroup(t2, m3).arrange(UP, buff=0.5), m4).arrange(UP, buff=1)
    ff = VGroup(m, t3).arrange(UP, buff=0.5)
    decoder = VGroup(mmha, ca, ff).arrange(UP, buff=1)
    boxes = VGroup(gsa, decoder).arrange(RIGHT, buff=2)
    gsa.align_to(decoder, DOWN)

    return boxes

def box_arrows_setup(gsa, mmha, ca, ff):

    a1 = arrows_setup_simple(gsa[0][0], gsa[0][1])
    a2 = arrows_setup_gsa(gsa[0][1], gsa[1])
    a3 = arrows_setup_mid(gsa[1], ca)
    a4 = arrows_setup_simple(mmha[0][0], mmha[0][1])
    a5 = arrows_setup_mmsa(mmha[0][1], mmha[1])
    a6 = arrows_setup_simple(mmha[1], ca)
    a7 = arrows_setup_simple(ca[:5], ff[0])
    a8 = arrows_setup_simple(ff[0], ff[1])

    return a1, a2, a3, a4, a5, a6, a7, a8

def code_setup():
            
        ba = Code(file_name="code_ba.py", tab_width=4, insert_line_no=False, background="window", language="python").rescale_to_fit(12,0)
        ca = Code(file_name="code_ca.py", tab_width=4, insert_line_no=False, background="window", language="python").rescale_to_fit(12,0)
        gsa = Code(file_name="code_gsa.py", tab_width=4, insert_line_no=False, background="window", language="python").rescale_to_fit(12,0)
        csa = Code(file_name="code_csa.py", tab_width=4, insert_line_no=False, background="window", language="python").rescale_to_fit(12,0)

        v = VGroup(ba.copy(), ca.copy(), gsa.copy(), csa.copy()).arrange(RIGHT).scale(0.2).to_edge(UP)

        return ba, ca, gsa, csa, v