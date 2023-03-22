# CICD_Project


# Overview
In this project, you will build a Github repository from scratch and create a scaffolding that will assist you in performing both Continuous Integration and Continuous Delivery. You'll use Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle. Next, you'll integrate this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.

## Project Plan
- [Trello board for the project](https://trello.com/invite/b/zeoZeJUF/ATTIfd7db4d8edc32debe6a65ddeef181d391B736957/cicdproject).
- [Spreadsheet for the project](./assets/project-management.xlsx)

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
![image](https://user-images.githubusercontent.com/94620177/227003583-e48d6cf2-27ec-44a9-a6a0-bff389e4a1bf.png)
![image](https://user-images.githubusercontent.com/94620177/227003664-67310c3e-f73f-4c8b-9849-bd611893ca6f.png)

* Start flask webapp 
![image](https://user-images.githubusercontent.com/94620177/227003894-863b9795-5a96-40b0-9f25-bec2486eb21f.png)

* Open second Azure Cloud Shell terminal and test the app by making a prediction
```
./make_prediction.sh
```
![image](https://user-images.githubusercontent.com/94620177/227004103-df374382-4948-4ac1-8ed3-6a96be47b714.png)

## Azure DevOps Pipeline





