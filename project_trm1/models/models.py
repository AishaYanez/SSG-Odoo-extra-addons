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
 show_task = fields.Boolean(string="Mostrar tareas", default=lambda self: self._get_show_task(), readonly=True)

 def _get_show_task(self):
   param = self.env['ir.config_parameter'].sudo().get_param('project_trm1.show_task')
   return param.lower() == 'true' if param else False

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


class ResCofinSettings(models.TransientModel):
   _inherit = 'res.config.settings'

   show_task = fields.Boolean(String='Ver tareas', config_parameter='project_trm1.show_task')
   project_display_option = fields.Selection([('show_projects', 'Mostrar proyectos'), ('hide_projects', 'Ocultar proyectos')],
                                               string='Opción de visualización de proyectos',
                                               config_parameter='project_trm1.project_display_option')