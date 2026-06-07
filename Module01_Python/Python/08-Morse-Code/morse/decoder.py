# $CHALLENGIFY_BEGIN
"""
This module provides functions to decode Morse code into plain text.

Functions:
- decode(morse_text): Decodes a given Morse code string into plain text, separating words by spaces.
- decode_word(morse_word): Decodes a single Morse code word into plain text.
"""
from morse.mapping import MORSE
from morse.encoder import encode


# Create a reverse lookup dictionary for decoding
MORSE_REVERSE = {value: key for key, value in MORSE.items()}


def decode(morse_text):
    """
    Decodes the given Morse code into plain text.
    Words are separated by a pipe (|) and letters by a space.
    """
    return " ".join(decode_word(morse_word) for morse_word in morse_text.split("|"))


def decode_word(morse_word):
    """
    Decodes a single Morse code word into plain text.
    Letters are separated by a space.
    """
    return "".join(MORSE_REVERSE[morse_letter] for morse_letter in morse_word.split())
# $CHALLENGIFY_END


if __name__ == "__main__":
    # Example usage for one word
    # $CHALLENGIFY_BEGIN
    EXAMPLE = "abc"
    EXAMPLE_MORSE = encode(EXAMPLE)
    DECODED_TEXT = decode_word(EXAMPLE_MORSE)
    print(f"Encoded word '{EXAMPLE}' into '{EXAMPLE_MORSE}'")
    print(f"    and decoded back into plain text: '{DECODED_TEXT}'")
    # $CHALLENGIFY_END

    # Example usage for one sentence
    # $CHALLENGIFY_BEGIN
    EXAMPLE = "abc ABC"
    EXAMPLE_MORSE = encode(EXAMPLE)
    DECODED_TEXT = decode(EXAMPLE_MORSE)
    print(f"Encoded word '{EXAMPLE}' into '{EXAMPLE_MORSE}'")
    print(f"    and decoded back into plain text: '{DECODED_TEXT}'")
    # $CHALLENGIFY_END
