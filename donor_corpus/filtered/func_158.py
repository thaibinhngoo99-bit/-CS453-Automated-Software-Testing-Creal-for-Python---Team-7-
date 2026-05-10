def combine_schema(borough_name):
    borough_name = borough_name.lower()
    neighborhood_data = ''
    with open('../scraped_data/borough_schema/' + borough_name + '.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for zipCodes in range(len(data[borough_name])):
            with open('../scraped_data/neighborhood_schema/' + borough_name + '.json', 'r+', encoding='utf-8') as zipcode_file:
                neighborhood_data = json.load(zipcode_file)
                neighborhood_data[borough_name][zipCodes]['zipCodes'] = data[borough_name][zipCodes]['zipCodes']
                print(neighborhood_data)
                with open('../scraped_data/neighborhood_schema/' + borough_name + '.json', 'w', encoding='utf-8') as combined_file:
                    json.dump(neighborhood_data, combined_file, sort_keys=True, indent='\t', separators=(',', ': '))