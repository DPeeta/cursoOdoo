# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    session_ids = fields.Many2many('openacademy.session',
        string="Sessions")
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    def subscribe(self):
        for session in self.session_ids:
            if (session.start_date  and session.start_date > date.today()):
                session.attendee_ids |= self.attendee_ids
        return {}


