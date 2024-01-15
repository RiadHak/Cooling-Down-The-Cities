    
def filter_data(jsn, **kwarg):
    
    uplink_message = jsn.get("uplink_message", {})
    decoded_payload = uplink_message.get("decoded_payload", {})
    
    if uplink_message and decoded_payload:
        for k, v in decoded_payload.items():
            if v.get('field') and v.get('value') not in kwarg:
                kwarg[v.get('field')] = round(v.get('value'), 2)
            else:
                continue
    else:
        return kwarg
    return kwarg


             