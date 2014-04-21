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
        'specialty_ids': fields.many2many('oebase.specialty', 
                                          'oebase_professional_specialty_rel', 
                                          'professional_id', 
                                          'specialty_id', 
                                          'Specialties'),
    }

oebase_professional()

class oebase_specialty(orm.Model):
    _inherit = 'oebase.specialty'

    _columns = {
        'professional_ids': fields.many2many('oebase.professional', 
                                             'oebase_professional_specialty_rel', 
                                             'specialty_id', 
                                             'professional_id', 
                                             'Professionals'),
    }

oebase_specialty()
