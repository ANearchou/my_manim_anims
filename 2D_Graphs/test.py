from manimlib.imports import *


class coords(GraphScene):
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
        
        tracker = ValueTracker(1)
        func = lambda a: lambda x: a*x+1
        graph = VMobject()
        def update_func(mob):
            mob.become(
                self.get_graph(
                    func(tracker.get_value())
                )
            )

        update_func(graph)
        graph.add_updater(update_func)
        self.play(ShowCreation(graph))
        self.wait()
        self.play(
            tracker.set_value, 2,
            run_time = 3
        )
