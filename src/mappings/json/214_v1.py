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
        lx_ref_numbers = lx.getloop({'BOTSID': 'lx'}, {'BOTSID': 'l11'})
        lx_prf_numbers = lx.getloop({'BOTSID': 'lx'}, {'BOTSID': 'prf'})
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

            ms1_city = at7.get({'BOTSID': 'at7'}, {
                'BOTSID': 'ms1',
                'city': None
            })
            ms1_state = at7.get({'BOTSID': 'at7'}, {
                'BOTSID': 'ms1',
                'state': None
            })
            ms1_country_code = at7.get({'BOTSID': 'at7'}, {
                'BOTSID': 'ms1',
                'country_code': None
            })

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

            #AT7
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

            ## MS1

            at7_out_loop.put({'BOTSID': 'AT7'}, {
                'BOTSID': 'MS1',
                'MS101': ms1_city
            })

            at7_out_loop.put({'BOTSID': 'AT7'}, {
                'BOTSID': 'MS1',
                'MS102': ms1_state
            })

            at7_out_loop.put({'BOTSID': 'AT7'}, {
                'BOTSID': 'MS1',
                'MS103': ms1_country_code
            })

            ## MS2

            at7_out_loop.put({'BOTSID': 'AT7'}, {
                'BOTSID': 'MS2',
                'MS201': ms2_carrier_code
            })

            at7_out_loop.put({'BOTSID': 'AT7'}, {
                'BOTSID': 'MS2',
                'MS202': ms2_equipment_number
            })

            at7_out_loop.put({'BOTSID': 'AT7'}, {
                'BOTSID': 'MS2',
                'MS203': ms2_equipment_type
            })

        ## L11
        for lxr in lx_ref_numbers:
            value = lxr.get({'BOTSID': 'l11', 'value': None})
            qualifier = lxr.get({'BOTSID': 'l11', 'qualifier': None})
            lou = out.putloop({'BOTSID': 'ST'}, {'BOTSID': 'LX'},
                              {'BOTSID': 'L11'})
            lou.put({'BOTSID': 'L11', 'L1101': value})
            lou.put({'BOTSID': 'L11', 'L1102': qualifier})

        ## prf
        for prf in lx_prf_numbers:
            po_number = prf.get({'BOTSID': 'prf', 'po_number': None})
            prf_location_loop = prf.getloop({'BOTSID': 'prf'},
                                            {'BOTSID': 'n1'})

            prf_loop_out = out.putloop({'BOTSID': 'ST'}, {'BOTSID': 'LX'},
                                       {'BOTSID': 'PRF'})

            prf_loop_out.put({'BOTSID': 'PRF', 'PRF01': po_number})

            for prf_loc in prf_location_loop:
                locations_loop_out = prf_loop_out.putloop({'BOTSID': 'PRF'},
                                                          {'BOTSID': 'N1'})

                location_qualifier = prf_loc.get({
                    'BOTSID': 'n1',
                    'qualifier': None
                })
                location_name = prf_loc.get({'BOTSID': 'n1', 'name': None})
                location_code_qualifier = prf_loc.get({
                    'BOTSID':
                    'n1',
                    'location_code_qualifier':
                    None
                })
                location_code = prf_loc.get({
                    'BOTSID': 'n1',
                    'location_code': None
                })

                location_address1 = prf_loc.get({'BOTSID': 'n1'}, {
                    'BOTSID': 'n3',
                    'address1': None
                })

                location_city = prf_loc.get({'BOTSID': 'n1'}, {
                    'BOTSID': 'n4',
                    'city': None
                })
                location_state = prf_loc.get({'BOTSID': 'n1'}, {
                    'BOTSID': 'n4',
                    'state': None
                })
                location_zip = prf_loc.get({'BOTSID': 'n1'}, {
                    'BOTSID': 'n4',
                    'zip': None
                })
                location_country = prf_loc.get({'BOTSID': 'n1'}, {
                    'BOTSID': 'n4',
                    'country': None
                })

                locations_loop_out.put({
                    'BOTSID': 'N1',
                    'N101': location_qualifier
                })
                locations_loop_out.put({'BOTSID': 'N1', 'N102': location_name})
                locations_loop_out.put({
                    'BOTSID': 'N1',
                    'N103': location_code_qualifier
                })
                locations_loop_out.put({'BOTSID': 'N1', 'N104': location_code})

                locations_loop_out.put({'BOTSID': 'N1'}, {
                    'BOTSID': 'N3',
                    'N301': location_address1
                })

                locations_loop_out.put({'BOTSID': 'N1'}, {
                    'BOTSID': 'N4',
                    'N401': location_city
                })
                locations_loop_out.put({'BOTSID': 'N1'}, {
                    'BOTSID': 'N4',
                    'N402': location_state
                })
                locations_loop_out.put({'BOTSID': 'N1'}, {
                    'BOTSID': 'N4',
                    'N403': location_zip
                })
                locations_loop_out.put({'BOTSID': 'N1'}, {
                    'BOTSID': 'N4',
                    'N404': location_country
                })

    out.put({'BOTSID': 'ST'}, {
        'BOTSID': 'SE',
        'SE01': out.getcount(),
        'SE02': '0001'
    })
