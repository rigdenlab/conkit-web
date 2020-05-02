from loaders import DatasetReference
from parsers import ConservationFormats
from loaders.membranetopologyloader import MembraneTopologyLoader


class ConservationLoader(MembraneTopologyLoader):
    """Class with methods and data structures to store all the information related with conservation scores obtained
    for a given sequence and its validity"""

    def __init__(self):
        super(ConservationLoader, self).__init__()
        self.prediction = None

    @property
    def datatype(self):
        return DatasetReference.CONSERVATION

    @property
    def parser_formats(self):
        return ConservationFormats