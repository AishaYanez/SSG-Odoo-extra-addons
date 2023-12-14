# -*- coding: utf-8 -*-

from odoo import models, fields, api

class project_trm1_contrating_companies(models.Model):
 _name = 'project_trm1.contrating_companies'
 _description = 'project_trm1.contrating_companies'

 projects = fields.One2many('project.project','company', string="Proyectos")
 name = fields.Char(string="Nombre de la empresa",required=True)
 employees = fields.Integer(string="Número de empleados")
 logo= fields.Binary(string="Logo de la empresa")
 company_size = fields.Char(string="Tamaño de la empresa", compute="_companysize", store=True)
 user = fields.Many2one('res.users',string='Usuario que le da de alta',  default=lambda self: self.env.user, readonly=True)

 @api.depends('employees')
 def _companysize(self):
  for r in self:
     if r.employees > 100:
        r.company_size = 'Compañia grande'
     else:
        r.company_size = 'Compañia pequeña'

class project_trm1_project(models.Model):
 _name = 'project.project'
 _inherit = 'project.project'
 
 company = fields.Many2one("project_trm1.contrating_companies",string="Empresa",required=True,ondelete="cascade")

class project_trm1_task(models.Model):
 _name = 'project.task'
 _inherit = 'project.task'