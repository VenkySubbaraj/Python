name: Glue Job Failure Notification

on:
  workflow_run:
    workflows: ["Your Glue Job Workflow Name"]  # Replace with the name of your Glue Job workflow
    types:
      - completed

jobs:
  notify_on_glue_failure:
    runs-on: ubuntu-latest
    
    steps:
    - name: Check if Glue Job Failed
      id: check_glue_job
      run: |
        job_status=$(aws glue get-job-runs --job-name YourGlueJobName --max-results 1 | jq -r '.JobRuns[0].JobRunState')
        if [ "$job_status" == "FAILED" ]; then
          echo "::set-output name=failed::true"
        else
          echo "::set-output name=failed::false"
        fi
      env:
        AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
        AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        AWS_DEFAULT_REGION: us-east-1  # Replace with your Glue job region
      continue-on-error: true
      
    - name: Send Notification on Failure
      if: steps.check_glue_job.outputs.failed == 'true'
      run: |
        curl -X POST -H "Content-Type: application/json" -d '{
          "type": "message",
          "attachments": [
            {
              "contentType": "application/vnd.microsoft.card.adaptive",
              "content": {
                "type": "AdaptiveCard",
                "body": [
                  {
                    "type": "TextBlock",
                    "text": "AWS Glue Job Failed",
                    "size": "large",
                    "weight": "bolder"
                  },
                  {
                    "type": "TextBlock",
                    "text": "The AWS Glue job failed. Check the Glue job logs for more details."
                  }
                ],
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "version": "1.3"
              }
            }
          ]
        }' "YOUR_TEAMS_WEBHOOK_URL"
      env:
        YOUR_TEAMS_WEBHOOK_URL: ${{ secrets.TEAMS_WEBHOOK_URL }}
