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

from osv import osv
from osv import fields
from datetime import *

class oebase_professional_history(osv.Model):
    _name = 'oebase.professional.history'

    _columns = {
        'professional_id': fields.many2one('oebase.professional', 'Professional', required=True),
        'user_id' : fields.many2one ('res.users', 'User', required=True),
        'date': fields.datetime("Date", required=True),
        'state': fields.selection([('new','New'),
                                   ('active','Active'),
                                   ('inactive','Inactive'),
                                   ('suspended','Suspended')], 'Status', readonly=True),
        'notes': fields.text(string='Notes'),
        }
    
    _order = "date desc"

    _defaults = {
        'user_id': lambda obj,cr,uid,context: uid, 
        'date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }

oebase_professional_history()

class oebase_professional(osv.Model):
    _inherit = 'oebase.professional'

    _columns = {
        'history_ids': fields.one2many('oebase.professional.history', 'professional_id', 'Annotation History'),
    }

    def insert_oebase_professional_history(self, cr, uid, id_request, notes, context=None):
        request = self.browse(cr, uid, id_request, context)
        values = { 
            'professional_id':  id_request[0],
            'state': request[0].state,
            'notes': notes,
        }
        tracing_ids = self.pool.get('oebase.professional.history').create(cr, uid,values)
        return True

    def write(self, cr, uid, ids, vals, context=None):
        
        if context is None:
            context = {}

        if (not 'state' in vals):
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            notes = vals.keys()
            vals['date'] = date
            self.insert_oebase_professional_history(cr, uid, ids, notes, context)
        return super(oebase_professional, self).write(cr, uid, ids, vals, context)

    def new(self, cr, uid, ids, context=None):
         date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         self.write(cr, uid, ids, {'state': 'new', 'date': date})
         self.insert_oebase_professional_history(cr, uid, ids, '', context)
         return True

    def activate(self, cr, uid, ids, context=None):
         date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         self.write(cr, uid, ids, {'state': 'active', 'date': date})
         self.insert_oebase_professional_history(cr, uid, ids, '', context)
         return True

    def inactivate(self, cr, uid, ids, context=None):
         date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         self.write(cr, uid, ids, {'state': 'inactive', 'date': date})
         self.insert_oebase_professional_history(cr, uid, ids, '', context)
         return True

    def suspend(self, cr, uid, ids, context=None):
         date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         self.write(cr, uid, ids, {'state': 'suspended', 'date': date})
         self.insert_oebase_professional_history(cr, uid, ids, '', context)
         return True

oebase_professional()
