from emojimod import strip_emoji_skin_tone, extract_human_emoji, color_emoji, Fitzpatrick

# Stripping skin-tone modifiers
text = 'Hello 👩🏿'
stripped_text = strip_emoji_skin_tone(text)
print(stripped_text)

# Extracting human emoji
text = 'Hello 👨👩🏿'
emoji_list = extract_human_emoji(text)
print(emoji_list)

# Coloring emoji
text = 'Hello 👨👧'
colored_text = color_emoji(text, Fitzpatrick.TYPE_1_2)
print(colored_text)
