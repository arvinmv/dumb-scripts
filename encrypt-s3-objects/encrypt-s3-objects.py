import boto3
import subprocess

bucket_name = ''

def list_of_files(user_bucket):
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(user_bucket)
    object_summary_iterator = my_bucket.objects.all()
    files = []
    for bucket_object in object_summary_iterator:
        files.append(bucket_object.key)
        print(bucket_object.key)
    return files

def encrypt_object(bucket_name, files):
    for bucket_object in files:
        aws_command = "aws s3 cp s3://{}/{} s3://{}/{} --sse AES256".format(bucket_name, bucket_object, bucket_name, bucket_object)
        subprocess.run(aws_command, shell=True)
        print('The {} object has been encrypted'.format(bucket_object))


def main():
    bucket_name = str(input('Enter bucket name: '))
    bucket_files = list_of_files(bucket_name)
    encrypt_object(bucket_name, bucket_files)

if __name__ == '__main__':
    main()