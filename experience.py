#!/usr/bin/env python

from manimlib.imports import *
import numpy as np


class SebExperience:
    def __init__(self, seb_resume):
        self.seb_resume = seb_resume
        self.current_experience_title = None
        self.current_experience_year = None
        self.current_group = None

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

    def widm_lab(self, is_first=0):

        self.introduce_job_position("Research Assistant - WIDM Lab", '(2016-2019)', is_first=is_first)

        verso_object = self.create_experience('$\\cdot \\text{ Facebook Data Extraction}$')
        verso_object.move_to(self.current_experience_year.get_center() + DOWN)

        election_object = self.create_experience('$\\cdot \\text{ U.S Election Forecasting}$')
        election_object.move_to(verso_object.get_center() + DOWN)

        ir_chatbot_object = self.create_experience('$\\cdot \\text{ Retrieval-Based Chatbot}$')
        ir_chatbot_object.move_to(election_object.get_center() + DOWN)

        rec_sys_object = self.create_experience('$\\cdot \\text{ Recommendation System}$')
        rec_sys_object.move_to(ir_chatbot_object.get_center() + DOWN)

        emotional_machine = self.create_experience('$\\cdot \\text{ Emotionally-Triggered Conversational Agent}$')
        emotional_machine.move_to(rec_sys_object.get_center() + DOWN)

        # PLAYING THE ANIMATIONS
        self.seb_resume.play(FadeInFromDown(verso_object))
        self.seb_resume.wait(1.5)
        self.seb_resume.play(FadeInFromDown(election_object))
        self.seb_resume.wait(1.5)
        self.seb_resume.play(FadeInFromDown(ir_chatbot_object))
        self.seb_resume.wait(1.5)
        self.seb_resume.play(FadeInFromDown(rec_sys_object))
        self.seb_resume.wait(1.5)
        self.seb_resume.play(FadeInFromDown(emotional_machine))
        self.seb_resume.wait(2)

        # REMOVING THE OBJECTS
        self.seb_resume.play(FadeOut(verso_object),
                             FadeOut(election_object),
                             FadeOut(ir_chatbot_object),
                             FadeOut(rec_sys_object),
                             FadeOut(emotional_machine))
        self.seb_resume.wait(1.5)

    def orange_intern(self):
        self.introduce_job_position("Research Intern - Orange Labs", '(Feb. 2019 - August 2019)')

        in_out_classification = self.create_experience("$\\cdot \\text{ Indoor-Outdoor Classification in 5G context}$", size=0.80)
        in_out_classification.move_to(self.current_experience_year.get_center() + 1.5 * DOWN)

        nlp_intern = self.create_experience("$\\cdot \\text{ Study on Graph Embeddings for Language Generation}$", size=0.80)
        nlp_intern.move_to(in_out_classification.get_center() + 2 * DOWN)

        # PLAYING THE ANIMATIONS
        self.seb_resume.play(FadeInFromDown(in_out_classification))
        self.seb_resume.wait(1.5)
        self.seb_resume.play(FadeInFromDown(nlp_intern))
        self.seb_resume.wait(2)

        # REMOVING THE OBJECTS
        self.seb_resume.play(FadeOut(in_out_classification),
                             FadeOut(nlp_intern))
        self.seb_resume.wait(1.5)

    def create_experience(self, text, size=0.80, color=WHITE):
        description = TextMobject(text)
        description.scale(size)
        description.set_color(color)
        return description


