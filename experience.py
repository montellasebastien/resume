#!/usr/bin/env python

from manimlib.imports import *
import numpy as np


class SebExperience:
    def __init__(self, seb_resume):
        self.seb_resume = seb_resume
        self.current_experience_title = None
        self.current_experience_year = None
        self.current_group = None

    def widm_lab(self, is_first=0):

        self.introduce_job_position("Research Assistant - WIDM Lab", '(2016-2019)', is_first=is_first)
        self.verso()
        self.us_election_prediction()
        self.ntcir_13()
        self.qnap_user_simulator()
        self.taiwan_iii()
        self.ntcir_14()

    def orange_intern(self):
        self.introduce_job_position("Research Intern - Orange Labs", '(Feb. 2019 - August 2019)')

    def introduce_job_position(self, title_string, period_string, is_first=0):
        experience_title = TextMobject("\\textit{ " + title_string +"}")
        experience_title.scale(0.7)
        experience_title.set_color(YELLOW_C)

        experience_year = TextMobject(period_string)
        experience_year.scale(0.65)
        experience_year.set_color(GREEN)

        # RELATIVE POSITIONS
        # experience_title.next_to(self.seb_resume.transition['current_title_position'], 2 * DOWN)
        experience_year.next_to(experience_title, DOWN)

        # GROUPS
        new_group = VGroup(experience_title,
                           experience_year)

        if is_first:
            self.current_experience_title = experience_title
            self.current_experience_year = experience_year
            self.current_group = new_group

            self.seb_resume.play(FadeInFromDown(new_group))
            self.seb_resume.wait(3)
            self.seb_resume.play(ApplyMethod(new_group.move_to,
                                             self.seb_resume.transition['current_title_position'] + DOWN))
            self.seb_resume.wait(3)
        else:
            new_group.move_to(self.seb_resume.transition['current_title_position'] + DOWN)
            self.seb_resume.play(ReplacementTransform(self.current_group, new_group))
            self.seb_resume.wait(3)

            # UPDATING GETTER OF THE CLASS
            self.current_experience_title = experience_title
            self.current_experience_year = experience_year
            self.current_group = new_group

    def verso(self):
        print("haha")

    def us_election_prediction(self):
        print('')

    def ntcir_13(self):
        print('haha')

    def ntcir_14(self):
        print('haha')

    def qnap_user_simulator(self):
        print("haha")

    def taiwan_iii(self):
        print('haha')
