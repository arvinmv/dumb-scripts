# Encrypt

Here's my first python script. Needed to encrypt objects in S3 so that's where the idea came for this came from. I got the chance to work with the boto3 module and subprocess module. It's definitely not clean but it got the job done until I realized that it only encrypted top level objects within a bucket and not objects within sub directories.

TODO: Update to encrypt all objects (not just at top level)
