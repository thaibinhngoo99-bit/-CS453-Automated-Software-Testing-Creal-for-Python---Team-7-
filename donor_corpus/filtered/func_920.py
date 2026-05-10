def test_printmethod():

    class R(Abs):

        def _sympystr(self, printer):
            return 'foo(%s)' % printer._print(self.args[0])
    assert sstr(R(x)) == 'foo(x)'

    class R(Abs):

        def _sympystr(self, printer):
            return 'foo'
    assert sstr(R(x)) == 'foo'