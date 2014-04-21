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

{
    'name': 'OpenERP Base: Group',
    'version': '1.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://oehealth.org',
    'description': '''
    ''',
    'depends': ['oebase_base',
                'oebase_tag',
                'oebase_annotation',
                ],
    'data': ['security/ir.model.access.csv',
             ],
    'init_xml': ['security/oebase_group_security.xml',
                 'oebase_group_view.xml',
                 'oebase_group_wkf_view.xml',
                 'oebase_group_uid_view.xml',
                 'oebase_group_workflow.xml',
                 'oebase_group_category_view.xml',
                 'oebase_group_category_uid_view.xml',
                 'oebase_group_participant_view.xml',
                 'oebase_group_participant_uid_view.xml',
                 'oebase_group_participant_role_view.xml',
                 'oebase_group_participant_role_uid_view.xml',
                 'oebase_annotation_view.xml',
                 'oebase_tag_view.xml',
                 ],
    'test': [],
    'update_xml': ['oebase_group_sequence.xml',
                   ],
    'installable': True,
    'active': False,
}
