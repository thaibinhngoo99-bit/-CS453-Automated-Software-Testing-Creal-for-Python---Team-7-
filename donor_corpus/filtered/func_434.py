def test_str_cat_result_is_a_string(no_nulls_df):
    """
    Test wrapper for Pandas `.str.cat()` method
    when the outcome is a string.
    """
    result = no_nulls_df.process_text(column_name='text', string_function='cat')
    expected = no_nulls_df.assign(text=no_nulls_df['text'].str.cat())
    assert_frame_equal(result, expected)