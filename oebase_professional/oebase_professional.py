# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).                        #
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
from datetime import datetime
from dateutil.relativedelta import relativedelta
from openerp import addons
from openerp import tools
import logging

_logger = logging.getLogger(__name__)

class oebase_professional(osv.Model):
    _name = 'oebase.professional'
    _inherits = {'resource.resource': "resource_id"}


    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        reads = self.read(cr, uid, ids, ['name_professional_code'], context=context)
        res = []
        for record in reads:
            name = record['name_professional_code']
            res.append((record['id'], name))
        return res
    
    def name_professional_code_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if isinstance(ids, (int, long)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['name', 'professional_code'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['professional_code']:
                name = name + ' (' + record['professional_code'] + ')'
            res.append((record['id'], name))
        return res

    def _name_professional_code_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
        res = self.name_professional_code_get(cr, uid, ids, context=context)
        return dict(res)

    def _get_image(self, cr, uid, ids, name, args, context=None):
        result = dict.fromkeys(ids, False)
        for obj in self.browse(cr, uid, ids, context=context):
            result[obj.id] = tools.image_get_resized_images(obj.image)
        return result
    
    def _set_image(self, cr, uid, id, name, value, args, context=None):
        return self.write(cr, uid, [id], {'image': tools.image_resize_image_big(value)}, context=context)
    
    _columns = {
        #we need a related field in order to be able to sort the professional by name
        'name_related': fields.related('resource_id', 'name', type='char', string='Name', readonly=True, store=True),
        'alias' : fields.char('Alias', size=64, help='Common name that the Professional is referred'),
        'professional_code': fields.char(size=64, string='Professional Code', required=False),
        'name_professional_code': fields.function(_name_professional_code_get_fnc, type="char", string='Name (Professional Code)'),
        'country_id': fields.many2one('res.country', 'Nationality'),
        'birthday': fields.date("Date of Birth"),
        'identification_id': fields.char('Identification No', size=32),
        'otherid': fields.char('Other Id', size=64),
        'gender': fields.selection([('male', 'Male'),('female', 'Female')], 'Gender'),
        'marital': fields.selection([('single', 'Single'), ('married', 'Married'), ('widower', 'Widower'), ('divorced', 'Divorced')], 'Marital Status'),
        'address_id': fields.many2one('res.partner', 'Working Address'),
        'address_home_id': fields.many2one('res.partner', 'Home Address'),
        'work_phone': fields.char('Work Phone', size=32, readonly=False),
        'mobile_phone': fields.char('Work Mobile', size=32, readonly=False),
        'work_email': fields.char('Work Email', size=240),
        'work_location': fields.char('Office Location', size=32),
        'notes': fields.text('Notes'),
        'parent_id': fields.many2one('oebase.professional', 'Manager'),
        'child_ids': fields.one2many('oebase.professional', 'parent_id', 'Subordinates'),
        'resource_id': fields.many2one('resource.resource', 'Resource', ondelete='restrict', required=True),
        'coach_id': fields.many2one('oebase.professional', 'Coach'),
        #'job_id': fields.many2one('oebase.job', 'Function'),
        # image: all image fields are base64 encoded and PIL-supported
        'image': fields.binary("Photo",
            help="This field holds the image used as photo for the professional, limited to 1024x1024px."),
        'image_medium': fields.function(_get_image, fnct_inv=_set_image,
            string="Medium-sized photo", type="binary", multi="_get_image",
            store = {
                'oebase.professional': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Medium-sized photo of the professional. It is automatically "\
                 "resized as a 128x128px image, with aspect ratio preserved. "\
                 "Use this field in form views or some kanban views."),
        'image_small': fields.function(_get_image, fnct_inv=_set_image,
            string="Smal-sized photo", type="binary", multi="_get_image",
            store = {
                'oebase.professional': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Small-sized photo of the professional. It is automatically "\
                 "resized as a 64x64px image, with aspect ratio preserved. "\
                 "Use this field anywhere a small image is required."),
        'color': fields.integer('Color Index'),
        'login': fields.related('user_id', 'login', type='char', string='Login', readonly=1),
        'last_login': fields.related('user_id', 'login_date', type='datetime', string='Latest Connection', readonly=1),
        'active': fields.boolean('Active', help="If unchecked, it will allow you to hide the professional without removing it."),
    }

    _order='name_related'

    _sql_constraints = [('professional_code_uniq', 'unique(professional_code)', u'Duplicated Professional Code!')]

    def create(self, cr, uid, data, context=None):
        professional_id = super(oebase_professional, self).create(cr, uid, data, context=context)
        try:
            (model, mail_group_id) = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'mail', 'group_all_professionals')
            professional = self.browse(cr, uid, professional_id, context=context)
            self.pool.get('mail.group').message_post(cr, uid, [mail_group_id],
                body=_('Welcome to %s! Please help him/her take the first steps with OeHealth!') % (professional.name),
                subtype='mail.mt_comment', context=context)
        except:
            pass # group deleted: do not push a message
        return professional_id

    def unlink(self, cr, uid, ids, context=None):
        resource_ids = []
        for professional in self.browse(cr, uid, ids, context=context):
            resource_ids.append(professional.resource_id.id)
        return self.pool.get('resource.resource').unlink(cr, uid, resource_ids, context=context)

    def _get_default_image(self, cr, uid, context=None):
        image_path = addons.get_module_resource('oebase', 'static/src/img', 'default_image.png')
        return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

    def onchange_address_id(self, cr, uid, ids, address, context=None):
        if address:
            address = self.pool.get('res.partner').browse(cr, uid, address, context=context)
            return {'value': {'work_phone': address.phone, 'mobile_phone': address.mobile}}
        return {'value': {}}

    def onchange_company(self, cr, uid, ids, company, context=None):
        address_id = False
        if company:
            company_id = self.pool.get('res.company').browse(cr, uid, company, context=context)
            address = self.pool.get('res.partner').address_get(cr, uid, [company_id.partner_id.id], ['default'])
            address_id = address and address['default'] or False
        return {'value': {'address_id' : address_id}}

    def onchange_user(self, cr, uid, ids, user_id, context=None):
        work_email = False
        if user_id:
            work_email = self.pool.get('res.users').browse(cr, uid, user_id, context=context).email
        return {'value': {'work_email' : work_email}}

    def _get_default_image(self, cr, uid, context=None):
        image_path = addons.get_module_resource('hr', 'static/src/img', 'default_image.png')
        return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

    _defaults = {
        'active': 1,
        'image': _get_default_image,
        'color': 0,
    }

    def _check_recursion(self, cr, uid, ids, context=None):
        level = 100
        while len(ids):
            cr.execute('SELECT DISTINCT parent_id FROM oebase_professional WHERE id IN %s AND parent_id!=id',(tuple(ids),))
            ids = filter(None, map(lambda x:x[0], cr.fetchall()))
            if not level:
                return False
            level -= 1
        return True

    _constraints = [
        (_check_recursion, 'Error! You cannot create recursive hierarchy of Professional(s).', ['parent_id']),
    ]

oebase_professional()

class res_users(osv.osv):
    _name = 'res.users'
    _inherit = 'res.users'

    def create(self, cr, uid, data, context=None):
        user_id = super(res_users, self).create(cr, uid, data, context=context)

        # add shortcut unless 'noshortcut' is True in context
        if not(context and context.get('noshortcut', False)):
            data_obj = self.pool.get('ir.model.data')
            try:
                data_id = data_obj._get_id(cr, uid, 'oebase_professional', 'ir_ui_view_sc_health_professional')
                view_id  = data_obj.browse(cr, uid, data_id, context=context).res_id
                self.pool.get('ir.ui.view_sc').copy(cr, uid, view_id, default = {'user_id': user_id}, context=context)
            except:
                # Tolerate a missing shortcut. See product/product.py for similar code.
                _logger.debug('Skipped meetings shortcut for user "%s".', data.get('name','<new'))

        return user_id

    _columns = {
        'health_professional_ids': fields.one2many('oebase.professional', 'user_id', 'Related health professionals'),
        }

res_users()
