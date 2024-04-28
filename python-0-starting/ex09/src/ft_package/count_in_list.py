def count_in_list(src_list: list, q_item: any) -> int:
    """Count the number of occurences of q_item in src_list"""
    count = 0
    for item in src_list:
        if item == q_item:
            count += 1
    return count
