import xmltodict
import json
import sys

def create_json_file(output):

    file = open("gl-sast-report.json","w+")

    file.write(output)

    file.close()
#-----------------------------------------------------------------------------------------------------
def parse_xml(doc):
    sastReport = {}
    vulnList = []

    sastReport['version'] = "2.0"

    if doc and 'CxXMLResults' in doc:
        xml_results = doc['CxXMLResults']

        if xml_results and 'Query' in xml_results:
            for query in xml_results['Query']:
                results = query['Result']
                list_results = []
                if isinstance(results, list):
                    list_results = results
                else:
                    list_results.append(results)
                for result in list_results:
                    vulnElement = {}

                    vulnElement['category'] = "sast"
                    vulnElement['name'] = query["@name"]
                    vulnElement['message'] = query["@name"] + " found in code."
                    vulnElement['description'] = query["@name"]
                    vulnElement['cve'] = query["@cweId"]
                    vulnElement['severity'] = query["@Severity"]
                    vulnElement['confidence'] = query["@Severity"]
                    vulnElement['solution'] = "Review " + result["@DeepLink"] + " for details."

                    scanner = {}
                    scanner['id'] = "Checkmarx"
                    scanner['name'] = "Checkmarx"

                    vulnElement['scanner'] = scanner

                    location = {}
                    location['file'] = result["@FileName"]
                    location['start_line'] = result["@Line"]
                    location['end_line'] = "0"
                    location['class'] = "N/A"
                    location['method'] = "N/A"

                    dependency = {}
                    package = {}

                    dependency['package'] = package
                    location['dependency'] = dependency

                    vulnElement['location'] = location

                    identifiersList = []

                    identifiers= {}
                    identifiers['type'] = "checkmarx_bug"
                    identifiers['name'] = "Checkmarx - " + query["@name"]
                    identifiers['value'] = query["@name"]
                    identifiers['url'] = result["@DeepLink"]

                    identifiersList.append(identifiers)

                    identifiers= {}
                    identifiers['type'] = "cwe"
                    identifiers['name'] = query["@cweId"]
                    identifiers['value'] = "0"
                    identifiers['url'] = "https://cwe.mitre.org"

                    identifiersList.append(identifiers)

                    vulnElement['identifiers'] = identifiersList

                    vulnList.append(vulnElement)

    sastReport['vulnerabilities'] = vulnList

    remediations = []
    sastReport['remediations'] = remediations 

    return (json.dumps(sastReport))
#-----------------------------------------------------------------------------------------------------

args = sys.argv

xml = args[1]

with open(xml) as fd:
	print (fd.read())
	document = xmltodict.parse(fd.read())

json_output = parse_xml(document)
create_json_file (json_output)