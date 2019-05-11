# [WORK IN PROGRESS] cx_app_three

Demo of an advanced Checkmarx integration into Gitlab: how to run a CxSAST and/or CxOSA scan in Gitlab pipeline integrated with the Security Dashboard

Requirements: 
- CxServer up-and-running instance, network-accessible from Gitlab instance 
- Environment variables:
    - CX_USERNAME
    - CX_PASSWORD (if it has a $ make sure you input two $$)
    - CX_SERVER
    - CX_SERVER_URI
    - CXARM_SERVER_URI (needed to break build on a violated policy)
    - GL_COMMENT_TOKEN (created by User Account -> Settings -> Access Tokens)
    - GL_URL (i.e. https://gitlab.com)


Please consult:

Docker repo: https://gitlab.com/cxrepositories/cxutilities/cxdocker

Helpers repo: https://gitlab.com/cxrepositories/cxutilities/cxhelpers


