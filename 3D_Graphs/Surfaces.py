from manimlib.imports import *
import numpy as np

#There seems to be no change between Scene and ThreeDScene
class CameraPosition1(SpecialThreeDScene):
    def construct(self):
        circulo=Circle()
        self.play(ShowCreation(circulo))
        self.wait()

class CameraPosition2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=0 * DEGREES)
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.wait()
        

class test(ThreeDScene):
    def construct(self):
        
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        axes = ThreeDAxes()
        z_tracker = ValueTracker(0)

        plane = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                z_tracker.get_value()
            ]), v_min=-2, v_max=2, u_min=-2, u_max=2,
            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32),fill_opacity=0.5
        )
        

        def plane_updater(mob):
            mob.become(
                ParametricSurface(
                    lambda u, v: np.array([
                        u,
                        v,
                        z_tracker.get_value()
                    ]), v_min=-2, v_max=2, u_min=-2, u_max=2,
                    checkerboard_colors=[RED_D, RED_E], resolution=(15, 32),fill_opacity=0.5
                )
            )
        
        plane.add_updater(plane_updater)


        self.add(axes)

        self.play(Write(plane))
        self.play(z_tracker.set_value, 0.5, run_time = 1.5,rate_func=linear)
        plane.remove_updater(plane_updater)
        self.play(FadeOut(plane))
        

class ThreeDParametricSpring(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        axes = ThreeDAxes()
        z_tracker = ValueTracker(0)

        parabola = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2
            ]), v_min=-2, v_max=2, u_min=-2, u_max=2,
            checkerboard_colors=[BLUE_D, BLUE_E], resolution=(15, 32),fill_opacity=0.5
        )
        plane = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                z_tracker.get_value()
            ]), v_min=-2, v_max=2, u_min=-2, u_max=2,
            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32),fill_opacity=0.5
        )
        curve = ParametricFunction(
            lambda theta: np.array([
                np.sqrt(z_tracker.get_value()) * np.cos(theta),
                np.sqrt(z_tracker.get_value()) * np.sin(theta),
                z_tracker.get_value()
            ]), color="#F1C40F", t_min=0, t_max=2*PI
        ).set_shade_in_3d(True)

        def plane_updater(mob):
            mob.become(
                ParametricSurface(
                    lambda u, v: np.array([
                        u,
                        v,
                        z_tracker.get_value()
                    ]), v_min=-2, v_max=2, u_min=-2, u_max=2,
                    checkerboard_colors=[RED_D, RED_E], resolution=(15, 32),fill_opacity=0.5
                )
            )
        def curve_updater(mob):
            mob.become(
                ParametricFunction(
                    lambda theta: np.array([
                        np.sqrt(z_tracker.get_value()) * np.cos(theta),
                        np.sqrt(z_tracker.get_value()) * np.sin(theta),
                        z_tracker.get_value()
                    ]), color="#F1C40F", t_min=0, t_max=2*PI
                ).set_shade_in_3d(True)
            )
        plane.add_updater(plane_updater)
        curve.add_updater(curve_updater)

        self.add(axes)
        self.play(Write(parabola))
        self.wait()
        self.play(Write(plane), Write(curve))
        self.wait()
        self.play(z_tracker.set_value, 0.5, run_time = 1.5,rate_func=linear)
        self.add(
            ParametricFunction(
            lambda theta: np.array([
                np.sqrt(0.5) * np.cos(theta),
                np.sqrt(0.5) * np.sin(theta),
                0.5
            ]), color="#D35400", t_min=0, t_max=2*PI
        ).set_shade_in_3d(True)
        )
        self.play(z_tracker.set_value, 1, run_time = 1.5,rate_func=linear)
        self.add(
            ParametricFunction(
            lambda theta: np.array([
                np.sqrt(1) * np.cos(theta),
                np.sqrt(1) * np.sin(theta),
                1
            ]), color="#E67E22", t_min=0, t_max=2*PI
        ).set_shade_in_3d(True)
        )
        self.play(z_tracker.set_value, 1.5, run_time = 1.5,rate_func=linear)
        self.add(
            ParametricFunction(
            lambda theta: np.array([
                np.sqrt(1.5) * np.cos(theta),
                np.sqrt(1.5) * np.sin(theta),
                1.5
            ]), color="#F39C12", t_min=0, t_max=2*PI
        ).set_shade_in_3d(True)
        )
        self.play(z_tracker.set_value, 2, run_time = 1.5,rate_func=linear)
        self.wait()
        self.move_camera(phi = 0, theta = -PI/2)
        plane.remove_updater(plane_updater)
        self.play(FadeOut(parabola), FadeOut(plane))
        


class Surfaces(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        z_tracker = ValueTracker(0)
        
        def param_gauss(u, v):
            x = u
            y = v
            d = np.sqrt(x * x + y * y)
            sigma, mu = 0.4, 0.0
            z = np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))
            return np.array([x, y, z])

        sphere = ParametricSurface(
            lambda u, v: np.array([
                2*np.cos(u)*np.cos(v),
                2*np.cos(u)*np.sin(v),
                2*np.sin(u)
            ]), v_min=0, v_max=2*PI, u_min=-PI/2, u_max=PI/2,
            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32)
        )

        self.begin_ambient_camera_rotation(rate=0.1)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, sphere)
        self.wait(4)

        gauss_plane = ParametricSurface(
            param_gauss,
            v_min=-2,
            v_max=+2,
            u_min=-2,
            u_max=+2,
            checkerboard_colors=[GREEN_D, GREEN_E], resolution=(15, 32)
            )
        gauss_plane.scale_about_point(2, ORIGIN)
        
        self.play(ReplacementTransform(sphere, gauss_plane))
        self.wait(4)

        hyperbolic = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v**2
            ]), v_min=-1, v_max=1, u_min=-1, u_max=1,
            checkerboard_colors=[YELLOW_D, YELLOW_E], resolution=(15, 32)
        )

        self.play(ReplacementTransform(gauss_plane, hyperbolic))
        self.wait(4)

        parabola = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2
            ]), v_min=-1.5, v_max=1.5, u_min=-1.5, u_max=1.5,
            checkerboard_colors=[BLUE_D, BLUE_E], resolution=(15, 32), fill_opacity = 0.5
        )

        self.play(ReplacementTransform(hyperbolic, parabola))
        self.wait(4)

        plane = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                z_tracker.get_value()
            ]), v_min=-2, v_max=2, u_min=-2, u_max=2,
            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32),fill_opacity=0.5
        )
        curve = ParametricFunction(
            lambda theta: np.array([
                np.sqrt(z_tracker.get_value()) * np.cos(theta),
                np.sqrt(z_tracker.get_value()) * np.sin(theta),
                z_tracker.get_value()
            ]), color="#F1C40F", t_min=0, t_max=2*PI
        ).set_shade_in_3d(True)

        def plane_updater(mob):
            mob.become(
                ParametricSurface(
                    lambda u, v: np.array([
                        u,
                        v,
                        z_tracker.get_value()
                    ]), v_min=-2, v_max=2, u_min=-2, u_max=2,
                    checkerboard_colors=[RED_D, RED_E], resolution=(15, 32),fill_opacity=0.5
                )
            )
        def curve_updater(mob):
            mob.become(
                ParametricFunction(
                    lambda theta: np.array([
                        np.sqrt(z_tracker.get_value()) * np.cos(theta),
                        np.sqrt(z_tracker.get_value()) * np.sin(theta),
                        z_tracker.get_value()
                    ]), color="#F1C40F", t_min=0, t_max=2*PI
                ).set_shade_in_3d(True)
            )
        plane.add_updater(plane_updater)
        curve.add_updater(curve_updater)

        

        self.play(Write(plane), Write(curve))
        self.wait()
        self.play(z_tracker.set_value, 0.5, run_time = 1.5,rate_func=linear)
        self.add(
            ParametricFunction(
            lambda theta: np.array([
                np.sqrt(0.5) * np.cos(theta),
                np.sqrt(0.5) * np.sin(theta),
                0.5
            ]), color="#D35400", t_min=0, t_max=2*PI
        ).set_shade_in_3d(True)
        )
        self.play(z_tracker.set_value, 1, run_time = 1.5,rate_func=linear)
        self.add(
            ParametricFunction(
            lambda theta: np.array([
                np.sqrt(1) * np.cos(theta),
                np.sqrt(1) * np.sin(theta),
                1
            ]), color="#E67E22", t_min=0, t_max=2*PI
        ).set_shade_in_3d(True)
        )
        self.play(z_tracker.set_value, 1.5, run_time = 1.5,rate_func=linear)
        self.add(
            ParametricFunction(
            lambda theta: np.array([
                np.sqrt(1.5) * np.cos(theta),
                np.sqrt(1.5) * np.sin(theta),
                1.5
            ]), color="#F39C12", t_min=0, t_max=2*PI
        ).set_shade_in_3d(True)
        )
        self.play(z_tracker.set_value, 2, run_time = 1.5,rate_func=linear)
        self.stop_ambient_camera_rotation()
        self.wait()
        self.move_camera(phi = 0, theta = -PI/2)
        plane.remove_updater(plane_updater)
        self.play(FadeOut(parabola), FadeOut(plane))

        

        








