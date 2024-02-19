import tempfile
import zipfile
from lxml import etree

target_part_with_word = 'позволяет яркий н выполн'
target_word = 'яркий'
docx_filename = 'word.docx'


def get_word_xml(docx_filename):
    with open(docx_filename, 'rb') as f:
        zip = zipfile.ZipFile(f)
        xml_content = zip.read('word/document.xml')
    return xml_content


def get_xml_tree(xml_string):
    return etree.fromstring(xml_string)


print(get_xml_tree(get_word_xml(docx_filename)))
