"""
@author hakon.fjelstad@entur.org
"""
import glob
from zipfile import ZipFile
import xml.etree.ElementTree as ET
from XSD_Helper import XSD_annotation as XA

def netex_unzip():
    for file in glob.glob("09-XML-Source/NAP Examples/"+"/*.zip"):
        with ZipFile(file, "r") as unzip:
            print("Processing: " + file)
            unzip.extractall("09-XML-Source/NAP Examples/Cache/")

# Function to remove namespace from tag
def strip_namespace(tag):
    return tag.split('}', 1)[-1] if '}' in tag else tag

def extractor(File):
    objects = []
    objects_dict = {}
    tree = ET.parse(File)
    root = tree.getroot()
    for c in root.iter():
        if c.attrib and "Frame" not in c.tag:
            for x in c.attrib:
                if x == 'id':
                    if strip_namespace(c.tag) not in objects:
                        objects.append(strip_namespace(c.tag))
        
        if c.attrib and "Frame" in c.tag:
            if strip_namespace(c.tag) not in objects:
                        objects.append(strip_namespace(c.tag))
            #print(strip_namespace(c.tag))
            #for gc in c:
            #    print(strip_namespace(gc.tag))
        
    #print(objects)
    for all in objects:
        attributes = []
        elements = []
        reference = []
        
        listDict = {}
        for x in root.iter():
            
            if strip_namespace(x.tag) == all:
                for y in x:
                    yStripped = strip_namespace(y.tag)
                    if yStripped != all:
                        lists = []
                        subElements = []
                        if not y.attrib:
                            
                            try:
                                for sub in y:
                                    
                                    lists.append(yStripped)
                                    if 'gis' in sub.tag:
                                        gisSubElement = 'gis:' + strip_namespace(sub.tag)
                                        if gisSubElement not in subElements:
                                            subElements.append('gis:' + strip_namespace(sub.tag))
                                    elif strip_namespace(sub.tag) not in subElements:
                                        subElements.append(strip_namespace(sub.tag))
                                    
                                    listDict[yStripped] = subElements 
                            except:
                                pass


                        if 'ref' in strip_namespace(y.attrib) and yStripped not in reference:
                            reference.append(yStripped)
                        
                        if y.text:
                            if 'gis' in y.tag:
                                gisElement = 'gis:' + yStripped
                                if gisElement not in elements:
                                    elements.append('gis:' + yStripped)
                            elif yStripped not in elements and not lists and not subElements and not reference and not y.attrib:
                                elements.append(yStripped)
                    
                    for a in x.attrib:
                        if strip_namespace(a) not in attributes:
                            attributes.append(strip_namespace(a))
    
        objects_dict[all] = {}
        objects_dict[all]['Attribute'] = attributes 
        objects_dict[all]['Element'] = elements
        objects_dict[all]['Reference'] = reference
        objects_dict[all]['List'] = listDict
    return(objects_dict)
                    
if __name__ == "__main__":
    netex_unzip()
    profileDict = {}
    cacheDict = {}
    for file in glob.glob("09-XML-Source/NAP Examples/Cache/"+"/*.xml"):
        print("Processing: " + file)
        cacheDict.update(extractor(file))
        for cD in cacheDict:
            if cD not in profileDict:
                profileDict[cD] = {}
            for cD1 in cacheDict[cD]:
                if cD1 not in profileDict[cD]:
                    profileDict[cD][cD1] = {}
                for cD2 in cacheDict[cD][cD1]:
                    if cD2 not in profileDict[cD][cD1]:
                        profileDict[cD][cD1][cD2] = {}
                    try:
                        for cD3 in cacheDict[cD][cD1][cD2]:
                            if cD3 not in profileDict[cD][cD1][cD2]:
                                profileDict[cD][cD1][cD2][cD3] = {}
                    except:
                        pass
                    


                   

        """   
        for key, value in cacheDict.items():
            print(key, value)
            if key and value not in profileDict.items():
                profileDict[key] = value
        """
    for x in profileDict:
        fileName = x + '.md'
        if 'Frame' in x:
            markdownFile = open('01-Frames\\' + fileName, 'w')
            try:
                for file in glob.glob("01-Frames/"+ x +".markdown"):
                    markdownFile.write('This content is added from a manually generated file: \n\n')
                    for line in open(file, 'r'):      
                        markdownFile.write(line)
                    
                    markdownFile.write('\n\n --------------------------- \n\n')
                    markdownFile.write('\n\n This content is automaticly generated using NAP as source: \n\n')
            except:
                pass
            markdownFile.write(('\n\n'))
            markdownFile.write('### ' + x + '\n\n')
            markdownFile.write('```\n' + '# NeTEx annotation: \n' +  '***' + XA(x) + '***' + '\n```' + '\n\n')
            markdownFile.write('| Type | Name | SubElement | NeTEx annotation |' + ' \n')
            markdownFile.write('| --- | --- | --- | --- |' + ' \n')
            for y in profileDict[x]:
                if y == 'List':
                    for z in profileDict[x][y]:
                        try:
                            for last in profileDict[x][y][z]:
                                definition = ''
                                try:
                                    definition = XA(last)
                                except:
                                    pass
                                if 'Frame' in last:
                                    link = '[' + last + '](' + last + '.md' + ')'
                                    markdownFile.write('| ' + y + ' | ' + z + ' | ' + link + ' | ' + '***' + definition + '***' + ' |' + ' \n')
                                else:
                                    link = '[' + last + '](' + '/10-Objects/' + last + '.md' + ')'
                                    markdownFile.write('| ' + y + ' | ' + z + ' | ' + link + ' | ' + '***' + definition + '***' + ' |' + ' \n')
                        except:
                            pass
                else:
                    for z in profileDict[x][y]:
                        definition = ''
                        try:
                            definition = XA(z)
                        except:
                            pass
                        markdownFile.write('| ' + y + ' | ' + z + ' | ' + ' | ' + '***' + definition + '***' + ' |' + ' \n')
        else:           
            markdownFile = open('10-Objects\\' + fileName, 'w')
            try:
                for file in glob.glob("10-Objects/"+ x +".markdown"):
                    markdownFile.write('This content is added from a manually generated file: \n\n')
                    for line in open(file, 'r'):      
                        markdownFile.write(line)
                    
                    markdownFile.write('\n\n --------------------------- \n\n')
                    markdownFile.write('\n\n This content is automaticly generated using NAP as source: \n\n')
            except:
                pass
            markdownFile.write(('\n\n'))
            markdownFile.write('### ' + x + '\n\n')
            markdownFile.write('```\n' + '# NeTEx annotation: \n' + '***' + XA(x) + '***' + '\n```' + '\n\n')
            markdownFile.write('| Type | Name | SubElement | NeTEx annotation |' + ' \n')
            markdownFile.write('| --- | --- | --- | --- |' + ' \n')
            for y in profileDict[x]:
                if y == 'List':
                    for z in profileDict[x][y]:
                        try:
                            for last in profileDict[x][y][z]:
                                definition = ''
                                try:
                                    definition = XA(z)
                                except:
                                    pass
                                if 'Ref' in last:
                                    link = '[' + last + '](' + last[:-3] + '.md' + ')'
                                    markdownFile.write('| ' + y + ' | ' + z + ' | ' + link + ' | ' + '***' + definition + '***' + ' |' + ' \n')
                                else:
                                    markdownFile.write('| ' + y + ' | ' + z + ' | ' + last + ' | ' + '***' + definition + '***' + ' |' + ' \n')
                        except:
                            pass
                elif y == 'Reference':
                    for z in profileDict[x][y]:
                        referenceDefinition = ''
                        link = '[' + z + '](' + z[:-3] + '.md' + ')'
                        try:
                            referenceDefinition = XA(z)
                        except:
                            pass
                        markdownFile.write('| ' + y + ' | ' + link + ' | ' + ' | ' + '***' + referenceDefinition + '***' + ' |' + ' \n')
                else:
                    for z in profileDict[x][y]:
                        definition = ''
                        try:
                            definition = XA(z)
                        except:
                            pass
                        markdownFile.write('| ' + y + ' | ' + z + ' | ' + ' | '  + '***' + definition + '***' + ' |' + ' \n')