import re


def len_words(text):
    """
        Returns a dictionary that maps each unique lowercase word in the given string to its length.
        Non-alphabetic characters and whitespaces are removed from the input string before processing.

        :param text: The string to process.
        :return: A dictionary with lowercase words as keys and their lengths as values.
        """
    # Filter out any non-alphabetic characters and whitespaces using a regular expression pattern
    clean_text = "".join(ch for ch in text if re.match("[a-zA-z\\s]", ch))

    return {word.lower(): len(word) for line in clean_text.split("\n") for word in line.split(" ")}