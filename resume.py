#!/usr/bin/env python
from experience import SebExperience
from manimlib.imports import *
import numpy as np


class SebResume(Scene):

    def construct(self):

        self.transition = {
            'current_title': None,
            'current_title_position': None
        }
        self.self_introduction()
        self.education()
        self.experience()
        # self.publication()
        # self.hard_skills()
        # self.soft_skills()
        # self.languages()
        # self.contact()

    def self_introduction(self):
        name = TextMobject('Sebastien Montella')
        job = TextMobject('\\textit{Machine Learning \& Deep Learning Researcher}')
        education_title = TextMobject('Education')
        job.set_color(BLUE)
        education_title.set_color(YELLOW)

        my_pic = ImageMobject('seb_circle_logo_color.png')
        my_pic.scale(0.60)

        name.next_to(my_pic, DOWN)
        job.next_to(name, DOWN)

        name_group = VGroup(name,
                            job)

        self.play(FadeIn(my_pic, run_time=2),
                  FadeIn(name, run_time=2))

        self.wait(3)
        self.play(Write(job, run_time=2.5))
        self.wait(3)
        self.play(ApplyMethod(my_pic.to_corner, UL, run_time=1.1),
                  ApplyMethod(name_group.to_corner, UP, run_time=1.3))
        self.wait(3)
        education_title.move_to(job.get_center())
        self.play(ReplacementTransform(job, education_title))
        self.wait(3)

        # UPDATE TRANSITION TITLE DICT
        self.transition['current_title'] = education_title
        self.transition['current_title_position'] = education_title.get_center()

    def education(self):

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

        self.play(FadeIn(utbm_group))
        self.wait(2)
        self.play(Transform(utbm_name_txt, utbm_txt))
        self.wait(3)
        self.play(FadeIn(ncu_group))
        self.wait(2)
        self.play(Transform(ncu_name_txt, ncu_txt))
        self.wait(3)

        separate_line = Line(np.asarray([0, -5, 0]), np.asarray([0, 2, 0]))
        self.play(Write(separate_line),
                  ApplyMethod(utbm_txt.move_to, utbm_txt.get_center() + 2 * UP),
                  ApplyMethod(ncu_txt.move_to, ncu_txt.get_center() + 2 * UP),
                  FadeOut(utbm_group),
                  FadeOut(ncu_group))
        self.wait(3)

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
        self.play(FadeInFromDown(programming_basics))
        self.wait(1.5)
        self.play(FadeInFromDown(mathematics_txt))
        self.wait(1.0)
        self.play(FadeInFromDown(management_txt))
        self.wait(0.5)
        self.play(FadeInFromDown(marketing_txt))
        self.wait(3)

        # PLAY ANIMATION NCU
        self.play(FadeInFromDown(machine_learning_txt))
        self.wait(1.5)
        self.play(FadeInFromDown(deep_learning_txt))
        self.wait(1.0)
        self.play(FadeInFromDown(nlp_txt))
        self.wait(0.5)
        self.play(FadeInFromDown(ir_txt))
        self.wait(3)

        # REMOVE EDUCATION
        self.play(FadeOut(utbm_txt),
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

        self.wait(3)

        experience_title = TextMobject('Experience')
        experience_title.set_color(BLUE)
        experience_title.move_to(self.transition['current_title_position'])

        self.play(Transform(self.transition['current_title'], experience_title))
        self.wait(3)

    def experience(self):
        seb_experience = SebExperience(self)
        seb_experience.widm_lab(is_first=1)
        seb_experience.orange_intern()

    def publication(self):
        print("TODO")

    def hard_skills(self):
        print('TODO')

    def soft_skills(self):
        print('todo')

    def languages(self):
        print("todo")

    def contact(self):
        print("contact me :)")





