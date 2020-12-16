import xml.etree.ElementTree as ET
from collections import Counter


def xml_read():
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()
    all_list = []

    descript = root.findall("channel/item/description")
    for descr in descript:
        news = descr.text.split()
        # print(news)

        for words in news:
            if len(words.lower()) >= 6:
                all_list.append(words.lower())

            stat = Counter(all_list)
            sort_stat = stat.most_common(10)
    print("Наиболее частые слова: ", sort_stat)


xml_read()