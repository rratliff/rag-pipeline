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

```
ollama pull nomic-embed-text
ollama pull llama3
```
