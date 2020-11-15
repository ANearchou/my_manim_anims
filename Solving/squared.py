from manimlib.imports import *

class squared(Scene):
    CONFIG = {
        "a_side" : 1,
        "b_side" : 2.5
    }
    def construct(self):

        init = TexMobject("(a + b)^2"," = ","a^2"," + ","2ab"," + ","b^2")
        self.play(Write(init))
        self.wait()
        self.play(init.to_edge, UP)
        
        a_line = Line([0,0,0], [0,self.a_side,0]).set_color(RED)
        a_label = TexMobject("a").next_to(a_line, LEFT, buff = 0.2)

        b_line = Line([1,0,0], [1,self.b_side,0]).set_color(BLUE)
        b_label = TexMobject("b").next_to(b_line, LEFT, buff = 0.2)

        self.play(Write(a_line), Write(b_line),
                  Write(a_label), Write(b_label))
        
        self.wait()
        self.play(a_line.shift, 2*LEFT + (self.a_side + 1) * DOWN,
                  MaintainPositionRelativeTo(a_label, a_line),
                  b_line.shift, 3*LEFT + DOWN,
                  MaintainPositionRelativeTo(b_label, b_line)
                  )
        a_b_label = TexMobject("a+b").move_to(b_line.get_end() + (self.a_side + self.b_side)/2 * DOWN + 0.8 * LEFT)
        tmp = VGroup(a_label, b_label)

        self.wait()
        self.play(ReplacementTransform(tmp, a_b_label))

        full_sq = Polygon(a_line.get_start(),
                          b_line.get_end(),
                          b_line.get_end() + [self.b_side + self.a_side, 0,0],
                          a_line.get_start() + [self.b_side + self.a_side, 0,0],
                          fill_color = "#9000BD", fill_opacity = 0.5, color = "#9000BD")

        

        self.wait()
        self.play(Write(full_sq),
                  #FadeIn(init_a_b_2)
                  init.set_color_by_tex, "(a + b)^2", "#9000BD",
                  FadeOut(a_b_label))
        self.wait()

        a1_label = TexMobject("a").next_to(a_line, LEFT, buff = 0.2)
        b1_label = TexMobject("b").next_to(b_line, LEFT, buff = 0.2)
       

        self.play(FadeOut(full_sq),
                  FadeIn(a_line), FadeIn(b_line),
                  FadeIn(a1_label), FadeIn(b1_label))

        up_b = Line(b_line.get_end(), b_line.get_end() + [self.b_side,0,0]).set_color(BLUE)
        up_a = Line(up_b.get_end(), up_b.get_end() + [self.a_side,0,0]).set_color(RED)
        ri_b = Line(up_a.get_end(),up_a.get_end() + [0,-self.b_side,0]).set_color(BLUE)
        ri_a = Line(ri_b.get_end(),ri_b.get_end() + [0,-self.a_side,0]).set_color(RED)
        do_a = Line(ri_a.get_end(), ri_a.get_end() + [-self.a_side,0,0]).set_color(RED)
        do_b = Line(do_a.get_end(), do_a.get_end() + [-self.b_side,0,0]).set_color(BLUE)

        a2_label = TexMobject("a").next_to(up_a, UP, buff = 0.2)
        a3_label = TexMobject("a").next_to(ri_a, RIGHT, buff = 0.2)
        a4_label = TexMobject("a").next_to(do_a, DOWN, buff = 0.2)
        b2_label = TexMobject("b").next_to(up_b, UP, buff = 0.2)
        b3_label = TexMobject("b").next_to(ri_b, RIGHT, buff = 0.2)
        b4_label = TexMobject("b").next_to(do_b, DOWN, buff = 0.2)
        
        self.wait()
        self.play(Write(up_a),Write(up_b),Write(ri_a),
                  Write(ri_b),Write(do_a),Write(do_b),
                  Write(a2_label),Write(a3_label),Write(a4_label),
                  Write(b2_label),Write(b3_label),Write(b4_label))

        a_sq = Polygon(ri_a.get_start(), ri_a.get_end(), do_a.get_end(), do_a.get_end() + [0,self.a_side,0],
                       fill_color = RED, fill_opacity = 0.5, color = RED)
        b_sq = Polygon(up_b.get_start(), up_b.get_end(), up_b.get_end() + [0,-self.b_side,0], b_line.get_start(),
                       fill_color = BLUE, fill_opacity = 0.5, color = BLUE)     

        ab1 =  Polygon(up_b.get_end(), up_a.get_end(), ri_b.get_end(), ri_b.get_end() + [-self.a_side,0,0],
                       fill_color = PINK, fill_opacity = 0.5, color = PINK)   
        ab2 =  Polygon(a_line.get_start(), a_line.get_end(), a_line.get_end() + [self.b_side,0,0], do_b.get_start() ,
                       fill_color = PINK, fill_opacity = 0.5, color = PINK)

        a_sq_label = TexMobject("a^2").move_to(a_sq.get_center())
        b_sq_label = TexMobject("b^2").move_to(b_sq.get_center())
        ab_label1 = TexMobject("ab").move_to(ab1.get_center())
        ab_label2 = TexMobject("ab").move_to(ab2.get_center())

        self.wait()
        self.play(Write(a_sq), Write(b_sq), Write(ab1), Write(ab2))
        self.play(Write(a_sq_label), Write(b_sq_label), Write(ab_label1), Write(ab_label2))
        self.wait()
        self.play(a_sq.set_opacity,1,
                  init.set_color_by_tex, "a^2", RED )
        self.wait()
        self.play(b_sq.set_opacity,1,
                  init.set_color_by_tex, "b^2", BLUE )
        self.wait()
        self.play(ab1.set_opacity,1,
                  ab2.set_opacity,1,
                  init.set_color_by_tex, "2ab", PINK )



        
class test(Scene):
    def construct(self):

        c = Circle().set_color("#EAAB47")
        self.play(Write(c))
        self.wait()

        self.play(c.set_color, "#EA9208")
        self.wait()