# bb-slack-notify
![](https://raw.githubusercontent.com/danielwhatmuff/bb-slack-notify/master/img/screenshot.png)

## Overview
* Install and execute this CLI from within your Bitbucket Pipeline deployment steps to notify a Slack channel on deployment events.
* Note: It only works from within Bitbucket pipelines, as it reads from the provided [Environment Variables](https://confluence.atlassian.com/bitbucket/environment-variables-794502608.html)

## Example bitbucket-pipelines.yml YAML
### Use a legacy API token
* Add your token or webhook URL as a secure environment variable within repository settings
```yaml
---
pipelines:
  custom:
    deploy-to-prod:
    - step:
        name: Deploy to prod, this can be triggered manually
        script:
          - python deploy_my_app.py
          - pip install bb-slack-notify && bb-slack-notify -t $SLACK_TOKEN -c your-slack-channel
```
### Use an incoming webhook URL
```yaml
          ...
          - pip install bb-slack-notify && bb-slack-notify -w $SLACK_WEBHOOK -c your-slack-channel
```

## Related docs
* [Webhooks](https://api.slack.com/incoming-webhooks)
* [API Tokens](https://api.slack.com/custom-integrations/legacy-tokens)
* [Bitbucket Pipelines](https://confluence.atlassian.com/bitbucket/configuring-your-pipeline-872013574.html)
