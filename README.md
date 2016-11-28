# Purpose
The default Webhook emitted from gitlab.com will not trigger a repository update for a remote crucible installation. Crucible requires that the repository name be included in the URL of the PUT request, and by default it is not included from gitlab requests. This code can be called from a gitlab webhook, and will forward the webhook request on to your crucible installation so that a gitlab repository will be re-indexed automatically when new changesets are pushed to gitlab.com.

# Setup
  1. Deploy this code to AWS Lambda using [Zappa](https://github.com/Miserlou/Zappa)
  2. Setup the gitlab.com web hook:
    1. From your gitlab repository, select: Settings -> Webhooks
    2. Enter the URL of your Lambda once Zappa deploys your code.
    3. For the secret token, enter both the Crucible REST Api Token, and the repository name as it is defined in crucible, separated by a semicolon. (;) e.g.: 123abc456def;MyCodeRepository
