from manimlib.imports import *
import numpy as np

class Integral2(Scene):
    
    def construct(self):
        axes_kwargs = {
            "x_min" : -1,
            "x_max" : 7,
            "y_min" : -1,
            "y_max" : 7,
            "axes_center" : 3*LEFT + 3*DOWN
        }
        function = lambda x: 2*np.sin(0.7*x-1)+2
        function_kwargs = {"x_min" : 0.5,
                           "x_max" : 4.25}

        axes = Axes(**axes_kwargs)
        self.play(ShowCreation(axes))
        self.wait()

class Integral(GraphScene):
    CONFIG = {
            "x_min" : -1,
            "x_max" : 7,
            "y_min" : -1,
            "y_max" : 7,
            "grapg_origin" : 3*LEFT + 3*DOWN,
            "x_axis_label" : None,
            "y_axis_label" : None
        }
    def construct(self):
        
        # OPTIONS
        definition_bounds = [1.5, 4.5]
        function_kwargs = {"x_min" : 0.5,
                           "x_max" : 5.5,
                           "color" : GREEN}
        color_direction=[0,1,0]


        def fact(n):
            f=1    
            for i in range(1,n+1): 
                f = f * i
            return f
        function = lambda x: 4+(x-3)-(x-3)**3/fact(3)+(x-3)**5/fact(5)
        
        self.setup_axes(animate = True)
        self.wait()

        func = self.get_graph(function,
                              **function_kwargs)
        self.play(ShowCreation(func))
        self.wait()

        for i in [2**ii for ii in range(1,7)]:
            partition_length = (definition_bounds[1] - definition_bounds[0])/i
            partition_points = []
            for j in range(0,i+1):
                partition_points.append(definition_bounds[0] + j*partition_length)

            recs = []
            for jj in range(i):
                mob = Polygon(self.coords_to_point( partition_points[jj],0 ),
                            self.coords_to_point( partition_points[jj],function(partition_points[jj]) ),  
                            self.coords_to_point( partition_points[jj + 1],function(partition_points[jj]) ),
                            self.coords_to_point( partition_points[jj + 1],0),
                            fill_opacity = 1).set_color(color=[RED,BLUE]).set_sheen_direction(color_direction)    
                recs.append(mob)

            self.play(
                      *[ShowCreation(recs[k]) for k in range(len(recs))]
                      )
            self.wait()
        self.wait(2)