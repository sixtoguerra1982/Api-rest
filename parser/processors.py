from bs4 import BeautifulSoup
import re


def convert_html_to_text(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()


def convert_p_to_line_break(text):
    founds = re.findall("<p[\s\n\r\t_\w-]*>([\w\s@#%$.,;:\"\']+)</p>", text)
    for found in founds:
        regex = "<p[\s\n\r\t_\w-]*>%s</p>" % found
        text = re.sub(regex, "%s\n\r\n\r" % found, text)
    return text


def convert_iframe_to_url(text):
    founds = re.findall("<iframe[\w\s=\"-]*src=\"([:\w/.-]+)\"[\w\s=\"-]+></iframe>", text)
    for found in founds:
        regex = "<iframe[\w\s=\"-]*src=\"%s\"[\w\s=\"-]+></iframe>" % found
        text = re.sub(regex, "%s\n\r" % found, text)
    return text
