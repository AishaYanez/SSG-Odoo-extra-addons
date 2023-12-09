# -*- coding: utf-8 -*-

from odoo import models, fields, api

class project_trm1_project_manager(models.Model):
    _name = 'project_trm1.project_manager'
    _description = 'project_trm1.project_manager'

    company = fields.Char(string="Nombre de la empresa")
    project = fields.Char(string="Nombre del proyecto")
    user = fields.Char(string="Nombre del jefe de proyectos")
