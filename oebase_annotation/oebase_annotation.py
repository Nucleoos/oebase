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
from openerp.tools.translate import _
from datetime import *

class oebase_annotation(osv.Model):
    _name = 'oebase.annotation'

    def name_get(self, cr, uid, ids, context=None):
        """Return the annotation's display name, including their direct
           parent by default.

        :param dict context: the `annotation_display` key can be
                             used to select the short version of the
                             annotation name (without the direct parent),
                             when set to ``'short'``. The default is
                             the long version."""
        if context is None:
            context = {}
        if context.get('annotation_display') == 'short':
            return super(oebase_annotation, self).name_get(cr, uid, ids, context=context)
        if isinstance(ids, (int, long)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['name', 'parent_id'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['parent_id']:
                name = record['parent_id'][1] + ' / ' + name
            res.append((record['id'], name))
        return res

    def name_search(self, cr, uid, name, args=None, operator='ilike', context=None, limit=100):
        if not args:
            args = []
        if not context:
            context = {}
        if name:
            # Be sure name_search is symetric to name_get
            name = name.split(' / ')[-1]
            ids = self.search(cr, uid, [('name', operator, name)] + args, limit=limit, context=context)
        else:
            ids = self.search(cr, uid, args, limit=limit, context=context)
        return self.name_get(cr, uid, ids, context)


    def _name_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
        res = self.name_get(cr, uid, ids, context=context)
        return dict(res)

    _columns = {
        'name' : fields.char('Subject', size=64, select=1, required=True),
        'complete_name': fields.function(_name_get_fnc, type="char", string='Subject', store=True),
        'ref' : fields.char ('Reference',size=128, required=False),
        'author': fields.many2one('res.users', 'Author', required=True, readonly=True),
        'date': fields.datetime("Date", required=True, readonly=True),
        'body': fields.text(string='Body'),
        'parent_id': fields.many2one('oebase.annotation', 'Parent Annotation', select=True, ondelete='restrict'),
        'child_ids': fields.one2many('oebase.annotation', 'parent_id', 'Child Annotations'),
        'parent_left': fields.integer('Left parent', select=True),
        'parent_right': fields.integer('Right parent', select=True),
        'active': fields.boolean('Active', help="If unchecked, it will allow you to hide the annotation without removing it."),
        }
    
    _constraints = [
                    (osv.osv._check_recursion, 'Error! You can not create recursive annotations.', ['parent_id'])
                    ]

    _sql_constraints = [
                        ('uniq_ref', 'unique(ref)', "The annotation reference must be unique!"),
                        ]

    _defaults = {
        'active': True,
        'date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'author': lambda obj,cr,uid,context: uid, 
        }

    _parent_store = True
    _parent_order = 'name'
    _order = 'parent_left'

oebase_annotation()
