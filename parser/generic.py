from pydoc import locate


class GenericParser:
    processor_classes = []
    _data = None

    def __init__(self, text=None, processor_classes=None):
        if not text:
            raise TypeError("data parameter is required")

        if processor_classes:
            self.processor_classes = processor_classes

        if not self.processor_classes:
            raise Exception("you must to provide middleware_classes")

        self._data = self.perform_parse(text)

    def perform_parse(self, text):
        for processor in self.processor_classes:
            processor = locate(processor)
            text = processor(text)
        return text

    @property
    def data(self):
        return self._data



