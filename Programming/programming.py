from manimlib.imports import *

class BubbleSort(Scene):
    def construct(self):

        nums = [TexMobject("4"), TexMobject("3"),TexMobject("2"),TexMobject("9"), TexMobject("2"),TexMobject("1"),TexMobject("6")]
        ints = [4,3,2,9,2,1,6]
        
        leng = 7 #At the meantimes only odd number length is possible


        nums[0].shift(3*UP)
        nums[1].shift(2*UP)
        nums[2].shift(1*UP)
        nums[3].shift(0*UP)
        nums[4].shift(1*DOWN)
        nums[5].shift(2*DOWN)
        nums[6].shift(3*DOWN)
        
        self.play(Write(nums[0]),
                  Write(nums[1]),
                  Write(nums[2]),
                  Write(nums[3]),
                  Write(nums[4]),
                  Write(nums[5]),
                  Write(nums[6])
        )  
        self.wait(3)

        green_sq = [Square().surround(nums[0]), Square().surround(nums[1]), Square().surround(nums[2]), 
                   Square().surround(nums[3]), Square().surround(nums[4]), Square().surround(nums[5]),
                   Square().surround(nums[6])]
        for i in range(leng):
              green_sq[i].set_color(GREEN)         
        

        for i in range(leng-1,-1,-1):

            if i > 0:
                s0_red = Square().surround(nums[0])
                s1_red = Square().surround(nums[1])
                s0_red.set_color(RED)
                s1_red.set_color(RED)
                self.play(FadeIn(s0_red),
                          FadeIn(s1_red))
                self.wait()

            for j in range(i):
                
                if  ints[j] > ints[j+1]:
                    tmp = ints[j]
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



                    
