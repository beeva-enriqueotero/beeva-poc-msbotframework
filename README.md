# beeva-poc-msbotframework
Proof of Concept with MS Bot Framework &amp; QnA

### Azure account

- Use an existing Azure account. Or set-up a new one.
- Recommended to [set-up billing alerts](https://docs.microsoft.com/en-us/azure/billing/billing-set-up-alerts)

### qnamaker.ai
- Create new service
- Train Knowledge Base
- Test
- Publish
- View settings

### Microsoft Azure Bot Service
- Go to portal.azure.com
- Create a bot (Web app Bot or Functions Bot (\*))
- Select name and [pricing plan](https://azure.microsoft.com/en-us/pricing/details/bot-service/)
  - For a Functions Bot, the Azure Bot Service will run on Azure Functions in consumption mode.
  - For a Web App Bot, the Azure Bot Service will run as standard Azure Web App. (45€/month)
- Select Question and Answer template
- In Application Settings, edit `QnAKnowledgebaseId` and `QnASubscriptionKey`
- In Build, edit, open online code editor
- In online code editor, edit `BasicQnAMakerDialog.cs`.
- Set `scoreThreshold` to 0.0 and edit default `No good match in FAQ.` message.
- Open console, and execute `build.cmd`
- Test

### Connect to Slack
- Follow https://docs.microsoft.com/en-us/bot-framework/channel-connect-slack
  - Build slack App
  - Add redirect url via permissions
  - Add a bot user
  - Enable events on event subscriptions
  - Enter slack credentials on https://dev.botframework.com/

### Advanced
- Test, edit, retrain and publish the update knowledge base.
- Change the default message. [See instructions](https://docs.microsoft.com/es-es/bot-framework/azure-bot-service-template-question-answer)
- Add web chat: `<iframe src='https://webchat.botframework.com/embed/chatbot-gc-qna?s=YOUR_SECRET_HERE'></iframe>`

### Issues
- Not able to deploy and test a Functions Bot
