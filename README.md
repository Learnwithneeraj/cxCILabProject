# Cx Gitlab Integration Demo - Advanced way

Demo of an advanced Checkmarx integration into Gitlab: how to run a CxSAST and/or CxOSA scan in Gitlab pipeline AND comment on commit and merge request

Requirements: 
- CxServer up-and-running instance, network-accessible from Gitlab instance 
- Environment variables:
    - CX_USERNAME
    - CX_PASSWORD
    - CX_SERVER_URI
    - CXARM_SERVER_URI (needed to break build on a violated policy)
- Please consult: 
    - Docker repo: https://gitlab.com/cxrepositories/cxutilities/cxdocker
    - Helpers repo: https://gitlab.com/cxrepositories/cxutilities/cxhelpers