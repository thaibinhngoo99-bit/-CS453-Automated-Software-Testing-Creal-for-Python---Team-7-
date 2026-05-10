@pytest.mark.xfail(reason='new_column_names is deprecated.')
def test_new_column_names(process_test_df):
    """
    Test that a new column name is created when
    `new_column_name` is not None.
    """
    result = process_test_df.process_text(column_name='text', new_column_names='new_text', string_function='slice', start=2)
    expected = process_test_df.assign(new_text=process_test_df['text'].str.slice(start=2))
    assert_frame_equal(result, expected)