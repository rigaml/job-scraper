"""
Utils to manipulate text.
"""
import re
import hashlib


def join_without_overlap(text1: str, text2: str) -> str:
    """
    Joins two text paragraphs, resolving any overlap.

    Args:
        paragraph1 (str): The first text paragraph.
        paragraph2 (str): The second text paragraph.

    Returns:
        str: The joined text with no overlap.
    """
    if not text1:
        return text2
    if not text2:
        return text1

    len1 = len(text1)
    len2 = len(text2)

    if len1 < 1:
        return text2
    if len2 < 1:
        return text1

    for i in range(len1):
        for j in range(len2):
            if i + j < len1 - 1:
                if text1[i+j] != text2[j]:
                    break
            elif i + j == len1 - 1:
                if text1[i+j] != text2[j]:
                    break

                return text1 + text2[j + 1:]
            else:
                break

    return text1 + text2


def generate_hash_key(text: str):
    """
    Generate a short identifier based on the given text.

    Args:
        input (str): The input text to generate the identifier from.

    Returns:
        str: An 8-character string representing the short identifier for the input text.
    """

    text_cleaned = re.sub(r"\s+", "", text)
    text_bytes = text_cleaned.encode("utf-8")
    sha256_hash = hashlib.sha256(text_bytes).hexdigest()
    short_id = sha256_hash[:8]

    return short_id
