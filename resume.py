#!/usr/bin/env python
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
