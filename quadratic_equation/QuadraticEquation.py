from manimlib.imports import *
from io import *

class SolveGeneralQuadraticEquation(Scene):
    def construct(self):
        formulas=[]

        a_color=RED_B
        b_color=BLUE_B
        c_color=GREEN_B
        x_color=YELLOW_B

        for i in range(1,17):
            formula_open=open("C:/my_manim_anims/quadratic_equation/formulas/formula%de.txt"%i,"r")
            formula=formula_open.readlines()
            formulas.append(TexMobject(*formula).scale(1.7))


        for i in range(10):
            formulas[i].set_color_by_tex("a", a_color)
            formulas[i].set_color_by_tex("b", b_color)
            formulas[i].set_color_by_tex("c", c_color)
            formulas[i].set_color_by_tex("x", x_color)

        set_color_formulas=[
                        (10,
                            (
                                (a_color,[10,25,31]),
                                (b_color,[6,21]),
                                (c_color,[26]),
                                (x_color,[3]))
                            ),
                        (11,
                            (
                                (a_color,[6,18,24]),
                                (b_color,[3,14]),
                                (c_color,[19]),
                                (x_color,[0]))
                            ),
                        (12,
                            (
                                (a_color,[7,18,24]),
                                (b_color,[4,14]),
                                (c_color,[19]),
                                (x_color,[0]))
                            ),
                        (13,
                            (
                                (a_color,[7,18,23]),
                                (b_color,[4,14]),
                                (c_color,[20]),
                                (x_color,[0]))
                            ),
                        (14,
                            (
                                (a_color,[13,18]),
                                (b_color,[4,9]),
                                (c_color,[15]),
                                (x_color,[0]))
                            ),
        ]
        for f,changes in set_color_formulas:
            for colors,symbols in changes:
                for symbol in symbols:
                    formulas[f][symbol].set_color(colors)
        
        self.play(
            LaggedStart(*[
                Write(formulas[0][i])
                for i in [0,  1, 3,  4,  5,  6,  7,  8,  9, 10]
                # If you use Write(self.formulas[0])
                # the animation is not displayed correctly because
                # self.formulas[2] is empty
            ])
            
        )
        
        self.set_changes()
        self.step_formula(n_step=1,
            changes=self.set_of_changes[0],
            fade=[10],
            path_arc=-PI/2,
            forms=formulas
            )
        self.step_formula(n_step=2,
            changes=self.set_of_changes[1],
            write=[6,14],
            pre_copy=[0],
            pos_copy=[15],
            forms=formulas
            )
        self.step_formula(n_step=3,
            changes=self.set_of_changes[2],
            pos_write=[10,  11, 13, 14, 15, 16, 18, 20, 28, 29, 31, 32, 33, 34, 36, 38],
            forms=formulas
            )
        self.step_formula(n_step=4,
            changes=self.set_of_changes[3],
            forms=formulas
            )
        self.step_formula(n_step=5,
            changes=self.set_of_changes[4],
            fade=[20,27],
            pre_copy=[29],
            pos_copy=[28],
            forms=formulas
            )
        self.step_formula(n_step=6,
            changes=self.set_of_changes[5],
            fade=[19],
            forms=formulas
            )
        self.step_formula(n_step=7,
            changes=self.set_of_changes[6],
            pos_write=[25,28],
            forms=formulas
            )
        self.step_formula(n_step=8,
            changes=self.set_of_changes[7],
            pos_write=[32,26],
            forms=formulas
            )
        self.step_formula(n_step=9,
            changes=self.set_of_changes[8],
            forms=formulas
            )
        self.step_formula(n_step=10,
            changes=self.set_of_changes[9],
            pos_write=[0,   1,  16, 18, 20],
            forms=formulas
            )
        self.step_formula(n_step=11,
            changes=self.set_of_changes[10],
            fade=[0,    1,  2,  12, 14],
            forms=formulas
            )
        self.step_formula(n_step=12,
            changes=self.set_of_changes[11],
            forms=formulas
            )
        self.step_formula(n_step=13,
            changes=self.set_of_changes[12],
            forms=formulas,
            fade=[25]
            )
        self.step_formula(n_step=14,
            changes=self.set_of_changes[13],
            forms=formulas
            )
        #
        c1=SurroundingRectangle(formulas[14],buff=0.2)
        c2=SurroundingRectangle(formulas[14],buff=0.2)
        c2.rotate(PI)
        self.play(ShowCreationThenDestruction(c1),ShowCreationThenDestruction(c2))
        self.wait(2)

    def import_formulas(self):
        # from quadratic_equation.formulas.formulas import formulas
        # self.formulas=formulas

        

        formulas=[]

        a_color=RED_B
        b_color=BLUE_B
        c_color=GREEN_B
        x_color=YELLOW_B

        for i in range(1,17):
            formula_open=open("C:/my_manim_anims/quadratic_equation/formulas/formula%de.txt"%i,"r")
            formula=formula_open.readlines()
            formulas.append(TexMobject(*formula).scale(1.7))


        for i in range(10):
            formulas[i].set_color_by_tex("a", a_color)
            formulas[i].set_color_by_tex("b", b_color)
            formulas[i].set_color_by_tex("c", c_color)
            formulas[i].set_color_by_tex("x", x_color)

        set_color_formulas=[
                        (10,
                            (
                                (a_color,[10,25,31]),
                                (b_color,[6,21]),
                                (c_color,[26]),
                                (x_color,[3]))
                            ),
                        (11,
                            (
                                (a_color,[6,18,24]),
                                (b_color,[3,14]),
                                (c_color,[19]),
                                (x_color,[0]))
                            ),
                        (12,
                            (
                                (a_color,[7,18,24]),
                                (b_color,[4,14]),
                                (c_color,[19]),
                                (x_color,[0]))
                            ),
                        (13,
                            (
                                (a_color,[7,18,23]),
                                (b_color,[4,14]),
                                (c_color,[20]),
                                (x_color,[0]))
                            ),
                        (14,
                            (
                                (a_color,[13,18]),
                                (b_color,[4,9]),
                                (c_color,[15]),
                                (x_color,[0]))
                            ),
        ]
        for f,changes in set_color_formulas:
            for colors,symbols in changes:
                for symbol in symbols:
                    formulas[f][symbol].set_color(colors)

        #return formulas



    def write_formulas(self):
        self.play(
            LaggedStart(*[
                Write(self.formulas[0][i])
                for i in [0,  1, 3,  4,  5,  6,  7,  8,  9, 10]
                # If you use Write(self.formulas[0])
                # the animation is not displayed correctly because
                # self.formulas[2] is empty
            ])
            
        )

    def set_changes(self):
        self.set_of_changes=[
        #1
        [[
                        (   0,  1,  3,  4,  5,  6,  7,  8,  9   ),
                        (   0,  1,  3,  4,  5,  6,  8,  9,  7   )
        ]],
        #2
        [[
                        (   0,      1,  3,  4,  5,  6,  7,  8,  9   ),
                        (   7,      0,  2,  3,  5,  9,  10, 11, 13  )
        ]],
        #3
        [[
            (   0,  2,  3,  5,  6,  7,  9,  10, 11, 13, 14, 15  ),
            (   0,  2,  3,  5,  6,  7,  9,  21, 22, 24, 25, 26  )
        ]],
        #4
        [[
                (   0,  2,  10, 11, 13, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 28, 29, 31, 32, 33, 34, 36, 38  ,5,6,7,9,3),
                (   1,  11, 2,  0,  4,  5,  6,  7,  9,  11, 12, 13, 15, 16, 17, 19, 20, 22, 23, 24, 25, 27, 29  ,4,5,7,1,2)
        ]],
        #5
        [[
        (   0,  1,  2,  4,  5,  6,  7,  9,  11, 12, 13, 15, 16, 17, 19, 22, 23, 24, 25, 29),
        (   0,  1,  2,  4,  5,  6,  7,  9,  11, 12, 13, 15, 16, 17, 19, 21, 24, 25, 26, 23)
        ]],
        #6
        [[
            (   0,  1,  2,  4,  5,  6,  7,  9,  11, 12, 13, 15, 16, 17, 21, 23, 24, 25, 26, 28  ),
            (   0,  1,  2,  4,  5,  6,  7,  9,  11, 12, 23, 25, 26, 27, 14, 16, 17, 18, 19, 21  )
        ]],
        #7
        [[
            (   0,  1,  2,      4,  5,  6,  7,      9,      11, 12,     14,     16, 17, 18, 19,     21,     23,     25, 26, 27  ),
            (   0,  1,  2,      4,  5,  6,  7,      9,      11, 12,     14,     16, 17, 18, 19,     21,     23,     26, 27, 29  )
        ]],
        #8
        [[
            (   0,  1,  2,      4,  5,  6,  7,      9,      11, 12,     14,     16, 17, 18, 19,     21,     23,     25, 26, 27, 28, 29, ),
            (   0,  1,  2,      4,  5,  6,  7,      9,      11, 12,     14,     16, 17, 18, 19,     21,     23,     25, 27, 28, 29, 30, )
        ]],
        #9
        [[
            (   0,  1,  2,      4,  5,  6,  7,      9,      11, 12,     14,     16, 17, 18, 19,     21,     23,     25, 26, 27, 28, 29, 30,     32, ),
            (   0,  1,  2,      4,  5,  6,  7,      9,      11, 12,     14,     16, 21, 22, 23,     25,     17,     18, 19, 20, 21, 22, 23,     25, )
        ]],
        #10
        [[
            (   0,  1,  2,      4,  5,  6,  7,      9,      11, 12,     14,     16, 17, 18, 19, 20, 21, 22, 23,     25, ),
            (   2,  3,  5,      6,  7,  8,  10,     12,     14, 15,     21,     22, 23, 24, 25, 26, 27, 30, 31,     32, )
        ]],
        #11
        [[
            (               3,      5,  6,  7,  8,      10,                 15, 16,     18,     20, 21, 22, 23, 24, 25, 26, 27,         30, 31, 32, ),
            (               0,      1,  3,  4,  5,      6,                  8,  9,      10,     12, 14, 15, 16, 17, 18, 19, 20,         21, 24, 25, )
        ]],
        #12
        [[
            (   0,  1,      3,  4,  5,  6,      8,  9,  10,     12,     14, 15, 16, 17, 18, 19, 20, 21,         24, 25, ),
            (   0,  2,      4,  5,  6,  7,      1,  9,  10,     12,     14, 15, 16, 17, 18, 19, 20, 21,         24, 25, )
        ]],
        #13
        [[
            (   0,  1,  2,      4,  5,  6,  7,      9,  10,     12,     14, 15, 16, 17, 18, 19, 20, 21,         24, ),
            (   0,  1,  2,      4,  5,  6,  7,      9,  11,     12,     14, 15, 16, 17, 18, 20, 21, 22,         23, )
        ]],
        #14
        [[
            (   0,  1,  2,      4,  5,  6,  7,      9,      11, 12,     14, 15, 16, 17, 18,     20, 21, 22, 23, ),
            (   0,  1,  3,      4,  16, 17, 18,     5,      6,  7,      9,  10, 11, 12, 13,     15, 16, 17, 18, )
        ]]
        ]

    def step_formula(self,
                            pre_write=[],
                            pos_write=[],
                            pre_fade=[],
                            pos_fade=[],
                            fade=[],
                            write=[],
                            changes=[[]],
                            path_arc=0,
                            n_step=0,
                            pre_copy=[],
                            pos_copy=[],
                            time_pre_changes=0.3,
                            time_pos_changes=0.3,
                            run_time=2,
                            time_end=0.3,
                            pre_order=["w","f"],
                            pos_order=["w","f"],
                            forms = []):
        formula_copy=[]
        for c in pre_copy:
            formula_copy.append(forms[n_step-1][c].copy())

        for ani_ in pre_order:
            if len(pre_write)>0 and ani_=="w":
                self.play(*[Write(forms[n_step-1][w])for w in pre_write])
            if len(pre_fade)>0 and ani_=="f":
                self.play(*[FadeOut(forms[n_step-1][w])for w in pre_fade])

        self.wait(time_pre_changes)

        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    forms[n_step-1][i],forms[n_step][j],
                    path_arc=path_arc
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                *[FadeOut(forms[n_step-1][f])for f in fade if len(fade)>0],
                *[Write(forms[n_step][w])for w in write if len(write)>0],
                *[ReplacementTransform(formula_copy[j],forms[n_step][f])
                for j,f in zip(range(len(pos_copy)),pos_copy) if len(pre_copy)>0
                ],
                run_time=run_time
            )

        self.wait(time_pos_changes)

        for ani_ in pos_order:
            if len(pos_write)>0 and ani_=="w":
                self.play(*[Write(forms[n_step][w])for w in pos_write])
            if len(pos_fade)>0 and ani_=="f":
                self.play(*[FadeOut(forms[n_step][w])for w in pos_fade])

        self.wait(time_end)



class CheckFormulaByTXT(Scene):
    CONFIG={
    "camera_config":{"background_color": BLACK},
    "svg_type":"text",
    "text": TexMobject(""),
    "file":"",
    "svg_scale":0.9,
    "angle":0,
    "flip_svg":False,
    "fill_opacity": 1,
    "remove": [],
    "stroke_color": WHITE,
    "fill_color": WHITE,
    "stroke_width": 3,
    "numbers_scale":0.5,
    "show_numbers": True,
    "animation": False,
    "direction_numbers": UP,
    "color_numbers": RED,
    "space_between_numbers":0,
    "show_elements":[],
    "color_element":PURPLE,
    "set_size":"width",
    "remove_stroke":[],
    "show_stroke":[],
    "warning_color":RED,
    "stroke_":1
    }
    def construct(self):
        self.imagen=self.text
        if self.set_size=="width":
            self.imagen.set_width(FRAME_WIDTH)
        else:
            self.imagen.set_height(FRAME_HEIGHT)
        self.imagen.scale(self.svg_scale)
        if self.flip_svg==True:
            self.imagen.flip()
        if self.show_numbers==True:
            self.print_formula(self.imagen.copy(),
                self.numbers_scale,
                self.direction_numbers,
                self.remove,
                self.space_between_numbers,
                self.color_numbers)

        self.return_elements(self.imagen.copy(),self.show_elements)
        for st in self.remove_stroke:
            self.imagen[st].set_stroke(None,0)
        for st in self.show_stroke:
            self.imagen[st].set_stroke(None,self.stroke_)
        if self.animation==True:
            self.play(DrawBorderThenFill(self.imagen))
        else:
            c=0
            for j in range(len(self.imagen)):
                permission_print=True
                for w in self.remove:
                    if j==w:
                        permission_print=False
                if permission_print:
                    self.add(self.imagen[j])
            c = c + 1
        self.personalize_image()
        self.wait()

    def personalize_image(self):
        pass

    def print_formula(self,text,inverse_scale,direction,exception,buff,color):
        text.set_color(self.warning_color)
        self.add(text)
        c = 0
        for j in range(len(text)):
            permission_print=True
            for w in exception:
                if j==w:
                    permission_print=False
            if permission_print:
                self.add(text[j].set_color(self.stroke_color))
        c = c + 1

        c=0
        for j in range(len(text)):
            permission_print=True
            element = TexMobject("%d" %c,color=color)
            element.scale(inverse_scale)
            element.next_to(text[j],direction,buff=buff)
            for w in exception:
                if j==w:
                    permission_print=False
            if permission_print:
                self.add_foreground_mobjects(element)
            c = c + 1 

    def return_elements(self,formula,adds):
        for i in adds:
            self.add_foreground_mobjects(formula[i].set_color(self.color_element),
                TexMobject("%d"%i,color=self.color_element,background_stroke_width=0).scale(self.numbers_scale).next_to(formula[i],self.direction_numbers,buff=self.space_between_numbers))