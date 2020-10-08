from manimlib.imports import *
import numpy as np
from numpy import prod

class TaylorSin(GraphScene):
    CONFIG = {
            "y_min" : -3,
            "y_max" : 3,
            "x_min" : -2*PI,
            "x_max" : 2*PI,
            "graph_origin" : ORIGIN
    }
    def construct(self):

        def factorial(n):
            return prod(range(1,n+1))

        self.setup_axes(animate=True)
        self.wait(2)

        sin = self.get_graph(lambda x: np.sin(x),
                             color = RED)
        sin_label = TexMobject("sin(x)").set_color(RED).to_edge(UL)

        taylor_label = [TexMobject("x"),TexMobject("-"),TexMobject("\\frac{x^{3}}{3!}"),TexMobject("+"),TexMobject("\\frac{x^{5}}{5!}"),
                        TexMobject("-"),TexMobject("\\frac{x^{7}}{7!}"),TexMobject("+"),TexMobject("\\frac{x^{9}}{9!}"),TexMobject("-"),TexMobject("\\frac{x^{11}}{11!}")]
        taylor_label[0].next_to(sin_label.get_left(), DOWN, buff = 1).set_color(GREEN_E)

        for i in range(1,11,1):
            taylor_label[i].next_to(taylor_label[i-1], RIGHT, buff = 0.2).set_color(GREEN_E)


        
        self.play(ShowCreation(sin),
                  Write(sin_label),
                  run_time = 2)
        self.wait(2)

        sin1 = self.get_graph(lambda x: x,
                              color = GREEN)
        sin2 = self.get_graph(lambda x: x - (x**3/factorial(3)),
                              color = GREEN)
        sin3 = self.get_graph(lambda x: x - (x**3/factorial(3)) + (x**5/factorial(5)),
                              color = GREEN)
        sin4 = self.get_graph(lambda x: x - (x**3/factorial(3)) + (x**5/factorial(5)) - (x**7/factorial(7)),
                              color = GREEN)
        sin5 = self.get_graph(lambda x: x - (x**3/factorial(3)) + (x**5/factorial(5)) - (x**7/factorial(7)) + (x**9/factorial(9)),
                              color = GREEN)
        sin6 = self.get_graph(lambda x: x - (x**3/factorial(3)) + (x**5/factorial(5)) - (x**7/factorial(7)) + (x**9/factorial(9)) - (x**11/factorial(11)),
                              color = GREEN)
        self.play(ShowCreation(sin1),
                  Write(taylor_label[0]),
                  run_time = 2)

        self.wait(2)

        self.play(ReplacementTransform(sin1, sin2),
                  Write(taylor_label[1]), Write(taylor_label[2]),
                  run_time = 2)
        self.wait(2)

        self.play(ReplacementTransform(sin2, sin3),
                  Write(taylor_label[3]), Write(taylor_label[4]),
                  run_time = 2)
        self.wait(2)
        self.play(ReplacementTransform(sin3, sin4),
                  Write(taylor_label[5]), Write(taylor_label[6]),
                  run_time = 2)
        self.wait(2)
        self.play(ReplacementTransform(sin4, sin5),
                  Write(taylor_label[7]), Write(taylor_label[8]),
                  run_time = 2)
        self.wait(2)
        self.play(ReplacementTransform(sin5, sin6),
                  Write(taylor_label[9]), Write(taylor_label[10]),
                  run_time = 2)
        self.wait(2)



    

class FunctionProjection(GraphScene):
    CONFIG = {
            "y_min" : -2,
            "y_max" : 6,
            "x_min" : -2,
            "x_max" : 5,
            "graph_origin" : DOWN,
            "function_color":RED
    }
    def construct(self):

        self.setup_axes(animate = True)
        self.wait(2)

        func = self.get_graph(lambda z: (z-2)**2+1,
                              color = RED)
        self.play(ShowCreation(func))
        self.wait(2)

        definition_field = Line(self.coords_to_point(1,0), self.coords_to_point(4,0)).set_color(YELLOW)
        self.play(FadeIn(definition_field), run_time=2)
        self.wait(2)

        in_graph = self.get_graph(lambda y: (y-2)**2+1,
                                  color = YELLOW,
                                  x_max = 4, x_min = 1)
        in_graph_copy = in_graph.copy()
        self.play(ReplacementTransform(definition_field, in_graph), run_time = 2)
        self.add(in_graph_copy)                          
        self.wait(2)

        upper_dashed = DashedLine(self.coords_to_point(2,1), self.coords_to_point(0,1)).set_color(BLUE)
        down_dashed = DashedLine(self.coords_to_point(4,5), self.coords_to_point(0,5)).set_color(BLUE)
        self.play(Write(upper_dashed), run_time = 1)
        self.play(Write(down_dashed), run_time = 1)
        self.wait()

        value_file = Line(self.coords_to_point(0,1), self.coords_to_point(0,5)).set_color(YELLOW)
        self.play(ReplacementTransform(in_graph, value_file), run_time = 2)
        self.wait(0.5)

        self.play(FadeOut(upper_dashed), FadeOut(down_dashed))
        self.wait()

        self.play(FadeOut(value_file))
        self.wait(2)







class test(GraphScene):
    def construct(self):
        sin_label = TexMobject("sin(x)").set_color(RED).to_edge(UL)
        taylor_label = [TexMobject("x"),TexMobject("-"),TexMobject("\\frac{x^{3}}{3!}"),TexMobject("+"),TexMobject("\\frac{x^{5}}{5!}"),
                        TexMobject("-"),TexMobject("\\frac{x^{7}}{7!}"),TexMobject("+"),TexMobject("\\frac{x^{9}}{9!}"),TexMobject("-"),TexMobject("\\frac{x^{11}}{11!}")]
        taylor_label[0].next_to(sin_label, DOWN, buff = 0.5).set_color(GREEN)

        for i in range(1,11,1):
            taylor_label[i].next_to(taylor_label[i-1], RIGHT, buff = 0.2).set_color(GREEN)
        self.play(Write(taylor_label[0]),Write(taylor_label[1]),Write(taylor_label[2]),Write(taylor_label[3]),Write(taylor_label[4]),
        Write(taylor_label[5]),Write(taylor_label[6]),Write(taylor_label[7]),Write(taylor_label[8]),Write(taylor_label[9]),Write(taylor_label[10]))
        self.wait(2)