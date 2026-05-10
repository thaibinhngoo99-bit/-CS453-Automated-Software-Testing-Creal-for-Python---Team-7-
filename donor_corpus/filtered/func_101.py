def draw_data(ts, bssid, signal, lat, lon, walked_lon, walked_lat):
    grid_x, grid_y = numpy.mgrid[min(walked_lon):max(walked_lon):1000j, min(walked_lat):max(walked_lat):1000j]
    bssids = list(set(bssid))
    for s in bssids:
        points_lon = []
        points_lat = []
        values = []
        h = []
        for i in range(0, len(bssid)):
            if bssid[i] == s:
                hc = hash((lon[i], lat[i]))
                if hc not in h:
                    points_lon.append(lon[i])
                    points_lat.append(lat[i])
                    values.append(float(signal[i]))
                    h.append(hash((lon[i], lat[i])))
        for i in range(0, len(walked_lon)):
            hc = hash((walked_lon[i], walked_lat[i]))
            if hc not in h:
                points_lon.append(lon[i])
                points_lat.append(lat[i])
                values.append(float(-100))
                h.append(hash((walked_lon[i], walked_lat[i])))
        grid = griddata((points_lon, points_lat), numpy.array(values), (grid_x, grid_y), method='cubic')
        plt.show()
        plt.imsave('%s.png' % s, grid.T)
        a = (max(walked_lon) - min(walked_lon)) / 1000
        b = 0
        c = 0
        d = (max(walked_lat) - min(walked_lat)) / 1000
        e = min(walked_lon)
        f = min(walked_lat)
        open('%s.pngw' % s, 'w').write('%.16f\n%d\n%d\n%.16f\n%.16f\n%.16f' % (a, b, c, d, e, f))