def test_str_lower():
    """Test string conversion to lowercase using `.str.lower()`."""
    df = pd.DataFrame({'codes': range(1, 7), 'names': ['Graham Chapman', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones', 'Michael Palin']})
    expected = df.assign(names=df['names'].str.lower())
    result = df.process_text(column_name='names', string_function='lower')
    assert_frame_equal(result, expected)