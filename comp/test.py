from main import run_code
from data.main import FunctionTable, Output


def test(test_name, test_file, expected_result):

    print("--------------------------")
    print(f"{test_name}\n")
    print("Result:")

    run_code("tests/" + test_file)
    result = Output.get()
    passed = True

    try:
        assert result == expected_result
    except:
        passed = False

    print("\nExpected result:")
    print(expected_result)

    print(f"Passed: {passed} \n")

    FunctionTable.reset()
    Output.reset()

    return passed


if __name__ == "__main__":

    passed = 0
    failed = 0

    test_a = ("Test A", "test_a.carbon", "7\n3\n7\n")
    test_b = ("Test B", "test_b.carbon", "oi\n, tudo bem?\noi, tudo bem?\n")
    test_c = ("Test C", "test_c.carbon", "99\n")
    tests_args = [test_a, test_b, test_c]
    for args in tests_args:
        passed += 1 if test(*args) else passed

    print("--------------------------")
    print("Summary: \n")
    print(f"Passed in {passed} out of {len(tests_args)} tests\n")
