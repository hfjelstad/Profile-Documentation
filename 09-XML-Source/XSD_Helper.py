"""
@author hakon.fjelstad@entur.org
"""


import xmlschema
schema = xmlschema.XMLSchema("09-XML-Source/XSD/NeTEx_publication-NoConstraint.xsd")
def strip_namespace(tag):
    return tag.split('}', 1)[-1] if '}' in tag else tag

def XSD_annotation(Element):
    namespaces = {
    '': 'http://www.netex.org.uk/netex',
    'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema'
    }
    XSD_annotation = ''
    # Load the XSD
    
    for x in schema.findall(Element, namespaces):
        if strip_namespace(x.tag) == Element:
            for y in x.annotation.documentation:
                XSD_annotation = y.text
            #print(strip_namespace(x.tag))
        #print(x.annotation.documentation.text)
    Clean_annotation = ' '.join(XSD_annotation.split())
    return(Clean_annotation)
if __name__ == "__main__":
    print(XSD_annotation('DatedServiceJourney'))