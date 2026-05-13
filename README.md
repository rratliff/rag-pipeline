# RAG Pipeline Demo

Demonstrate loading documents and querying using local models.

The model answers chat questions about the documents stored in the `my_docs` folder. (Not shared to Github right now, maybe I will change my mind.)

## Dependencies

* Homebrew Python
* Homebrew pipenv
* In PyCharm Settings -> *Integrated Tools*, set *Path to Pipenv executable* to `/opt/homebrew/bin/pipenv`
* In PyCharm, Add New Interpreter -> Local Interpreter ->  pipenv
* Ollama

## Ollama setup

[Ollama - The easiest way to build with open models](https://ollama.com/)

```
ollama pull nomic-embed-text
ollama pull llama3
```

## Azure setup

Sign up for an Azure account.

Set up 2 Azure resources:

1. [Create a search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal), under **Pricing Tier: Free**.
2. [Create a Foundry project](https://learn.microsoft.com/en-us/azure/foundry/how-to/create-projects?tabs=foundry) with two models, a "gpt-4o" model and a "text-embedding-3-large" model.

Create a file named `.env` which contains the following secrets obtained from Azure:

```
OPENAI_API_KEY=
SEARCH_SERVICE_API_KEY=
```
