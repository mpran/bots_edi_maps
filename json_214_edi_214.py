def main(inn, out):
    reference_number = inn.get({'BOTSID': 'contents'}, {
        'BOTSID': 'shipment',
        'reference_number': None
    })
    shipment_number = inn.get({'BOTSID': 'contents'}, {
        'BOTSID': 'shipment',
        'shipment_number': None
    })
    carrier_code = inn.get({'BOTSID': 'contents'}, {
        'BOTSID': 'shipment',
        'carrier_code': None
    })
    shipment_ref_numbers = inn.getloop({'BOTSID': 'contents'},
                                       {'BOTSID': 'shipment'},
                                       {'BOTSID': 'l11'})
    shipment_locations = inn.getloop({'BOTSID': 'contents'},
                                     {'BOTSID': 'shipment'}, {'BOTSID': 'n1'})

    prf_locations = inn.getloop({'BOTSID': 'contents'}, {'BOTSID': 'detail'},
                                {'BOTSID': 'prf'}, {'BOTSID': 'n1'})

    lx_loop = inn.getloop({'BOTSID': 'contents'}, {'BOTSID': 'detail'},
                          {'BOTSID': 'lx'})

    out.put({'BOTSID': 'ST', 'ST01': '214', 'ST02': '0001'})
    out.put({'BOTSID': 'ST'}, {
        'BOTSID': 'B10',
        'B1001': reference_number,
        'B1002': shipment_number,
        'B1003': carrier_code
    })
    for srn in shipment_ref_numbers:
        value = srn.get({'BOTSID': 'l11', 'value': None})
        qualifier = srn.get({'BOTSID': 'l11', 'qualifier': None})
        lou = out.putloop({'BOTSID': 'ST'}, {'BOTSID': 'L11'})
        lou.put({'BOTSID': 'L11', 'L1101': value, 'L1102': qualifier})

    for sl in shipment_locations:
        qualifier = sl.get({'BOTSID': 'n1', 'qualifier': None})
        name = sl.get({'BOTSID': 'n1', 'name': None})
        location_code_qualifier = sl.get({
            'BOTSID': 'n1',
            'location_code_qualifier': None
        })
        location_code = sl.get({'BOTSID': 'n1', 'location_code': None})
        address1 = sl.get({'BOTSID': 'n1'}, {'BOTSID': 'n3', 'address1': None})
        city = sl.get({'BOTSID': 'n1'}, {'BOTSID': 'n4', 'city': None})
        state = sl.get({'BOTSID': 'n1'}, {'BOTSID': 'n4', 'state': None})
        zip_ = sl.get({'BOTSID': 'n1'}, {'BOTSID': 'n4', 'zip': None})
        country = sl.get({'BOTSID': 'n1'}, {'BOTSID': 'n4', 'country': None})

        lou = out.putloop({'BOTSID': 'ST'}, {'BOTSID': 'N1'})

        lou.put({
            'BOTSID': 'N1',
            'N101': qualifier,
            'N102': name,
            'N103': location_code_qualifier,
            'N104': location_code
        })

        lou.put({'BOTSID': 'N1'}, {'BOTSID': 'N3', 'N301': address1})
        lou.put({'BOTSID': 'N1'}, {
            'BOTSID': 'N4',
            'N401': city,
            'N402': state,
            'N403': zip_,
            'N404': country
        })

    for sl in prf_locations:
        qualifier = sl.get({'BOTSID': 'n1', 'qualifier': None})
        name = sl.get({'BOTSID': 'n1', 'name': None})
        location_code_qualifier = sl.get({
            'BOTSID': 'n1',
            'location_code_qualifier': None
        })
        location_code = sl.get({'BOTSID': 'n1', 'location_code': None})
        address1 = sl.get({'BOTSID': 'n1'}, {'BOTSID': 'n3', 'address1': None})
        city = sl.get({'BOTSID': 'n1'}, {'BOTSID': 'n4', 'city': None})
        state = sl.get({'BOTSID': 'n1'}, {'BOTSID': 'n4', 'state': None})
        zip_ = sl.get({'BOTSID': 'n1'}, {'BOTSID': 'n4', 'zip': None})
        country = sl.get({'BOTSID': 'n1'}, {'BOTSID': 'n4', 'country': None})

        lou = out.putloop({'BOTSID': 'ST'}, {'BOTSID': 'LX'},
                          {'BOTSID': 'PRF'})

        lou.put({
            'BOTSID': 'N1',
            'N101': qualifier,
            'N102': name,
            'N103': location_code_qualifier,
            'N104': location_code
        })

        lou.put({'BOTSID': 'N1'}, {'BOTSID': 'N3', 'N301': address1})
        lou.put({'BOTSID': 'N1'}, {
            'BOTSID': 'N4',
            'N401': city,
            'N402': state,
            'N403': zip_,
            'N404': country
        })

    for lx in lx_loop:
        # sequence_number = lx.get({'BOTDSID': 'lx', 'sequence_number': None})
        sequence_number = 1
        at7_in_loop = lx.getloop({'BOTSID': 'lx'}, {'BOTSID': 'at7'})
        lx_out_loop = out.putloop({'BOTSID': 'ST'}, {'BOTSID': 'LX'})

        lx_out_loop.put({'BOTSID': 'LX', 'LX01': sequence_number})

        for at7 in at7_in_loop:
            at7_out_loop = out.putloop({'BOTSID': 'ST'}, {'BOTSID': 'LX'},
                                       {'BOTSID': 'AT7'})
            status_code = at7.get({'BOTSID': 'at7', 'status_code': None})
            status_reason_code = at7.get({
                'BOTSID': 'at7',
                'status_reason_code': None
            })
            appointment_code = at7.get({
                'BOTSID': 'at7',
                'appointment_code': None
            })
            appointment_reason_code = at7.get({
                'BOTSID': 'at7',
                'appointment_reason_code': None
            })
            date = at7.get({'BOTSID': 'at7', 'date': None})
            time = at7.get({'BOTSID': 'at7', 'time': None})
            timezone = at7.get({'BOTSID': 'at7', 'timezone': None})

            ms2_carrier_code = at7.get({'BOTSID': 'at7'}, {
                'BOTSID': 'ms2',
                'carrier_code': None
            })

            ms2_equipment_number = at7.get({'BOTSID': 'at7'}, {
                'BOTSID': 'ms2',
                'equipment_number': None
            })

            ms2_equipment_type = at7.get({'BOTSID': 'at7'}, {
                'BOTSID': 'ms2',
                'equipment_type': None
            })

            at7_out_loop.put({'BOTSID': 'AT7', 'AT701': status_code})
            at7_out_loop.put({'BOTSID': 'AT7', 'AT702': status_reason_code})
            at7_out_loop.put({'BOTSID': 'AT7', 'AT703': appointment_code})
            at7_out_loop.put({
                'BOTSID': 'AT7',
                'AT704': appointment_reason_code
            })
            at7_out_loop.put({'BOTSID': 'AT7', 'AT705': date})
            at7_out_loop.put({'BOTSID': 'AT7', 'AT706': time})
            at7_out_loop.put({'BOTSID': 'AT7', 'AT707': timezone})

            at7_out_loop.put({'BOTSID': 'AT7'}, {
                'BOTSID': 'MS2',
                'MS201': ms2_carrier_code,
                'MS202': ms2_equipment_number,
                'MS203': ms2_equipment_type
            })

    out.put({'BOTSID': 'ST'}, {
        'BOTSID': 'SE',
        'SE01': out.getcount() + 1,
        'SE02': '0001'
    })
