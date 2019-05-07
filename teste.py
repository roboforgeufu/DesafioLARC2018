
"""
    Remove repeating letters.
"""
# pylint: disable=C0103

import re

class RepeatReplacer(object):  # pylint: disable = R0903
    """
        Class implementation
    """
    def __init__(self):
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        self.repl = r'\1\2\3'

    def replace(self, word):
        """
            Replace repeating letters.
        """
        repl_word = self.repeat_regexp.sub(self.repl, word)

        if repl_word != word:
            return self.replace(repl_word)
        return repl_word

# Replacing
replacer = RepeatReplacer()
replacer.replace()
