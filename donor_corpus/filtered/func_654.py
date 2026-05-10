def ListAttributes(self):
    """
        Print Structured Attributes List
        
        Documentation last updated:  March. 24, 2008 - Ruben E. Perez
        """
    print('\n')
    print('Attributes List of: ' + repr(self.__dict__['name']) + ' - ' + self.__class__.__name__ + ' Instance\n')
    self_keys = self.__dict__.keys()
    self_keys.sort()
    for key in self_keys:
        if key != 'name':
            print(str(key) + ' : ' + repr(self.__dict__[key]))
    print('\n')