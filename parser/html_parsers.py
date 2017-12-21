from parser.generic import GenericParser


DEFAULT_HTML_PROCESSORS_CLASSES = (
    'parser.processors.convert_iframe_to_url',
    'parser.processors.convert_p_to_line_break',
    'parser.processors.convert_html_to_text',
)


class HTMLParser(GenericParser):
    processor_classes = DEFAULT_HTML_PROCESSORS_CLASSES
