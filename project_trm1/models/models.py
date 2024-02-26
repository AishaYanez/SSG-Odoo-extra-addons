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
 project_display_option = fields.Selection([('show_projects', 'Mostrar proyectos'), ('hide_projects', 'Ocultar proyectos')],string="Mostrar proyectos", compute="_compute_show_projects", readonly=True)

 @api.model
 def create(self, vals):
        new_company = super(project_trm1_contrating_companies, self).create(vals)
        self.env['project_trm1.register'].sudo().register_company_creation(
            user=self.env.user,
            name=new_company.name,
            creation_date=fields.Datetime.now()
        )
        return new_company

 def write(self, vals):
    modified_company = super(project_trm1_contrating_companies, self).write(vals)
    self.env['project_trm1.register'].sudo().register_company_modification(
            user=self.env.user,
            name=self.name,
            creation_date=fields.Datetime.now()
     )
    return self

 def unlink(self):
   deleted_companies = self.env['project_trm1.register']
   for company in self:
      deleted_companies.sudo().register_company_elimination(
            user=self.env.user,
            name=company.name,
            creation_date=fields.Datetime.now()
      )
   return super(project_trm1_contrating_companies, self).unlink()

 def _compute_show_projects(self):
        param = self.env['ir.config_parameter'].sudo().get_param('project_trm1.project_display_option')
        self.project_display_option = param if param else 'hide_projects'

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
 tasks = fields.One2many('project.task','project', string="Tareas")
 show_task = fields.Boolean(string="Mostrar tareas", compute="_compute_show_task", readonly=True)

 def _compute_show_task(self):
   param = self.env['ir.config_parameter'].sudo().get_param('project_trm1.show_task')
   self.show_task = param.lower() == 'true' if param else False

class project_trm1_task(models.Model):
 _name = 'project.task'
 _inherit = 'project.task'

 project = fields.Many2one("project.project",string="Proyecto",required=True,ondelete="cascade")

class project_trm1_register(models.Model):
   _name = 'project_trm1.register'
   _description = 'project_trm1.register'

   user_name = fields.Char(string='Nombre de usuario')
   company_name = fields.Char(string='Nombre de la Empresa')
   creation_date = fields.Datetime(string='Fecha/Hora de Creación')
   action_type = fields.Selection([
        ('creacion', 'Creación'),
        ('modificacion', 'Modificación'),
        ('eliminacion', 'Eliminación'),
        ('consulta', 'Consulta')],
        string='Tipo de Acción')

   @api.model
   def register_company_creation(self, user, name, creation_date):
        vals = {
            'user_name': user.name,
            'company_name': name,
            'creation_date': creation_date,
            'action_type': 'creacion'
        }
        self.create(vals)

   @api.model
   def register_company_modification(self, user, name, creation_date):
        vals = {
            'user_name': user.name,
            'company_name': name,
            'creation_date': creation_date,
            'action_type': 'modificacion'
        }
        self.env['project_trm1.register'].create(vals)

   @api.model
   def register_company_elimination(self, user, name, creation_date):
        vals = {
            'user_name': user.name,
            'company_name': name,
            'creation_date': creation_date,
            'action_type': 'eliminacion'
        }
        self.create(vals)


   # @api.model
   # def  default_get(self,  fields_list):
   #    company = super(project_trm1_contrating_companies, self).default_get(fields_list)

   #    company['name'] = 'Empresa'

   # self.env['project_trm1.register'].register_company_consult(
   #          user=self.env.user,
   #          name=company['name'],
   #          creation_date=fields.Datetime.now()
   #      )
   # return company

   # @api.model
   # def register_company_consult(self, user, name, creation_date):
   #      vals = {
   #          'user_name': user.name,
   #          'company_name': name,
   #          'creation_date': creation_date,
   #          'action_type': 'consulta'
   #      }
   #      self.create(vals)

        
class ResCofinSettings(models.TransientModel):
   _inherit = 'res.config.settings'

   show_task = fields.Boolean(String='Ver tareas', config_parameter='project_trm1.show_task')
   project_display_option = fields.Selection([('show_projects', 'Mostrar proyectos'), ('hide_projects', 'Ocultar proyectos')],
                                               string='Opción de visualización de proyectos',
                                               config_parameter='project_trm1.project_display_option')
