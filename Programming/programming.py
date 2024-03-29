from manimlib.imports import *

class BubbleSort(Scene):
    def construct(self):
        
        def BSPythonCode(self):
            
            line0 = TextMobject("x = [4,3,2,9,2,1,6]",
                                tex_to_color_map={"4": GREEN, "3": GREEN,"2": GREEN, "1": GREEN,"6": GREEN,"9": GREEN}).move_to(3*UP)

            line1 = TextMobject("for i in range(6,-1,-1):",
                                tex_to_color_map={"for": PINK, "in": PINK," range": YELLOW, "6": GREEN,"1": GREEN})
            line1.next_to(line0, DOWN, buff=0.5, aligned_edge=LEFT)

            line2 = TextMobject("···for j in range(i):",
                                tex_to_color_map={"···": GREY, "for": PINK,"in": PINK," range": YELLOW})
            line2.next_to(line1, DOWN, buff=0.15, aligned_edge=LEFT)       

            line3 = TextMobject("······if x[j] > x[j+1]:",
                                tex_to_color_map={"······": GREY, "if": PINK,"1": GREEN})
            line3.next_to(line2, DOWN, buff=0.15, aligned_edge=LEFT) 

            line4 = TextMobject("·········temp = x[j]",
                                tex_to_color_map={"·········": GREY})
            line4.next_to(line3, DOWN, buff=0.15, aligned_edge=LEFT) 

            line5 = TextMobject("·········x[j] = x[j+1]",
                                tex_to_color_map={"·········": GREY,"1": GREEN})
            line5.next_to(line4, DOWN, buff=0.15, aligned_edge=LEFT) 

            line6 = TextMobject("·········x[j+1] = temp",
                                tex_to_color_map={"·········": GREY,"1": GREEN})
            line6.next_to(line5, DOWN, buff=0.15, aligned_edge=LEFT) 

            self.play(Write(line0))
            self.play(Write(line1))
            self.play(Write(line2))
            self.play(Write(line3))
            self.play(Write(line4))
            self.play(Write(line5))
            self.play(Write(line6))
            self.wait(2)
            self.play(FadeOut(line0),
                    FadeOut(line1),
                    FadeOut(line2),
                    FadeOut(line3),
                    FadeOut(line4),
                    FadeOut(line5),
                    FadeOut(line6))
        
        # def RemoveCode(self):
        #     self.play(FadeOut(line0),
        #             FadeOut(line1),
        #             FadeOut(line2),
        #             FadeOut(line3),
        #             FadeOut(line4),
        #             FadeOut(line5))


        nums = [TexMobject("4"), TexMobject("3"),TexMobject("2"),TexMobject("9"), TexMobject("2"),TexMobject("1"),TexMobject("6")]
        ints = [4,3,2,9,2,1,6]
        
        leng = 7 #At the meantimes only odd number length is possible


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
        self.wait()

        BSPythonCode(self)
        #RemoveCode(self)

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
        self.wait() 


        green_sq = [Square().surround(nums[0]), Square().surround(nums[1]), Square().surround(nums[2]), 
                   Square().surround(nums[3]), Square().surround(nums[4]), Square().surround(nums[5]),
                   Square().surround(nums[6])]
        for i in range(leng):
              green_sq[i].set_color(GREEN)         
        

        i_pos = [sum(x) for x in zip(c_names[0].get_bottom() , [0,-0.6,0])]
        j_pos = [sum(x) for x in zip(c_names[1].get_bottom() , [0,-0.6,0])]
        x_j_pos = [sum(x) for x in zip(c_names[2].get_bottom() , [0,-0.6,0])]
        x_j1_pos = [sum(x) for x in zip(c_names[3].get_bottom() , [0,-0.6,0])]
        stat_pos = [sum(x) for x in zip(c_names[5].get_bottom() , [0,-0.6,0])]
        tmp_pos = [sum(x) for x in zip(c_names[7].get_bottom() , [0,-0.6,0])]


        for i in range(leng-1,-1,-1):
            if i < leng-2 :
                t = 0.1
            else:
                t = 0.2

            if i > 0:
                s0_red = Square().surround(nums[0])
                s1_red = Square().surround(nums[1])
                s0_red.set_color(RED)
                s1_red.set_color(RED)
                self.play(FadeIn(s0_red),
                          FadeIn(s1_red),run_time=t)
                self.wait(t)

            i_txt = TextMobject("{\\footnotesize"+str(i)+"}").move_to(i_pos)
            self.play(Write(i_txt),run_time=t)
            self.wait(t)
            i_pos = [sum(x) for x in zip(i_pos, [0,-0.3,0])]

            for j in range(i):
                
                j_txt = TextMobject("{\\footnotesize"+str(j)+"}").move_to(j_pos)
                self.play(Write(j_txt),run_time=t)
                self.wait(t)
                j_pos = [sum(x) for x in zip(j_pos, [0,-0.3,0])]

                x_j_txt = TextMobject("{\\footnotesize"+str(ints[j])+"}").move_to(x_j_pos)
                x_j_pos = [sum(x) for x in zip(x_j_pos, [0,-0.3,0])]
                x_j1_txt = TextMobject("{\\footnotesize"+str(ints[j+1])+"}").move_to(x_j1_pos)
                x_j1_pos = [sum(x) for x in zip(x_j1_pos, [0,-0.3,0])]
                self.play(Write(x_j_txt),  Write(x_j1_txt),run_time=t)
                self.wait(t)

                if  ints[j] > ints[j+1]:

                    stat_txt = TextMobject("{\\footnotesize T").move_to(stat_pos)
                    stat_pos = [sum(x) for x in zip(stat_pos, [0,-0.3,0])]
                    self.play(Write(stat_txt),run_time=t)
                    self.wait(t)

                    tmp = ints[j]
                    tmp_txt = TextMobject("{\\footnotesize"+str(ints[j+1])+"}").move_to(tmp_pos)
                    tmp_pos = [sum(x) for x in zip(tmp_pos, [0,-0.3,0])]
                    self.play(Write(tmp_txt),run_time=t)
                    self.wait(t)
                    ints[j] = ints[j+1]
                    ints[j+1] = tmp


                    

                    self.play(nums[j].shift, [0, -1, 0],
                              nums[j+1].shift, [0, 1, 0]
                             ,run_time=t)
                    self.wait(t)

                    tmp_lab = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = tmp_lab
                else:
                    stat_txt = TextMobject("{\\footnotesize F").move_to(stat_pos)
                    stat_pos = [sum(x) for x in zip(stat_pos, [0,-0.3,0])]
                    self.play(Write(stat_txt),run_time=t)
                    self.wait(t)


                if j < i-1 :
                    self.play(s0_red.shift, [0,-1,0],
                              s1_red.shift, [0,-1,0],run_time=t)
                    self.wait(t)          
                else :
                    self.wait(t)
                    #self.remove(s0_red, s1_red)
                    self.play(FadeIn(green_sq[i]),
                              FadeOut(s0_red), FadeOut(s1_red),run_time=t)
                    
                
        self.wait(t)
        self.remove(s0_red, s1_red)
        self.play(FadeIn(green_sq[0]),run_time=t)
        self.wait(t)    






class BubbleSort1(Scene):
    def construct(self):

        nums = [TexMobject("4"), TexMobject("3"),TexMobject("2"),TexMobject("9"), TexMobject("2"),TexMobject("1"),TexMobject("6")]
        ints = [4,3,2,9,2,1,6]
        
        leng = 7 #At the meantimes only odd number length is possible


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
        self.wait(3)

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


        green_sq = [Square().surround(nums[0]), Square().surround(nums[1]), Square().surround(nums[2]), 
                   Square().surround(nums[3]), Square().surround(nums[4]), Square().surround(nums[5]),
                   Square().surround(nums[6])]
        for i in range(leng):
              green_sq[i].set_color(GREEN)         
        

        i_pos = [sum(x) for x in zip(c_names[0].get_bottom() , [0,-0.6,0])]
        j_pos = [sum(x) for x in zip(c_names[1].get_bottom() , [0,-0.6,0])]
        x_j_pos = [sum(x) for x in zip(c_names[2].get_bottom() , [0,-0.6,0])]
        x_j1_pos = [sum(x) for x in zip(c_names[3].get_bottom() , [0,-0.6,0])]
        stat_pos = [sum(x) for x in zip(c_names[5].get_bottom() , [0,-0.6,0])]
        tmp_pos = [sum(x) for x in zip(c_names[7].get_bottom() , [0,-0.6,0])]


        for i in range(leng-1,-1,-1):

            if i > 0:
                s0_red = Square().surround(nums[0])
                s1_red = Square().surround(nums[1])
                s0_red.set_color(RED)
                s1_red.set_color(RED)
                self.play(FadeIn(s0_red),
                          FadeIn(s1_red))
                self.wait()

            i_txt = TextMobject("{\\footnotesize"+str(i)+"}").move_to(i_pos)
            self.play(Write(i_txt))
            self.wait()
            i_pos = [sum(x) for x in zip(i_pos, [0,-0.3,0])]

            for j in range(i):
                
                j_txt = TextMobject("{\\footnotesize"+str(j)+"}").move_to(j_pos)
                self.play(Write(j_txt))
                self.wait()
                j_pos = [sum(x) for x in zip(j_pos, [0,-0.3,0])]

                x_j_txt = TextMobject("{\\footnotesize"+str(ints[j])+"}").move_to(x_j_pos)
                x_j_pos = [sum(x) for x in zip(x_j_pos, [0,-0.3,0])]
                x_j1_txt = TextMobject("{\\footnotesize"+str(ints[j+1])+"}").move_to(x_j1_pos)
                x_j1_pos = [sum(x) for x in zip(x_j1_pos, [0,-0.3,0])]
                self.play(Write(x_j_txt),  Write(x_j1_txt))
                self.wait()

                if  ints[j] > ints[j+1]:

                    stat_txt = TextMobject("{\\footnotesize T").move_to(stat_pos)
                    stat_pos = [sum(x) for x in zip(stat_pos, [0,-0.3,0])]
                    self.play(Write(stat_txt))
                    self.wait()

                    tmp = ints[j]
                    tmp_txt = TextMobject("{\\footnotesize"+str(ints[j+1])+"}").move_to(tmp_pos)
                    tmp_pos = [sum(x) for x in zip(tmp_pos, [0,-0.3,0])]
                    self.play(Write(tmp_txt))
                    self.wait()
                    ints[j] = ints[j+1]
                    ints[j+1] = tmp


                    

                    self.play(nums[j].shift, [0, -1, 0],
                              nums[j+1].shift, [0, 1, 0]
                             )
                    self.wait()

                    tmp_lab = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = tmp_lab
                else:
                    stat_txt = TextMobject("{\\footnotesize F").move_to(stat_pos)
                    stat_pos = [sum(x) for x in zip(stat_pos, [0,-0.3,0])]
                    self.play(Write(stat_txt))
                    self.wait()


                if j < i-1 :
                    self.play(s0_red.shift, [0,-1,0],
                              s1_red.shift, [0,-1,0])
                    self.wait()          
                else :
                    self.wait()
                    #self.remove(s0_red, s1_red)
                    self.play(FadeIn(green_sq[i]),
                              FadeOut(s0_red), FadeOut(s1_red))
                    
                
        self.wait()
        self.remove(s0_red, s1_red)
        self.play(FadeIn(green_sq[0]))
        self.wait()    




class BSPythonCode(Scene):
    def construct(self):
        
        line0 = TextMobject("x = [4,3,2,9,2,1,6]",
                            tex_to_color_map={"4": GREEN, "3": GREEN,"2": GREEN, "1": GREEN,"6": GREEN,"9": GREEN}).move_to(3*UP)

        line1 = TextMobject("for i in range(6,-1,-1):",
                            tex_to_color_map={"for": PINK, "in": PINK," range": YELLOW, "6": GREEN,"1": GREEN})
        line1.next_to(line0, DOWN, buff=0.5, aligned_edge=LEFT)

        line2 = TextMobject("···for j in range(i):",
                            tex_to_color_map={"···": GREY, "for": PINK,"in": PINK," range": YELLOW})
        line2.next_to(line1, DOWN, buff=0.15, aligned_edge=LEFT)       

        line3 = TextMobject("······if x[j] > x[j+1]:",
                            tex_to_color_map={"······": GREY, "if": PINK,"1": GREEN})
        line3.next_to(line2, DOWN, buff=0.15, aligned_edge=LEFT) 

        line4 = TextMobject("·········temp = x[j]",
                            tex_to_color_map={"·········": GREY})
        line4.next_to(line3, DOWN, buff=0.15, aligned_edge=LEFT) 

        line5 = TextMobject("·········x[j] = x[j+1]",
                            tex_to_color_map={"·········": GREY,"1": GREEN})
        line5.next_to(line4, DOWN, buff=0.15, aligned_edge=LEFT) 

        line6 = TextMobject("·········x[j+1] = temp",
                            tex_to_color_map={"·········": GREY,"1": GREEN})
        line6.next_to(line5, DOWN, buff=0.15, aligned_edge=LEFT) 

        self.play(Write(line0))
        self.play(Write(line1))
        self.play(Write(line2))
        self.play(Write(line3))
        self.play(Write(line4))
        self.play(Write(line5))
        self.play(Write(line6))
        self.wait()

     



class test_time(Scene):
    def construct(self):

        nums = [TexMobject("4"), TexMobject("3"),TexMobject("2"),TexMobject("9"), TexMobject("2"),TexMobject("1"),TexMobject("6")]
        ints = [4,3,2,9,2,1,6]
        
        leng = 7 #At the meantimes only odd number length is possible


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
        self.wait(3)

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


        green_sq = [Square().surround(nums[0]), Square().surround(nums[1]), Square().surround(nums[2]), 
                   Square().surround(nums[3]), Square().surround(nums[4]), Square().surround(nums[5]),
                   Square().surround(nums[6])]
        for i in range(leng):
              green_sq[i].set_color(GREEN)         
        

        i_pos = [sum(x) for x in zip(c_names[0].get_bottom() , [0,-0.6,0])]
        j_pos = [sum(x) for x in zip(c_names[1].get_bottom() , [0,-0.6,0])]
        x_j_pos = [sum(x) for x in zip(c_names[2].get_bottom() , [0,-0.6,0])]
        x_j1_pos = [sum(x) for x in zip(c_names[3].get_bottom() , [0,-0.6,0])]
        stat_pos = [sum(x) for x in zip(c_names[5].get_bottom() , [0,-0.6,0])]
        tmp_pos = [sum(x) for x in zip(c_names[7].get_bottom() , [0,-0.6,0])]


        for i in range(leng-1,-1,-1):

            if i > 0:
                s0_red = Square().surround(nums[0])
                s1_red = Square().surround(nums[1])
                s0_red.set_color(RED)
                s1_red.set_color(RED)
                self.play(FadeIn(s0_red),
                          FadeIn(s1_red), run_time = (i+1)/7)
                self.wait((i+1)/7)

            i_txt = TextMobject("{\\footnotesize"+str(i)+"}").move_to(i_pos)
            self.play(Write(i_txt), run_time = (i+1)/7)
            self.wait((i+1)/7)
            i_pos = [sum(x) for x in zip(i_pos, [0,-0.3,0])]

            for j in range(i):
                
                j_txt = TextMobject("{\\footnotesize"+str(j)+"}").move_to(j_pos)
                self.play(Write(j_txt), run_time = (i+1)/7)
                self.wait((i+1)/7)
                j_pos = [sum(x) for x in zip(j_pos, [0,-0.3,0])]

                x_j_txt = TextMobject("{\\footnotesize"+str(ints[j])+"}").move_to(x_j_pos)
                x_j_pos = [sum(x) for x in zip(x_j_pos, [0,-0.3,0])]
                x_j1_txt = TextMobject("{\\footnotesize"+str(ints[j+1])+"}").move_to(x_j1_pos)
                x_j1_pos = [sum(x) for x in zip(x_j1_pos, [0,-0.3,0])]
                self.play(Write(x_j_txt),  Write(x_j1_txt), run_time = (i+1)/7)
                self.wait((i+1)/7)

                if  ints[j] > ints[j+1]:

                    stat_txt = TextMobject("{\\footnotesize T").move_to(stat_pos)
                    stat_pos = [sum(x) for x in zip(stat_pos, [0,-0.3,0])]
                    self.play(Write(stat_txt), run_time = (i+1)/7)
                    self.wait((i+1)/7)

                    tmp = ints[j]
                    tmp_txt = TextMobject("{\\footnotesize"+str(ints[j+1])+"}").move_to(tmp_pos)
                    tmp_pos = [sum(x) for x in zip(tmp_pos, [0,-0.3,0])]
                    self.play(Write(tmp_txt), run_time = (i+1)/7)
                    self.wait((i+1)/7)
                    ints[j] = ints[j+1]
                    ints[j+1] = tmp


                    

                    self.play(nums[j].shift, [0, -1, 0],
                              nums[j+1].shift, [0, 1, 0]
                             , run_time = (i+1)/7)
                    self.wait((i+1)/7)

                    tmp_lab = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = tmp_lab
                else:
                    stat_txt = TextMobject("{\\footnotesize F").move_to(stat_pos)
                    stat_pos = [sum(x) for x in zip(stat_pos, [0,-0.3,0])]
                    self.play(Write(stat_txt), run_time = (i+1)/7)
                    self.wait((i+1)/7)


                if j < i-1 :
                    self.play(s0_red.shift, [0,-1,0],
                              s1_red.shift, [0,-1,0], run_time = (i+1)/7)
                    self.wait((i+1)/7)          
                else :
                    self.wait((i+1)/7)
                    #self.remove(s0_red, s1_red)
                    self.play(FadeIn(green_sq[i]),
                              FadeOut(s0_red), FadeOut(s1_red), run_time = (i+1)/7)
                    
                
        self.wait()
        self.remove(s0_red, s1_red)
        self.play(FadeIn(green_sq[0]))
        self.wait()    

