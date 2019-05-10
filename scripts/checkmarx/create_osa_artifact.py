import sys
import json

def create_json_file(output):

    file = open("gl-dependency-scanning-report.json","w+")

    file.write(output)

    file.close()
#-----------------------------------------------------------------------------------------------------
def convert_json(output):
    
    vulnList = []

    for result in output:
        vulnElement = {}

        vulnElement['tool'] = "CxOSA"
        vulnElement['message'] = result['description']
        vulnElement['url'] = result['url']
        vulnElement['cve'] = result['cveName']
        vulnElement['file'] = result['sourceFileName']
        vulnElement['priority'] = result['severity']['name']
                    
        vulnList.append(vulnElement)

    return (json.dumps(vulnList))

#-----------------------------------------------------------------------------------------------------

args = sys.argv

osa_report = args[1]

with open(osa_report) as json_file:
    data = json.load(json_file)

out = convert_json(data)

create_json_file(out)