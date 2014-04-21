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

class oebase_tag(orm.Model):
    _inherit = 'oebase.tag'

    _columns = {
        'event_ids': fields.many2many('oebase.event', 
                                      'oebase_event_tag_rel', 
                                      'tag_id', 
                                      'event_id', 
                                      'Events'),
    }

oebase_tag()

class oebase_event(orm.Model):
    _inherit = 'oebase.event'

    _columns = {
        'tag_ids': fields.many2many('oebase.tag', 
                                    'oebase_event_tag_rel', 
                                    'event_id', 
                                    'tag_id', 
                                    'Tags'),
    }

oebase_event()
