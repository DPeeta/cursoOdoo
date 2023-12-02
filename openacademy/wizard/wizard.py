# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

#  wizard suscrivir varios usuarios a varias sesiones 
class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    sessions_id = fields.Many2many('openacademy.session',
        string="Sessions")
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    def subscribe(self):
        for session in self.sessions_id:
            if (session.start_date  and session.start_date > date.today()):
                session.attendee_ids |= self.attendee_ids
        return {}

#  todas las sesiones con duración A (en días) la reemplace por le valor de B
class Wizard(models.TransientModel):
    _name = 'openacademy.wizardrempduration'
    _description = "Wizard: Replace in sessions with duration A with B "

    sessions_id = fields.Many2many('openacademy.session',
        string="Sessions")
    duration = fields.Float(digits=(6, 2), help="Value of duration in days")
    duration_find = fields.Float(digits=(6, 2), help="Value of duration in days to find", string="Sessions with this duration")
    duration_replace = fields.Float(digits=(6, 2), help="New value of duration in days", string="Will be replaced for this one")

    def replace(self):
        for session in self.sessions_id:
            if (session.duration  and session.duration == self.duration_find):
                session.duration == self.duration_replace
        return {}