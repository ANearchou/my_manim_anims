from manimlib.imports import *
import numpy as np
import random as rd

class Normal(GraphScene):
    CONFIG = {
        "x_min" : -4,
        "x_max" : 4,
        "y_min" : 0,
        "y_max" : 0.5,
        "y_axis_height": 4,
        "graph_origin" : 3*DOWN,
        "x_axis_label" : None,
        "y_axis_label" : None,
        "miu" : 0,
        "sigma" : 1,
        "bins" : 16
    }
    def construct(self):

        self.setup_axes(animate = True)
        self.wait()

        pdf = lambda m, s: lambda x: 1/(s*np.sqrt(2*np.pi)) * np.exp((-0.5)*((x - m)/s)**2) 

        #pdf = lambda x: x
        #num_line = NumberLine().move_to(3*UP)
        num_line = NumberLine(x_min=self.x_min -1,
                                x_max=self.x_max +1 ,
                                #unit_size=self.space_unit_to_x,
                                tick_frequency=0.5,
                                x_labeled_nums= True,
                                #leftmost_tick=self.x_leftmost_tick,
                                #numbers_with_elongated_ticks=self.x_labeled_nums,
                                color=BLUE
                                ).move_to(3*UP)
        
        distribution = self.get_graph( pdf(self.miu, self.sigma),
                                      color = BLUE)

    
        self.play(ShowCreation(distribution))
        self.wait()

        self.play(ShowCreation(num_line))
        self.wait()

        all_num = []
        hist = Dot()
        partition_length = (self.x_max - self.x_min) / self.bins
        partition_points = np.linspace(self.x_min, self.x_max, self.bins+1)
        rd.seed(1)
        
        for i in range(100):
            x = rd.normalvariate(self.miu, self.sigma)
            all_num.append( x )
            arr = np.array(all_num)
            self.play(ShowCreation(
                        Dot(num_line.number_to_point(x)).set_color(RED)
                        ,run_time = 0.1))

            graph = []
            for j in range(self.bins):
                graph.append(
                    Polygon(self.coords_to_point(partition_points[j],0),
                            self.coords_to_point(partition_points[j+1],0),
                            self.coords_to_point(partition_points[j+1],len(arr[(arr >= partition_points[j]) & (arr < partition_points[j+1])]) / len(arr) / partition_length),
                            self.coords_to_point(partition_points[j],len(arr[(arr >= partition_points[j]) & (arr < partition_points[j+1])]) / len(arr) / partition_length),
                            fill_opacity = 1 ).set_color(color=[GREEN,YELLOW]).set_sheen_direction([0,1,0])
                )
            hist_new = VGroup(*graph)
            if i == 1:
                self.play(ReplacementTransform(hist, hist_new),run_time = 0.1)
            if i > 1:
                self.play(ReplacementTransform(hist, hist_new),run_time = 0.1)

            hist = hist_new






        
