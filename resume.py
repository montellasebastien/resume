#!/usr/bin/env python
from skill import Skill
from experience import SebExperience
from education import Education
from introduction import Introduce
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
        self.skills()
        # self.publication()
        # self.hard_skills()
        # self.soft_skills()
        # self.languages()
        # self.contact()

    def self_introduction(self):
        my_name = 'Sebastien Montella'
        my_job = 'Machine Learning \\& Deep Learning Researcher'

        introduce_seb = Introduce(self)
        introduce_seb.introducing(my_name_string=my_name,
                                  my_job_string=my_job)

    def apply_transition(self, title, color):
        new_title = TextMobject(title)
        new_title.set_color(color)
        new_title.move_to(self.transition['current_title_position'])

        self.play(ReplacementTransform(self.transition['current_title'], new_title))
        self.transition['current_title'] = new_title
        self.transition['current_title_position'] = new_title.get_center()
        self.wait(3)

    def education(self):
        my_education = Education(self)
        my_education.show_universities()

    def experience(self):
        my_experience = SebExperience(self)
        my_experience.widm_lab(is_first=1)
        my_experience.orange_intern(is_last=1)

    def publication(self):
        print("TODO")

    def skills(self):
        my_skills = Skill(self)
        my_skills.show_skills()

    def soft_skills(self):
        print('TODO')

    def languages(self):
        print("TODO")

    def contact(self):
        print("TODO")
