# CICD_Project

[![Python application test with Github Actions](https://github.com/ShaheerShokry/CICD_Project/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/ShaheerShokry/CICD_Project/actions/workflows/pythonapp.yml)


# Overview
In this project, you will build a Github repository from scratch and create a scaffolding that will assist you in performing both Continuous Integration and Continuous Delivery. You'll use Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle. Next, you'll integrate this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.

## Project Plan
- [Trello board for the project](https://trello.com/b/zeoZeJUF/cicdproject)
- [Spreadsheet for the project](./project-management-sh.xlsx)

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

## Testing the flask application in Azure CLI
* Clone the reop to your existing directory
* run make all
![image](https://user-images.githubusercontent.com/94620177/227331113-d21a03b9-7a24-435c-8eee-d8e28604545f.png)


* Start flask webapp 
![image](https://user-images.githubusercontent.com/94620177/227003894-863b9795-5a96-40b0-9f25-bec2486eb21f.png)

* Open second Azure Cloud Shell terminal and test the app by making a prediction
```
./make_prediction.sh
```
![image](https://user-images.githubusercontent.com/94620177/227004103-df374382-4948-4ac1-8ed3-6a96be47b714.png)

## Deploy Flask Webapp on Azure

* cd CICD_Project
* az webapp up -n Flask-app-1 -g RG1 --sku F1
![image](https://user-images.githubusercontent.com/94620177/227008533-d1edb400-5899-4c5b-b053-08b14f384e65.png)
![image](https://user-images.githubusercontent.com/94620177/227008826-643ca051-d5db-42f8-b257-4e01e979599e.png)
![image](https://user-images.githubusercontent.com/94620177/227008925-7f832e01-dd04-417e-84ef-c302646c5a38.png)


## Deploy with AzureDevOps

* Create a new project in Azure DevOps
* Create a new service connection in Azure DevOps (you can find it under project settings). The Azure Resource Manager comes in handy for that. Choose         Service principal (automatic) if asked and establish a connection to your subscription and resource group.
* Go to Azure DevOps Pipelines and create one by connecting it to your GitHub repo. Once, you can configure your pipeline, choose 'Python to Linux Web App     on Azure'. This will generate the appropriate YML file for the Flask web app.
  Once, this step is successfully done, you have deployed the Flask Web App.

![image](https://user-images.githubusercontent.com/94620177/227025518-61b63e79-5624-44b8-b73d-050f3501fb3f.png)
![image](https://user-images.githubusercontent.com/94620177/227025660-5940f634-53a9-4d4a-b09b-13ba29b8f382.png)


* Test the Flask Web App
![image](https://user-images.githubusercontent.com/94620177/227026937-8d2b9578-45c4-4eab-9c14-f2543a672933.png)

* Logs can be found here:
![image](https://user-images.githubusercontent.com/94620177/227027342-b949808b-65b0-45cf-be72-74feb63f18b0.png)

## Demo

- [Video Demo](https://youtu.be/1uz3NmUpPAo)







