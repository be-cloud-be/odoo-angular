# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2020 be-cloud.be
#                       Jerome Sonnet <jerome.sonnet@be-cloud.be>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class AngularApplication(models.Model):
    '''Angular Application'''
    _name = 'angular.application'
    _description = 'Angular Application'
    _inherit = ['mail.thread']
    
    name = fields.Char(string="Name")
    
    path = fields.Char(string="Application Path", help="Application access is app/$path.")
    
    port = fields.Integer(string="Port", help="Network port for the devel server.")
    
    is_devel_running = fields.Boolean(string="Devel Server", help="True if development server is running")
    
    def action_build(self):
        # Shoud do ng build and link into static
        pass
    
    def action_start_devel(self):
        # Shoud do ng serve
        pass
    
    def action_stop_devel(self):
        # Shoud kill ng serve
        pass