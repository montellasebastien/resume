#!/usr/bin/env python

from manimlib.imports import *


class Introduce:
    def __init__(self, seb_resume):
        self.seb_resume = seb_resume

    def introducing(self, my_name_string, my_job_string):
        name = TextMobject(my_name_string)
        job = TextMobject('\\textit{' + my_job_string + '}')
        education_title = TextMobject('Education')
        job.set_color(BLUE)
        education_title.set_color(YELLOW)

        my_pic = ImageMobject('seb_circle_logo_color.png')
        my_pic.scale(0.60)

        name.next_to(my_pic, DOWN)
        job.next_to(name, DOWN)

        name_group = VGroup(name,
                            job)

        self.seb_resume.play(FadeIn(my_pic, run_time=2),
                             FadeIn(name, run_time=2))

        self.seb_resume.wait(3)
        self.seb_resume.play(Write(job, run_time=2.5))
        self.seb_resume.wait(3)
        self.seb_resume.play(ApplyMethod(my_pic.to_corner, UL, run_time=1.1),
                             ApplyMethod(name_group.to_corner, UP, run_time=1.3))
        self.seb_resume.wait(3)
        education_title.move_to(job.get_center())
        self.seb_resume.play(ReplacementTransform(job, education_title))
        self.seb_resume.wait(3)

        # UPDATE TRANSITION TITLE DICT
        self.seb_resume.transition['current_title'] = education_title
        self.seb_resume.transition['current_title_position'] = education_title.get_center()



