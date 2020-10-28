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



class Code(Scene):
    def construct(self):

        
        line1 = TexMobject("x = [4,3,2,9,2,1,6]",
                            tex_to_color_map={"4": GREEN, "3": GREEN,"2": GREEN,"9": GREEN,"2": GREEN,"1": GREEN,"6": GREEN},)

        line2 = TexMobject("for i in range(6,-1,-1):",
                            tex_to_color_map={"for": PINK, "in": PINK,"range": YELLOW,"6": GREEN,"1": GREEN},)
        self.play(Write(line2))
        self.wait()
