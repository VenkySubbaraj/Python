**Adding user from the Azure directory to aws**
```
 https://community.amazonquicksight.com/t/enable-federation-to-amazon-quicksight-with-automatic-provisioning-of-users-between-aws-iam-identity-center-and-microsoft-azure-ad/8234 
```


**Checkov Checks**

```
terraform plan -out tf.plan
terraform show -json tf.plan > tf.json
pip install checkov
checkov -f tf.json

```

