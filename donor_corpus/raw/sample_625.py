import educative.course1.stacks_queues.stack as s

input_data = [23, 60, 12, 42, 4, 97, 2]
expected_output_data = [2, 4, 12, 23, 42, 60, 97]


# This solution uses a second stack
# 1. until input stack is not empty, we pop the top value and compare it
#    with the top value of the second stack
# 2. if value > top of stack 2, we insert the popped value in stack 2
# 3. else while popped value < top of stack 2, we keep pushing top of stack 2 to stack 1
# 4. finally when stack 2 is empty we push the popped value and start over again
# 5. The output will be a sorted stack
# ---------------------------------------------
# NOTE - This can also be done by recursion ---
# ---------------------------------------------
def sort_stack_1(stack):
    result = s.Stack(stack.capacity, True) # suppress_printing = True

    while not stack.is_empty():
        value = stack.pop()
        if not result.is_empty() and value >= int(result.peek()):
            result.push(value)
        else:
            while not result.is_empty() and value < int(result.peek()):
                stack.push(result.pop())

            result.push(value)

    return result.prettify()


def main():
    input_stack = s.Stack(len(input_data), True) # suppress_printing = True
    [input_stack.push(x) for x in input_data]

    expected_output_stack = s.Stack(len(expected_output_data), True) # suppress_printing = True
    [expected_output_stack.push(x) for x in expected_output_data]

    print("Input: \n" + str(input_stack.prettify()))
    print("Expected: \n" + str(expected_output_stack.prettify()))
    print("Output: \n" + str(sort_stack_1(input_stack)))


if __name__ == '__main__':
    main()
