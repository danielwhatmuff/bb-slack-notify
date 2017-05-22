# deploybot
![](https://raw.githubusercontent.com/danielwhatmuff/notifybot/master/img/screenshot.png)

## Overview
* Install and execute this CLI from within your Travis jobs to notify a Slack channel on deployment events.
* Note: It only works from within Travis jobs, as it reads from the provided [Convenience Variables](https://docs.travis-ci.com/user/environment-variables/#Convenience-Variables)

## Example Travis YAML
### Be sure to encrypt your token or webhook URL
```bash
$ gem install travis
$ travis encrypt SLACK_TOKEN=yourtoken --add
$ travis encrypt SLACK_WEBHOOK=yourwebhook--add
```
### Use a legacy API token
```yaml
after_deploy:
  - pip install notifybot && notifybot -t $SLACK_TOKEN -c your-slack-channel
```
### Use an incoming webhook URL
```yaml
after_deploy:
  - pip install notifybot && notifybot -w $SLACK_WEBHOOK -c your-slack-channel
```

## Related docs
* [Webhooks](https://api.slack.com/incoming-webhooks)
* [API Tokens](https://api.slack.com/custom-integrations/legacy-tokens)
* [Travis Build Docs](https://docs.travis-ci.com/user/customizing-the-build)
