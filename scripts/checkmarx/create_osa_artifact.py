import sys
import json

def create_json_file(output):

    file = open("gl-dependency-scanning-report.json","w+")

    file.write(output)

    file.close()
#-----------------------------------------------------------------------------------------------------
def convert_json(output):
    
    print output
    
    vulnList = []


    for result in output:
        print "*************"
        print result
        print "*************"
        
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

with open(osa_report) as fd:
	out = convert_json(fd.read())

create_json_file(out)