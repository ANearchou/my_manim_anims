from manimlib.imports import *

class test(Scene):
    def construct(self):
        s = Square()
        d = Dot()
        d.move_to(s.get_center())

        txt = TexMobject(str(d.get_center()[1]))
        txt.to_edge(UL)
        txt.add_updater(lambda g: TexMobject())
        d.add_updater(
            lambda f: f.move_to(s.get_center())
        )

        self.play(FadeIn(s))
        self.wait(0.5)

        self.play(Write(d))
        self.wait(2)

        self.play(s.shift, 2*LEFT)
        self.wait()

        self.play(s.shift, 5*RIGHT)
        self.wait()