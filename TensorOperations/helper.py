from manim import *

def mat(m, rows, cols, row_first = True):
    vg = VGroup()

    if row_first:
        for i in range(rows):
            temp = VGroup()
            for j in range(cols):
                temp.add(m.copy())
            temp.arrange(RIGHT)
            vg.add(temp)
        vg.arrange(DOWN)

    if not row_first:
        for i in range(cols):
            temp = VGroup()
            for j in range(rows):
                temp.add(m.copy())
            temp.arrange(DOWN)
            vg.add(temp)
        vg.arrange(RIGHT)

    return vg