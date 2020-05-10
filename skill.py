#!/usr/bin/env python

from manimlib.imports import *


class Skill:
    def __init__(self, seb_resume, title='Skills', color=PINK):
        self.seb_resume = seb_resume
        self.seb_resume.apply_transition(title=title,
                                         color=color)
        self.hard_title = None
        self.soft_title = None
        self.separate_line = None

    def show_skills(self):
        self.hard_title = self.create_skill_title(title="Hard",
                                             size=0.80,
                                             color=RED,
                                             coordinate=3 * LEFT + 0 * DOWN)

        self.soft_title = self.create_skill_title(title="Soft",
                                             size=0.80,
                                             color=BLUE,
                                             coordinate=3 * RIGHT + 0 * DOWN)

        self.separate_line = Line(np.asarray([0, -5, 0]), np.asarray([0, 2, 0]))

        self.seb_resume.play(Write(self.separate_line),
                             ApplyMethod(self.hard_title.move_to, self.hard_title.get_center() + 2 * UP),
                             ApplyMethod(self.soft_title.move_to, self.soft_title.get_center() + 2 * UP),
                             )
        self.seb_resume.wait(3)

        # self.show_hard_skills()
        # self.show_soft_skills()


    # def show_hard_skills(self):
    #
    #
    # def show_soft_skills(self):

    def create_skill_title(self, title, size, color, coordinate):
        txt = TextMobject(title)
        txt.scale(size)
        txt.set_color(color)
        txt_coordinate = coordinate
        txt.move_to(txt_coordinate)
        return txt