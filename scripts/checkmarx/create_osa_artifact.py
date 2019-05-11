import sys
import json

def create_json_file(output):

    file = open("gl-dependency-scanning-report.json","w+")

    file.write(output)

    file.close()
#-----------------------------------------------------------------------------------------------------
def convert_json(output):
    osaReport = {}
    vulnList = []

    osaReport['version'] = "2.0"

    for result in output:
        vulnElement = {}

        vulnElement['category'] = "dependency_scanning"
        vulnElement['message'] = result['description']
        vulnElement['cve'] = result['cveName']
        vulnElement['severity'] = result['severity']['name']
        vulnElement['solution'] = "To DO"
        
        scanner = {}
        scanner['id'] = "Checkmarx OSA"
        scanner['name'] = "Checkmarx OSA"
                    
        vulnElement['scanner'] = scanner
        
        location = {}
        location['file'] = result['sourceFileName']

        dependency = {}
        package = {}
        package['name'] = "To DO"

        dependency['package'] = package
        location['dependency'] = dependency
        location['version'] = "To do"

        vulnElement['location'] = location
        
        identifiersList = []

        identifiers= {}
        identifiers['type'] = "cve"
        identifiers['name'] = result['cveName']
        identifiers['value'] = result['cveName']
        identifiers['url'] = result['url']

        identifiersList.append(identifiers)
        
        vulnElement['identifiers'] = identifiersList
        
        linksList = []
        links= {}
        links['url'] = "To do"
        linksList.append(links)
        
        vulnElement['links'] = linksList
        
        vulnElement['priority'] = result['severity']['name']

        vulnList.append(vulnElement)

    osaReport['vulnerabilities'] = vulnList

    remediations = []
    osaReport['remediations'] = remediations 

    return (json.dumps(osaReport))

#-----------------------------------------------------------------------------------------------------

args = sys.argv

osa_report = args[1]

with open(osa_report) as json_file:
    data = json.load(json_file)

out = convert_json(data)

create_json_file(out)