
---

# **SOPPY-MAILS**  
**Automated Customer Feedback Management**

Managing customer feedback manually can be challenging, often leading to delays and errors that strain service teams. With tools like **Datamatics TruBot** and **TruCap+**, this process can be streamlined through automation. These tools facilitate feedback retrieval, sentiment analysis, and data extraction, ensuring faster response times, higher accuracy, and personalized service.  

### Demo video: [SOPPY-MAILS](https://drive.google.com/file/d/14-loxEZCDvs69AX_8h5m-QMEtp-y1u7A/view?usp=sharing)
### Presentation: [SOPPY-MAILS](https://www.canva.com/design/DAGXrc0lbAM/lewC5WZi2dPAFPslQR2Hkg/view?utm_content=DAGXrc0lbAM&utm_campaign=designshare&utm_medium=link&utm_source=editor#12)
---

## **Getting Started**  
Follow the steps below to set up and run the project on your local machine for development and testing.

---

### **Prerequisites**  

Ensure you have active subscriptions to the following services:  
- [**TruCap+**](https://www.datamatics.com/intelligent-automation/idp-trucap)  
- [**TruBot RPA Software**](https://www.datamatics.com/intelligent-automation/rpa-trubot)  
- [**TruBot Cockpit Personal**](https://www.datamatics.com/intelligent-automation/rpa-trubot/cockpit)  

Additionally, install the following software:  
- **TruBot Cockpit Personal**  
- **TruBot Designer**  

---

### **Installation**  

1. Clone the repository to your local machine:  
   ```bash
   git clone https://github.com/45H15H/Datamatics-Hackathon.git
   ```  
2. Alternatively, download the repository as a ZIP file and extract it.

---

## **Running the Project**  

### **Step 1: Sending Fake Emails (SendFakeEmails Bot)**  
1. Open the `email_dispatcher.py` script and update the placeholders with your credentials:  

   ```diff
   --GEMINI_API_KEY = 'api_key'
   ++GEMINI_API_KEY = '<your API key>'
   ```

   ```diff
   --SENDER_EMAIL = 'customer@example'
   ++SENDER_EMAIL = '<your email address>'
   ```

   ```diff
   --APP_PASSWORD = 'password'
   ++APP_PASSWORD = '<your app password>'
   ```

> [!NOTE]  
> You can get your Gemini API key [here.](https://ai.google.dev/gemini-api/docs/api-key)

> [!NOTE]  
> If using Gmail, create an App Password [here](https://myaccount.google.com/apppasswords).  

2. Update the recipient's email address:  
   ```diff
   --RECIPIENT_EMAIL = 'company@example.com'
   ++RECIPIENT_EMAIL = '<company email address>'
   ```

3. Configure the **TruBot Designer** workflow:  
   - Open the `ProcessInfo.json` file located in the `SendFakeEmails` folder.  
   - Edit the `Python Folder Path` property in the `Python Scope` component to point to the embedded Python folder in the repository.  
     Example:  
     ```plaintext
     C:\Datamatics-Hackathon\python-3.9.13-embed-win32
     ```  
   - Import the `email_dispatcher.py` script into the `Execute Python Script` component.  
   - Save, publish, and export the workflow as a ZIP file.

---

### **Step 2: Automating Feedback Analysis (FeedbackAnalysis Bot)**  



1. Configure the **TruBot Designer** workflow:  
   - Edit the `Get IMAP Mail` component in the workflow. Set the `Email` and `Password` properties to the assumed company email and app password.
   - Edit the `Python Folder Path` property in the `Python Scope` component to point to the embedded Python folder in the repository.  
     Example:  
     ```plaintext
     C:\Datamatics-Hackathon\python-3.9.13-embed-win32
     ```
   - Import the `process_email.py` script into the `Execute Python Script` component.
   - Select the `GSuite Application Scope` component in the workflow and edit the `User Email`, `User ID`, `User Password` and `Username` properties to the Google Authentication details. Refer to the [documentation](https://docs.datamatics.com/TruBot/Designer/5.4.0/Components/GSuite/GSuiteApplicationScope.htm) for more information.
   - Select the `ForEach DataRow` component in the workflow and edit the `Send SMTP Mail` component. Set the `Email ID` and `Sender Email ID` property to the assumed company email. Set the `Password` property to the app password of company email. Set the `To` property to the email address of the assumed customer support team email. Don't update the `Subject` and `Message Body` properties.
   - Save, publish, and export the workflow as a ZIP file.

---

### **Step 3: Running the Bots**  

1. Import the exported ZIP files for both bots into **TruBot Cockpit Personal**.  
2. Run the workflows in the following order:  
   - `SendFakeEmails`  
   - `FeedbackAnalysis`  

---

## **Results**  

1. **SendFakeEmails Bot**:  
   - Sends fake emails to the assumed company email address.  

   ![sample email](images/sample_email.png)

2. **FeedbackAnalysis Bot**:  
   - Extracts responses from emails, saves them in a CSV file (`eml_responses.csv`) and sends the analyzed responses to a Google Sheet and a customer support team email.

   ![sample summary email](images/sample_summary_email.png)

---

## **Team Details**  

**Team ID**: Data-230344  

| **Name**             | **Role**                                                                                     |  
|-----------------------|---------------------------------------------------------------------------------------------|  
| **Ashish Singh**      | Team Leader: Design and development of the bot using TruBot Designer                        |  
| **Khushi B Hanumannavar** | Team Member: Managed tasks related to TruCap+                                             |  

Paradiso LMS course completion:

- Datamatics TruBot Designer: [Certificate](https://drive.google.com/file/d/1lwG8KamWXB2-Jvq2g8CTw7oEKeJaeFfE/view?usp=sharing)
- TruCap+ Certification: [Certificate](https://drive.google.com/file/d/1yYGAlTr5eOqDEaX1dRbVdVzge2Uk9MK9/view?usp=sharing)

---
