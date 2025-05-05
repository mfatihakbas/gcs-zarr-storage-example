"""
⚠️ Security Note on AWS Credentials

For security reasons, this project does not include any AWS Access Key or Secret Key directly in the codebase.
All AWS interactions are done using credentials securely configured through the AWS CLI.

Each user is expected to:
- Configure their own credentials using `aws configure`
- Use their own S3 bucket for testing
- ❌ Never share access keys in public repositories

If you do not have credentials yet, please follow the "Amazon S3 Setup" instructions in the README to:
- Create an IAM user
- Attach the required S3 permissions (e.g., AmazonS3FullAccess)
- Generate your own Access Key ID and Secret Access Key

🔐 Reminder: This script assumes AWS CLI is already configured using your personal credentials.
This script does not handle key files or manual secret access in code.
"""

import numpy as np
import zarr
import s3fs

# Generate a small and readable NumPy array for demonstration
data = np.arange(20).reshape(4, 5)

# Define the S3 bucket name and the target Zarr directory
bucket_name = "zarr-test-bucket"
store_path = f"{bucket_name}/test-array.zarr"

# Initialize the S3 filesystem store using s3fs
# Assumes AWS CLI authentication has already been completed via 'aws configure'
store = s3fs.S3Map(root=store_path, s3=s3fs.S3FileSystem(), check=False)

# Save the NumPy array to the specified S3 location in Zarr format
zarr.save(store, data)
print(f"✅ Array successfully uploaded to S3 bucket at '{store_path}'\n")

# Read the array back from S3 to verify the upload
restored = zarr.load(store)

# Display the retrieved array content
print("📥 Array successfully read from S3:")
print(restored)
