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
import datetime

class oebase_event(osv.Model):
    _name = 'oebase.event'

    _columns = {
        'name' : fields.char('Reference', size=64, select=1, required=True),
        'subject' : fields.char ('Subject',size=128, required=False),
        'responsible' : fields.many2one ('res.users', 'Responsible'),
        'date_event_inclusion' : fields.date('Inclusion Date'),
        'start_time': fields.datetime("Start Time"),
        'end_time': fields.datetime("End Time"),
        'notes': fields.text(string='Notes'),
        'active': fields.boolean('Active', help="If unchecked, it will allow you to hide the event without removing it."),
        }

    _sql_constraints = [('uniq_name', 'unique(name)', "The event reference must be unique!"),
                        ]

    _defaults = {
        'active': True,
        'date_event_inclusion': lambda *a: datetime.date.today().strftime('%Y-%m-%d'),
        'start_time': lambda *a: datetime.date.today().strftime('%Y-%m-%d'),
        'end_time': lambda *a: datetime.date.today().strftime('%Y-%m-%d'),
        'responsible': lambda obj,cr,uid,context: uid, 
        }

oebase_event()
