@pytest.mark.xfail(reason='new_column_names is deprecated.')
def test_str_cat_result_is_a_string_and_new_column_names(no_nulls_df):
    """
    Test wrapper for Pandas `.str.cat()` method when the outcome is a string,
    and `new_column_names` is not None.
    """
    result = no_nulls_df.process_text(column_name='text', string_function='cat', new_column_names='combined')
    expected = no_nulls_df.assign(combined=no_nulls_df['text'].str.cat())
    assert_frame_equal(result, expected)