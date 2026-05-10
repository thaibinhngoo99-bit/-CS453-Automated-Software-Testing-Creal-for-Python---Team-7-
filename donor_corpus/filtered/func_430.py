@pytest.mark.xfail(reason='string_function must be present.')
def test_string_function_is_None(process_test_df):
    """Test that dataframe is returned if string_function is None."""
    result = process_test_df.process_text(column_name='text')
    assert_frame_equal(result, process_test_df)