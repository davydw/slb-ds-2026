
# GCP Compute Engine - Iris Model Training and Storage

This exercise will guide you through setting up a virtual machine on Google Compute Engine (GCE), creating a virtual environment, training a machine learning model using the Iris dataset, saving the model as a pickle file, and uploading it to a Google Cloud Storage (GCS) bucket.

## Prerequisites

1. **Google Cloud Account**: Ensure you have access to Google Cloud and billing is enabled.
2. **Google Cloud SDK Installed**: The `gcloud` CLI must be set up locally.
3. **Project Setup**: Ensure a project is created in Google Cloud with Compute Engine and Cloud Storage API enabled.

## Steps

### 1. Create a Virtual Machine on Google Compute Engine (GCE)

1. **Open the Google Cloud Console** and navigate to **Compute Engine > VM Instances**.
2. Click on **Create Instance**.
3. Choose the following settings:
   - **Name**: `iris-vm`
   - **Region**: Choose any preferred region.
   - **Machine type**: Choose an appropriate size, e.g., `e2-micro`.
   - **Boot disk**: Use a standard Ubuntu image (e.g., `Ubuntu 22.04 LTS`).
4. Click **Create**.

### 2. SSH into the Virtual Machine

1. Once the VM is created, click on **SSH** next to your VM instance.
2. In the terminal, update the system and install Python 3:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip
   ```

3. Install the Python virtual environment package:
   ```bash
   sudo apt install python3.11-venv
   ```

### 3. Create a Virtual Environment and Install Packages

1. Create a virtual environment to manage your Python dependencies:
   ```bash
   python3 -m venv myenv
   ```

2. Activate the virtual environment:
   ```bash
   source myenv/bin/activate
   ```

3. Install the necessary Python libraries inside the virtual environment:
   ```bash
   pip install scikit-learn pandas google-cloud-storage
   ```

### 4. Create a Python Script for Model Training

1. In the SSH terminal, create a new Python file:
   ```bash
   nano train_iris.py
   ```

2. Add the following code to the file:

```python
import pickle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from google.cloud import storage

# Load the Iris dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save the model to a pickle file
model_filename = 'iris_model.pkl'
with open(model_filename, 'wb') as model_file:
    pickle.dump(model, model_file)

# Function to upload file to GCS bucket
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    # Uploads a file to the bucket.
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

# Replace with your GCS bucket name
bucket_name = 'your-gcs-bucket-name'
upload_to_gcs(bucket_name, model_filename, model_filename)
```

3. Save the file (`Ctrl + X`, then `Y` and `Enter` to confirm).

### 5. Create a GCP Storage Bucket

1. Go to **Google Cloud Console** and navigate to **Cloud Storage**.
2. Click **Create Bucket** and follow the instructions to create a bucket.
   - Name it something like `iris-model-bucket`.
   - Set location to **multi-region** for this example.
   - Set the access to **Uniform**.

3. In your SSH session, authenticate your VM to access Google Cloud services:
   ```bash
   gcloud auth application-default login
   ```

4. Make sure you replace the placeholder `your-gcs-bucket-name` in the Python script with the actual bucket name.

### 6. Run the Python Script on GCE VM

1. In the SSH terminal, run the Python script:
   ```bash
   python3 train_iris.py
   ```

This will train a RandomForest model on the Iris dataset, save it as a pickle file, and upload it to your specified Google Cloud Storage bucket.

### 7. Verify the Model in GCS

1. Go back to the **Cloud Storage** section in Google Cloud Console.
2. Navigate to your bucket, and you should see the `iris_model.pkl` file.

### 8. Deactivate the Virtual Environment (Optional)

When you’re done, you can deactivate the virtual environment by running:

```bash
deactivate
```

If you need to use the virtual environment again, you can reactivate it by running:

```bash
source myenv/bin/activate
```

## Optional Improvements
- Have students test loading the model back from the GCS bucket.
- Experiment with different machine learning algorithms or dataset preprocessing techniques.

## Summary of Key Concepts:
- Setting up and using a GCE VM.
- Creating and using Python virtual environments.
- Training and saving machine learning models using Scikit-learn.
- Using Google Cloud Storage to store files from a Python program.
