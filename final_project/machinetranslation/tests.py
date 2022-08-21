import unittest
from translator import frenchToEnglish, englishToFrench

class TestF2E(unittest.TestCase): 
    def test(self): 
        self.assertEqual(englishToFrench(None), None) # test null
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # test Hello > Bonjour
        
class TestE2F(unittest.TestCase): 
    def test(self): 
        self.assertEqual(frenchToEnglish(None), None) # test null
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test Bonjour > Hello
        
unittest.main()