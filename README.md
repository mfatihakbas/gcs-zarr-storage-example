# GCS Zarr Test Project

This project demonstrates a complete workflow of storing and retrieving a NumPy array in Zarr format using Google Cloud Storage (GCS).  
It was developed as part of a programming assignment and illustrates cloud-based data handling in Python.

---

## 📁 Project Contents

- `main.py` — Python script that creates, uploads, and retrieves a Zarr array  
- `requirements.txt` — Python dependencies  
- `README.md` — Setup and usage instructions  
- (Optional) `zarr-storage-project-xxxxx.json` — GCP service account key (not included)

---

## ⚙️ Requirements

- Python 3.8 or newer  
- A Google Cloud Platform (GCP) service account key file

Install all dependencies using:

```bash
pip install -r requirements.txt
```

Required libraries:
```
numpy  
zarr  
gcsfs
```

---

## 🛠 How to Set Up Google Cloud Storage (Key Pair Generation)

If you prefer to use your own Google Cloud credentials instead of the provided key file, you can follow these steps to create your own S3-like storage and key:

1. **Create a Google Cloud Project**  
   Visit: https://console.cloud.google.com/

2. **Enable Cloud Storage API**  
   Go to: `APIs & Services > Library > Cloud Storage`  
   Click "Enable".

3. **Create a Storage Bucket**  
   Navigate to: `Cloud Storage > Buckets`  
   Click “Create Bucket” and follow the prompts.  
   (You can use a name like `zarr-test-bucket-xxxxx`)

4. **Create a Service Account**  
   Go to: `IAM & Admin > Service Accounts`  
   Click “Create Service Account”  
   Grant the role: Cloud Storage > Storage Admin

5. **Generate a JSON Key File**  
   - Open the created service account  
   - Go to the "Keys" tab  
   - Click “Add Key” → “Create New Key” → Select JSON  
   - Download the `.json` file

6. **Use the Key in Your Project**  
   Save the downloaded file into your project directory.  
   Then in `main.py`, use it like this:

   ```python
   gcs = gcsfs.GCSFileSystem(token='your-key.json')
   ```

---

## 🔐 Service Account Key

For security reasons, the `.json` key file is not included in this repository.  
However, you can download it from the following secure link to test the script:

[Download the service account key](https://drive.google.com/file/d/1P4hyfF_nwtBlddg7n1nTWAQ-0c1kfpKs/view?usp=sharing)

Make sure to place the downloaded `.json` file in the project directory before running the script.

---

## ▶️ How to Run

After completing the setup, run the script with:

```bash
python main.py
```

Expected output:

```
✅ Array successfully saved to local Zarr directory.
✅ Successfully uploaded to GCS at: zarr-test-bucket-20250503/test_array.zarr
📥 Successfully read array back from GCS download:
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
```

---

## ✅ Conclusion

This project satisfies the assignment criteria by:

- Creating a sample NumPy array and saving it in Zarr format  
- Uploading the array to a Google Cloud Storage bucket  
- Downloading and reading it back to verify data integrity

If you need assistance or access to the credentials, feel free to contact the project author.
