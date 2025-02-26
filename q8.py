def is_valid_url(url):
    """

    :param url: The string to be checked as a URL.
    :return: True if the URL is valid, False otherwise.
    """
    # checks if the URL starts with "http://" or "https://"
    # we use string slicing to compare the beginning of the string.
    if url[:7] != "http://" and url[:8] != "https://": #false is returned if both of these are not found in the link
        return False

    # determines where the domain part should start.
    if url[:7] == "http://":
        start_index = 7
    else:
        start_index = 8

    # check if there is at least one dot after the protocol.
    # The find method returns -1 if the dot is not found.
    if url.find(".", start_index) == -1: #checks if there is a dot in the url, if there is not -1 is returned meaning that flase is returned as -1 is a "false" number
        return False

    # checks that the URL does not contain any spaces.
    for ch in url:
        if ch == " ":
            return False

    # ff all checks pass, the URL is considered valid.
    return True


# Example usage:
print(is_valid_url("https://www.example.com"))  # Expected: True
print(is_valid_url("http://example.com"))  # Expected: True
print(is_valid_url("ftp://example.com"))  # Expected: False (wrong protocol)
print(is_valid_url("http://examplecom"))  # Expected: False (no dot)
print(is_valid_url("http://exa mple.com"))  # Expected: False (contains a space)
