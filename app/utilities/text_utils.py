def join_without_overlap(paragraph1: str, paragraph2: str) -> str:
    """
    Joins two text paragraphs, resolving any overlap.
    
    Args:
        paragraph1 (str): The first text paragraph.
        paragraph2 (str): The second text paragraph.
    
    Returns:
        str: The joined text with no overlap.
    """
    if paragraph1 is None:
        return paragraph2
    if paragraph2 is None: 
        return paragraph1
    
    len1= len(paragraph1)
    len2= len(paragraph2)
    
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
    

