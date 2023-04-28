###############################################################################
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
###############################################################################

import csv
import json

dict_ = {
    'type': 'FeatureCollection',
    'features': []
}


with open('participants.csv') as fh:
    reader = csv.DictReader(fh)
    for row in reader:

        marker_icon = None

        if row['Component'] == 'Global Discovery Catalogue':
            marker_icon = 'gdc'
        elif row['Component'] == 'Global Broker':
            marker_icon = 'gb'
        elif row['Component'] == 'Global Cache':
            marker_icon = 'gc'
        elif row['Component'] == 'Global Monitoring':
            marker_icon = 'gm'
        elif row['Component'].startswith('WIS2 Node'):
            marker_icon = 'node'

        dict_['features'].append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [
                    float(row['Longitude']), float(row['Latitude'])
                ]
            },
            'properties': {
                'Country': row['Country'],
                'City': row['City'],
                'Component': row['Component'],
                'Status': row['Status'],
                'markerIcon': f'{marker_icon}.png'
            }
        })

print(json.dumps(dict_, ensure_ascii=False, indent=4))
