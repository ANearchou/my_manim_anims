import numpy as np
import math
from manimlib.imports import *



class test(Scene):
    CONFIG = {
        "left_matrix":  [[5, -6 ,-3],[0  ,0 , 1],[4 ,-6 ,-3]],
        "right_matrix": [[-2 , 5  ,4],[-2, -6 , 2],[-3, -1 , 0]],
        "use_parens": True,
    }
    def construct(self):
        left = Matrix(self.left_matrix).shift(4*LEFT + DOWN)
        print(left[0])
        print(left[1][0])
        print(left[2][0])


class NumericalMatrixMultiplication(Scene):
    CONFIG = {
        "left_matrix":  [[5, -6 ,-3],[0  ,0 , 1],[4 ,-6 ,-3]],
        "right_matrix": [[-2 , 5  ,4],[-2, -6 , 2],[-3, -1 , 0]],
        "use_parens": True,
    }
    

    def construct(self):

        template = [TexMobject("("),TexMobject(-2), TexMobject(")("),TexMobject(-2), TexMobject(") + ("),TexMobject(-2), TexMobject(")("),
                    TexMobject(-2), TexMobject(") + ("),TexMobject(-2) ,TexMobject(")("),TexMobject(-2) ,TexMobject(") =")]
        
        template[0].move_to(2*UP + 6*LEFT)
        for i in range(1,len(template)):
            template[i].next_to(template[i-1], RIGHT, buff = 0.2)
        
        template_group = VGroup(
            *[mob for mob in template]
        )
        
        
        numerical_result = np.matmul(np.array(self.left_matrix), np.array(self.right_matrix))

        left = Matrix(self.left_matrix).shift(4.5*LEFT + DOWN)
        right = Matrix(self.right_matrix).next_to(left, buff = 0.1)
        eq = TexMobject("=").next_to(right, RIGHT, buff = 0.2)
        result = Matrix(
            np.matmul(np.array(self.left_matrix), np.array(self.right_matrix))
        ).next_to(eq, RIGHT, buff = 0.2)

        (m, k), n = np.array(self.left_matrix).shape, np.array(self.right_matrix).shape[1]
         
        self.play(Write(left), Write(right))
        self.play(Write(eq))
        self.play(Write(result[1][0]),
                  Write(result[2][0]))

        
        

        for a in range(m):
            if a > 0:
                t = 0.3
            else:
                t = 1
            for b in range(n):
                lrow = []
                rcol = []
                lnum = []
                rnum = []
                for c1 in range(a*k,a*k+k):
                    lrow.append(TexMobject(str(self.left_matrix[a][c1%n])).set_color(RED).move_to(left[0][c1].get_center()))
                    lnum.append(str(self.left_matrix[a][c1%n]))
                for c2 in range(b,n*(k-1)+1+b,n):
                    rcol.append(TexMobject(str(self.right_matrix[math.floor(c2/n)][b])).set_color(BLUE).move_to(right[0][c2].get_center()))
                    rnum.append(str(self.right_matrix[math.floor(c2/n)][b]))
                current = VGroup(*[m1 for m1 in lrow], *[m2 for m2 in rcol])
                self.play(FadeIn(current), run_time = t)
                self.wait(t)

                if a == 0 and b == 0:

                    self.play(lrow[0].move_to, template[1].get_center(),
                            lrow[1].move_to, template[5].get_center(),
                            lrow[2].move_to, template[9].get_center(),
                            rcol[0].move_to, template[3].get_center(),
                            rcol[1].move_to, template[7].get_center(),
                            rcol[2].move_to, template[11].get_center(),
                            Write(template[0]),Write(template[2]),Write(template[4]),
                            Write(template[6]),Write(template[8]),Write(template[10]),
                            Write(template[12])
                    , run_time = t)
                else:
                    self.play(lrow[0].move_to, template[1].get_center(),
                            lrow[1].move_to, template[5].get_center(),
                            lrow[2].move_to, template[9].get_center(),
                            rcol[0].move_to, template[3].get_center(),
                            rcol[1].move_to, template[7].get_center(),
                            rcol[2].move_to, template[11].get_center()
                    , run_time = t)
                self.wait(t)
                curr_result = TexMobject(str(numerical_result[a][b])).next_to(template[12], RIGHT, buff = 0.2).set_color(YELLOW)
                self.play(Write(curr_result), run_time = t)
                self.wait(t)
                self.play(curr_result.move_to, result[0][a*3+b].get_center(), run_time = t)
                self.wait(t)
                self.play(FadeOut(lrow[0]),
                          FadeOut(lrow[1]),
                          FadeOut(lrow[2]),
                          FadeOut(rcol[0]),
                          FadeOut(rcol[1]),
                          FadeOut(rcol[2])
                          , run_time = t)

        self.play(FadeOut(template[0]),FadeOut(template[2]),FadeOut(template[4]),
                    FadeOut(template[6]),FadeOut(template[8]),FadeOut(template[10]),FadeOut(template[12])
                    )
        
        
        
        # for a in range(m):
        #     for b in range(n):
        #         template = "(%s)(%s)" if self.use_parens else "%s%s"
        #         parts = [
        #             prefix + template % (left[a][c], right[c][b])
        #             for c in range(k)
        #             for prefix in ["" if c == 0 else "+"]
        #         ]


    def get_result_matrix(self, left, right):
        (m, k), n = left.shape, right.shape[1]
        
        mob_list = []
        for a in range(m):
            r = []
            for b in range(n):
                template = "(%s)(%s)" if self.use_parens else "%s%s"
                parts = [
                    prefix + template % (left[a][c], right[c][b])
                    for c in range(k)
                    for prefix in ["" if c == 0 else "+"]
                ]
                r.append(TexMobject(parts, next_to_buff=0.1))
                # mob_matrix[a][b] = TexMobject(parts, next_to_buff=0.1)
            mob_list.append(r)
        #mob_matrix = np.array([mob_list])
        mob_matrix = mob_list
        return Matrix(mob_matrix)

    def add_lines(self, left, right):
        line_kwargs = {
            "color": BLUE,
            "stroke_width": 2,
        }
        left_rows = [
            VGroup(*row) for row in left.get_mob_matrix()
        ]
        h_lines = VGroup()
        for row in left_rows[:-1]:
            h_line = Line(row.get_left(), row.get_right(), **line_kwargs)
            h_line.next_to(row, DOWN, buff=left.v_buff / 2.)
            h_lines.add(h_line)

        right_cols = [
            VGroup(*col) for col in np.transpose(right.get_mob_matrix())
        ]
        v_lines = VGroup()
        for col in right_cols[:-1]:
            v_line = Line(col.get_top(), col.get_bottom(), **line_kwargs)
            v_line.next_to(col, RIGHT, buff=right.h_buff / 2.)
            v_lines.add(v_line)

        self.play(ShowCreation(h_lines))
        self.play(ShowCreation(v_lines))
        self.wait()
        self.show_frame()

    def organize_matrices(self, left, right, result):
        equals = TexMobject("=")
        everything = VGroup(left, right, equals, result)
        everything.arrange()
        everything.set_width(FRAME_WIDTH - 1)
        self.add(everything)

    def animate_product(self, left, right, result):
        l_matrix = left.get_mob_matrix()
        r_matrix = right.get_mob_matrix()
        result_matrix = result.get_mob_matrix()
        circle = Circle(
            radius=l_matrix[0][0].get_height(),
            color=GREEN
        )
        circles = VGroup(*[
            entry.get_point_mobject()
            for entry in (l_matrix[0][0], r_matrix[0][0])
        ])
        (m, k), n = l_matrix.shape, r_matrix.shape[1]
        for mob in result_matrix.flatten():
            mob.set_color(BLACK)
        lagging_anims = []
        for a in range(m):
            for b in range(n):
                for c in range(k):
                    l_matrix[a][c].set_color(YELLOW)
                    r_matrix[c][b].set_color(YELLOW)
                for c in range(k):
                    start_parts = VGroup(
                        l_matrix[a][c].copy(),
                        r_matrix[c][b].copy()
                    )
                    result_entry = result_matrix[a][b].split()[c]

                    new_circles = VGroup(*[
                        circle.copy().shift(part.get_center())
                        for part in start_parts.split()
                    ])
                    self.play(Transform(circles, new_circles))
                    self.play(
                        Transform(
                            start_parts,
                            result_entry.copy().set_color(YELLOW),
                            path_arc=-np.pi / 2,
                            lag_ratio=0,
                        ),
                        *lagging_anims
                    )
                    result_entry.set_color(YELLOW)
                    self.remove(start_parts)
                    lagging_anims = [
                        ApplyMethod(result_entry.set_color, WHITE)
                    ]

                for c in range(k):
                    l_matrix[a][c].set_color(WHITE)
                    r_matrix[c][b].set_color(WHITE)
        self.play(FadeOut(circles), *lagging_anims)
        self.wait()
