# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description = "OpenAcademy Courses"
    
    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    @api.onchange('description', 'name')
    def _onchange_description(self):
        for r in self:
            if not r.description and r.name:  # Si description está vacío y name tiene un valor
                r.description = r.name  # Tomar el mismo valor que name

    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)

class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
    
    attendee_id = fields.Many2many('res.partner',
        ondelete='cascade', string="Attendees", index=True)
    
    instructor_ids = fields.Many2one('res.partner',
        ondelete='cascade', string="Instructor", index=True, domain="[('is_Instructor', '=', True)]" )

class Partner(models.Model):
    _inherit = 'res.partner'

    is_Instructor = fields.Boolean(string='Is Instructor')
    sessions_id = fields.One2many('openacademy.session', 'instructor_ids', string="Sessions", index=True)
    
