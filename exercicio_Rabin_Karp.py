from pandas import read_csv


def rabin_karp(text, pattern):
    """
    Rabin-Karp algorithm for searching for all occurrences of a pattern in a text.
    Returns a list of lines containing the pattern in the text, or an empty list if the pattern is not found.
    Time complexity: O(n + p)
    Space complexity: O(1)
    """
    pattern = str(pattern).lower()
    occurrences = []

    for line in text:
        line_str = str(line).lower()
        pattern_hash = hash_pattern(pattern)
        line_hash = hash_text(line_str, 0, len(pattern))

        for i in range(len(line_str) - len(pattern) + 1):
            if pattern_hash == line_hash:
                if line_str[i:i + len(pattern)] == pattern:
                    occurrences.append(line)
                    break
            if i < len(line_str) - len(pattern):
                line_hash = recalculate_hash(line_hash, line_str, i, len(pattern))
    
    return occurrences

def recalculate_hash(old_hash, text, start, pattern_length):
    """
    Recalculates the hash value for the next window using the hash of the previous window.
    Time complexity: O(1)
    Space complexity: O(1)
    """
    old_char = ord(text[start]) - ord('a') + 1
    new_char = ord(text[start + pattern_length]) - ord('a') + 1
    new_hash = old_hash - old_char * (26 ** (pattern_length - 1))
    new_hash = new_hash * 26 + new_char
    return new_hash

def hash_pattern(pattern):
    """
    Returns the hash value of the pattern.
    Time complexity: O(n)
    Space complexity: O(1)
    """
    pattern = str(pattern).lower()
    pattern_hash = 0
    for i in range(len(pattern)):
        pattern_hash = pattern_hash * 26 + (ord(pattern[i]) - ord('a') + 1)
    return pattern_hash

def hash_text(text, start, length):
    """
    Returns the hash value of the text for a given substring.
    Time complexity: O(n)
    Space complexity: O(1)
    """
    text_hash = 0
    for i in range(start, start + length):
        text_hash = text_hash * 26 + (ord(text[i]) - ord('a') + 1)
    return text_hash


def main():
    file = "" #Set any csv file to search a key
    text = read_csv(file, sep=";")
    pattern = "ZSH_5262631"
    occurrences = rabin_karp(text.values.tolist(), pattern)

    if occurrences:
        print(f"Matches com a tag {pattern}:")
        for line in occurrences:
            print(line)
    else:
        print(f"O padrão '{pattern}' não foi encontrado no texto.")

if __name__ == '__main__':
    main()
