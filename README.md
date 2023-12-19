## Notes by Gustavo Carmona - Certified Cloud Architect - 

The Users pool have username, email, password for each user. You want send username, password and get Token.   

![Cloud Architecture](./images/Cognito.png "Cloud Architecture")    

**First:**   
Amazon Cognito -> Users pool - > User pool name -> App Integration -> app client Name 
-> show details/Edit -> Authentication flows -> Allow user-password-auth flow for app-based authentication (USER_PASSWORD_AUTH).

**Second:**   
LambaFunction.py and main.py have almost the same code. Find Lambda Environment variables !!     

![Env Variables](./images/CognitoLambda1.png "Env Variables")   

**Third:**  
Write local Python Code as in main.py

Four:   
You can use Postman, as shown in the image below, to test the API and Lambda function.

![PostMan](./images/CognitoPostman.png "PostMan")   


