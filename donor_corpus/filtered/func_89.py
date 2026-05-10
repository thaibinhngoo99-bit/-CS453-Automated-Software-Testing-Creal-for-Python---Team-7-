def sort_stack_1(stack):
    result = s.Stack(stack.capacity, True)
    while not stack.is_empty():
        value = stack.pop()
        if not result.is_empty() and value >= int(result.peek()):
            result.push(value)
        else:
            while not result.is_empty() and value < int(result.peek()):
                stack.push(result.pop())
            result.push(value)
    return result.prettify()