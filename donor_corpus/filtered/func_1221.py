def main():
    bottom_toolbar = HTML(' <b>[f]</b> Print "f" <b>[q]</b> Abort  <b>[x]</b> Send Control-C.')
    kb = KeyBindings()
    cancel = [False]

    @kb.add('f')
    def _(event):
        print('You pressed `f`.')

    @kb.add('q')
    def _(event):
        """Quit by setting cancel flag."""
        cancel[0] = True

    @kb.add('x')
    def _(event):
        """Quit by sending SIGINT to the main thread."""
        os.kill(os.getpid(), signal.SIGINT)
    with patch_stdout():
        with ProgressBar(key_bindings=kb, bottom_toolbar=bottom_toolbar) as pb:
            for i in pb(range(800)):
                time.sleep(0.01)
                if cancel[0]:
                    break