# -*- coding: utf-8 -*-

from odoo import models, fields, api

class project_trm1_contrating_companies(models.Model):
 _name = 'project_trm1.contrating_companies'
 _description = 'project_trm1.contrating_companies'

 projects = fields.One2many('project.project','company', string="Proyectos")
 name = fields.Char(string="Nombre de la empresa")
 employees = fields.Integer(string="Número de empleados")
 logo= fields.Binary(string="Logo de la empresa")
 company_size = fields.Char(string="Tamaño de la empresa", compute="_companysize", store=True)
#  digital_signature = fields.Binary(string="Firma",related='user_id.digital_signature',readonly=True)

#  user_id = fields.Many2one('res.user',string='Usuario que le da de alta')

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
#  user_id = fields.Many2one('res.user',string='Jefe de proyecto')

class project_trm1_task(models.Model):
 _name = 'project.task'
 _inherit = 'project.task'

 programmer = fields.Char(string="Programador")