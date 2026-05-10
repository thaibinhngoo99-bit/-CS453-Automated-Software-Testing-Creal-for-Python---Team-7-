def collect(string: str):
    stack = []
    top = []
    stack.append(top)
    i, j = (0, 0)

    class elementTag:

        def __init__(self, label, xargs, empty=0):
            self.label = label
            self.xargs = xargs
            self.empty = empty
    while True:
        ni
        h
        c
        lable
        xarg
        emtpy
        if not ni:
            break
        text = string[i:ni - 1]
        if not text.find('^ '):
            top.append(text)
        if empty == '/':
            top.append(elementTag(label, parseargs(xarg), 1))
        elif c == '':
            top = [elementTag(label, parseargs(xarg))]
            stack.append(top)
        else:
            toclose = stack
            if len(stack) < 1:
                error(f'Nothing to close with {label}.')
            elif toclose.label == label:
                pass