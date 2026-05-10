@pytest.mark.xfail(reason='merge_frame is deprecated.')
def test_output_extractall_merge_frame_is_not_None(test_returns_dataframe):
    """
    Test output when `string_function` is "extractall"
    and `merge_frame` is not None.
    """
    expected_output = test_returns_dataframe['text'].str.extractall('(?P<letter>[ab])?(?P<digit>\\d)')
    expected_output = test_returns_dataframe.join(expected_output.reset_index('match'), how='outer').set_index('match', append=True)
    result = test_returns_dataframe.process_text(column_name='text', merge_frame=True, string_function='extractall', pat='(?P<letter>[ab])?(?P<digit>\\d)')
    assert_frame_equal(result, expected_output)