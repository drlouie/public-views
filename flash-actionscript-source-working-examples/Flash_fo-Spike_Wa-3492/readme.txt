What does this sample show?
- This sample shows how to use JSP to generate and interact with a Flash form.

Key Concepts:
- Generating the HTML required to display the Flash form from JSP:
   The HTML for the generating the Flash form is cut and pasted from the published HTML page created by flash.

- Handling submitted data with JSP:
   The email.jsp contains logic to handle the POST submission from the Flash form by printing the submitted
   values back to the browser.

- Setting Flash variables from JavaScript:
   Notice that the Object tag in the email_form.jsp assigns a JavaScript name  to the Flash movie using the name="emailForm".
   This name is used by the setFlashVars() JavaScript function to assign values to the Flash variables.

- Submitting a Flash form back to the URL of the parent document it is embeded within:
   The setFlashVars() function sets the 'url' Flash variable for use within the ActiveScript of the SubmitButton

- Remembering submitted data:
   The email_form.jsp page accepts the submitted data and stores it into the HTTP session so that it can
   be remembered the next time the user requests the form.  When the HTML to show the Flash form is
   generated, the stored form data is extracted from the session and is encoded into the setFlashVars()
   client-side JavaScript function.   When the browser displays the Flash form, the setFlashVars() is executed
   and sets the values as Flash variables.

JRun Setup Instuctions:
1. Download and Install JRun 3.0
2. Unzip the email_form.zip file into your <jrun_root>/servers/default/default-app directory
3. Request the following URL: http://localhost:8100/email_form.jsp
4. Fill in the form
5. Press the submit button.  You should see the posted values displayed in HTML.
6. Press the reload button. You should see the Flash formagain, but notice that the form has
    remembered all of the previously entered values.

General Setup Instructions:
1. Must have a webserver which supports JSP 1.1
2. Drop the email_form.swf and email_form.jsp pages into your webroot directory.
3. Use you web browser to request the email_form.jsp page

Acknowledgements:
The Flash form used in this sample is a modification of the Flash Forms tutorial written by Roman Lebedinskiy (http://www.acky.net/tutorials/flash/forms/).



