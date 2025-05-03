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
- A Google Cloud Platform (GCP) account with Cloud Storage enabled

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

## ☁️ Google Cloud Setup Steps

To run the script using your own GCP credentials:

1. **Create a Google Cloud project**  
   Visit: https://console.cloud.google.com/

2. **Enable Cloud Storage API**  
   Go to: `APIs & Services > Library > Cloud Storage`

3. **Create a Storage Bucket**  
   Example name: `zarr-test-bucket-20250503`

4. **Create a Service Account**  
   - Go to: `IAM & Admin > Service Accounts`  
   - Click “Create Service Account”  
   - Grant role: `Storage Admin`

5. **Download a JSON Key File**  
   - Go to the service account’s “Keys” tab  
   - Click “Add Key” → “Create New Key” → JSON  
   - Save the `.json` file to your project folder

6. **Update the Python Script**  
   Modify this line in `main.py` with your file name:

   ```python
   gcs = gcsfs.GCSFileSystem(token='your-key.json')
   ```

---

## 🔐 Service Account Key

For security reasons, the `.json` key file is not included in this repository.  
However, you can download it from the following secure link to test the script:

👉 [Download the service account key](https://drive.google.com/file/d/1P4hyfF_nwtBlddg7n1nTWAQ-0c1kfpKs/view?usp=sharing)

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

For any questions or if you need help accessing the key, feel free to contact the project author.
