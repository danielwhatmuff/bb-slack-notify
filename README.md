# deploybot

## Overview
* Install and execute this CLI from within your Travis jobs to notify a Slack channel on deployment events.
* Note: It only works from within Travis jobs, as it reads from the provided [Convenience Variables](https://docs.travis-ci.com/user/environment-variables/#Convenience-Variables)

## Example Travis YAML
```yaml
after_deploy:
  - pip install notifybot && notifybot -t your-api-token -c your-slack-channel
  - pip install notifybot && notifybot -w https://your-slack-webhook-url -c your-slack-channel
```

## Related docs
* [Webhooks](https://api.slack.com/incoming-webhooks)
* [API Tokens](https://api.slack.com/custom-integrations/legacy-tokens)
* [Travis Build Docs](https://docs.travis-ci.com/user/customizing-the-build)
