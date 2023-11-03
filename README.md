# emojimod

A Python package for emoji string manipulation with skin-tone modifiers.

## Installation

To install the package, use pip:


## Usage

```python
from emojimod import strip_emoji_skin_tone, extract_human_emoji, color_emoji, Fitzpatrick

# Stripping skin-tone modifiers
text = 'Hello 👩🏿'
stripped_text = strip_emoji_skin_tone(text)
print(stripped_text)  # 'Hello 👧'

# Extracting human emoji
text = 'Hello 👨👧'
emoji_list = extract_human_emoji(text)
print(emoji_list)  # ['👨', '👧']

# Coloring emoji
text = 'Hello 👨'
colored_text = color_emoji(text, Fitzpatrick.TYPE_6)
print(colored_text)  # 'Hello 👨🏿'
