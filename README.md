# End to End Text-summarization-project

## PROBLEM STATEMENT:
-> consider there is a text or paragraph will be given to our api we need to identify the most important from the given text which ever words are more important and we have to present the abridged version of it we have to combine this together then we have to present this to user this type of problems is called the extractive text summarization because we are extracting from the given text we are not abstracting it which means we are not creating the new text.

-> Given a text/ paragraph identify the most important information from the given text and present the abridged version of it to the end users.




## Workflows
1. update config.yaml file.
2. upadte params.yaml.
3. update entity
4. update configuration manager in src/config.
5. update the components.
6. update the pipeline.
7. update the main.py
8. update the app.py.


How to run?
STEPS:
Clone the repository

https://github.com/Anuragreddy-Naredla/text-summarization

STEP 01- Create a conda environment after opening the repository

conda create -n summary python=3.8 -y

conda activate summary

STEP 02- install the requirements

pip install -r requirements.txt

# Finally run the following command
python app.py
Now,

open up you local host and port
AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
- Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/text-s
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
6. Configure EC2 as self-hosted runner:

setting>actions>runner>new self hosted runner> choose os> then run command one by one

7. Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app
