from manimlib.imports import *

def get_vect_tex(*strings):
    result = ["\\vec{\\textbf{%s}}"%s for s in strings]
    if len(result) == 1:
        return result[0]
    else:
        return result


class cross(LinearTransformationScene):
    CONFIG = {
        "show_basis_vectors" : False,
        "v_coords" : [3, 2],
        "w_coords" : [2, -1],
    }
    def construct(self):
        self.plane.fade()
        v = self.add_vector(self.v_coords, color = YELLOW) #V_COLOR
        w = self.add_vector(self.w_coords, color = PINK) #W_COLOR
        for vect, name, direction in (v, "v", "left"), (w, "w", "right"):
            color = vect.get_color()
            vect.label = self.label_vector(
                vect, name, color = color, direction = direction,
            )
        self.v, self.w = v, w

        self.wait()



        self.add_unit_square()
        transform = self.get_matrix_transformation(np.array([
            self.v_coords, 
            self.w_coords,
        ]))
        self.square.apply_function(transform)
        self.play(
            ShowCreation(self.square),
            *list(map(Animation, [self.v, self.w]))
        )
        self.wait()
        self.play(FadeOut(self.square))
        v_copy = self.v.copy()
        w_copy = self.w.copy()
        self.play(v_copy.shift, self.w.get_end())
        self.play(w_copy.shift, self.v.get_end())
        self.wait()
        self.play(
            FadeIn(self.square),
            *list(map(Animation, [self.v, self.w, v_copy, w_copy]))
        )
        self.wait()
        self.play(*list(map(FadeOut, [v_copy, w_copy])))

class ScalingRule(LinearTransformationScene):
    CONFIG = {
        "v_coords" : [3, 2],
        "w_coords" : [2, -1],
        "show_basis_vectors" : False
    }
    def construct(self):
        self.lock_in_faded_grid()
        self.add_unit_square(animate = False)
        self.remove(self.square)
        square = self.square

        v = Vector(self.v_coords, color = YELLOW)
        w = Vector(self.w_coords, color = PINK)
        v.label = self.get_vector_label(v, "v", "right", color = YELLOW)
        w.label = self.get_vector_label(w, "w", "left", color = PINK)
        new_v = v.copy().scale(3)
        new_v.label = self.get_vector_label(
            new_v, "3\\vec{\\textbf{v}}", "right", color = YELLOW
        )
        for vect in v, w, new_v:
            vect.add(vect.label)

        transform = self.get_matrix_transformation(
            [self.v_coords, self.w_coords]
        )
        square.apply_function(transform)
        new_squares = VGroup(*[
            square.copy().shift(m*v.get_end())
            for m in range(3)
        ])

        v_tex, w_tex = get_vect_tex("v", "w")
        cross_product = TexMobject(v_tex, "\\times", w_tex)
        rhs = TexMobject("=3(", v_tex, "\\times", w_tex, ")")
        three_v = TexMobject("(3", v_tex, ")")
        for tex_mob in cross_product, rhs, three_v:
            tex_mob.set_color_by_tex(v_tex, YELLOW)
            tex_mob.set_color_by_tex(w_tex, PINK)
        equation = VGroup(cross_product, rhs)
        equation.arrange()
        equation.to_edge(UP)
        v_tex_mob = cross_product[0]
        three_v.move_to(v_tex_mob, aligned_edge = RIGHT)
        for tex_mob in cross_product, rhs:
            tex_mob.add_background_rectangle()

        self.add(cross_product)
        self.play(ShowCreation(v))
        self.play(ShowCreation(w))
        self.play(
            ShowCreation(square),
            *list(map(Animation, [v, w]))
        )
        self.wait()
        self.play(
            Transform(v, new_v),
            Transform(v_tex_mob, three_v),
        )
        self.wait()
        self.play(
            Transform(square, new_squares),
            *list(map(Animation, [v, w])),
            path_arc = -np.pi/6
        )
        self.wait()
        self.play(Write(rhs))
        self.wait()