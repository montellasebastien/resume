#!/usr/bin/env python

from manimlib.imports import *


class Education:
    def __init__(self, seb_resume, title='Education', color=YELLOW):
        self.seb_resume = seb_resume
        self.seb_resume.apply_transition(title=title,
                                         color=color)

    def show_universities(self):

        # COUNTRIES
        france_txt = TextMobject("France")
        france_txt.scale(0.8)
        france_txt.set_color(BLUE)

        taiwan_txt = TextMobject("Taiwan")
        taiwan_txt.scale(0.8)
        taiwan_txt.set_color(BLUE)

        # SCHOOLS
        utbm_name_txt = TextMobject('University of Technology of Belfort-Montbeliard')
        utbm_name_txt.scale(0.65)
        utbm_name_txt.set_color(WHITE)

        utbm_txt = TextMobject('UTBM')
        utbm_txt.scale(0.75)
        utbm_txt.set_color(WHITE)

        ncu_name_txt = TextMobject('National Central University')
        ncu_name_txt.scale(0.65)
        ncu_name_txt.set_color(WHITE)

        ncu_txt = TextMobject('NCU')
        ncu_txt.scale(0.75)
        ncu_txt.set_color(WHITE)

        # DATES
        utbm_date = TextMobject("(2013 - 2019)")
        utbm_date.scale(0.6)
        utbm_date.set_color(GREEN)

        ncu_date = TextMobject('(2016 - 2019)')
        ncu_date.scale(0.6)
        ncu_date.set_color(GREEN)

        # RELATIVE POSITION
        france_txt.next_to(utbm_name_txt, DOWN)
        utbm_date.next_to(france_txt, DOWN)

        taiwan_txt.next_to(ncu_name_txt, DOWN)
        ncu_date.next_to(taiwan_txt, DOWN)

        # GROUPS
        utbm_group = VGroup(utbm_name_txt,
                            france_txt,
                            utbm_date)

        ncu_group = VGroup(ncu_name_txt,
                           taiwan_txt,
                           ncu_date)

        coordinate_utbm = 3 * LEFT + 0.5 * DOWN
        coordinate_ncu = 3 * RIGHT + 0.5 * DOWN
        utbm_group.move_to(coordinate_utbm)
        ncu_group.move_to(coordinate_ncu)

        utbm_txt.move_to(utbm_name_txt.get_center())
        ncu_txt.move_to(ncu_name_txt.get_center())

        self.seb_resume.play(FadeIn(utbm_group))
        self.seb_resume.wait(2)
        self.seb_resume.play(Transform(utbm_name_txt, utbm_txt))
        self.seb_resume.wait(3)
        self.seb_resume.play(FadeIn(ncu_group))
        self.seb_resume.wait(2)
        self.seb_resume.play(Transform(ncu_name_txt, ncu_txt))
        self.seb_resume.wait(3)

        separate_line = Line(np.asarray([0, -5, 0]), np.asarray([0, 2, 0]))
        self.seb_resume.play(Write(separate_line),
                             ApplyMethod(utbm_txt.move_to, utbm_txt.get_center() + 2 * UP),
                             ApplyMethod(ncu_txt.move_to, ncu_txt.get_center() + 2 * UP),
                             FadeOut(utbm_group),
                             FadeOut(ncu_group))

        self.seb_resume.wait(3)

        scale_txt = 0.75

        # UTBM
        programming_basics = TextMobject("Programming Fundamentals")
        programming_basics.move_to(utbm_txt.get_center() + DOWN)
        programming_basics.scale(scale_txt)
        programming_basics.set_color(BLUE)

        mathematics_txt = TextMobject("Mathematics")
        mathematics_txt.move_to(programming_basics.get_center() + DOWN)
        mathematics_txt.scale(scale_txt)
        mathematics_txt.set_color(GREEN)

        management_txt = TextMobject('Management')
        management_txt.move_to(mathematics_txt.get_center() + DOWN)
        management_txt.scale(scale_txt)
        management_txt.set_color(RED)

        marketing_txt = TextMobject('Marketing')
        marketing_txt.move_to(management_txt.get_center() + DOWN)
        marketing_txt.scale(scale_txt)
        marketing_txt.set_color(WHITE)

        # NCU
        machine_learning_txt = TextMobject("Machine Learning")
        machine_learning_txt.move_to(ncu_txt.get_center() + DOWN)
        machine_learning_txt.scale(scale_txt)
        machine_learning_txt.set_color(BLUE)

        deep_learning_txt = TextMobject("Deep Learning")
        deep_learning_txt.move_to(machine_learning_txt.get_center() + DOWN)
        deep_learning_txt.scale(scale_txt)
        deep_learning_txt.set_color(GREEN)

        nlp_txt = TextMobject("NLP")
        nlp_txt.move_to(deep_learning_txt.get_center() + DOWN)
        nlp_txt.scale(scale_txt)
        nlp_txt.set_color(RED)

        ir_txt = TextMobject('Information Retrieval')
        ir_txt.move_to(nlp_txt.get_center() + DOWN)
        ir_txt.scale(scale_txt)
        ir_txt.set_color(WHITE)

        # PLAY ANIMATION UTBM
        self.seb_resume.play(FadeInFromDown(programming_basics))
        self.seb_resume.wait(1.5)
        self.seb_resume.play(FadeInFromDown(mathematics_txt))
        self.seb_resume.wait(1.0)
        self.seb_resume.play(FadeInFromDown(management_txt))
        self.seb_resume.wait(0.5)
        self.seb_resume.play(FadeInFromDown(marketing_txt))
        self.seb_resume.wait(3)

        # PLAY ANIMATION NCU
        self.seb_resume.play(FadeInFromDown(machine_learning_txt))
        self.seb_resume.wait(1.5)
        self.seb_resume.play(FadeInFromDown(deep_learning_txt))
        self.seb_resume.wait(1.0)
        self.seb_resume.play(FadeInFromDown(nlp_txt))
        self.seb_resume.wait(0.5)
        self.seb_resume.play(FadeInFromDown(ir_txt))
        self.seb_resume.wait(3)

        # REMOVE EDUCATION
        self.seb_resume.play(FadeOut(utbm_txt),
                             FadeOut(ncu_txt),
                             FadeOut(separate_line),
                             FadeOut(programming_basics),
                             FadeOut(mathematics_txt),
                             FadeOut(management_txt),
                             FadeOut(marketing_txt),
                             FadeOut(machine_learning_txt),
                             FadeOut(deep_learning_txt),
                             FadeOut(nlp_txt),
                             FadeOut(ir_txt))

        self.seb_resume.wait(3)


