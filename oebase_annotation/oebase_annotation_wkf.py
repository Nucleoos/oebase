# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol                  #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################

from openerp.osv import orm, fields
from datetime import *

class oebase_annotation(orm.Model):
    _inherit = 'oebase.annotation'

    _columns = {
        'state': fields.selection([('new','New'),
                                   ('revised','Revised'),
                                   ('waiting','Waiting'),
                                   ('okay','Okay')], 'Stage', readonly=True),
    }

    _defaults = {
        'state': 'new',
    }
    
    def new(self, cr, uid, ids, context=None):
         date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         self.write(cr, uid, ids, {'state': 'new', 'date': date})
         return True

    def revised(self, cr, uid, ids, context=None):
         date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         self.write(cr, uid, ids, {'state': 'revised', 'date': date})
         return True

    def waiting(self, cr, uid, ids, context=None):
         date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         self.write(cr, uid, ids, {'state': 'waiting', 'date': date})
         return True

    def okay(self, cr, uid, ids, context=None):
         date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         self.write(cr, uid, ids, {'state': 'okay', 'date': date})
         return True

oebase_annotation()
