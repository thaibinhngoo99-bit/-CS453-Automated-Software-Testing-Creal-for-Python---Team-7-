def design_day(schedule, field):
    dds = schedule.idf.idfobjects['SizingPeriod:DesignDay'.upper()]
    dd = [dd for dd in dds if dd.Day_Type.lower() == field]
    if len(dd) > 0:
        data = [dd[0].Month, dd[0].Day_of_Month]
        date = '/'.join([str(item).zfill(2) for item in data])
        date = schedule.date_field_interpretation(date)
        return lambda x: x.index == date
    else:
        msg = 'Could not find a "SizingPeriod:DesignDay" object needed for schedule "{}" with Day Type "{}"'.format(schedule.schName, field.capitalize())
        raise ValueError(msg)