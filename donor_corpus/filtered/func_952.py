def test_empty_printer():
    str_printer = StrPrinter()
    assert str_printer.emptyPrinter('foo') == 'foo'
    assert str_printer.emptyPrinter(x * y) == 'x*y'
    assert str_printer.emptyPrinter(32) == '32'