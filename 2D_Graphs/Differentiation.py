from manimlib.imports import *

class Diff(GraphScene):
    CONFIG = {
            "x_min" : -0.25,
            "x_max" : 6,
            "y_min" : -0.25,
            "y_max" : 6,
            "grapg_origin" : 3*LEFT + 3*DOWN,
            "x_axis_label" : None,
            "y_axis_label" : None,
            "x" : 1.5,
            "h" : 3
        }
    def construct(self):

        # OPTIONS
        function = lambda x: 4-1.5/2*(x-3.5)**2 + (x-3)**4 / 24
        derivative = lambda x: -1.5 * (x-3.5) + 1/6 * (x - 3)**3

        function_kwargs = {"x_min" : 1.1,
                        "x_max" : 5.3,
                        "color" : GOLD_E}

        
        self.setup_axes(animate = True)
        self.wait()
        func = self.get_graph(function,
                            **function_kwargs)
        self.play(ShowCreation(func))
        self.wait()

        fx = self.coords_to_point(self.x, function(self.x))
        #h = self.h
        fx_h = self.coords_to_point(self.x + self.h, function(self.x + self.h)) 

        x_label = TexMobject("x").move_to( self.coords_to_point(self.x, -0.3) )
        x_h_label = TexMobject("x+h").move_to( self.coords_to_point(self.x + self.h, -0.3) )
        
        h_arrow = Line(self.coords_to_point(self.x, -0.75), self.coords_to_point(self.x+ self.h, -0.75)).set_color(RED)
        h_label = TexMobject("h").set_color(RED).next_to(h_arrow, DOWN, buff = 0.1)

        d1_helper = Line(self.coords_to_point(self.x+self.h,0)+0.1*UP,self.coords_to_point(self.x+self.h,0)+0.1*DOWN)
        d2_helper = Line(self.coords_to_point(0, function(self.x+self.h))+0.1*LEFT,self.coords_to_point(0, function(self.x+self.h))+0.1*RIGHT)
        
        d3_helper = Line(self.coords_to_point(self.x,0)+0.1*UP,self.coords_to_point(self.x,0)+0.1*DOWN)
        d4_helper = Line(self.coords_to_point(0, function(self.x))+0.1*LEFT,self.coords_to_point(0, function(self.x))+0.1*RIGHT)

        self.play(Write(d3_helper))
        self.play(Write(x_label))
        self.play(Write(h_arrow))
        self.play(Write(h_label))
        self.play(Write(d1_helper))
        self.play(Write(x_h_label))
        self.wait(0.3)

        x_first_proj = DashedLine( self.coords_to_point(self.x, 0), self.coords_to_point(self.x, function(self.x)) )
        x_h_first_proj = DashedLine( self.coords_to_point(self.x + self.h, 0), self.coords_to_point(self.x + self.h, function(self.x + self.h)) )
        self.play(Write(x_first_proj), Write(x_h_first_proj))
        self.wait(0.3)

        first_point_x = Dot( self.coords_to_point(self.x, function(self.x)))
        first_point_x_h = Dot( self.coords_to_point(self.x + self.h, function(self.x + self.h)))
        self.play(Write(first_point_x), Write(first_point_x_h))
        self.wait(0.3)

        y_first_proj = DashedLine( self.coords_to_point(self.x, function(self.x)), self.coords_to_point(0, function(self.x)) )
        y_h_first_proj = DashedLine( self.coords_to_point(self.x + self.h, function(self.x + self.h)), self.coords_to_point(0, function(self.x + self.h)) )
        self.play(Write(y_first_proj), Write(y_h_first_proj), Write(d2_helper), Write(d4_helper))
        self.wait(0.3)

        fx_label = TexMobject("f(x)").next_to(y_first_proj.get_end(), LEFT, buff = 0.3)
        fx_h_label = TexMobject("f(x+h)").next_to(y_h_first_proj.get_end(), LEFT, buff = 0.3)
        self.play(Write(fx_label), Write(fx_h_label))
        self.wait(0.3)


        line = lambda a,b: lambda x: a * x + b
        graph = VMobject()
        graph_kwargs = {"color": DARK_BLUE}

        h_tracker = ValueTracker(self.h) 
        slope_tracker = ValueTracker((function(self.x) - function(self.x + h_tracker.get_value()))/(self.x - (self.x + h_tracker.get_value())))
        constunt_tracker = ValueTracker(function(self.x) - slope_tracker.get_value() * self.x)

        def dot_updater(mob):
            mob.move_to(self.coords_to_point(self.x + h_tracker.get_value(), function(self.x + h_tracker.get_value())))
        first_point_x_h.add_updater(dot_updater)

        def update_graph(mob):
            slope = (self.point_to_coords(first_point_x_h.get_center())[1] - self.point_to_coords(first_point_x.get_center())[1] )/( self.point_to_coords(first_point_x_h.get_center())[0] - self.point_to_coords(first_point_x.get_center())[0] )
            constunt = self.point_to_coords(first_point_x_h.get_center())[1] - slope * self.point_to_coords(first_point_x_h.get_center())[0]
            mob.become(
                self.get_graph(
                    line(slope, constunt),
                    **graph_kwargs
                )
            )
        graph.add_updater(update_graph)

        def horizontal_updater(mob):
            mob.become( DashedLine( first_point_x_h.get_center(), self.coords_to_point(0, self.point_to_coords(first_point_x_h.get_center())[1]) ) ) 
               
        y_h_first_proj.add_updater(horizontal_updater)

        def vertical_updater(mob):
            mob.become( DashedLine( first_point_x_h.get_center(), self.coords_to_point( self.point_to_coords(first_point_x_h.get_center())[0],0 ) ) ) 
        
        x_h_first_proj.add_updater(vertical_updater)
        
        def arrow_updater(mob):
            mob.become( Line(self.coords_to_point(self.x, -0.75), self.coords_to_point(self.x+ h_tracker.get_value(), -0.75)).set_color(RED) )
        h_arrow.add_updater(arrow_updater)

        def d1_updater(mob):
            mob.move_to(self.coords_to_point(self.x+h_tracker.get_value(),0))
        d1_helper.add_updater(d1_updater)
        def d2_updater(mob):
            mob.move_to(self.coords_to_point(0, function(self.x+h_tracker.get_value())))
        d2_helper.add_updater(d2_updater)
        
        self.play(ShowCreation(graph))
        self.wait(2)


        dx = DashedLine(self.coords_to_point(self.x , function(self.x)) , self.coords_to_point(self.x + h_tracker.get_value() ,  function(self.x))).set_color(GREEN)
        dx_label = TexMobject("{\\scriptsize dx}").next_to(dx, DOWN, buff = 0.1).set_color(GREEN)
        dy = DashedLine(self.coords_to_point(self.x + h_tracker.get_value() ,  function(self.x)) , self.coords_to_point(self.x + h_tracker.get_value() ,  function(self.x + h_tracker.get_value()))).set_color(GREEN)
        dy_label = TexMobject("{\\scriptsize dy}").next_to(dy, RIGHT, buff = 0.1).set_color(GREEN)

        ds_helper = Dot(self.coords_to_point(self.x+self.h, function(self.x)))
        def ds_updater(mob):
            mob.move_to(self.coords_to_point(self.x+h_tracker.get_value(), function(self.x)))

        def dx_updater(mob):
            #mob.become( DashedLine(self.coords_to_point(self.x , function(self.x)) , self.coords_to_point(self.x + h_tracker.get_value() ,  function(self.x))).set_color(GREEN) )
            mob.become(
                DashedLine( self.coords_to_point(self.x,function(self.x)) , self.coords_to_point(self.x + h_tracker.get_value(), function(self.x))).set_color(GREEN)
            )
        
        def dy_updater(mob):
            #mob.become( DashedLine(self.coords_to_point(self.x + h_tracker.get_value() ,  function(self.x)) , self.coords_to_point(self.x + h_tracker.get_value() ,  function(self.x))).set_color(GREEN)  )
            mob.become(
                DashedLine( self.coords_to_point( self.x + h_tracker.get_value(), function(self.x) ) , self.coords_to_point( self.x + h_tracker.get_value(), function(self.x + h_tracker.get_value()))).set_color(GREEN)
            )
        
        dx.add_updater(dx_updater)
        dy.add_updater(dy_updater)

        self.play(Write(dx), Write(dy))
        self.wait(0.3)
        self.play(Write(dx_label), Write(dy_label))
        self.wait()

        self.play(h_tracker.set_value, 0.7, 
                  MaintainPositionRelativeTo(x_h_label, d1_helper),
                  MaintainPositionRelativeTo(fx_h_label, d2_helper),
                  MaintainPositionRelativeTo(h_label, h_arrow),
                  MaintainPositionRelativeTo(dx_label, dx),
                  MaintainPositionRelativeTo(dy_label, dy),
                  run_time = 5,
                  rate_func=linear)
        self.play(h_tracker.set_value, 0.0000001, 
                  MaintainPositionRelativeTo(h_label, h_arrow),
                  MaintainPositionRelativeTo(dx_label, dx),
                  MaintainPositionRelativeTo(dy_label, dy),
                  run_time = 1,
                  rate_func=linear)
        self.wait()

        self.play(FadeOut(dy_label), 
                  FadeOut(dx_label),
                  FadeOut(fx_h_label), 
                  FadeOut(x_h_label), 
                  FadeOut(h_label),
                  FadeOut(x_h_first_proj),
                  FadeOut(y_h_first_proj),
                  FadeOut(first_point_x_h))
        self.wait()

        der_label = TexMobject("f'(x)").move_to(self.coords_to_point(5.5,6)).set_color(DARK_BLUE)
        self.play(Write(der_label))
        self.wait(0.3)

        x_tracker = ValueTracker(self.x)
        def der_x_updater(mob):
            mob.become(
                DashedLine( self.coords_to_point(x_tracker.get_value(), 0), self.coords_to_point(x_tracker.get_value(), function(x_tracker.get_value())) )
            )
        def der_y_updater(mob):
            mob.become(
                DashedLine( self.coords_to_point(x_tracker.get_value(), function(x_tracker.get_value())), self.coords_to_point(0, function(x_tracker.get_value())) )
            )
        x_first_proj.add_updater(der_x_updater)
        y_first_proj.add_updater(der_y_updater)

        graph.remove_updater(update_graph)

        def der_updater(mob):
            slope = derivative(x_tracker.get_value())
            constunt = function(x_tracker.get_value()) - slope*x_tracker.get_value()
            mob.become(
                self.get_graph(
                    line(slope, constunt),
                    **graph_kwargs
                )
            )
        graph.add_updater(der_updater)

        def der_dot_updater(mob):
            mob.move_to(
                self.coords_to_point(x_tracker.get_value(), function(x_tracker.get_value()))
            )
        first_point_x.add_updater(der_dot_updater)

        self.play(x_tracker.set_value, 5.2,
                  run_time = 5)
        self.wait()




        





class test(GraphScene):
    def construct(self):
        # slope_tracker = ValueTracker(3)
        # constunt_tracker = ValueTracker(slope_tracker.get_value())
        #self.setup_axes()
        # print(self.coords_to_point(0,0))
        # print(self.point_to_coords([-4, -2.5, 0]))
        self.setup_axes()
        y = DashedLine(self.coords_to_point(0,0), self.coords_to_point(3,0))
        self.play(Write(y))

        tracker = ValueTracker(3)
        def up(mob):
            mob.become( DashedLine(self.coords_to_point(0,0), self.coords_to_point(tracker.get_value(),0)) )

        y.add_updater(up)
        self.play(tracker.set_value, 0.7)
        self.wait()