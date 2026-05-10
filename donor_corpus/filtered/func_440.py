@pytest.mark.xfail(reason='merge_frame is deprecated.')
def test_return_dataframe_merge_is_not_None_new_column_names_is_a_list(returns_frame_1):
    """
    Test that the dataframe returned when `merge_frame` is not None
    is a merger of the original dataframe, and the dataframe
    generated from the text processing. Also, the `new_column_names`
    is a list.
    """
    expected_output = pd.concat([returns_frame_1, returns_frame_1['ticker'].str.split(' ', expand=True).set_axis(['header1', 'header2', 'header3'], axis='columns')], axis='columns')
    result = returns_frame_1.process_text(column_name='ticker', new_column_names=['header1', 'header2', 'header3'], merge_frame=True, string_function='split', expand=True, pat=' ')
    assert_frame_equal(result, expected_output)