from manimlib.imports import * 

class Continuity(GraphScene):
    CONFIG = {
        "start_x" : 2,
        "h_color" : GREEN,
        "f_color" : YELLOW,
        "two_color" : RED,
        "graph_origin" : 3*DOWN+LEFT,
        "x_min" : -8,
        "x_max" : 8,
        "x_axis_label" : None,
        "x_labeled_nums" : None,
        "y_min" : 0,
        "y_max" : 5,
        "y_tick_frequency" : 0.5,
        "y_labeled_nums" : None,
        "y_axis_label" : "",
        "big_delta" : 0.7,
        "small_delta" : 0.01,
    }
    def construct(self):

        delta = ValueTracker(2)

        cont_func = lambda h : 3*(2**2) + 3*2*h + h**2
        left_fun = lambda x: -0.25*x**2+1
        right_fun = lambda x: 0.25*x**2+2

        self.setup_axes(animate = True)
        self.wait()


        func1 = self.get_graph(left_fun, 
                               x_min = -8,
                               x_max = -0.01,
                               color = BLUE)
        func2 = self.get_graph(right_fun,
                               x_min = 0,
                               x_max = 5,
                               color= BLUE)

        self.play(ShowCreation(func1))
        self.play(ShowCreation(func2))

        left_hole = Circle(
                            radius =  0.075,
                            stroke_color = BLUE,
                            fill_color = BLACK,
                            fill_opacity = 1,).move_to(self.coords_to_point(0,1))
        right_hole = Circle(
                            radius =  0.075,
                            stroke_color = BLUE,
                            fill_color = BLUE,
                            fill_opacity = 1,).move_to(self.coords_to_point(0,2))                    
        self.play(Write(left_hole), Write(right_hole))
        self.wait()


        

        def_field = Line(self.coords_to_point(-2,0), self.coords_to_point(2,0)).set_color(YELLOW)
        def def_field_uptater(mob):
            mob.become(
                Line(self.coords_to_point(-delta.get_value(),0), self.coords_to_point(delta.get_value(),0)).set_color(YELLOW)
            )
        def_field.add_updater(def_field_uptater)
        
        
        left = self.get_graph(left_fun, 
                               x_min = -delta.get_value(),
                               x_max = -0.01,
                               color = YELLOW)
        right = self.get_graph(right_fun,
                               x_min = 0,
                               x_max = delta.get_value(),
                               color= YELLOW)
        tmp_left = self.get_graph(left_fun, 
                               x_min = -delta.get_value(),
                               x_max = -0.01,
                               color = YELLOW)
        tmp_right = self.get_graph(right_fun,
                               x_min = 0,
                               x_max = delta.get_value(),
                               color= YELLOW)

        def value_field_left_uptater(mob):
            mob.become(
                self.get_graph(lambda x: -0.25*x**2 + 1, 
                                x_min = -delta.get_value(),
                                x_max = -0.01,
                                color = YELLOW)
            )

        def value_field_right_uptater(mob):
            mob.become(
                self.get_graph(lambda x: 0.25*x**2 + 2, 
                                x_min = 0.01,
                                x_max = delta.get_value(),
                                color = YELLOW)
            )

        left.add_updater(value_field_left_uptater)
        right.add_updater(value_field_right_uptater)
        tmp = Line(self.coords_to_point(-2,0), self.coords_to_point(2,0)).set_color(YELLOW)
   

        left_hole_y = Circle(
                            radius =  0.075,
                            stroke_color = YELLOW,
                            fill_color = BLACK,
                            fill_opacity = 1,).move_to(self.coords_to_point(0,1))
        right_hole_y = Circle(
                            radius =  0.075,
                            stroke_color = YELLOW,
                            fill_color = YELLOW,
                            fill_opacity = 1,).move_to(self.coords_to_point(0,2))
        tmp_left_hole_y = Circle(
                            radius =  0.075,
                            stroke_color = YELLOW,
                            fill_color = BLACK,
                            fill_opacity = 1,).move_to(self.coords_to_point(0,1))
        tmp_right_hole_y = Circle(
                            radius =  0.075,
                            stroke_color = YELLOW,
                            fill_color = YELLOW,
                            fill_opacity = 1,).move_to(self.coords_to_point(0,2))

        tmp_group = VGroup(tmp_left,tmp_right, tmp_left_hole_y,tmp_right_hole_y)


        hori_l = DashedLine(self.coords_to_point(-2, left_fun(-2)) + 2*DOWN,
                            self.coords_to_point(-2, left_fun(-2)) + 8*UP,
                            stroke_width = 3)
        perp_l = DashedLine(self.coords_to_point(-2, left_fun(-2)) + 8*LEFT,
                            self.coords_to_point(-2, left_fun(-2)) + 8*RIGHT,
                            stroke_width = 3)
        def hori_l_up(mob):
            mob.become(
                DashedLine(self.coords_to_point(-delta.get_value(), left_fun(-delta.get_value())) + 2*DOWN,
                            self.coords_to_point(-delta.get_value(), left_fun(-delta.get_value())) + 8*UP,
                            stroke_width = 3)
            )
        def perp_l_up(mob):
            mob.become(
                DashedLine(self.coords_to_point(-delta.get_value(), left_fun(-delta.get_value())) + 8*LEFT,
                            self.coords_to_point(-delta.get_value(), left_fun(-delta.get_value())) + 8*RIGHT,
                            stroke_width = 3)
            )
        hori_l.add_updater(hori_l_up)
        perp_l.add_updater(perp_l_up)

        hori_r = DashedLine(self.coords_to_point(2, right_fun(2)) + 8*DOWN,
                            self.coords_to_point(2, right_fun(2)) + 8*UP,
                            stroke_width = 3)
        perp_r = DashedLine(self.coords_to_point(2, right_fun(2)) + 8*LEFT,
                            self.coords_to_point(2, right_fun(2)) + 8*RIGHT,
                            stroke_width = 3)
        def hori_r_up(mob):
            mob.become(
                DashedLine(self.coords_to_point(delta.get_value(), right_fun(delta.get_value())) + 8*DOWN,
                            self.coords_to_point(delta.get_value(), right_fun(delta.get_value())) + 8*UP,
                            stroke_width = 3)
            )
        def perp_r_up(mob):
            mob.become(
                DashedLine(self.coords_to_point(delta.get_value(), right_fun(delta.get_value())) + 8*LEFT,
                            self.coords_to_point(delta.get_value(), right_fun(delta.get_value())) + 8*RIGHT,
                            stroke_width = 3)
            )
        hori_r.add_updater(hori_r_up)
        perp_r.add_updater(perp_r_up)

        self.play(Write(def_field), Write(tmp))
        self.wait()
        self.play(ReplacementTransform(tmp, tmp_group))
        self.play(FadeIn(left), 
                  FadeIn(right), 
                  FadeIn(left_hole_y), 
                  FadeIn(right_hole_y), 
                  FadeOut(tmp_left),
                  FadeOut(tmp_right),
                  FadeOut(tmp_left_hole_y),
                  FadeOut(tmp_right_hole_y),
                  )
        self.play(Write(hori_l), Write(perp_l),
                  Write(hori_r), Write(perp_r))
        self.wait()
        self.play(delta.set_value, 0.02,
        run_time = 5)
        self.play(delta.set_value, 1,
                  rate_func = there_and_back)
        self.wait()          
        self.play(delta.set_value, 1,
                  rate_func = there_and_back,
                  run_time = 0.5)
        self.play(delta.set_value, 1,
                  rate_func = there_and_back,
                  run_time = 0.5)          
        self.wait()
        tmp_brace = Line(self.coords_to_point(4,1), self.coords_to_point(4,2))
        brace = Brace(tmp_brace, RIGHT, buff = 0)
        brace_text = brace.get_text("Can't get \\\\ smaller", buff = 0.1)
        self.play(
            GrowFromCenter(brace),
            Write(brace_text)
        )

        self.wait(2)
        hori_l.remove_updater(hori_l_up)
        perp_l.remove_updater(perp_l_up)
        hori_r.remove_updater(hori_r_up)
        perp_r.remove_updater(perp_r_up)
        def_field.remove_updater(def_field_uptater)
        left.remove_updater(value_field_left_uptater)
        right.remove_updater(value_field_right_uptater)

        self.play(FadeOut(hori_l),
                 FadeOut(hori_r),
                 FadeOut(perp_l),
                 FadeOut(perp_r),
                 FadeOut(left),
                 FadeOut(right),
                 FadeOut(left_hole_y),
                 FadeOut(right_hole_y),
                 FadeOut(func1),
                 FadeOut(func2),
                 FadeOut(brace),
                 FadeOut(brace_text),
                 FadeOut(left_hole),
                 FadeOut(right_hole)
                 )

        

class kwargs_update(GraphScene):
    def construct(self):

        self.setup_axes()
        tracker = ValueTracker(-1)

        f_graph = self.get_graph(lambda x : x,
                                 x_min = -1,
                                 x_max = 2)
        def updater(mob):
            mob.become(
                self.get_graph(lambda x : x,
                               x_min = tracker.get_value(),
                               x_max = 2)
            ) 

        f_graph.add_updater(updater)
        self.play(ShowCreation(f_graph))
        self.wait()
        self.play(tracker.set_value,2)

# ```python
# class kwargs_update(GraphScene):
#     def construct(self):

#         self.setup_axes()
#         tracker = ValueTracker(-1)

#         f_graph = self.get_graph(lambda x : x,
#                                  x_min = -1,
#                                  x_max = 2)
#         def updater(mob):
#             mob.become(
#                 self.get_graph(lambda x : x,
#                                x_min = tracker.get_value(),
#                                x_max = 2)
#             ) 

#         f_graph.add_updater(updater)
#         self.play(ShowCreation(f_graph))
#         self.wait()
#         self.play(tracker.set_value,2)
# ```