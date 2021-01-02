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
import time
import werkzeug.utils
import json

from datetime import datetime, timedelta
import dateutil
import dateutil.parser
import dateutil.relativedelta

from odoo import api, fields
from odoo import http
from odoo.http import request
from odoo.addons.auth_oauth.controllers.main import OAuthLogin as Home

_logger = logging.getLogger(__name__)

class AnngularController(http.Controller):

    @http.route(['/','/apps'], website=True, auth='public', type='http')
    def main_route(self, redirect=None, *args, **kw):
        _logger.info('Angular Application Route')
        pass