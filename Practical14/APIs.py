import xml.sax
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ''
        self.namespace = ''
        self.ontology_counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
    def startElement(self, name, attributes):
        self.current_element = name
    def characters(self, content):
        if self.current_element == 'namespace':
            self.namespace += content
            if self.namespace == 'molecular_function':
                self.ontology_counts['molecular_function'] += 1
            elif self.namespace == 'biological_process':
                self.ontology_counts['biological_process'] += 1
            elif self.namespace == 'cellular_component':
                self.ontology_counts['cellular_component'] += 1
    def endElement(self, name):
        if self.current_element == 'namespace':
            self.current_element=''
            self.namespace=''
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)
handler = GOHandler()
parser.setContentHandler(handler)

import datetime
start_time = datetime.datetime.now()
parser.parse('go_obo.xml')
end_time = datetime.datetime.now()
parsing_time = end_time - start_time

print('SAX:')
print("The frequency of GO terms in three ontologies:")
for ontology, count in handler.ontology_counts.items():
    print(f"{ontology}: {count}")
print(f"Time used: {parsing_time} seconds")

import matplotlib.pyplot as plt
ontologies = list(handler.ontology_counts.keys())
counts = list(handler.ontology_counts.values())
plt.bar(ontologies, counts, color='skyblue')
plt.xlabel('Ontologies',fontsize=10)
plt.ylabel('Number of Terms',fontsize=10)
plt.title('Occurrences of Each Ontology in go_obo.xml (SAX)',fontsize=15)
for i, count in enumerate(counts):
    plt.text(i, count, str(count), ha='center', va='bottom')
plt.show()
plt.clf()



import xml.dom.minidom
start_time = datetime.datetime.now()
dom_tree = xml.dom.minidom.parse('go_obo.xml')
end_time = datetime.datetime.now()
parsing_time = end_time - start_time

root_element = dom_tree.documentElement
ontology_counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
terms = root_element.getElementsByTagName('term')
for term in terms:
    namespace_elements = term.getElementsByTagName('namespace')
    if namespace_elements:
        namespace = namespace_elements[0].childNodes[0].data
        if namespace in ontology_counts:
            ontology_counts[namespace] += 1

print('DOM:')
print("The frequency of GO terms in three ontologies:")
for ontology, count in ontology_counts.items():
    print(f"{ontology}: {count}")
print(f"Time used: {parsing_time} seconds")

ontologies = list(ontology_counts.keys())
counts = list(ontology_counts.values())
plt.bar(ontologies, counts, color='mediumorchid')
plt.xlabel('Ontologies',fontsize=10)
plt.ylabel('Number of Terms',fontsize=10)
plt.title('Occurrences of Each Ontology in go_obo.xml (DOM)',fontsize=15)
for i, count in enumerate(counts):
    plt.text(i, count, str(count), ha='center', va='bottom')
plt.show()
plt.clf()

print('SAX ran fastest.')
