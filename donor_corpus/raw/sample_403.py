class MenuItem(object):
    TEXT_NAME = 'name'
    TEXT_URL = 'url_name'
    TEXT_SUBMENU = 'submenu'

    def __init__(self, name, url=None, *args):
        super(MenuItem, self).__init__()
        self.name = name
        self.url = url
        self.url_args = args
        self.sub_menu = []

    def add_sub_menu_item(self, name, url):
        item = {self.TEXT_NAME: name, self.TEXT_URL: url}
        self.sub_menu.append(item)

    def __getitem__(self, key):
        return self[key]

    def to_text(self):
        output = {}
        output[self.TEXT_NAME] = self.name
        if self.url:
            output[self.TEXT_URL] = self.url
        if self.sub_menu:
            output[self.TEXT_SUBMENU] = self.sub_menu

        return output


class Nav:
    def __init__(self, *args, **kwargs):
        self.menu = []

    def add_menu(self, menu):
        self.menu.append(menu)

    def get_menu_list(self):
        output = []
        for x in self.menu:
            output.append(x.to_text())

        return output
