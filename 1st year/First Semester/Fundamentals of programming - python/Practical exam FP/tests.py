import unittest
from controller import Controller
from repo import Repository

class AllTests(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAddProposition(self):
        repo = Repository("sentences.txt")
        controller = Controller(repo)

        assert controller.addProp("a") == False
        assert controller.addProp("anna has apples") == False
        assert controller.addProp("Unu doi trei") == True

        assert repo.verifyPropositionFromText("a") == False
        assert repo.verifyPropositionFromText("anna has apples") == False
        assert repo.verifyPropositionFromText("Unu doi trei") == False
        assert repo.verifyPropositionFromText("Unu doi trei patru") == True

    def testGetLettersEnd(self):
        repo = Repository("sentences.txt")
        controller = Controller(repo)
        assert controller.GetLettersEnd("") == False
        assert controller.GetLettersEnd("doi patru") == ['d', 'i', 'p', 'u']

if __name__ == '__main__':
    unittest.main()