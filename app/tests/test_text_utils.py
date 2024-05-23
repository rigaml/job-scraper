import pytest
import utils.text_utils as text_utils


@pytest.mark.parametrize(
    "paragraph1, paragraph2, expected",
    [
        # 1st string is Empty
        ("", "paragraph2", "paragraph2"),
        # 2nd string is Empty
        ("paragraph1", "", "paragraph1"),
        # Not overlap
        ("paragraph1", "paragraph2", "paragraph1paragraph2"),
        # Strings same length overlap full
        ("paragraph1", "paragraph1", "paragraph1"),
        # 2nd string shorter overlap full 2nd string
        ("paragraph1", "graph1", "paragraph1"),
        # 2nd string only 1 character overlap
        ("graph1", "1", "graph1"),
        # 2nd string only 1 character no overlap
        ("graph1", "a", "graph1a"),
        # 2nd string shorter overlap full 1st string
        ("graph1", "graph1 and para", "graph1 and para"),
        # Partial overlap
        ("graph1", "h1 and para", "graph1 and para"),
    ],
)
def test_join_without_overlap(paragraph1: str, paragraph2: str, expected: str):

    result = text_utils.join_without_overlap(paragraph1, paragraph2)

    assert result == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        # String empty
        ("", "e3b0c442"),
        # String with only spaces have same hash than empty
        ("   ", "e3b0c442"),
        # Only one letter
        ("a", "ca978112"),
        # Some word
        ("paragraph1", "83c22e57"),
        # Different hash when change last letter
        ("paragraph2", "e5a6ec4e"),
        # 2 words
        ("1paragraph1 paragraph1", "80e8e06b"),
        # 2 words removing the space have same hash
        ("1paragraph1paragraph1", "80e8e06b"),
        # Same as previous changing first letter returns different reference than previous
        ("2paragraph1paragraph1", "fc9cddea"),
        # Long word
        ("graph1 " * 100, "344f04d4"),
    ],
)
def test_generate_ref(text: str, expected: str):

    result = text_utils.generate_hash_key(text)

    assert result == expected
