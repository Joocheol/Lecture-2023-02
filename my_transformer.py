from manim import *

def blocks():
    # Masked MHA
    text = Tex(r"Masked\\ Multi-Head\\ Attention")
    box = RoundedRectangle(width=3.0, height=0.6*3, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.3)
    mmha = VGroup(box, text)

    # MHA
    text = Tex(r"Multi-Head \\ Attention")
    box = RoundedRectangle(width=3.0, height=0.6*2, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.3)
    mha = VGroup(box, text)

    # Add & Norm
    text = Tex(r"Add \& Norm")
    box = RoundedRectangle(width=3.0, height=0.6, corner_radius=0.1, color=RED).set_fill(RED, opacity=0.3)
    ann = VGroup(box, text)

    # Feed Forward
    text = Tex(r"Feed \\ Forward")
    box = RoundedRectangle(width=3.0, height=0.6*2, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.3)
    ff = VGroup(box, text)

    return VDict([("mmha", mmha), ("mha", mha), ("ann", ann), ("ff", ff)])

def connect(start, arg1, arg2):
    temp = VGroup()
    temp.add(Dot().move_to(start))
    end = start

    for i, j in zip(arg1, arg2):
        end = start + i * j
        temp.add(Line(start, end))
        start = end

    temp.add(Dot().move_to(end))

    return temp

def add_ann(obj):
    v = blocks()
    return VGroup(obj, Line(obj.get_top(), obj.get_top() + UP * 0.3), v["ann"].copy()).arrange(UP, buff=0)

def skeleton():
    v = blocks()
    mmha_n = add_ann(v["mmha"].copy())
    l_mha_n = add_ann(v["mha"].copy())
    r_mha_n = add_ann(v["mha"].copy())
    l_ff_n = add_ann(v["ff"].copy())
    r_ff_n = add_ann(v["ff"].copy())

    left = VGroup(l_mha_n, l_ff_n).arrange(UP, buff=LARGE_BUFF)
    right = VGroup(mmha_n, r_mha_n, r_ff_n).arrange(UP, buff=LARGE_BUFF)
    tmp = VGroup(left, right).arrange(RIGHT, buff=LARGE_BUFF*2)
    left.align_to(right, DOWN)

    return tmp

def skeleton_connect():

    v = skeleton()

    block_1 = v[0][0]
    block_2 = v[0][1]
    block_3 = v[1][0]
    block_4 = v[1][1]
    block_5 = v[1][2]

    btn = LARGE_BUFF * 2
    width = 3
    height = 0.6
    block_buff = LARGE_BUFF
    small_buff = 0.3

    temp = VGroup()
    # -> block_1
    temp.add(connect(block_1[0].get_bottom() + DOWN, [UP], [block_buff]))
    temp.add(connect(block_1[0].get_bottom() + DOWN, [UP, LEFT, UP], [2*block_buff/3, width/4, block_buff/3]))
    temp.add(connect(block_1[0].get_bottom() + DOWN, [UP, RIGHT, UP], [2*block_buff/3, width/4, block_buff/3]))
    temp.add(connect(block_1[0].get_bottom() + DOWN, [UP, LEFT, UP, RIGHT], [block_buff/2, width/2 + btn/2, height*3 + block_buff/2, btn/2]))
    # block_1 -> block_2
    temp.add(connect(block_1[2].get_top(), [UP], [block_buff]))
    temp.add(connect(block_1[2].get_top(), [UP, LEFT, UP, RIGHT], [block_buff/2, width/2 + btn/2, height*3 + block_buff/2, btn/2]))
    # block_2 -> block_3
    temp.add(connect(block_2[2].get_top(), [UP, RIGHT, DOWN, RIGHT, UP], [small_buff, width/2 + btn/2, height*3 + block_buff/3, btn/2 + width/4, block_buff/3]))
    temp.add(connect(block_2[2].get_top(), [UP, RIGHT, DOWN, RIGHT, UP], [small_buff, width/2 + btn/2, height*3 + block_buff/3, btn/2 + 2*width/4, block_buff/3]))
    # -> block_3
    temp.add(connect(block_3[0].get_bottom() + DOWN, [UP], [block_buff]))
    temp.add(connect(block_3[0].get_bottom() + DOWN, [UP, LEFT, UP], [2*block_buff/3, width/4, block_buff/3]))
    temp.add(connect(block_3[0].get_bottom() + DOWN, [UP, RIGHT, UP], [2*block_buff/3, width/4, block_buff/3]))
    temp.add(connect(block_3[0].get_bottom() + DOWN, [UP, RIGHT, UP, LEFT], [block_buff/2, width/2 + btn/2, height*4 + block_buff/2, btn/2]))
    # block_3 -> block_4
    temp.add(connect(block_3[2].get_top(), [UP, RIGHT, UP], [block_buff/2, width/4, block_buff/2]))
    temp.add(connect(block_3[2].get_top(), [UP, RIGHT, UP, LEFT], [block_buff/3, width/2 + btn/2, height*3 + 2*block_buff/3, btn/2]))
    # block_4 -> block_5
    temp.add(connect(block_4[2].get_top(), [UP], [block_buff]))
    temp.add(connect(block_4[2].get_top(), [UP, RIGHT, UP, LEFT], [block_buff/2, width/2 + btn/2, height*3 + block_buff/2, btn/2]))
    # block_5 ->
    temp.add(connect(block_5[2].get_top(), [UP], [block_buff]))

    return temp

def make_box(rows, cols):
    width = 1
    height = 1
    
    temp = VGroup()
    for i in range(cols):
        temp_in = VGroup()
        for j in range(rows):
            temp_in.add(Rectangle(width=width, height=height))
        temp_in.arrange(DOWN, buff=0)
        temp.add(temp_in)
    temp.arrange(RIGHT, buff=0)

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

def setup_boxes():

    ca = make_box(5,5)
    m = make_box(1,5)
    m1 = m.copy()
    m2 = m.copy()
    m3 = m.copy()
    m4 = m.copy()
    t1, t2, t3 = setup_text_box()

    gsa = VGroup(VGroup(t1, m1).arrange(UP, buff=0.5), m2).arrange(UP, buff=1)
    csa = VGroup(VGroup(t2, m3).arrange(UP, buff=0.5), m4).arrange(UP, buff=1)
    ff = VGroup(m, t3).arrange(UP, buff=0.5)
    decoder = VGroup(csa, ca, ff).arrange(UP, buff=1)
    boxes = VGroup(gsa, decoder).arrange(RIGHT, buff=2)
    gsa.align_to(decoder, DOWN)

    return boxes

# TODO
def boxes_connect():
    tmp = VGroup()
    m = setup_boxes()

    s = m[0][1]
    t = m[1][1][0]


    for i in range(5):
        x = s[i].get_top()[0]
        y = t[i].get_left()[1]
        p = np.array([x, y, 0.0])
        tmp.add(Line(s[i].get_top(), p))
        tmp.add(Line(p, t[i].get_left()))

    return tmp
