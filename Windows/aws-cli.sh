########################################################
####  To generate the access token for 24 hours  #######
########################################################

aws sts get-session-token --duration-seconds 86400
