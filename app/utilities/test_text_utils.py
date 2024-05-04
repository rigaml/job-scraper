import pytest
import unittest.mock as mock

import utilities.text_utils as text_utils

@pytest.mark.parametrize("paragraph1, paragraph2, expected", 
                         [
                          # 1st string is None
                          (None, "paragraph2", "paragraph2"), 
                          # 2nd string is None
                          ("paragraph1", None, "paragraph1"), 
                          # 1st string empty
                          ("", "paragraph2", "paragraph2"), 
                          # 2nd string empty
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
                         ])
def test_join_without_overlap(paragraph1, paragraph2, expected):

    result= text_utils.join_without_overlap(paragraph1, paragraph2)

    assert result == expected


    

