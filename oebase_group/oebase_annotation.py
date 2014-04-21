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

class oebase_annotation(orm.Model):
    _inherit = 'oebase.annotation'

    _columns = {
        'group_id' : fields.many2one ('oebase.group', 'Group'),
    }

oebase_annotation()

class oebase_group(orm.Model):
    _inherit = 'oebase.group'

    _columns = {
        'annotation_ids': fields.one2many('oebase.annotation',
                                          'group_id',
                                          'Annotations'),
    }

oebase_group()
