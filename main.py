"""
main.py

This script creates a sample NumPy array, saves it in Zarr format,
uploads it to Google Cloud Storage (GCS), then downloads it and reads it back.

🔐 CREDENTIALS NOTICE:
This script uses a GCP service account JSON key 
(`zarr-storage-project-a68666d70bdf.json`) to authenticate with GCS.

⚠️ For security reasons, the key file is not included in this repository.  
Please refer to the README file for instructions on how to access it securely.
"""

import numpy as np
import zarr
import gcsfs

# These variables are required by the assignment, but not used in GCS authentication
ACCESS_KEY_ID = ''
SECRET_ACCESS_KEY = ''

# Initialize GCS filesystem using a service account JSON file
gcs = gcsfs.GCSFileSystem(token='zarr-storage-project-a68666d70bdf.json')

# Create a sample NumPy array
array = np.arange(20).reshape(4, 5)

# 1. Save the array locally in Zarr format
zarr.save('local_array.zarr', array)
print("✅ Array successfully saved to local Zarr directory.")

# 2. Upload the local Zarr directory to Google Cloud Storage
gcs_path = 'zarr-test-bucket-20250503/test_array.zarr'
gcs.put('local_array.zarr', gcs_path, recursive=True)
print(f"✅ Successfully uploaded to GCS at: {gcs_path}")

# 3. (Optional test) Download the Zarr directory back from GCS and read it
gcs.get(gcs_path, 'downloaded_array.zarr', recursive=True)
loaded_array = zarr.load('downloaded_array.zarr')

print("📥 Successfully read array back from GCS download:")
print(loaded_array)
