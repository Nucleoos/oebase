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

class oebase_event_participant(osv.Model):
    _name = 'oebase.event.participant'

    _columns = {
        'event_id': fields.many2one('oebase.event', string='Event',
                                    help='Event'),
        'role': fields.many2one('oebase.event.participant.role', 'Role', required=True),
        'notes': fields.text(string='Notes'),
        'user_id': fields.many2one('res.users', string='User'),
        'active': fields.boolean('Active', help="If unchecked, it will allow you to hide the participant without removing it."),
    }

oebase_event_participant()

class oebase_event(osv.osv):
    _inherit = 'oebase.event'

    _columns = {
        'participant_ids': fields.one2many('oebase.event.participant',
                                           'event_id',
                                           'Participants'),
    }

oebase_event()
