from advent_of_code_2023.day1.trebuchet import extract_calibration_code


def test_only_one_digit_in_calibration_document_line():
    line = "treb7uchet"
    expected_result = 77

    actual_result = extract_calibration_code(line)

    assert actual_result == expected_result


def test_two_digits_in_calibration_document_line():
    line = "1abc2"
    expected_result = 12

    actual_result = extract_calibration_code(line)

    assert actual_result == expected_result


def test_more_than_two_digits_in_calibration_document_line():
    line = "a1b2c3d4e5f"
    expected_result = 15

    actual_result = extract_calibration_code(line)

    assert actual_result == expected_result
