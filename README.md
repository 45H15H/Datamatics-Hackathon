# Project Title



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need active subscriptions to the following services:

* [TruCap+](https://www.datamatics.com/intelligent-automation/idp-trucap)
* [TruBot RPA Software](https://www.datamatics.com/intelligent-automation/rpa-trubot)
* [TruBot Cockpit Personal](https://www.datamatics.com/intelligent-automation/rpa-trubot/cockpit)

You will also need to install the following software:

* TruBot Cockpit Personal
* TruBot Designer

### Installing

Clone the repository to your local machine or download the zip file and extract the contents to a folder.

```bash
git clone https://github.com/45H15H/Datamatics-Hackathon.git
```

## Running the project

1. First, we need to send fake emails from the assumed customers to the company. To do this, open the `email_dispatcher.py` script.

Make the required changes to the script and save it.

```diff
--GEMINI_API_KEY = 'api_key'
++GEMINI_API_KEY = '<your api key>'
```

note: You can get your Gemini API key [here.](https://ai.google.dev/gemini-api/docs/api-key)

```diff
--SENDER_EMAIL = 'customer@example'
++SENDER_EMAIL = '<your email address>'
```

```diff
--APP_PASSWORD = 'password'
++APP_PASSWORD = '<your app password>'
```

note: If you are using Gmail, you need to make App Passwords [here.](https://myaccount.google.com/apppasswords)

```diff
--RECIPIENT_EMAIL = 'company@example.com'
++RECIPIENT_EMAIL = '<company email address>'
```

2. Prepare the TruBot workflow to process the emails.

1. Open the TruBot Designer.
2. Click on the `Open Process` button and select the `ProcessInfo.json` file in `SendFakeEmails` folder.
3. Select `Python Scope` coponent in the workflow and edit the `Python Folder Path` in properties to the path where the `Python Embedded` folder is saved in the repository. Example: `C:\Datamatics-Hackathon\python-3.9.13-embed-win32`
4. Double click on the `Python Scope` component and click on the `Import File` button of `Execute Python Script` component and select the `email_dispatcher.py` file.
5. Save the workflow.
6. Publish the workflow by clicking on the `Publish` button. Then click on the `Export` button to export the workflow into a zip file.

Now let's setup the __Email Feedback Analysis Automation__.

1. Create a folder where you want to save the customer emails. Example: `C:\Datamatics-Hackathon\Emails`. In that folder create a folder called `SaveIMAPmail`. This folder will be used to save the emails from the customers.

2. Edit the `process_email.py` script.

```diff
--folder_path = r'C:\Emails\SaveIMAPmail'
++folder_path = r'path\to\your\Emails\SaveIMAPmail'
```

```diff
--output_csv = r'C:\Emails\eml_responses.csv'
++output_csv = r'path\to\your\EmailDatabase\eml_responses.csv'
```

This script will read the saved emails in the `SaveIMAPmail` folder and save the responses in the `eml_responses.csv` file.

3. Open the TruBot Designer.
4. Click on the `Open Process` button and select the `ProcessInfo.json` file in the `FeedbackAnalysis` folder.
5. Edit the `Get IMAP Mail` component in the workflow. Set the `Email` and `Password` properties to the assumed company email and app password.
6. In the next `For Each` component, edit the `Save Mails` component and set the `File Path` property to the path where the `SaveIMAPmail` folder is saved in the repository. Format: `<path to the folder> +  Item.Subject + .eml`. Example: "C:\Emails\SaveIMAPmail\" + Item.Subject + ".eml"
7. Select `Python Scope` coponent in the workflow and edit the `Python Folder Path` in properties to the path where the `Python Embedded` folder is saved in the repository. Example: `C:\Datamatics-Hackathon\python-3.9.13-embed-win32`
8. Double click on the `Python Scope` component and click on the `Import File` button of `Execute Python Script` component and select the `process_email.py` file.
9. Select `Read CSV` component in the workflow and edit the `File Path` property to the path where the `eml_responses.csv` file is saved in the repository. Example: `C:\Emails\eml_responses.csv`
10. Select the `GSuite Application Scope` component in the workflow and edit the `User Email`, `User ID`, `User Password` and `Username` properties to the Google Authentication details. Refer to the [documentation](https://docs.datamatics.com/TruBot/Designer/5.4.0/Components/GSuite/GSuiteApplicationScope.htm) for more details.
11. Select the `ForEach DataRow` component in the workflow and edit the `Send SMTP Mail` component. Set the `Email ID` and `Sender Email ID` property to the assumed company email. Set the `Password` property to the app password of company email. Set the `To` property to the email address of the assumed customer support team email. Don't update the `Subject` and `Message Body` properties.
12. Save the workflow.
13. Publish the workflow by clicking on the `Publish` button. Then click on the `Export` button to export the workflow into a zip file.


## Running the bots

1. Open the TruBot Cockpit Personal.
2. Click on the `Import` button and select the exported zip file of the `SendFakeEmails` workflow.
3. Click on the `Import` button and select the exported zip file of the `FeedbackAnalysis` workflow.
4. Click on the `Run` button to run the `SendFakeEmails` workflow.
5. Click on the `Run` button to run the `FeedbackAnalysis` workflow.




## Built With

* [Technology 1](link)
* [Technology 2](link)


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


## Versioning

We use SemVer for versioning. For the versions available, see the [tags on this repository](https://github.com/yourusername/yourrepo/tags).


## Authors

* **Your Name** - *Initial work* - [yourusername](https://github.com/yourusername)


## License

This project is licensed under the [MIT License](LICENSE.md) - see the [LICENSE.md](LICENSE.md) file for details.


## Acknowledgments

Give credit to anyone who has contributed to this project.  For example:

* [Inspiration](https://www.example.com)
* [Other project](https://www.example.com)
