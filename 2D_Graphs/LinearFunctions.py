from manimlib.imports import *
import random

class Lines(Scene):
    def construct(self):
        # SETUP GRAPH
        pairs = [(2,1),(2,3),(1.5,-2),(-0.3,-2.2),(-0.1,-2.2),(1,1)]
        axes = Axes()
        slope_tracker = ValueTracker(1)
        constunt_tracker = ValueTracker(0)

        func = lambda a,b: lambda x: a * x + b
        graph = VMobject()
        graph_kwargs = {"color": GREEN}
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
        

        # SET UPDATERS
        def update_graph(mob):
            mob.become(
                axes.get_graph(
                    func(slope_tracker.get_value(), constunt_tracker.get_value()),
                    **graph_kwargs
                )
            )
        # SET INITIAL STATE OF GRAPH
        update_graph(graph)
        graph.add_updater(update_graph)
        self.add(axes)
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
        self.wait(2)    

        #[7,6,5,4,3,2]

        # self.play(
        #     constunt_tracker.set_value, 1,
        #     ChangeDecimalToValue(constunt,1),
        #     run_time = 2
        # )
        # self.wait()


class PointsOnLine(GraphScene):
    CONFIG = {
            "y_min" : -7,
            "y_max" : 7,
            "x_min" : -7,
            "x_max" : 7,
            "graph_origin" : ORIGIN
    }

    def construct(self):
        def outer_func(x):
            return 2*x+1

        self.setup_axes(animate=True)
        self.wait()
        func = self.get_graph(lambda x: 2*x+1,
                             color = RED)
        self.play(ShowCreation(func),
                  run_time = 1)
        self.wait()

        dot = Dot().move_to(self.coords_to_point(-2, outer_func(-2)))
        self.play(FadeIn(dot), run_time = 2)
        self.wait()

        x_projection = DashedLine(self.coords_to_point(-2, outer_func(-2)),
                                  self.coords_to_point(-2, 0)
                                  ).set_color(YELLOW)
        y_projection = DashedLine(self.coords_to_point(-2, outer_func(-2)),
                                  self.coords_to_point(0, outer_func(-2))
                                  ).set_color(YELLOW)

        self.play(Write(x_projection),
                  Write(y_projection))
        self.wait(0.5)

        x = DecimalNumber(-2,num_decimals=2, include_sign = True)
        y = DecimalNumber(outer_func(-2),num_decimals=2, include_sign = True)
        parenth = TexMobject("(", ",", ")")
        pair_points = VGroup(parenth, x, y)
        parenth[2].move_to(dot.get_center() + 0.2*(UP+LEFT))
        y.next_to(parenth[2], LEFT, buff = 0.1)
        parenth[1].next_to(y, LEFT, buff = 0.1)
        x.next_to(parenth[1], LEFT, buff = 0.1)
        parenth[0].next_to(x, LEFT, buff = 0.1)
        
        self.play(Write(pair_points))
        self.wait()

        # pair_points = [
        #                 MaintainPositionRelativeTo(pp, dot)
        #                 for pp in [parenth, x, y]
        #                 ]
        

        tracker = ValueTracker(-2)
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
                  MaintainPositionRelativeTo(pair_points, dot),
                  run_time = 5)



class EquationTransform(Scene):
    CONFIG = {
            "y_min" : -7,
            "y_max" : 7,
            "x_min" : -7,
            "x_max" : 7,
            "graph_origin" : ORIGIN
    }

    def construct(self):
        def outer_func(x):
            return 2*x+1

        
        equation = TexMobject("y ","="," 2x + 1").to_corner(UL)
        equation_cp = TexMobject("y = 2x + 1").to_corner(UL)
        eq_trans = TexMobject("2(","x",") + 1 ","="," y").to_corner(UR)
        eq_trans[1].set_color(RED)
        eq_trans[4].set_color(RED)
        grp = VGroup(eq_trans[0],eq_trans[1],eq_trans[2])

        self.wait(2)
        self.play(Write(equation), Write(equation_cp))
        self.wait(2)

        self.play(ReplacementTransform(equation[0], grp),
                  ReplacementTransform(equation[1], eq_trans[3]),
                  ReplacementTransform(equation[2], eq_trans[4])
                  )
        
        self.wait(2)





class test(Scene):
    def construct(self):
        # SETUP GRAPH
        pairs = [(2,1),(2,3),(1.5,-2),(-0.3,-2.2),(-0.1,-2.2),(1,1)]
        axes = Axes()
        slope_tracker = ValueTracker(1)
        constunt_tracker = ValueTracker(0)

        func = lambda a,b: lambda x: a * x + b
        graph = VMobject()
        graph_kwargs = {"color": GREEN}
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
        

        # SET UPDATERS
        def update_graph(mob):
            mob.become(
                axes.get_graph(
                    func(slope_tracker.get_value(), constunt_tracker.get_value()),
                    **graph_kwargs
                )
            )
        # SET INITIAL STATE OF GRAPH
        update_graph(graph)
        graph.add_updater(update_graph)
        self.add(axes)
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

        # func = self.get_graph(lambda x: 2*x+1,
        #                      color = RED)
        # self.play(ShowCreation(func),
        #           run_time = 1)
        # self.wait()

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








class ttest(Scene):
    def construct(self):
        # t = ValueTracker(1)
        l = DecimalNumber(1, num_decimals = 2, include_sign = True)
        l2 = DecimalNumber(2, num_decimals = 2, include_sign = True)
        l2.next_to(l, RIGHT, buff = 1)

        self.play(Write(l), Write(l2))
        self.wait()
        self.play(ChangeDecimalToValue(l,2),
                  ChangeDecimalToValue(l2, 3))

        l_cp = l.copy()
        l2_cp = l2.copy()

        self.add(l_cp, l2_cp)
        self.wait()

        self.play(l.shift, DOWN,
                  l2.shift, DOWN,
                  l_cp.shift, 2*DOWN,
                  l2_cp.shift, 2*DOWN)
        self.wait(2)
