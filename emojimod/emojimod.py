from .fitzpatrick import Fitzpatrick


def strip_emoji_skin_tone(input_str):
    return re.sub('[\U0001F3FB-\U0001F3FF]', '', input_str)


import re

def extract_human_emoji(input_str):
    human_emoji_pattern = '[\U0001F468-\U0001F469\U0001F474-\U0001F475\U0001F9B0-\U0001F9B3\U0001F9D1\U0001F44B][\U0001F3FB-\U0001F3FF]?'
    return re.findall(human_emoji_pattern, input_str)



def color_emoji(input_str, skin_tone):
    if not isinstance(skin_tone, Fitzpatrick):
        raise ValueError('Skin tone must be a value from the Fitzpatrick Enum.')

    return re.sub('([\U0001F466-\U0001F469])', r'\1' + skin_tone.value, input_str)
