@echo off
set /p profile="Enter the name of the AWS CLI profile to use: "
set /a timeout=36000

aws sts get-session-token --duration-seconds %timeout% --profile %profile%
