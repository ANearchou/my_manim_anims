from manimlib.imports import *


class path_move(Scene):
    def construct(self):

        s = Square()
        self.add(s)

        d = Dot().move_to(s.get_bottom()).set_color(RED)
        self.play(FadeIn(d))
        self.wait()

        self.play(MoveAlongPath(d, s, run_time = 5, rate_func = linear))
        self.play(MoveAlongPath(d, s, run_time = 1))
        self.wait(2)


x = [4,3,2,9,2,1,6]

for i in range(6,-1,-1):
    for j in range(i):
        if x[j] > x[j+1]:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp

line1 = [TexMobject("x = ["),TexMobject("4"),TexMobject(","),TexMobject("3"),TexMobject(","),
        TexMobject("2"),TexMobject(","),TexMobject("9"),TexMobject(","),TexMobject("2"),TexMobject(","),]
        TexMobject("1"),TexMobject(","),TexMobject("6"),TexMobject("]")]

for i in range(16,2):
    line1[i].set_color(GREEN)
for i in range(1,16):
    line1[i].next_to(line1[i-1], RIGHT, buff = 0.1)
    