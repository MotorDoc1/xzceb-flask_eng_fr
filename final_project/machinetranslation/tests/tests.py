#Test translation
import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        #test null then test to see if Hello translates to Bonjour
        self.assertEqual(englishToFrench(''), 'Input is null')
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        #test null then test to see if Bonjour translates to Hello
        self.assertEqual(frenchToEnglish(''), 'Input is null')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()