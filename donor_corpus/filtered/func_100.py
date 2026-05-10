def parse_xml(filename):
    tree = etree.parse(open(filename, 'rb'))
    ts = []
    bssid = []
    signal = []
    lat = []
    lon = []
    walked_lon = []
    walked_lat = []
    for z in tree.findall('.//gps-point'):
        if z.get('bssid') == 'GP:SD:TR:AC:KL:OG':
            walked_lon.append(float(z.get('lon')))
            walked_lat.append(float(z.get('lat')))
        elif z.get('signal_dbm') is not None:
            bssid.append(z.get('bssid'))
            ts.append(int(z.get('time-sec')))
            lat.append(float(z.get('lat')))
            lon.append(float(z.get('lon')))
            signal.append(int(z.get('signal_dbm')))
    return (ts, bssid, signal, lat, lon, walked_lon, walked_lat)