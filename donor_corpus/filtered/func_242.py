def is_valid_minnesota_zip(zip: str):
    list_of_dicts_of_minnesota_zips = zipcodes.filter_by(state='MN')
    list_of_minnesota_zips = [d['zip_code'] for d in list_of_dicts_of_minnesota_zips]
    if len(zip) > 10:
        return False
    elif type(zip) != str:
        return False
    elif zip in list_of_minnesota_zips:
        return True
    else:
        return False