def main():
    locale.setlocale(locale.LC_ALL, '')
    lang = locale.getdefaultlocale()[0]
    if lang:
        global _translations
        localedir = filesystem2unicode(openslides.__file__)
        localedir = os.path.dirname(localedir)
        localedir = os.path.join(localedir, 'locale')
        _translations = gettext.translation('django', localedir, [lang], fallback=True)
    app = OpenslidesApp()
    app.MainLoop()