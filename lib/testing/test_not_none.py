from not_none_functions import return_not_none

def test_return_not_none():
    '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
    result = return_not_none()
    print(f"Return value: {result}")  # Debugging line to print the value
    assert result is not None
