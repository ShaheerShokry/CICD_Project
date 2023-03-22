# Overview

<TODO: complete this with an overview of your project>

## Project Plan
<TODO: Project Plan

* A link to a Trello board for the project
* A link to a spreadsheet that includes the original and final project plan>

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


## Architectural Diagram
![image](https://user-images.githubusercontent.com/94620177/226965171-9e2dfb43-905c-43af-97f9-a14ed72e72af.png)


# Instructions
## Azure Cloud Shell
Lets deploy the application using Azure Cloud Shell.

* Create ssh key and add the public key to the github Repo.

* Clone the repo in Azure Cloud Shell:
```
git@github.com:ShaheerShokry/CICD_Project.git
```
![image](https://user-images.githubusercontent.com/94620177/226966318-2be08565-c7c6-43ec-8fdc-9fe8774d7f47.png)

* Test and verify output of testing by running command ```make all```
![image](https://user-images.githubusercontent.com/94620177/226967699-fca23ca8-910f-4f27-b9c3-a6075c2597d0.png)
![image](https://user-images.githubusercontent.com/94620177/226967822-80d82039-1d1f-4c8e-842d-85e6e14f4c88.png)

* Enable Github Actions on your repo.
* Output of continuous integration with Github Actions
![image](https://user-images.githubusercontent.com/94620177/226968683-9dd7556f-ecb9-4fcd-b37f-fe8818ec3817.png)


