import abc

from backend.model.SentenceTokenise import SentenceTokenise
from backend.service.ExtractSentences import extract_sentences
from backend.service.ReadCorpus import read_corpus


class Corpus:
    def __init__(self):
        self.receive_text = ""
        self.input_file = "t1_biology_0_0.txt"
        self.base_train_folder = "../data/source_txt/train/"
        pass

    sentences = SentenceTokenise()

    @abc.abstractmethod
    def getInputText(self):
        # Corpusul curat
        Corpus.receivedText = read_corpus(self.base_train_folder, self.input_file)
        return Corpus.receivedText

    def getSentences(self, text):
        # Lista de propozitii
        self.sentences.listOfSentence = extract_sentences(text)

        return self.sentences.listOfSentence

    def setInputText(self, text):
        pass
