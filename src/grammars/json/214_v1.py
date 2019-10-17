from bots.botsconfig import *

structure = [
    {ID: 'contents', MIN: 1, MAX: 1,
        QUERIES: {
             'frompartner':  ({'BOTSID': 'contents'}, {'BOTSID': 'header', 'sender_id': None}),
             'topartner':   ({'BOTSID': 'contents'},{'BOTSID': 'header', 'receiver_id': None}),
             'testindicator': ({'BOTSID': 'contents'},{'BOTSID': 'header', 'testindicator': None})
         },
        LEVEL: [
        {ID: 'header', MIN: 1, MAX: 1},
        {ID: 'shipment', MIN: 1, MAX: 1, LEVEL: [
            {ID: 'l11', MIN: 0, MAX: 9999},
            {ID: 'n1', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'n3', MIN: 1, MAX: 1},
                {ID: 'n4', MIN: 1, MAX: 1}
            ]}
        ]},
        {ID: 'detail', MIN: 1, MAX: 1, LEVEL: [
            {ID: 'lx', MIN: 1, MAX: 10, LEVEL: [
                {ID: 'at7', MIN: 1, MAX: 10, LEVEL: [
                    {ID: 'ms1', MIN: 0, MAX: 1},
                    {ID: 'ms2', MIN: 0, MAX: 1}
                ]},
                {ID: 'l11', MIN:0, MAX: 9999},
                {ID: 'prf', MIN: 0, MAX: 9999, LEVEL: [
                    {ID: 'n1', MIN: 0, MAX: 10, LEVEL: [
                        {ID: 'n3', MIN: 1, MAX: 1},
                        {ID: 'n4', MIN: 1, MAX: 1}
                    ]}
                ]}
            ]}
        ]}
    ]}
]

#nextmessage = {'BOTSID': 'contents'}

recorddefs = {
    'contents': [
        ['BOTSID', 'C', 8, 'A'],
    ],
    'header': [
        ['BOTSID', 'C', 6, 'A'],
        ['sender_id', 'M', 20, 'A'],
        ['receiver_id', 'M', 20, 'A'],
        ['testindicator', 'C', 1, 'A'],
    ],
    'shipment': [
        ['BOTSID', 'C', 8, 'A'],
        ['reference_number', 'M', 50, 'A'],
        ['shipment_number', 'M', 50, 'A'],
        ['carrier_code', 'C', 4, 'A']
    ],
    'detail': [
        ['BOTSID', 'C', 6, 'A'],
    ],
    'l11': [
        ['BOTSID', 'C', 3, 'A'],
        ['value', 'M', 50, 'A'],
        ['qualifier', 'M', 2, 'A']
    ],
    'n1': [
        ['BOTSID', 'C', 2, 'A'],
        ['qualifier', 'M', 2, 'A'],
        ['name', 'M', 100, 'A'],
        ['location_code_qualifier', 'C', 2, 'A'],
        ['location_code', 'C', 10, 'A']
    ],
    'n3': [
        ['BOTSID', 'C', 2, 'A'],
        ['address1', 'M', 50, 'A'],
        ['address2', 'C', 50, 'A']
    ],
    'n4': [
        ['BOTSID', 'C', 2, 'A'],
        ['city', 'M', 50, 'A'],
        ['state', 'M', 2, 'A'],
        ['zip', 'M', 50, 'A'],
        ['country', 'M', 3, 'A']
    ],
    'lx': [
        ['BOTSID', 'C', 2, 'A'],
        ['sequence_number', 'C', 2, 'N']
    ],
    'at7': [
        ['BOTSID', 'C', 3, 'A'],
        ['status_code', 'C', 2, 'A'],
        ['status_reason_code', 'C', 2, 'A'],
        ['appointment_code', 'C', 2, 'A'],
        ['appointment_reason_code', 'C', 2, 'A'],
        ['date', 'C', 8, 'D'],
        ['time', 'C', 4, 'T'],
        ['timezone', 'C', 2, 'A']
    ],
    'ms1': [
        ['BOTSID', 'C', 3, 'A'],
        ['city', 'C', 50, 'A'],
        ['state', 'C', 2, 'A'],
        ['country_code', 'C', 3, 'A']
    ],
    'ms2': [
        ['BOTSID', 'C', 3, 'A'],
        ['carrier_code', 'C', 4, 'A'],
        ['equipment_number', 'C', 50, 'A'],
        ['equipment_type', 'C', 4, 'A']
    ],
    'prf': [
        ['BOTSID', 'C', 3, 'A'],
        ['po_number', 'C', 50, 'A']
    ]
}
