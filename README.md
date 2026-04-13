# DSI-SLAIF Workshop

Welcome to the DSI-SLAIF Workshop! This repository contains all code and materials required for the workshop.

## Exercises and Directory Structure

The repository is organized into three main exercises:
- `01_model_inference/` - **Local Inference:** The point of this exercise is to learn how to load and run LLM inference locally using both the standard Hugging Face `transformers` library and the highly optimized `vLLM` engine.
- `02_rag/` - **RAG-based Predictions:** This exercise focuses on Retrieval-Augmented Generation (RAG). You will learn how to combine a vector database with an LLM to generate answers based on a retrieved external context.
- `03_local_server/` - **Local Inference Server:** The goal of this exercise is to set up a production-ready local inference server by integrating `vLLM` as a backend and `OpenWebUI` for a ChatGPT-like web interface.

> **Note:** Jupyter notebooks are used **only** for the first two exercises (`01_model_inference` and `02_rag`). For the third exercise (`03_local_server`), **only local setup is possible**, as it requires deploying local server infrastructure.

## Running the Code

For the first two exercises, there are two primary ways to run the code: locally on your machine or via Google Colab. The third exercise must be run locally. 

**Note:** There are separate notebooks for local and Colab setups. The main difference is that local setup does not require library installation on the fly, as required libraries are already a part of Docker images. Moreover, Colab notebooks use quantized models to fit within the free tier GPU memory limits. For the local usage, we assume that you are using a GPU with at least 40GB of VRAM. If you have less VRAM, you will need to use quantized models.

### 1. Google Colab (Recommended for ease of use)

To run the notebooks seamlessly in Google Colab:
1. Open [Google Colab](https://colab.research.google.com/) and choose to open a notebook from GitHub.
2. Provide the URL to this repository and select the notebook you want to explore.
3. **Change the Runtime:** Go to **Runtime > Change runtime type** and ensure that a hardware accelerator (like a T4 GPU) is selected.
4. Cells at the beginning of the notebooks will typically contain the necessary commands (e.g., `!pip install ...`) to set up the dependent libraries entirely within the Colab environment.

### 2. Local Environment Setup

If you have a local GPU and prefer to run the setup entirely on your machine, we have provided a Docker configuration.

#### Step 1: Environment Variables
First, you need to set up your local environment file. Copy the provided `.env.example` file and fill it with your own specific values:

```bash
cp .env.example .env
```
Open the `.env` file and correctly point `CODE_DIR` to the root folder of this repository, and `MODELS_DIR` to the directory where you want to cache downloaded Hugging Face models.

#### Step 2: Download Models

**Note 1:** If you are using Google Colab, you can skip this step as the models will be downloaded automatically in the notebook.

**Note 2:** If you want to download the models on the fly, you can skip this step as well. In that case, you will need to remove the mount of models in the `docker-compose.yml` file. Additionally, you will need to modify the code to use HF IDs instead of local paths.

Before starting the notebook, you need to download the required models. You can do this by running the `download_models` Docker Compose service:

```bash
docker compose run --rm download_models
```
*Note: This will download models into your configured `MODELS_DIR`.*

#### Step 3: Run the Workshop Notebook
Once the models have been successfully downloaded, you can start up the Jupyter Notebook server utilizing your local GPU:

```bash
docker compose up workshop_notebook
```
Look at your terminal output for the local URL (usually `http://127.0.0.1:8000/...` with a token) and open it in your browser. If you are working on a remote machine, you will need to use SSH port forwarding to access the notebook. You can do this by running the following command:

```bash
ssh -N -L 8000:localhost:8000 <username>@<remote-machine>
```