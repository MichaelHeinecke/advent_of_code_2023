from typing import List


def get_calibration_document_lines() -> List[str]:
    with open("calibration_document.txt", "r") as f:
        lines = f.readlines()
    return lines


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
    calibration_document_lines = get_calibration_document_lines()
    print(sum([extract_calibration_code(line) for line in calibration_document_lines]))
