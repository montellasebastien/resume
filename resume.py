#!/usr/bin/env python
from experience import SebExperience
from education import Education
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
        my_education = Education(self)
        my_education.show_universities()

    def experience(self):
        seb_experience = SebExperience(self)
        seb_experience.widm_lab(is_first=1)
        seb_experience.orange_intern()

    def publication(self):
        print("TODO")

    def hard_skills(self):
        print('TODO')

    def soft_skills(self):
        print('TODO')

    def languages(self):
        print("TODO")

    def contact(self):
        print("TODO")
