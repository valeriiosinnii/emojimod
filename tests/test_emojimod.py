import unittest
from emojimod import strip_emoji_skin_tone, extract_human_emoji, color_emoji, Fitzpatrick


class TestEmojimod(unittest.TestCase):
    def test_strip_emoji_skin_tone(self):
        self.assertEqual(strip_emoji_skin_tone('Hello 👋🏻'), 'Hello 👋')
        self.assertEqual(strip_emoji_skin_tone('Hello 👋🏿'), 'Hello 👋')
        self.assertEqual(strip_emoji_skin_tone('Hello 👋'), 'Hello 👋')

    def test_extract_human_emoji(self):
        self.assertEqual(extract_human_emoji('Hello 👋🏻'), ['👋🏻'])
        self.assertEqual(extract_human_emoji('Hello 👋🏿'), ['👋🏿'])
        self.assertEqual(extract_human_emoji('Hello 👋'), ['👋'])

    def test_color_emoji(self):
        self.assertEqual(color_emoji('Hello 👧', Fitzpatrick.TYPE_1_2), 'Hello 👧🏻')
        self.assertEqual(color_emoji('Hello 👧', Fitzpatrick.TYPE_6), 'Hello 👧🏿')
        with self.assertRaises(ValueError):
            color_emoji('Hello 👧', 'InvalidType')


if __name__ == '__main__':
    unittest.main()
