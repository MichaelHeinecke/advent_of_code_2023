from advent_of_code_2023.util import get_input_lines


def extract_calibration_code(calibration_document_line: str) -> int:
    code = ""
    for c in calibration_document_line:
        if c.isdigit():
            code += c
            break

    for c in calibration_document_line[::-1]:
        if c.isdigit():
            code += c
            break

    return int(code)


if __name__ == "__main__":
    calibration_document_lines = get_input_lines("calibration_document.txt")
    print(sum([extract_calibration_code(line) for line in calibration_document_lines]))
