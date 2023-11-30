# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Person(models.Model):
    _name = 'persons.person'
    _description = "Just a person"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")

    

