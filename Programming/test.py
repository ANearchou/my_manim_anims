from manimlib.imports import *

class test(Scene):
    def construct(self):
        
        nums = [TexMobject("4"), TexMobject("3"),TexMobject("2"),TexMobject("9"), TexMobject("2"),TexMobject("1"),TexMobject("6")]
        nums[0].shift(3*UP+4*LEFT)
        nums[1].shift(2*UP+4*LEFT)
        nums[2].shift(1*UP+4*LEFT)
        nums[3].shift(0*UP+4*LEFT)
        nums[4].shift(1*DOWN+4*LEFT)
        nums[5].shift(2*DOWN+4*LEFT)
        nums[6].shift(3*DOWN+4*LEFT)

        c_names = [TextMobject("{\\footnotesize i }")
                  ,TextMobject("{\\footnotesize j }")
                  ,TextMobject("{\\footnotesize x[j] }")
                  ,TextMobject("{\\footnotesize x[j+1] }")
                  ,TextMobject("\\footnotesize x[j] ")
                  ,TextMobject(">") 
                  ,TextMobject("\\footnotesize x[j+1]")
                  ,TextMobject("{\\footnotesize temp }")]
        c_names[7].to_edge(UR)
        c_names[6].next_to(c_names[7], LEFT, buff = 0.5)
        c_names[5].next_to(c_names[6], LEFT, buff = 0.2)
        c_names[4].next_to(c_names[5], LEFT, buff = 0.2)
        c_names[3].next_to(c_names[4], LEFT, buff = 0.5)
        c_names[2].next_to(c_names[3], LEFT, buff = 0.5)
        c_names[1].next_to(c_names[2], LEFT, buff = 0.5)
        c_names[0].next_to(c_names[1], LEFT, buff = 0.5)
        
        lines = [Line((c_names[0].get_right()+c_names[1].get_left())/2,  [sum(x) for x in zip((c_names[0].get_right()+c_names[1].get_left())/2, [0,-10,0])] ) ,
                Line((c_names[1].get_right()+c_names[2].get_left())/2,  [sum(x) for x in zip((c_names[1].get_right()+c_names[2].get_left())/2, [0,-10,0])] ) ,
                Line((c_names[2].get_right()+c_names[3].get_left())/2,  [sum(x) for x in zip((c_names[2].get_right()+c_names[3].get_left())/2, [0,-10,0])] ) ,
                Line((c_names[3].get_right()+c_names[4].get_left())/2,  [sum(x) for x in zip((c_names[3].get_right()+c_names[4].get_left())/2, [0,-10,0])] ) ,
                Line((c_names[6].get_right()+c_names[7].get_left())/2,  [sum(x) for x in zip((c_names[6].get_right()+c_names[7].get_left())/2, [0,-10,0])] ) ,
                Line([sum(x) for x in zip(c_names[0].get_bottom() , [-0.5,-0.3,0], )], [sum(x) for x in zip(c_names[7].get_bottom() , [1,-0.3,0], )])
                ]
        self.play(Write(nums[0]),
                  Write(nums[1]),
                  Write(nums[2]),
                  Write(nums[3]),
                  Write(nums[4]),
                  Write(nums[5]),
                  Write(nums[6])
        )  
        self.wait(2)
        self.play(Write(c_names[0])
                 ,Write(c_names[1])
                 ,Write(c_names[2])
                 ,Write(c_names[3])
                 ,Write(c_names[4])
                 ,Write(c_names[5])
                 ,Write(c_names[6])
                 ,Write(c_names[7]))
        self.wait()

        self.play(ShowCreation(lines[0]),
                  ShowCreation(lines[1]),
                  ShowCreation(lines[2]),
                  ShowCreation(lines[3]),
                  ShowCreation(lines[4]),
                  ShowCreation(lines[5]))
        self.wait(2)


        x = [2,9,1,6]
        i_pos = [sum(x) for x in zip(c_names[0].get_bottom() , [0,-0.6,0])]
        j_pos = [sum(x) for x in zip(c_names[1].get_bottom() , [0,-0.6,0])]
        x_j_pos = [sum(x) for x in zip(c_names[2].get_bottom() , [0,-0.6,0])]
        x_j1_pos = [sum(x) for x in zip(c_names[3].get_bottom() , [0,-0.6,0])]
        stat_pos = [sum(x) for x in zip(c_names[5].get_bottom() , [0,-0.6,0])]
        tmp_pos = [sum(x) for x in zip(c_names[7].get_bottom() , [0,-0.6,0])]

        for i in range(3,-1,-1):
            i_txt = TextMobject("{\\footnotesize"+str(i)+"}").move_to(i_pos)
            self.play(Write(i_txt))
            self.wait()
            i_pos = [sum(x) for x in zip(i_pos, [0,-0.3,0])]
            for j in range(i):
                j_txt = TextMobject("{\\footnotesize"+str(j)+"}").move_to(j_pos)
                self.play(Write(j_txt))
                self.wait()
                j_pos = [sum(x) for x in zip(j_pos, [0,-0.3,0])]

                x_j_txt = TextMobject("{\\footnotesize"+str(x[j])+"}").move_to(x_j_pos)
                x_j_pos = [sum(x) for x in zip(x_j_pos, [0,-0.3,0])]
                x_j1_txt = TextMobject("{\\footnotesize"+str(x[j+1])+"}").move_to(x_j1_pos)
                x_j1_pos = [sum(x) for x in zip(x_j1_pos, [0,-0.3,0])]
                self.play(Write(x_j_txt),  Write(x_j1_txt))
                self.wait()

                if x[j] > x[j+1]:
                    stat_txt = TextMobject("{\\footnotesize T").move_to(stat_pos)
                    stat_pos = [sum(x) for x in zip(stat_pos, [0,-0.3,0])]
                    self.play(Write(stat_txt))
                    self.wait()

                    tmp = x[j+1]
                    tmp_txt = TextMobject("{\\footnotesize"+str(x[j+1])+"}").move_to(tmp_pos)
                    tmp_pos = [sum(x) for x in zip(tmp_pos, [0,-0.3,0])]
                    self.play(Write(tmp_txt))
                    self.wait()
                    x[j+1] = x[j]
                    x[j] = tmp

                else:
                    stat_txt = TextMobject("{\\footnotesize F").move_to(stat_pos)
                    stat_pos = [sum(x) for x in zip(stat_pos, [0,-0.3,0])]
                    self.play(Write(stat_txt))
                    self.wait()





        

class test1(Scene):
    def construct(self):
        nums = [TexMobject("9"), TexMobject("3"),TexMobject("2"),TexMobject("9"), TexMobject("2"),TexMobject("1"),TexMobject("6")]
        nums[0].shift(3*UP)
        nums[1].shift(2*UP)
        nums[2].shift(1*UP)
        nums[3].shift(0*UP)
        nums[4].shift(1*DOWN)
        nums[5].shift(2*DOWN)
        nums[6].shift(3*DOWN)

        green_sq = [Square(side_length=1).move_to([0,3,0]), Square(side_length=1).move_to([0,2,0]), Square(side_length=1).move_to([0,1,0]), 
                   Square(side_length=1).move_to([0,0,0]), Square(side_length=1).move_to([0,-1,0]), Square(side_length=1).move_to([0,-2,0]),
                   Square(side_length=1).move_to([0,-3,0])]

        self.play(ShowCreation(nums[0]),
                  ShowCreation(nums[1]),
                  ShowCreation(nums[2]),
                  ShowCreation(nums[3]),
                  ShowCreation(nums[4]),
                  ShowCreation(nums[5]),
                  ShowCreation(nums[6]))

        self.wait()
        self.play(ShowCreation(green_sq[0]),
                  ShowCreation(green_sq[1]),
                  ShowCreation(green_sq[2]),
                  ShowCreation(green_sq[3]),
                  ShowCreation(green_sq[4]),
                  ShowCreation(green_sq[5]),
                  ShowCreation(green_sq[6]))
        self.wait()

        memory_position = [TextMobject("{\\tiny 0}")
                          ,TextMobject("{\\tiny 1}")
                          ,TextMobject("{\\tiny 2}")
                          ,TextMobject("{\\tiny 3}")
                          ,TextMobject("{\\tiny 4}")
                          ,TextMobject("{\\tiny 6}")
                          ,TextMobject("{\\tiny 4}")]

        
        #for i in range(7):
        memory_position[0].move_to([0.6, 2.6, 0]) 
        memory_position[1].move_to([0.6, 1.6, 0]) 
        memory_position[2].move_to([0.6, 0.6, 0]) 
        memory_position[3].move_to([0.6, -0.4, 0]) 
        memory_position[4].move_to([0.6, -1.4, 0]) 
        memory_position[5].move_to([0.6, -2.4, 0]) 
        memory_position[6].move_to([0.6, -3.4, 0]) 

        self.play(FadeIn(memory_position[0])
                 ,FadeIn(memory_position[1])
                 ,FadeIn(memory_position[2])
                 ,FadeIn(memory_position[3])
                 ,FadeIn(memory_position[4])
                 ,FadeIn(memory_position[5])
                 ,FadeIn(memory_position[6]))      

        self.wait(2)                   



        
        i_loop = [TextMobject("for "), TextMobject("i "), TextMobject("in "), TextMobject("range"), TextMobject("("), TexMobject("6"), TextMobject("):")]
        j_loop = [TextMobject("for "), TextMobject("j "), TextMobject("in "), TextMobject("range"), TextMobject("(i):")]
        if_stat = [TextMobject("if "), TextMobject("x[j] > x[j+"), TextMobject("1"), TextMobject("]:")]

        print("i loop length: " , len(i_loop))
        i_loop[0].set_color(PURPLE)
        i_loop[2].set_color(PURPLE)
        i_loop[3].set_color(YELLOW)
        i_loop[5].set_color(GREEN)

        j_loop[0].set_color(PURPLE)
        j_loop[2].set_color(PURPLE)
        j_loop[3].set_color(YELLOW)

        if_stat[0].set_color(PURPLE)
        if_stat[2].set_color(YELLOW)

        i_loop[0].move_to([3,3,0])
        i_loop[1].next_to(i_loop[0], RIGHT, buff=0)
        i_loop[2].next_to(i_loop[1], RIGHT, buff=0)
        i_loop[3].next_to(i_loop[2], RIGHT, buff=0)
        i_loop[4].next_to(i_loop[3], RIGHT, buff=0)
        i_loop[5].next_to(i_loop[4], RIGHT, buff=0)
        i_loop[6].next_to(i_loop[5], RIGHT, buff=0)
        for i in range(7):
            self.play(Write(i_loop[i]))




# i_loop = [TextMobject("for "), TextMobject("i "), TextMobject("in "), TextMobject("range "), TextMobject("("), TextMobject("6"), TextMobject("):")]
# i_loop = [TextMobject("for "), TextMobject("j "), TextMobject("in "), TextMobject("range"), TextMobject("(i):")]
# if_stat = [TextMobject("if "), TextMobject("x[j] > x[j+"), TextMobject("1"), TextMobject("]:")]

# i_loop[0].set_color(PURPLE)
# i_loop[2].set_color(PURPLE)
# i_loop[3].set_color(YELLOW)
# i_loop[5].set_color(GREEN)

# j_loop[0].set_color(PURPLE)
# j_loop[2].set_color(PURPLE)
# j_loop[3].set_color(YELLOW)

# if_stat[0].set_color(PURPLE)
# if_stat[2].set_color(YELLOW)

# for i in range(6):
#     for j in range(i):        
#         if x[j] > x[j+1]:
#         temp = x[j]
#         x[j] = x[j+1]
#         x[j+1] = temp

class test2(Scene):
    def construct(self):

        x1 = "{\\footnotesize"
        x2 = 2
        x3 = "}"

        x_text = TextMobject(x1+str(x2)+x3)

        

        self.play(Write(x_text))
        self.wait(2)          