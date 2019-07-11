# cx_app

Demo of an advanced Checkmarx integration into CircleCI: how to run a CxSAST and/or CxOSA scan in Circle CI pipeline

Requirements: 
- CxServer up-and-running instance, network-accessible from CircleCI instance 
- Environment variables:
    - CX_USERNAME
    - CX_PASSWORD (if it has a $ make sure you input two $$)
    - CX_SERVER
    - CX_SERVER_URI
    - CXARM_SERVER_URI (needed to break build on a violated policy)
    - GL_COMMENT_TOKEN (created by User Account -> Settings -> Access Tokens)
    - GL_URL (i.e. https://circleci.com)


Please consult:

Docker repo: https://gitlab.com/cxrepositories/cxutilities/cxdocker

Helpers repo: https://gitlab.com/cxrepositories/cxutilities/cxhelpers


