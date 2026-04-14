# Local LLM Server Infrastructure

This directory contains the necessary configurations to run a comprehensive local Large Language Model (LLM) serving stack, utilizing hardware resources alongside a standard OpenAI-compatible API mapping.

## Components Breakdown

The stack comprises three main components orchestrated through Docker Compose:

1. **vLLM Server:**  
   vLLM is a highly optimized, high-throughput, and memory-efficient LLM inference engine. It is responsible for directly loading our models (e.g., `GaMS3-12B-Instruct`) onto the GPU and efficiently handling generation requests. It runs on port `8001`.
    
2. **LiteLLM Proxy:**  
   LiteLLM acts as an API gateway/proxy layer that routes incoming and outgoing requests. It allows us to standardize our API consumption (translating backend model endpoints into perfect OpenAI API format), mapping local models to specific names, logging requests, and managing API keys. It runs on port `4000` and proxies traffic to the underlying vLLM server.

3. **OpenWebUI:**  
   OpenWebUI provides a user-friendly, ChatGPT-like web interface locally. It is configured to point directly to the LiteLLM proxy acting as the OpenAI backend, allowing users to interact with our self-hosted models natively using a fully-featured frontend. It runs on port `3000`.

---

## Instructions

### 1. Running the Local Server

To launch the entire stack in the background, navigate to this directory (`03_local_server`) and use Docker Compose:

```bash
cd 03_local_server
docker-compose up -d
```

You can view the logs of the running services to ensure everything started correctly:
```bash
docker-compose logs -f
```

*Note: Extracting and loading large models in the `vllm` service may take a few moments depending on GPU capabilities. The OpenWebUI will be accessible at `http://localhost:3000` once the services are fully up.*

To stop the server:
```bash
docker-compose down
```

### 2. Testing the Server

You can use the provided Python scripts to verify that everything is working. Ensure you have the `openai` python package installed (`pip install openai`).

#### A) Test Direct Endpoint (vLLM)
This test connects directly to the underlying `vLLM` server handling the inference without hitting the proxy.

Run the script:
```bash
python test_vllm_server.py
```

#### B) Test Proxy Endpoint (LiteLLM)
This test connects via the `LiteLLM` instance. Since production apps and our OpenWebUI use this proxy, testing this ensures the API routing is working gracefully.

Run the script:
```bash
python test_litellm_proxy.py
```

Both scripts should generate a response from the model confirming your prompt.
