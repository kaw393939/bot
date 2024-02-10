def count_characters(my_string: str) -> int:
    return len(my_string)

def token_count(total_characters: int) -> int:
    # Divide the total characters by 4 to get the base number of tokens
    tokens = total_characters // 4
    # Check if there are any extra characters that would form a partial token
    if total_characters % 4 > 0:
        tokens += 1  # Round up to account for the extra characters
    return tokens