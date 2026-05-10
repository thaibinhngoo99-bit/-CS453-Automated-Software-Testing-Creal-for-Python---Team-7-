@pytest.mark.xfail(reason='merge_frame is deprecated.')
def test_return_dataframe_merge_is_not_None(returns_frame_1):
    """
    Test that the dataframe returned when `merge_frame` is not None
    is a merger of the original dataframe, and the dataframe
    generated from the text processing.
    """
    expected_output = pd.concat([returns_frame_1, returns_frame_1['ticker'].str.split(' ', expand=True).add_prefix('new_')], axis='columns')
    result = returns_frame_1.process_text(column_name='ticker', new_column_names='new_', merge_frame=True, string_function='split', expand=True, pat=' ')
    assert_frame_equal(result, expected_output)