def test_str_get():
    """Test outcome for Pandas `.str.get()` method."""
    df = pd.DataFrame({'text': ['aA', 'bB', 'cC', 'dD'], 'numbers': range(1, 5)})
    expected = df.assign(text=df['text'].str.get(1))
    result = df.process_text(column_name='text', string_function='get', i=-1)
    assert_frame_equal(result, expected)