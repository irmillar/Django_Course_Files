import re

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print(f"Searching for pattern {pat}")
        print(re.findall(pat, phrase))
        print('\n')

test_phrase = "This is a string with numbers 12312 and a symbol #hashtag"

test_pattern = [r"\W+"]

multi_re_find(test_pattern, test_phrase)
