"""A Python Pulumi program"""

import pulumi
import pulumi_aws as aws

bucket = aws.s3.Bucket("my-bucket")