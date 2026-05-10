def test_str_split(process_test_df):
    """Test wrapper for Pandas `str.split()` method."""
    expected = process_test_df.assign(text=process_test_df['text'].str.split('_'))
    result = process_test_df.process_text(column_name='text', string_function='split', pat='_')
    assert_frame_equal(result, expected)