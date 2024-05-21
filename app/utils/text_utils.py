import re
import hashlib


def join_without_overlap(paragraph1: str, paragraph2: str) -> str:
    """
    Joins two text paragraphs, resolving any overlap.

    Args:
        paragraph1 (str): The first text paragraph.
        paragraph2 (str): The second text paragraph.

    Returns:
        str: The joined text with no overlap.
    """
    if not paragraph1:
        return paragraph2
    if not paragraph2:
        return paragraph1

    len1 = len(paragraph1)
    len2 = len(paragraph2)

    if len1 < 1:
        return paragraph2
    if len2 < 1:
        return paragraph1

    for i in range(len1):
        for j in range(len2):
            if i + j < len1 - 1:
                if paragraph1[i+j] != paragraph2[j]:
                    break
            elif i + j == len1 - 1:
                if paragraph1[i+j] != paragraph2[j]:
                    break
                else:
                    return paragraph1 + paragraph2[j+1:]
            else:
                break

    return paragraph1 + paragraph2


def generate_hash_key(text: str):
    """
    Generate a short identifier based on the given text.

    Args:
        input (str): The input text to generate the identifier from.

    Returns:
        str: An 8-character string representing the short identifier for the input text.
    """

    text_cleaned = re.sub(r'\s+', '', text)
    text_bytes = text_cleaned.encode('utf-8')
    sha256_hash = hashlib.sha256(text_bytes).hexdigest()
    short_id = sha256_hash[:8]

    return short_id
