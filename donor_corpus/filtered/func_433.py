def test_str_cat(no_nulls_df):
    """Test outcome for Pandas `.str.cat()` method."""
    result = no_nulls_df.process_text(column_name='text', string_function='cat', others=['A', 'B', 'C', 'D'])
    expected = no_nulls_df.assign(text=no_nulls_df['text'].str.cat(others=['A', 'B', 'C', 'D']))
    assert_frame_equal(result, expected)