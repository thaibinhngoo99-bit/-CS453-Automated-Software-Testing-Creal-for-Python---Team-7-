def to_df(distance_matrix_response, origin_ids=None, destination_ids=None):
    """
    Given a (decoded) JSON response to a Google Maps
    Distance Matrix API call, convert it into a DataFrame with the
    following columns.

    - ``'origin_address'``
    - ``'origin_id'``: ID of origin; defaults to an element of
      :func:`make_ids`
    - ``'destination_address'``
    - ``'destination_id'``: ID of destination; defaluts to an element of
      :func:`make_ids`
    - ``'duration'``: time from origin to destination; includes
      time in traffic if that's available in the response
    - ``'distance'``: distance from origin to destination

    The origin and destination addresses in the response can optionally
    be assigned IDs by setting ``origin_ids`` (list of strings) and
    ``destination_ids`` (list of strings).
    """
    r = distance_matrix_response
    columns = ['origin_address', 'destination_address', 'origin_id', 'destination_id', 'duration', 'distance']
    f = pd.DataFrame([], columns=columns)
    if not r['rows']:
        return f
    f['origin_address'], f['destination_address'] = zip(*product(r['origin_addresses'], r['destination_addresses']))
    if origin_ids is None:
        origin_ids = make_ids(len(r['origin_addresses']))
    if destination_ids is None:
        destination_ids = make_ids(len(r['destination_addresses']))
    f['origin_id'], f['destination_id'] = zip(*product(origin_ids, destination_ids))
    durs = []
    dists = []
    for row in r['rows']:
        for e in row['elements']:
            if e['status'] == 'OK':
                if 'duration_in_traffic' in e:
                    dur_key = 'duration_in_traffic'
                else:
                    dur_key = 'duration'
                durs.append(e[dur_key]['value'])
                dists.append(e['distance']['value'])
            else:
                durs.append(np.nan)
                dists.append(np.nan)
    f['duration'] = durs
    f['distance'] = dists
    return f