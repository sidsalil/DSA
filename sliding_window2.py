s = "abbcab"
char_set = set()
left = 0
for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
    char_set.add(s[right])
print(f'longest substring without repeating characters: {char_set}')