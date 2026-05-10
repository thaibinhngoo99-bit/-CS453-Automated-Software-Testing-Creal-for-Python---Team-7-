@pytest.mark.xfail(reason='merge_frame is deprecated.')
def test_return_dataframe_merge_is_None(returns_frame_1):
    """
    Test that the dataframe returned when `merge_frame` is None
    is the result of the text processing, and is not merged to
    the original dataframe.
    """
    expected_output = returns_frame_1['ticker'].str.split(' ', expand=True)
    result = returns_frame_1.process_text(column_name='ticker', string_function='split', expand=True, pat=' ')
    assert_frame_equal(result, expected_output)