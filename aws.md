## AWS Cloud Setup


1) Search for IAM 
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
2) Search for S3
- Click on `Create bucket`.
- Now add the `Bucket name` and keep all other information as it is.
    - **Bucket name must be globally unique.** 
- Then click on `Create bucket`. 

3) Search for ECR
- Click on `Create repository`.
- Enter the `Repository name`.
- Click on `Create`.


4) EC2 
- 




5) Github Setup `Actions secrets and variables`.
- Add `secrets` to your repository.
    - **AWS_ACCESS_KEY_ID**:
    - **AWS_DEFAULT_REGION**:
    - **AWS_ECR_LOGIN_URI**:
    - **AWS_SECRET_ACCESS_KEY**:
    - **BUCKET_NAME**:
    - **ECR_REPOSITORY_NAME**:
    - **MONGO_DB_URL**:





