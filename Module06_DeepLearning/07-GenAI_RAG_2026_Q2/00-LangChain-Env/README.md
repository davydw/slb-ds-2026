# ⚙️ Setting up LangChain 🦜🔗

## 🎯 Goal of this challenge

Setting up a separate environment for our LLM applications.

In this unit we need a lot of new packages. Some of these packages are not compatible with the package versions we needed for other parts of the bootcamp.

So we will set up a new virtual environment. That way we have two separate python environments, and our packages will not conflict. 🦾

This is something you will often do for your projects: create dedicated virtual environments.

## 🐍 Create a new virtual environment

If any of these steps fail, ask a TA for help.

👣 Make sure you're in the challenge folder:

```bash
cd ~/code/<user.github_nickname>/{{local_path_to("06-Deep-Learning/07-GenAI-and-RAG/00-LangChain-Env")}}
```
👣 Move to the unit's main folder:

```bash
cd ..
```

🐍 Check your Python version. It should output something like `3.12.9`:

```bash
python --version
```

🐍 Create the virtual env (replace `<YOUR_PYTHON_VERSION>` below with the output of the previous command (e.g. `3.12.9`))

```bash
pyenv virtualenv <YOUR_PYTHON_VERSION> langchain-env
```

🐍 Activate the virtual env locally, so that all challenges in this unit will use this virtual env:

```bash
pyenv local langchain-env
```

✅ Make sure your Terminal displays `[🐍 langchain-env]` to the right.


⚙️ Finally, upgrade pip (pip is the package installer):

```bash
pip install --upgrade pip
```


## 📦 Install the packages

Navigate back to this challenge's folder:

```bash
cd ~/code/<user.github_nickname>/{{local_path_to("06-Deep-Learning/07-GenAI-and-RAG/00-LangChain-Env")}}
```

In this folder, we created a `requirements.txt` file with all the requirements for this unit's challenges. We just need to `pip install` it to have all of them:

```bash
pip install -r requirements.txt
```

In essence we are installing:
- Jupyter Notebook and all its dependencies
- Classics like Pandas and NumPy
- `google-genai` to interact directly with Google's Gemini LLM
- `langchain`
- `langchain-google-genai` so we can use Gemini throug LangChain
- `langchain-community` with extra tools
- `langchain-chroma`, a vector store
- `pypdf`, to load pdf files

## 🔑 Authenticate to use Gemini through an API

In this unit's challenges we'll make use of Gemini, Google's flagship LLM.

Google offers two possibilities to use Gemini through an API:
- The standalone Gemini Developer API,
- The Vertex AI Gemini API, part of the Google Cloud Platform (GCP).

The standalone API is the fastest way to create Gemini-powered apps. It used to have a generous free tier, but this free tier has been reduced enormously in December 2025, and is not sufficient for what we'll do in this unit.

You have already created a free trial account on Google Cloud, either on setup day (for full time batches), or just recently (for part time and flex batches). This will allow us to use GCP's Vertex AI Gemini API, and pay for it using our free credits.

### Google Cloud setup for the challenges

Let's set up Google Cloud for this unit's challenges.

:warning: This assumes you have already set up Google Cloud on setup day (for full time batches), or just recently (for part time and flex batches). If you're unsure whether or not you have done that part of the setup, follow the instructions below. If you haven't done the GCP setup, you'll be blocked in step 4. In that case, ask a TA for help.

1. Make sure you're in this challenge's folder:

    ```bash
    cd ~/code/<user.github_nickname>/{{local_path_to("06-Deep-Learning/07-GenAI-and-RAG/00-LangChain-Env")}}
    ```

1. Copy the `.env.vertex.sample` file into a new `.env` file in the folder that will contain all of this unit's challenges:

    ```bash
    cp .env.vertex.sample ../.env
    ```

1. Open the `.env` file with your favourite code editor:

    ```bash
    code ../.env
    ```

1. Back in your terminal, run this command:

    ```bash
    gcloud config get project
    ```

    On the first line of the output, it will give you the name of the project you have created during the setup.

    🚫  If it does not, ask a TA for help. There is probably something wrong with your GCP setup. 🚫  Do not try to fix things yourself. Do not ask an LLM (that includes Wott) for help. Ask a TA. 🚫

    <details>
      <summary>Note for TAs
      </summary>

      Check the teacher guidelines for troubleshooting steps.

    </details>
    <br/>

1. In the `.env` file you created before, replace `your_project_id` with the name of your project (the output of the previous step).

1. Save the file and close it.

1. Finally, let's enable Vertex AI on your project. Run the following line in your terminal:

    ```bash
    gcloud services enable aiplatform.googleapis.com
    ```

    It should output `Operation "operations/......." finished successfully.` If it doesn't, ask a TA for help.


Skip the next part (it's for reference only) and proceed to the _Check your installation step_.


### 🔑 Google Gemini API key

🚧 This part is **for reference only**, in case you ever want to use the standalone API. Skip this for now. 🚧

<details>
  <summary>Instructions for the Gemini Developer API
  </summary>

To use Gemini through the Gemini Developer API, you need to sign up to get an API key for Google's Gemini API.

Let's get started:

1. Browse to `https://aistudio.google.com/apikey`
1. If you aren't signed in with your Google account yet, sign in.
1. In the top right corner, click on the blue `Create API key`.
1. Follow the steps to create your API key. Remember: no need to set up billing, we will stick to the free tier.

We don't want to save our personal API key straight into the notebooks and `.py` files we'll create. Think about: we might want to share our code later on with others, but they shouldn't get our API keys.

Instead, we will save the key in a separate file `.env`. We will then load the key from that file into memory so that the libraries can use it when they need to authenticate with the Gemini API.

Let's do this:

1. Make sure you're in this challenge's folder:

    ```bash
    cd ~/code/<user.github_nickname>/{{local_path_to("06-Deep-Learning/07-GenAI-and-RAG/00-LangChain-Env")}}
    ```

1. Copy the `.env.gemini.sample` file into a new `.env` file in the folder that will contain all of this unit's challenges:

    ```bash
    cp .env.gemini.sample ../.env
    ```

1. Open the `.env` file with your favourite code editor:

    ```bash
    code ../.env
    ```

1. In the `.env` file, replace `your_gemini_api_key` with the API key you obtained.

1. Save the file and close it.

</details>


## ✅ Check your installation

```bash
jupyter notebook check.ipynb
```

## 🏁 Finished

You now have a fresh environment to work with LLMs.

Just remember to always check that you are using the `langchain-env` environment. Especially when you are using VS Code, make sure to select this new environment.

Don't forget to commit and push this challenge.
