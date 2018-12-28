# -*- coding: utf-8 -*-


def _get_format_address(address):
    formatted_address = "%s, %s, %s, %s" % (address.street or '',
                                            address.zip or '',
                                            address.state_id.name
                                            or '', address.city or
                                            '')
    return formatted_address
