def setup(app):
    app.add_crossref_type(directivename='setting', rolename='setting', indextemplate='pair: %s; setting')
    app.add_crossref_type(directivename='templatetag', rolename='ttag', indextemplate='pair: %s; template tag')
    app.add_crossref_type(directivename='templatefilter', rolename='tfilter', indextemplate='pair: %s; template filter')
    app.add_crossref_type(directivename='router', rolename='router', indextemplate='pair: %s; router')
    app.add_config_value('rapidsms_next_version', '0.0', True)
    app.add_directive('versionadded', VersionDirective)
    app.add_directive('versionchanged', VersionDirective)