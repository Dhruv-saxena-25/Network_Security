## AWS Cloud Setup


1) IAM 
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
2) S3
- 
