def main():
    input_stack = s.Stack(len(input_data), True)
    [input_stack.push(x) for x in input_data]
    expected_output_stack = s.Stack(len(expected_output_data), True)
    [expected_output_stack.push(x) for x in expected_output_data]
    print('Input: \n' + str(input_stack.prettify()))
    print('Expected: \n' + str(expected_output_stack.prettify()))
    print('Output: \n' + str(sort_stack_1(input_stack)))