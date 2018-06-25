# This script collects information about each of the rivet analyses.

# Import Beautiful Soup and url library
from bs4 import BeautifulSoup
from urllib.request import urlopen, HTTPError, URLError
import regex as re
import json
# Open list of rivet Analyses from http://rivet.hepforge.org/analyses/
# If the structure of this page changes, this

analyses_list = urlopen("http://rivet.hepforge.org/analyses/")
analyses_html = analyses_list.read()
analyses_list.close()

analyses_soup = BeautifulSoup(analyses_html, "lxml")


id_list = []
info_dict = dict()
for analyses_name in analyses_soup.find_all('a'):
    analysis = str(analyses_name.get('id'))
    if (analysis != 'None'):
        info_dict[analysis] = dict()
        info_dict[analysis]['keywords'] = []

length = len(info_dict)
i = 0

def cleaner(string):
    string = string.replace(' ','_')
    return re.sub(r'\W+', '',string)

for link in info_dict:
    if "CMS" in link or "ATLAS" in link:
        analysis = urlopen("http://rivet.hepforge.org/analyses/" + str(link) + ".html")
        analysis_html = analysis.read()
        soup = BeautifulSoup(analysis_html, "lxml")
        analysis.close()

        # Find information components
        for section in soup.find_all('a'):
            link2 = section.get('href')
            if 'http://inspire-hep.net' in link2:
                try:
                    detail_link = urlopen(str(link2))
                    detail_html = detail_link.read()
                    soup_inner = BeautifulSoup(detail_html, "lxml")
                    detail_link.close()
                    for section_inner in soup_inner.find_all('div',class_ = "detailed_record_info"):
                        key_words = section_inner.find_all('a',{'href': re.compile(r'keyword')})
                        for key_word in key_words:
                            try:
                                kw_to_add = str(key_word).split('>')[1]
                                kw_to_add = kw_to_add.split('<')[0]
                                info_dict[str(link)]['keywords'].append(cleaner(kw_to_add))
                                print("Added: " + str(kw_to_add) + " to " + str(link))
                            except (IndexError,AttributeError,TypeError):
                                print("Failed to serialise " + str(kw_to_add) + " in " + str(link))
                                a = 1;
                except(HTTPError,URLError):
                    print("Error for " + str(link2))

with open('result.json', 'w') as fp:
    json.dump(info_dict, fp)
