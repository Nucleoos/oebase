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

class oebase_professional(orm.Model):
    _inherit = 'oebase.professional'

    _columns = {
        'group_ids': fields.one2many('oebase.group.participant',
                                     'professional_id',
                                     'Groups'),
    }

oebase_professional()

class oebase_group_participant(orm.Model):
    _inherit = 'oebase.group.participant'

    _columns = {
        'professional_id': fields.many2one('oebase.professional', string='Professional'),
    }

oebase_group_participant()
