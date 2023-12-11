# -*- coding: utf-8 -*-

from odoo import models, fields, api

class project_trm1_contrating_companies(models.Model):
    _name = 'project_trm1.contrating_companies'
    _description = 'project_trm1.contrating_companies'

    name = fields.Char(string="Nombre de la empresa")
    project = fields.Char(string="Proyectos contratados por la empresa")
    employees = fields.Integer(string="Número de empleados")
    logo= fields.Binary(string="Logo de la empresa")
    company_size = fields.Char(string="Tamaño de la empresa", compute="_companysize", store=True)

    @api.depends('employees')
    def _companysize(self):
    	for r in self:
						if r.employees > 100:
							r.company_size = 'Compañia grande'
						else:
									r.company_size = 'Compañia pequeña'