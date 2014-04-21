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
import re

class oebase_professional(orm.Model):
    _inherit = 'oebase.professional'

    _columns = {
        'professional_code': fields.char(size=64, string='Professional Code', required=False, help='Use "/" to get an automatic new Reference.'),
    }

    _defaults = {
        'professional_code': '/',
    }
    
    def create(self, cr, uid, vals, context=None):
        if context is None:
            context = {}
        if not 'professional_code' in vals or vals['professional_code'] == '/':
            val = self.pool.get('ir.sequence').get(cr, uid, 'oebase.professional.code')
            code = map(int, str(val))
            code_len = len(code)
            while len(code) < 14:
                code.insert(0, 0)
            while len(code) < 16:
                n = sum([(len(code) + 1 - i) * v for i, v in enumerate(code)]) % 11
                if n > 1:
                    f = 11 - n
                else:
                    f = 0
                code.append(f)
            code_str = "%s.%s.%s.%s.%s-%s" % (str(code[0]) + str(code[1]),
                                              str(code[2]) + str(code[3]) + str(code[4]),
                                              str(code[5]) + str(code[6]) + str(code[7]),
                                              str(code[8]) + str(code[9]) + str(code[10]),
                                              str(code[11]) + str(code[12]) + str(code[13]),
                                              str(code[14]) + str(code[15]))
            if code_len <= 3:
                vals['professional_code'] = code_str[18 - code_len:21]
            elif code_len > 3 and code_len <= 6:
                vals['professional_code'] = code_str[17 - code_len:21]
            elif code_len > 6 and code_len <= 9:
                vals['professional_code'] = code_str[16 - code_len:21]
            elif code_len > 9 and code_len <= 12:
                vals['professional_code'] = code_str[15 - code_len:21]
            elif code_len > 12 and code_len <= 14:
                vals['professional_code'] = code_str[14 - code_len:21]
        return super(oebase_professional, self).create(cr, uid, vals, context)

oebase_professional()
