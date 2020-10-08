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