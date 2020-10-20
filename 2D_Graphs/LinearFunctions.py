from manimlib.imports import *
import random


class Lines(GraphScene):
    CONFIG = {"color": GREEN,
              "y_min" : -10,
              "y_max" : 10,
              "x_min" : -10,
              "x_max" : 10,
              "graph_origin" : ORIGIN
              }
    def construct(self):
        # SETUP GRAPH
        pairs = [(2,1),(2,3),(1.5,-2),(-0.3,-2.2),(-0.1,-2.2),(1,1)]
        #axes = Axes()
        slope_tracker = ValueTracker(1)
        constunt_tracker = ValueTracker(0)

        func = lambda a,b: lambda x: a * x + b
        graph = VMobject()
       
        # SETUP FORMULA
        formula = TexMobject("y = ", "x ")
        formula.to_corner(UL)
        formula[1].shift(RIGHT*1.5)
        slope = DecimalNumber(1,num_decimals=1, include_sign = True)
        slope.next_to(formula[1], LEFT, buff = 0.1, aligned_edge = DOWN)
        constunt = DecimalNumber(0,num_decimals=1, include_sign = True)
        constunt.next_to(formula[1], RIGHT, buff = 0.2, aligned_edge = DOWN)
        grp = VGroup(formula, slope, constunt)
        initial_formula = TexMobject("y = x")
        initial_formula.to_corner(UL)
        
        graph_kwargs = {"color": RED}
        # SET UPDATERS
        def update_graph(mob):
            mob.become(
                self.get_graph(
                    func(slope_tracker.get_value(), constunt_tracker.get_value()),
                    **graph_kwargs
                )
            )
        # SET INITIAL STATE OF GRAPH
        #self.add(axes)
        self.setup_axes(animate=True)
        self.wait()

        update_graph(graph)
        graph.add_updater(update_graph)
        #self.add(axes)
        self.play(ShowCreation(graph),Write(initial_formula))
        self.wait(2)
        self.play(ReplacementTransform(initial_formula, grp))
        self.wait()

        ind = range(7,1,-1)
        for i in ind:
            self.play(
                slope_tracker.set_value, pairs[ind[i-2]-2][0],
                constunt_tracker.set_value, pairs[ind[i-2]-2][1],
                ChangeDecimalToValue(slope,pairs[ind[i-2]-2][0]),
                ChangeDecimalToValue(constunt,pairs[ind[i-2]-2][1]),
                run_time = (i-1)/2
            )
            self.wait(1.2 - (ind[i-2]-1)/9)
        self.wait(4)    

        random.seed(1)
        new_pairs = [(round(random.normalvariate(0,3),2), round(random.normalvariate(0,3),2)) for i in range(20)]
        new_pairs.append((2,1))
        for i in range(len(new_pairs)):
            self.play(
                slope_tracker.set_value, new_pairs[i][0],
                constunt_tracker.set_value, new_pairs[i][1],
                ChangeDecimalToValue(slope,new_pairs[i][0]),
                ChangeDecimalToValue(constunt,new_pairs[i][1]),
                run_time = 0.2
            )
            self.wait(0.1)


        self.wait(2)


        def outer_func(x):
            return 2*x+1

        dot = Dot().move_to(self.coords_to_point(-4, outer_func(-4)))
        self.play(FadeIn(dot), run_time = 2)
        self.wait()

        x_projection = DashedLine(self.coords_to_point(-4, outer_func(-4)),
                                  self.coords_to_point(-4, 0)
                                  ).set_color(YELLOW)
        y_projection = DashedLine(self.coords_to_point(-4, outer_func(-4)),
                                  self.coords_to_point(0, outer_func(-4))
                                  ).set_color(YELLOW)

        self.play(Write(x_projection),
                  Write(y_projection))
        self.wait()

        x = DecimalNumber(-4,num_decimals=2, include_sign = True)
        y = DecimalNumber(outer_func(-4),num_decimals=2, include_sign = True)
        parenth = TexMobject("(", ",", ")")
        pair_points = VGroup(parenth, x, y)
        parenth[2].move_to(dot.get_center() + 0.2*(UP+LEFT))
        y.next_to(parenth[2], LEFT, buff = 0.1)
        parenth[1].next_to(y, LEFT, buff = 0.1)
        x.next_to(parenth[1], LEFT, buff = 0.1)
        parenth[0].next_to(x, LEFT, buff = 0.1)
        
        new_f = TexMobject(" = ", "(", ")")
        slope_new = DecimalNumber(2,num_decimals=1, include_sign = True)
        constunt_new = DecimalNumber(1,num_decimals=1, include_sign = True)
        y_new = DecimalNumber(outer_func(-4),num_decimals=2, include_sign = True).to_corner(UL).set_color(RED)
        x_new = DecimalNumber(-4,num_decimals=2, include_sign = True).set_color(RED)
        new_f[0].next_to(y_new, RIGHT, buff = 0.1)
        slope_new.next_to(new_f[0], RIGHT, buff = 0.1)
        new_f[1].next_to(slope_new, RIGHT, buff = 0.1)
        x_new.next_to(new_f[1], RIGHT, buff = 0.1)
        new_f[2].next_to(x_new, RIGHT, buff = 0.1)
        constunt_new.next_to(new_f[2], RIGHT, buff = 0.1)
        new_formula = VGroup(x_new, y_new, slope_new, constunt_new, new_f )

        self.play(Write(pair_points))
        self.wait(0.5)
        self.play(ReplacementTransform(grp, new_formula))
        self.wait()

        
        tracker = ValueTracker(-4)
        def update_point(mob):
            mob.move_to(
                self.coords_to_point(
                    tracker.get_value(), 
                    outer_func(tracker.get_value()) 
                )
            )
        dot.add_updater(update_point)

        def update_x_projection(mob):
            mob.become(
                DashedLine(self.coords_to_point(tracker.get_value(), outer_func(tracker.get_value())),
                           self.coords_to_point(tracker.get_value(), 0)).set_color(YELLOW)
            )

        def update_y_projection(mob):
            mob.become(
                DashedLine(self.coords_to_point(tracker.get_value(), outer_func(tracker.get_value())),
                           self.coords_to_point(0, outer_func(tracker.get_value()))).set_color(YELLOW)
            )

        x_projection.add_updater(update_x_projection)
        y_projection.add_updater(update_y_projection)

        self.play(tracker.set_value, 4,
                  ChangeDecimalToValue(x,4),
                  ChangeDecimalToValue(y, outer_func(4)),
                  ChangeDecimalToValue(x_new,4),
                  ChangeDecimalToValue(y_new, outer_func(4)),
                  MaintainPositionRelativeTo(pair_points, dot),
                  run_time = 5)

        self.wait(2)

