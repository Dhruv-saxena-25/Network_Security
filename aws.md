## AWS Cloud Setup


# 1 Search for IAM 
- Click on Users:
    - Go to `create user`. 
    - Enter the `user name`.
    - Now attach policies to the user: `AdministratorAccess`, `AmazonEC2ContainerRegistryFullAccess`, `AmazonEC2FullAccess`, `AmazonS3FullAccess `.
    - Now click on `Next` and then click on `Create user`.

- Now add `Security credentials` for the user.
    - Go to `Access keys` and `Create access key` 
    - Select the Use Case: `Local code` and click on Next. 
- Now You `Access key` and `Secret access key` is ready. Configure this with the `aws configure` on terminal.
    - AWS Access Key ID [****************ZPUP]
    - AWS Secret Access Key [****************P184]:
    - Default region name [us-east-1]:
    - Default output format [None]:
# 2 Search for S3
- Click on `Create bucket`.
- Now add the `Bucket name` and keep all other information as it is.
    - **Bucket name must be globally unique.** 
- Then click on `Create bucket`. 

# 3 Search for ECR
- Click on `Create repository`.
- Enter the `Repository name`.
- Click on `Create`.


# 4 EC2 
 - 




# 5 Github Setup `Actions secrets and variables`.
- Add `secrets` to your repository.
    - **AWS_ACCESS_KEY_ID**:
    - **AWS_DEFAULT_REGION**:
    - **AWS_ECR_LOGIN_URI**:
    - **AWS_SECRET_ACCESS_KEY**:
    - **BUCKET_NAME**:
    - **ECR_REPOSITORY_NAME**:
    - **MONGO_DB_URL**:


# 6 Install Docker on EC2 Machine.


```bash
sudo apt-get update -y
```

```bash
sudo apt-get upgrade
```

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
```

```bash
sudo sh get-docker.sh
```

```bash
sudo usermod -aG docker ubuntu
```

```bash
newgrp docker
```



# 7 Github Setup `Runners`.
- Click on settings > Actions > Runners
- Select `New selfosted runner`.
- Select `Linux` for Runner image.


# Copy these code to EC2 Instance:

## Download

### Create a folder

```bash
$ mkdir actions-runner && cd actions-runner# Download the latest runner package
```

### Download the latest runner package


```bash
curl -o actions-runner-linux-x64-2.319.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.319.1/actions-runner-linux-x64-2.319.1.tar.gz
```

### Optional: Validate the hash
```bash
$ echo "3f6efb7488a183e291fc2c62876e14c9ee732864173734facc85a1bfb1744464  actions-runner-linux-x64-2.319.1.tar.gz" | shasum -a 256 -c
```

### Extract the installer
```bash
$ tar xzf ./actions-runner-linux-x64-2.319.1.tar.gz
```

## Configure

### Create the runner and start the configuration experience

```bash
$ ./config.sh --url https://github.com/Dhruv-saxena-25/Network_Security --token AR5GXAUBPERQHBLWT5JPFODG3GZ2G
```

### Last step, run it!
```bash
$ ./run.sh
```