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
    'name': 'OpenERP Base: Professional',
    'version': '1.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://oehealth.org',
    'description': '''
    ''',
    'images': ['static/src/img/default_image.png',
               ],
    'depends': ['base_setup',
                'mail',
                'resource',
                'board',
                'oebase_base',
                'oebase_event',
                'oebase_group',
                ],
    'data': ['security/ir.model.access.csv',
             ],
    'demo': [],
    'test': [],
    'init_xml': ['security/oebase_professional_security.xml',
                 'oebase_professional_view.xml',
                 'oebase_professional_wkf_view.xml',
                 'oebase_professional_uid_view.xml',
                 'oebase_professional_workflow.xml',
                 'oebase_specialty_view.xml',
                 'oebase_professional_category_view.xml',
                 'oebase_professional_category_uid_view.xml',
                 'oebase_annotation_view.xml',
                 'oebase_tag_view.xml',
                 'oebase_event_participant_view.xml',
                 'oebase_group_participant_view.xml',
                 'oebase_professional_department_view.xml',
                 'oebase_professional_history_view.xml',
                  ],
    'test': [],
    'update_xml': ['oebase_professional_sequence.xml'
                   ],
    'installable': True,
    'active': False,
    'css': ['static/src/css/oebase_professional.css'],
}
