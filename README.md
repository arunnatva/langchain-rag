# Langchain RAG Project

## Install dependencies

1. Do the following before installing the dependencies found in `requirements.txt` file because of current challenges installing `onnxruntime` through `pip install onnxruntime`. 

    - For MacOS users, a workaround is to first install `onnxruntime` dependency for `chromadb` using:

    ```python
     conda install onnxruntime -c conda-forge
    ```
    See this [thread](https://github.com/microsoft/onnxruntime/issues/11037) for additonal help if needed. 

     - For Windows users, follow the guide [here](https://github.com/bycloudai/InstallVSBuildToolsWindows?tab=readme-ov-file) to install the Microsoft C++ Build Tools. Be sure to follow through to the last step to set the enviroment variable path.


2. Now run this command to install dependenies in the `requirements.txt` file. 

Important note: the package installations had issues with Conda. With virtualenv, the installations went well, and I had to upgrade versions of langchain to latest versions of > 0.3.x

```python
pip install -r requirements.txt
```

3. Install markdown depenendies with: 

```python
pip install "unstructured[md]"
```

## Create database

Create the Chroma DB.

```python
python create_database.py
```

## Query the database

Query the Chroma DB.

```python
python query_data.py "what benefits are excluded in north carolina"
```

> You'll also need to set up an OpenAI account (and set the OpenAI key in your environment variable) for this to work.

This code is forked from the developer of this youtube link  (https://www.youtube.com/watch?v=tcqEUSNCn8I&ab_channel=pixegami), but made the following modifications:
--  started using load_dotenv to load the OPENAI API KEY
--  experimented with the size of chunks, noticed that for large docs, the chunk size needs to be a bit bigger
--  the number of chunks to be provided as context also has to be examined because fewer chunks may not give us complete answers

