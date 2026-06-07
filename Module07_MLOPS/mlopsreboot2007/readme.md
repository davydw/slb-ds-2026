# Introduction

In this reboot, you will complete the development of a machine learning application. This includes building and exporting a model pipeline (already provided in a notebook) 📊, loading the pipeline, building a predict function 🧠, and creating an API to serve predictions 🔮. You will then containerize the API using Docker 🐳 and deploy it to the cloud ☁️. A frontend application will be connected to the API to provide a user-friendly interface for making predictions 🖥️.

Follow the instructions carefully, take your time, and have fun deploying! 🎉

## 1. 🚀 Setting Up a New Project on Google Cloud Platform (GCP)

To deploy your app using Google Cloud services, follow these steps to set up a new GCP project:

### 1.1 📋 Creating a New GCP Project

1. **Go to the Google Cloud Console**: [Google Cloud Console](https://console.cloud.google.com/)
2. **Click the project dropdown** in the top navigation bar and select **New Project**.
3. **Fill in the project name**.
4. **Click `Create`** to generate a new project.

### 1.2 📛 Save the Project ID

Once the project is created, you'll see a **project ID**. This ID is important because it will be referenced throughout the rest of the setup. Make sure to save it.

You can find the project ID in the **Google Cloud Console** under **Project Settings** or by selecting your project in the top navigation bar.

### 1.3 🔐 Enable Required APIs

Enable the following APIs for your new project:

1. **Artifact Registry API**: Required for storing and managing Docker images.
2. **Cloud Run API**: Required for deploying your containerized app to Google Cloud Run.

You can enable these by going to the **API & Services** section of the Google Cloud Console and searching for each API.

### 1.4 🔑 Set Up Authentication

1. Install the Google Cloud SDK by following the instructions [here](https://cloud.google.com/sdk/docs/install).
2. Once installed, authenticate your GCP account using (in your terminal):

```bash
gcloud auth login
```

3. Set your new project as the active project using your saved project ID:

```bash
gcloud config set project <your-project-id>
```

Your project is now ready for deploying Dockerized apps.

---

## 2. 🏗️ Setting Up a Virtual Environment Using pyenv

### 2.1 🎓 Introduction to pyenv

pyenv is a popular tool used to manage multiple versions of Python on your system. It allows you to easily switch between different versions of Python and create virtual environments tied to specific versions. This is particularly useful when working on projects that require different Python versions.

### 2.2 🛠️ Installation and Setup

#### 2.2.1 📥 Install pyenv
Follow the installation instructions on the official pyenv GitHub repository. This typically involves running a few commands in your terminal to set up pyenv on your system.

#### 2.2.2 📂 Navigate to Your Project Root
Before creating a virtual environment, navigate to the root directory of your project. This ensures that the environment will be set up within the project folder.

```bash
cd /path/to/your/project
```

#### 2.2.3 🐍 Install Required Python Version
Use pyenv to install the specific version of Python that your project requires. For example, to install Python 3.9:

```bash
pyenv install 3.10.6
```

Explanation: This command downloads and installs the specified version of Python. You can install multiple versions and switch between them as needed.

#### 2.2.4 🌐 Create a Virtual Environment
With the desired Python version active, create a virtual environment. You can use pyenv's virtualenv plugin, which integrates directly with pyenv:

```bash
pyenv virtualenv 3.10.6 myenv
```

Explanation: This command creates a virtual environment named myenv using Python 3.9.1. The virtual environment will be tied to this specific Python version.

#### 2.2.5 ▶️ Activate the Virtual Environment
Set the newly created virtual environment as the local environment for your project:

```bash
pyenv local myenv
```

Alternatively, you can activate it directly using:

```bash
pyenv activate myenv
```

Explanation: Activating the virtual environment ensures that any Python commands or package installations you perform are done within this environment.

### 2.3 💡 Importance of Virtual Environments

- **Version Management**: pyenv allows you to easily switch between different Python versions, making it ideal for projects that require specific Python versions.
- **Project Isolation**: The virtual environment ensures that dependencies are isolated from other projects, preventing version conflicts.
- **Consistency Across Systems**: Using pyenv helps maintain consistent Python environments across different machines, crucial for collaboration and deployment.



## 3. 🐍 Creating a Python Package

In this section, we'll walk through the process of creating a Python package that contains a utility function for model predictions. This function will load a model stored in a pickle file, take in four feature values, and return a prediction. 🎯

### 3.1 📓 Familiarize yourself with the Notebook
Before starting, open the notebook file in the `notebooks` folder (`my_notebook.ipynb`). Review its contents to understand the structure and any relevant code or data. Once familiar, run the notebook to ensure everything works properly. This will give you context and set the foundation for the following steps. 🚀

Now, you're ready to move on to the next section. 🏁



### 3.2 ✏️ Creating the `iris.py` File

Start by creating a folder named `package_folder` at the root of your project directory. Inside this folder, create a file called `iris.py`. In this, code a function called `my_prediction_function`. This function must:

1. Take as arguments sepal_length, sepal_width, petal_length, petal_width.
2. Load the Machine Learning model pickle file, the one exported by the notebook.
3. Pass the arguments to the model to get a prediction.
4. Return the prediction 🤖

Go ahead! 🚀

<details>
<summary>🔍 Click here to see the solution</summary>

Here’s the Python code for `iris.py`:

```python
import pickle

def my_prediction_function(sepal_length, sepal_width, petal_length, petal_width):
    # Load the model from the pickle file
    with open('models/best_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Use the model to predict the given inputs
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    return prediction
```
</details>

### 3.3 🗂️ Creating the `__init__.py` File

To make the `package_folder` a Python package, you need to add a blank `__init__.py` file in the `package_folder` directory. This will signal Python that the folder is a package that can be imported.

Go ahead! 🛠️

### 3.4 📝 Create and Update the `requirements.txt` File

**Purpose**: The `requirements.txt` file lists all the Python packages your project depends on. This allows others to easily install the necessary packages in their environment, ensuring that the code runs as expected. 🔧

**How to Create/Update**:
1. At the root of your project folder (⚠️ not your package folder!), create a file named `requirements.txt`.
2. Add the required packages to this file. At a minimum, you'll need to include `scikit-learn`. 📦
3. You can generate this file automatically by running the following command in your terminal:
   ```bash
   pip freeze > requirements.txt
   ```
   This command will capture all installed packages in your environment and their versions, ensuring consistency across different setups. 🖥️

An example `requirements.txt` file could look like this:

```
scikit-learn
```

### 3.5 🛠️ Creating the `setup.py` File

At the root of your project directory (outside `package_folder`), you'll need to create a `setup.py` file. This file is crucial for defining your Python package, including its metadata and dependencies, allowing others to install and use it easily. 📋

The `setup.py` file typically includes the following elements:

1. **Package Metadata**: You'll need to specify basic details about your package, such as:
   - **name**: The name of your package. This is what will be used when someone installs your package (e.g., `pip install package_name`). 📛
   - **version**: The version of your package. You can start with `"0.0.1"` for an initial version. 🆕
   - **author** (optional): You may want to include the author's name and contact information. 👤

2. **Dependencies**: Your package will likely depend on external libraries. To manage these, the `setup.py` will read from the `requirements.txt` file you created earlier. It’s important that the `requirements.txt` file lists all the dependencies your package needs (e.g., `fastapi`, `uvicorn`, `scikit-learn`, etc.). 📦

3. **Packages**: You’ll also need to specify which packages should be included when your package is installed. This can be done using `find_packages()` to automatically find and include all relevant Python modules and sub-packages within your project. 📚

4. **Installation Requirements**: Specify how external libraries and dependencies should be installed. This typically involves reading from the `requirements.txt` file and parsing its content. 📄

In summary, your `setup.py` file should define:
- Basic package information (name, version, author, etc.).
- A method to install dependencies from `requirements.txt`.
- Which Python packages or modules should be included.

Once you've defined these elements, you’ll be ready to install your package locally or share it with others. 💻

We've provided you with the `setup.py` file below 👇. ctrl+c, ctrl+v 😉

```python
from setuptools import find_packages, setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(
    name='package_folder',
    version="0.0.1",
    install_requires=requirements,
    packages=find_packages()
)
```

### 3.6 📥 Installing the Package

To install your package locally in editable mode, use the following command in your terminal from the project’s root directory:

```bash
pip install -e .
```

This will install the package in editable mode, meaning any changes made to the code will be reflected without needing to reinstall the package. 🔄

Once the package is installed, you can use the `my_prediction_function` in other parts of your project like so:

```python
from package_folder.utils import my_prediction_function
```

This structure allows you to easily extend and reuse the function in various locations on your computer. Try it out if you don't believe me 😉. It also allows you to reuse the function in various parts of your application, such as within a FastAPI project. 🌐


## 4. 🌐 Creating an API

### 4.1 🔌 Introduction to APIs

An API (Application Programming Interface) allows different software systems to communicate with each other. In this exercise, you'll create a RESTful API using FastAPI, which will expose a machine learning model as a service. This API will accept input parameters, make a prediction using a pre-trained model, and return the result as a JSON response.

### 4.2 🚀 Setting Up FastAPI

### 4.2.1 Update your `requirements.txt` file

In order to run the API, you'll need two libraries: `fastapi` and `uvicorn`  (the ASGI server to run your FastAPI app). **Add them to your `requirements.txt` file.**

#### 4.2.2 🏗️ Organizing Your Project

1. **Inside `package_folder`, create a Python file named `api_file.py`**, which will house the code for your FastAPI application. You'll define your API routes, including endpoints for predictions and health checks, in this file.

2. **Proceed to follow the instructions below** to complete your API setup within `api_file.py`. If you're are struggling, unfold the solution at the end of the section.

#### 4.2.3 🏗️ Create FastAPI Instance

Inside `api_file.py`, initialize a FastAPI instance that will serve as the core of your application. Define routes (endpoints) that the API will expose. Each route corresponds to a specific function that processes the request and returns a response.

#### 4.2.4 🏠 Define Root Endpoint

Create a simple root endpoint (e.g., `/`) that returns a basic greeting message, allowing you to verify that the API is running correctly.

#### 4.2.5 🔮 Create Prediction Endpoint

Define an endpoint (e.g., `/predict`) that accepts input parameters such as `sepal_length`, `sepal_width`, `petal_length`, and `petal_width`. This endpoint should load a pre-trained machine learning model from the `models/best_model.pkl` file, make a prediction, and return the result.

<details>
<summary>🔍 Click here to see the solution</summary>

```python
from fastapi import FastAPI
import pickle

# FastAPI instance
app = FastAPI()

# Root endpoint
@app.get("/")
def root():
    return {'greeting':"hello"}

# Prediction endpoint
@app.get("/predict")
def predict(sepal_length, sepal_width, petal_length, petal_width):

    # Load the model
    with open('models/best_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Use model to predict inputs
    prediction = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])

    # Return prediction
    return {"prediction": float(prediction[0])}
```
</details>

#### 4.2.5 📦 Install as a package

Finally, reinstall your package so that it includes the new libraries that were added to the `requirements.txt`, as well as the api code. To do so, **run the following in your terminal, while being located at the root of your project:**

   ```bash
   pip install -e .
   ```

### 4.3 🧪 Running the API Locally and Testing with FastAPI /docs

Before deploying the API to production, it is recommended to run it locally and verify its functionality. FastAPI provides an automatic interactive documentation interface, available at `/docs`.

#### Steps to Run the API Locally:

1. **Start the FastAPI app locally** using Uvicorn with the following command:

   ```bash
   uvicorn package_folder.api_file:app --reload --port 8000
   ```

   This command will start the API on `http://127.0.0.1:8000/`. The `--reload` flag ensures that the server reloads if you make any changes to your code.

2. **Access the FastAPI documentation**:

   FastAPI generates interactive API documentation at `/docs`. You can access it by navigating to:

   ```bash
   http://127.0.0.1:8000/docs
   ```

   From the `/docs` page, you can explore all the available endpoints and even test them directly from the browser by sending requests to your API.

By running the API locally and testing it through `/docs`, you can ensure everything is functioning as expected before deploying it to the cloud.

To shut down the process, hold `ctrl + c` in your terminal.

## 5. 🐳 Dockerizing Your Application

### 5.1 🎓 Introduction to Docker

Docker is a platform for developing, shipping, and running applications in containers. Containers are lightweight, standalone, executable packages that include everything needed to run an application: code, runtime, system tools, libraries, and settings.

Benefits of using Docker:
- Consistency across development, testing, and production environments
- Easier deployment and scaling
- Isolation of applications and their dependencies

### 5.2 📄 Creating a Dockerfile

A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. Follow these steps to create a Dockerfile for your project:

#### 5.2.1 ➕ Create the Dockerfile
At the root of your project, create a new file named `Dockerfile` (no file extension).

```bash
touch Dockerfile
```

#### 5.2.2 ✏️ Edit the Dockerfile
Open the Dockerfile in your preferred text editor. Your Dockerfile should include the following elements, each on a separate line (unfold solution at the end of the section if needed):

1. **Base Image**: Specify a base image that includes Python 3.8.12. Use a slim version to keep the image size small.

2. **Copy Package Folder**: Add a command to copy your project's package folder into the Docker image. This should include all your application code.

3. **Copy Requirements File**: Include a command to copy your requirements.txt file into the Docker image. This file lists all the Python packages your project needs.

4. **Copy Models**: Add a command to copy your models folder into the Docker image. This folder should contain any pre-trained machine learning models your API uses.

5. **Install Dependencies**: Include a command that uses pip to install all the Python packages listed in your requirements.txt file.

6. **Specify Run Command**: Finally, add a command that will be executed when the container starts. This should use Uvicorn to run your FastAPI application, making sure to specify the correct path to your API file and the app object within it. The command should also set the host to 0.0.0.0 to make the application accessible outside the container.

Each of these commands should be written using the appropriate Dockerfile syntax. The result will be a complete Dockerfile that sets up the environment for your Python API application.

<details>
<summary>🔍 Click here to see the solution</summary>

```dockerfile
FROM python:3.8.12-slim

COPY package_folder package_folder
COPY requirements.txt requirements.txt
COPY models models

RUN pip install -r requirements.txt

CMD uvicorn package_folder.api_file:app --host 0.0.0.0
```

Let's break down each line of this Dockerfile:

1. `FROM python:3.8.12-slim`: This specifies the base image we're building from. In this case, it's a slim version of Python 3.8.12.

2. `COPY package_folder package_folder`: This copies your project's package folder into the Docker image.

3. `COPY requirements.txt requirements.txt`: This copies your requirements.txt file into the Docker image.

4. `COPY models models`: This copies your models folder into the Docker image.

5. `RUN pip install -r requirements.txt`: This command installs all the Python packages listed in your requirements.txt file.

6. `CMD uvicorn package_folder.api_file:app --host 0.0.0.0`: This specifies the command to run when the container starts. It starts the Uvicorn server to run your FastAPI application.

</details>

### 5.3 💡 Importance of Dockerization

- **Portability**: Your application can run on any system that has Docker installed, regardless of the underlying OS or installed libraries.
- **Scalability**: Easily scale your application by running multiple containers.
- **Isolation**: Each container runs in its own environment, preventing conflicts between applications.
- **Version Control**: Docker images can be versioned, allowing you to maintain different versions of your application environment.



### 5.4 📁 Using Environment Variables, `.env` and `.envrc` Files

Before running Docker commands, it’s essential to manage environment-specific values, like project names, image tags, API keys, and database URLs, in a secure and flexible way. This can be achieved by using a `.env` file, which allows you to manage configuration settings and sensitive information. You can easily load these variables in Python using the `python-dotenv` package. Additionally, using a `.envrc` file with `direnv` allows you to automatically load these environment variables when you enter the project directory.

#### 5.4.1 Setting Up Environment Variables with `.env` and `.envrc`

1. **Create a `.env` file**: At the root of your project, create a `.env` file to store key environment variables. Here's a breakdown of the variables you need:

```
IMAGE=my-api-app
GCP_PROJECT=my-gcp-project
GCP_REGION=europe-west1
ARTIFACTSREPO=my-artifact-repo
MEMORY=512Mi
```

- **IMAGE**: This is the name of the Docker image you're about to create. You can name this image whatever you like, but it should be something meaningful, like `my-api-app`, to identify your application.

- **GCP_PROJECT**: This is the **ID of the Google Cloud Project** you created. You can find this ID in your [Google Cloud Console](https://console.cloud.google.com/). It's required for interacting with GCP services like Artifact Registry and Cloud Run.

- **GCP_REGION**: This is the region where you want to deploy your application on Google Cloud. You can choose a region from the [list of available regions and zones](https://cloud.google.com/compute/docs/regions-zones). A common region choice in europe is `europe-west1`.

- **ARTIFACTSREPO**: This is the name of your Docker container repository within Google Cloud's Artifact Registry. You can name this repository however you like, such as `my-artifact-repo`, as it will store your Docker images for deployment.

- **MEMORY**: This refers to the amount of memory allocated to your application when deployed on Google Cloud Run. You can adjust this depending on your application’s requirements. A common value is `512Mi`, which stands for 512 megabytes. Larger applications may need more memory.

Ensure that these values are correctly set in your `.env` file before proceeding with Docker and deployment commands.

2. **Create a `.envrc` file**: At the root of your project, create a `.envrc` file. It should contain with the following line to ensure that `direnv` will automatically load your `.env` file:

```
dotenv
```

This command tells `direnv` to export the environment variables defined in the `.env` file to the shell whenever you enter the project directory.

3. **Reload `direnv`** when you modify the `.env` file or `.envrc` file:

```bash
direnv reload
```

This ensures that every time you enter the project folder, the environment variables in `.env` are automatically loaded into your shell, making the setup process seamless and reducing the risk of forgetting to load variables manually.

---

### 5.5 🧑‍💻 Building and Running Docker Locally

**Launch the docker app on your computer.** Let’s begin with the essential Docker commands for local development. We’ll use the `$IMAGE` environment variable from the `.env` file.

#### 5.5.1 🛠️ Build Container Locally

To build the Docker image for local development using the `IMAGE` variable, use this terminal command:

```bash
docker build --tag=$IMAGE:dev .
```

Explanation:
- `docker build`: Tells Docker to build a new container image.
- `--tag=$IMAGE:dev`: Uses the `IMAGE` variable from the `.env` file (which is `my-api-app`) and tags the image with `dev`.

Make sure you run this command from the root of your project, where your `Dockerfile` is located.

#### 5.5.2 ▶️ Run Container Locally

Once the image is built, run it locally using the following command, which also uses the `$IMAGE` environment variable:

```bash
docker run -it -e PORT=8000 -p 8000:8000 $IMAGE:dev
```

Explanation:
- `docker run`: Starts a new container from the built image.
- `-it`: Runs the container interactively so you can see the logs in real time.
- `-e PORT=8000`: Sets the `PORT` environment variable inside the container.
- `-p 8000:8000`: Maps port 8000 of your machine to port 8000 of the container, allowing you to access the app locally via `http://localhost:8000`.

You are now accessing your API, which itself lives inside a docker container, locally on your computer 🤯. You can access the `/docs` to test out your API endpoints. Once you are done playing around, close the process by holding `ctrl + c` in your terminal.

---


### 5.6 🌍 Building a Container for Deployment

Now that we’ve successfully built and run the container locally, we can prepare it for deployment to a cloud environment like Google Cloud Run.

#### 5.6.1 📦 Build for Production

To ensure your container works correctly when deployed, you need to make a small modification to the `Dockerfile`. Specifically, you must update the `CMD` instruction to dynamically bind to the port that the cloud platform provides at runtime.

In your `Dockerfile`, change this line:

```dockerfile
CMD uvicorn package_folder.api_file:app --host 0.0.0.0
```

To this:

```dockerfile
CMD uvicorn package_folder.api_file:app --host 0.0.0.0 --port $PORT
```

#### Why this change is necessary:
When deploying to platforms like Google Cloud Run, the application’s port is assigned dynamically through the `PORT` environment variable. This change ensures that Uvicorn listens on the correct port for incoming traffic during deployment. Locally, port 8000 is typically used by default, but in production, the platform may assign a different port, which is why this update is needed.

Once the `Dockerfile` is updated, you can proceed with building the container for deployment using this command:

```bash
docker build -t $GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$ARTIFACTSREPO/$IMAGE:prod .
```

Explanation:
- This command builds a Docker image suitable for deployment, using the `IMAGE` environment variable from the `.env` file.
- Ensure that other environment variables like `$GCP_REGION`, `$GCP_PROJECT`, and `$ARTIFACTSREPO` are correctly set in your `.env` file.

If you're using an ARM-based machine (e.g., an M1 Mac), you may need to add the `--platform linux/amd64` flag to ensure compatibility with cloud environments:

```bash
docker build --platform linux/amd64 -t $GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$ARTIFACTSREPO/$IMAGE:prod .
```

#### 5.6.2 📤 Push to Container Registry

Before pushing your production image to the container registry, follow these steps to fully authenticate and grand yourself permissions:

### 1. Configure Docker to Authenticate with Google Artifact Registry:

To ensure Docker is authenticated with Google Artifact Registry, run the following command:

```bash
gcloud auth configure-docker $GCP_REGION-docker.pkg.dev
```

This command configures Docker to use your Google Cloud credentials for authentication when pushing to Artifact Registry.

### Add Permissions to Your Google Cloud Account:

Before creating the Artifact Registry, ensure you have the necessary permissions. Run the following command to add the `Artifact Registry Writer` role to your account. Replace `YOUR_PROJECT_ID` with your Google Cloud project ID and `YOUR_EMAIL` with your email address:

```bash
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID   --member="user:YOUR_EMAIL"   --role="roles/artifactregistry.writer"
```

### 2. Create an Artifact Registry Repository using .env Variables:

If you haven't already created a Google Artifact Registry repository, you can do so by running the following command using the environment variables defined in your `.env` file:

```bash
gcloud artifacts repositories create $ARTIFACTSREPO     --repository-format=docker     --location=$GCP_REGION     --description="My Docker Artifact Repository"
```

This command creates a Docker repository in Google Artifact Registry in the specified region.

### 3. Push the Docker Image:

Once the production image is built, push it to your container registry using this command:

```bash
docker push $GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$ARTIFACTSREPO/$IMAGE:prod
```

This command uploads your Docker image to Google Artifact Registry, where it can be accessed for deployment.


#### 5.6.3 🚀 Deploy to Cloud Run

To deploy the image to Google Cloud Run, use the following command. When asked, **allow Enable APIs, and allow unauthenticated invocations.**:

```bash
gcloud run deploy --image $GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$ARTIFACTSREPO/$IMAGE:prod --memory $MEMORY --region $GCP_REGION
```

This deploys your API to Cloud Run using the production Docker image you just pushed to the container registry. The `--memory` and `--region` options are set using the values from your `.env` file.

If the process worked, you should see a message in your terminal signaling that the Service has been deployed and is serving 100 percent of traffic. You should also be provided with a Service URL, the one allowing anyone in the world to connect to your API 🤯.

---

### 5.7 📄 Automating with a Makefile

Now that you’ve run several Docker commands manually, it's clear that this process can become repetitive. To streamline this, we can store these commands in a `Makefile`.

A `Makefile` allows you to define these steps as simple commands that you can run from the terminal, reducing the need to retype long Docker commands.

#### 5.7.1 Create a Makefile

Create a file named `Makefile` at the root of your project. We’ll add the commands you’ve already executed, so they can be run with a single `make` command.

#### 5.7.2 Adding Local Build and Run Commands

Let’s add the commands for building and running the container locally using the `$IMAGE` variable:

```makefile

build_container_local:
	docker build --tag=${IMAGE}:dev .

run_container_local:
	docker run -it -e PORT=8000 -p 8000:8000 ${IMAGE}:dev
```

- `build_container_local`: This will build the Docker image for local development, using the `IMAGE` environment variable.
- `run_container_local`: This will run the Docker container locally with the `PORT` environment variable.

Now, instead of typing out the full `docker` commands, you can simply run:

```bash
make build_container_local
```

And to run the container:

```bash
make run_container_local
```

#### 5.7.3 Adding Production Build and Deployment Commands

You can also add commands for building and deploying the container to production using the `$IMAGE` variable:

```makefile
build_for_production:
	docker build -t ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${ARTIFACTSREPO}/${IMAGE}:prod .

# for M1 chips only
build_for_production_m1:
  docker build --platform linux/amd64 -t ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${ARTIFACTSREPO}/$IMAGE:prod .

push_image_production:
	docker push ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${ARTIFACTSREPO}/${IMAGE}:prod

deploy_to_cloud_run:
	gcloud run deploy --image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${ARTIFACTSREPO}/${IMAGE}:prod --memory ${MEMORY} --region ${GCP_REGION}
```

You can now run the following commands to automate building, pushing, and deploying:

```bash
make build_for_production
make push_image_production
make deploy_to_cloud_run
```

---

### 5.8 💡 Importance of Automation with Makefile

By using a `Makefile`, you:
- **Automate Repetitive Tasks**: Reduce manual errors and save time by automating Docker and deployment tasks.
- **Organize Commands**: Keep your commands organized and easy to run with simple `make` commands.
- **Use Environment Variables**: With a `.env` file, you can ensure the flexibility to adapt to different environments without changing the core commands.

This method provides a robust and maintainable way to manage your Docker container lifecycle both locally and in production.


## 6. 🌐 Building a Frontend with Streamlit

In this section, you'll create a simple frontend for your application using Streamlit, a fast and easy way to build web applications in Python. This frontend will allow users to input feature values for the Iris dataset and get a prediction from the API you created earlier. 🚀

### 6.1 ✏️ Setting Up a Separate frontend Folder

First, step out of the project folder you've been working on until now—this will be considered the backend folder. Now, create a new, fully separate folder that will contain the frontend elements.

Inside this new folder, create a file called frontend_file.py. This file will serve as the frontend for your app. In this file, you'll use Streamlit to create sliders for users to input values for sepal length, sepal width, petal length, and petal width. The values will then be sent to your API, and you'll display the prediction on the web page.

The API URL that you’ll be calling will be the one given to you in the previous sections when you deployed on GCP. You can find it on [GCP Cloud Run](https://console.cloud.google.com/run).

### 6.2 🖥️ Coding Your Frontend

To create your frontend, follow these steps (or unfold the solution at the end of the section!):

1. **Install `streamlit`, create a new `requirements.txt` file**, and add `streamlit` to it.

2. **Set the Title and Description**: Use Streamlit's `st.title()` to display a title for your application (e.g., "My awesome MVP"). You can also add a short description using `st.write()`. In this case, you'll describe what the application does (e.g., "Iris predictor").

3. **Create Sliders**: For the user to input values, you’ll create four sliders using the `st.slider()` function. These sliders should correspond to the sepal length, sepal width, petal length, and petal width. Set appropriate ranges for each slider (e.g., from 0 to 4).

4. **Send a Request to Your API**: Once the user selects values using the sliders, you'll need to send those values to your API using the `requests.get()` function. Construct the URL by passing the slider values as query parameters.

4. **Display the Prediction**: When the API returns the prediction, display it on the page using `st.write()`. This will show the predicted flower category to the user.

Once you have completed these steps, your frontend will be ready to interact with the API and display predictions based on the user input. 🎨

<details>
<summary>🔍 Click here to see a solution example</summary>

Here’s what your `frontend_file.py` file might look like:

```python
import streamlit as st
import requests

st.title("My awesome MVP")

st.write("Iris predictor")

value1 = st.slider('Select a value for Sepal length', min_value=0, max_value=4, value=1, step=1)
value2 = st.slider('Select a value for Sepal width',  min_value=0, max_value=4, value=1, step=1)
value3 = st.slider('Select a value for Petal length',  min_value=0, max_value=4, value=1, step=1)
value4 = st.slider('Select a value for Petal width',  min_value=0, max_value=4, value=1, step=1)

response = requests.get(f"https://my-api-app-255873005492.europe-west1.run.app/predict?sepal_length={value1}&sepal_width={value2}&petal_length={value3}&petal_width={value4}").json() # This URL should correspond to yours

st.write(f"This flower belongs to category {str(response['prediction'])}")
```
</details>

### 6.3 🛠️ Running Streamlit Locally

After coding your `frontend_file.py` file, you can run the following command in your terminal to launch the Streamlit app locally and see how it renders:

```bash
streamlit frontend_file.py
```

This will open a web page in your browser where you can interact with the sliders and see the prediction displayed in real-time. 🎨

### 6.4 🚀 Deploying Streamlit via GitHub

Once you're happy with how your Streamlit app looks and works locally, the next step is to deploy it. To do this, you'll need to create a GitHub repository and push your project files to it. You can set up the repository fully from the terminal using GitHub's CLI. Let's walk through the steps. 👇

#### 6.4.1 🗂️ Creating a GitHub Repository and Pushing Code from the Terminal (with GitHub CLI)

Before deploying your Streamlit app, you need to create a GitHub repository and push your project files to it. Follow these steps:

1. **Install GitHub CLI**
   - If you don’t already have the GitHub CLI (`gh`) installed, you can download it [here](https://cli.github.com/). Follow the instructions for your operating system.

2. **Login to GitHub via the CLI**
   - After installing the GitHub CLI, log in to your GitHub account by running:
     ```bash
     gh auth login
     ```
   - You will be prompted to authenticate with your GitHub credentials.

3. **Initialize a Git Repository**
   - Navigate to your project folder in the terminal using the `cd` command:
     ```bash
     cd path_to_your_project
     ```
   - Initialize Git in this folder:
     ```bash
     git init
     ```

4. **Add Your Files to the Git Repository**
   - Check which files have been added or modified:
     ```bash
     git status
     ```
   - Add all of your project files to the Git staging area:
     ```bash
     git add .
     ```
   - Commit your changes with a meaningful message:
     ```bash
     git commit -m "Initial commit with Streamlit frontend"
     ```

5. **Create a GitHub Repository from the Terminal**
   - To create a new repository on GitHub directly from your terminal, run:
     ```bash
     gh repo create your-repo-name --public --source=. --remote=origin
     ```
   - This command creates a public repository (you can also use `--private` for a private one) and links it to your local repository as `origin`.

6. **Push Your Code to GitHub**
   - Now that the repository is created and linked, push your code to GitHub:
     ```bash
     git push -u origin main
     ```

Now, your project is live on GitHub! 🎉 You can view it by going to your GitHub account and checking your repositories.

#### 6.4.2 🌐 Deploying Your Streamlit App from GitHub

With your project files now on GitHub, you can easily deploy your Streamlit app using Streamlit Cloud. Here’s how to deploy it:

1. Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in.
2. Click "New app" and link it to your GitHub repository.
3. Select the branch where your `frontend_file.py` is located and click "Deploy."

Within minutes, your frontend will be live, and you'll be able to share the URL with others! 🎉
