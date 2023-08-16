def parse_transactions(lines, start_keyword, end_keyword):
    """
    Extract relevant lines for a given section of the report,
    starting from the line containing start_keyword until the line containing end_keyword.
    """
    data = []
    capture = False
    for line in lines:
        if start_keyword in line:
            capture = True
            continue
        if end_keyword in line:
            capture = False
        if capture:
            # Check if the line is not empty and does not contain only spaces
            if line.strip():
                data.append(line.strip())
    return data