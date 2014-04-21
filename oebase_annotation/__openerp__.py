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
    'name': 'OpenERP Base - Annotation',
    'version': '7.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://oehealth.org',
    'description': '''
    ''',
    'depends': ['oebase_base',
                'oebase_tag',
                ],
    'data': ['security/ir.model.access.csv',
             ],
    'init_xml': ['oebase_annotation_view.xml',
                 'oebase_annotation_workflow.xml',
                 'oebase_annotation_uid_view.xml',
                 'oebase_annotation_wkf_view.xml',
                 'oebase_annotation_category_view.xml',
                 'oebase_annotation_category_uid_view.xml',
                 'oebase_annotation_history_view.xml',
                 'oebase_tag_view.xml',
                 ],
    'test': [],
    'update_xml': ['oebase_annotation_sequence.xml'
                   ],
    'installable': True,
    'active': False,
}
