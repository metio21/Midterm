def count_pattern(text):
    """
    :param text: The string to search in.
    :return: The number of pattern occurrences found.
    """
    count = 0
    # Loop through every character in the text.
    for i in range(len(text)):
        if text[i] == 'C':
            pos = i + 1
            while True:
                idx = text.find("jeb", pos)
                if idx == -1:
                    break
                candidate = text[i:idx + 3]
                valid = True
                for char in candidate[1:-3]:
                    if not char.isalpha():
                        valid = False
                        break
                if valid:
                    count += 1
                pos = idx + 1
    return count


# Example usage and explanation:
text = "Cxxxjeb Cyyyjeb Czzzjeb Cfsdlkjhflsdkjhjeb."
print(count_pattern(text))
