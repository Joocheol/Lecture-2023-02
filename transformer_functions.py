from manim import *
from constants import *

def arrow_setup(block_1, block_2, block_3, block_4, block_5):

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

def arrows(start, arg1, arg2):

    temp = VGroup()
    temp.add(Dot().move_to(start))

    for i, j in zip(arg1, arg2):
        end = start + i * j
        temp.add(Line(start, end))
        start = end

    temp.add(Dot().move_to(end))

    return temp

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

def Box(rows, cols, is_causal=False, is_emph=False, is_long=False):
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


def Arrows_setup_1(m, m1):
    vg = VGroup()

    dist = sum(m1.get_bottom() - m.get_top())

    for i, j in enumerate(m):
        vg.add(arrows(j.get_top(), [UP], [dist]))

    # for i, j in enumerate(m[:5]):
    #     vg.add(arrows(j.get_top() + UP * dist/6*(i+1), [LEFT, UP, RIGHT], [1.2 + 0.2*i, 2.8 - dist/6*(i+1) - 0.4*i, 1.0 - 0.2*i]))

    return vg

def Arrows_setup_2(m, m1):
    vg = VGroup()

    for i, j in enumerate(m):
        vg.add(arrows(j.get_top(), [UP, RIGHT], [5.5-i, 6.5-i]))

    # for i, j in enumerate(m[:5]):
    #     vg.add(arrows(j.get_top() + UP * dist/6*(i+1), [LEFT, UP, RIGHT], [1.2 + 0.2*i, 2.8 - dist/6*(i+1) - 0.4*i, 1.0 - 0.2*i]))

    return vg

def Arrows_setup_3(m, m1):
    vg = VGroup()

    for i in range(len(m)):
        vg.add(Polygon(m[0].get_corner(UL), m1[i].get_bottom(), m[-1].get_corner(UR), stroke_width=1))

    # for i, j in enumerate(m[:5]):
    #     vg.add(arrows(j.get_top() + UP * dist/6*(i+1), [LEFT, UP, RIGHT], [1.2 + 0.2*i, 2.8 - dist/6*(i+1) - 0.4*i, 1.0 - 0.2*i]))

    return vg

def Arrows_setup_4(m, m1):
    vg = VGroup()

    for i in range(len(m)):
        vg.add(Polygon(m[0].get_corner(UL), m1[i].get_bottom(), m[i].get_corner(UR), stroke_width=1))

    # for i, j in enumerate(m[:5]):
    #     vg.add(arrows(j.get_top() + UP * dist/6*(i+1), [LEFT, UP, RIGHT], [1.2 + 0.2*i, 2.8 - dist/6*(i+1) - 0.4*i, 1.0 - 0.2*i]))

    return vg


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