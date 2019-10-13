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

    out.put({'BOTSID': 'ST', 'ST01': '214', 'ST02': '0001'})
    out.put({'BOTSID': 'ST'}, {
        'BOTSID': 'B10',
        'B1001': reference_number,
        'B1002': shipment_number,
        'B1003': carrier_code
    })

    out.put({'BOTSID': 'ST'}, {'BOTSID': 'SE', 'SE01': out.getcount(), 'SE02': '0001'})
