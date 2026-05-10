def check_dataset_description(bids_dir, bids_version='1.4.0', ds_type='raw'):
    if not os.path.exists(bids_dir):
        os.makedirs(bids_dir)
    ds_desc = os.path.join(bids_dir, 'dataset_description.json')
    if not os.path.exists(ds_desc):
        js = {'Name': 'Made by YAXIL', 'BIDSVersion': bids_version, 'DatasetType': ds_type}
        with open(ds_desc, 'w') as fo:
            fo.write(json.dumps(js))