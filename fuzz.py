import parser

def test_function(func, input_value, function_name, file_writer):
    """Helper function to call parser methods and record errors."""
    try:
        if isinstance(input_value, tuple):
            func(*input_value)
        else:
            func(input_value)
    except Exception as e:
        error_message = f"Error in {function_name}: {e}\n"
        print(error_message)
        file_writer.write(error_message)
        return True
    return False

def fuzzValues():
    """Run fuzz testing on selected parser functions."""
    with open('fuzzValues.txt', 'w') as file:
        any_errors = False

        tests = [
            (parser.checkIfWeirdYAML, "some_random_text", "checkIfWeirdYAML"),
            (parser.keyMiner, {"metadata": {"name": "pod-name"}}, "keyMiner"),
            (parser.getKeyRecursively, ({"spec": {"containers": [{"name": "app"}]}}, "name"), "getKeyRecursively"),
            (parser.checkIfValidK8SYaml, "non_yaml_text", "checkIfValidK8SYaml"),
            (parser.getValsFromKey, ({"env": [{"name": "API_KEY", "value": "12345"}]}, "value"), "getValsFromKey")
        ]

        for func, input_val, name in tests:
            if isinstance(input_val, tuple):
                try:
                    func(*input_val)
                except Exception as e:
                    error_message = f"Error in {name}: {e}\n"
                    print(error_message)
                    file.write(error_message)
                    any_errors = True
            else:
                if test_function(func, input_val, name, file):
                    any_errors = True

        if not any_errors:
            success_message = "All parser functions handled fuzz inputs without error.\n"
            print(success_message)
            file.write(success_message)

if __name__ == "__main__":
    fuzzValues()
