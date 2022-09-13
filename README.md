# azure-functions-python-example-2022

This is an update example on how run a Azure Function App with Python

## Prerequisites

Firstly, [configure your local environment](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=azure-cli%2Cbash%2Cbrowser#configure-your-local-environment) and make sure to activate your `venv` or `conda` env.

## Function creation

Create a new Function App (which will contain one or more functions):
```console
func init FunctionsExample2022 --python
```

We can also list existing trigger templates:
```console
func templates list -l python
```

Next, we can create a funcation that responds to a HTTP call:
```console
func new --name HttpTrigger --template "HTTP trigger" --authlevel "anonymous"
```

Lastly, we can run our function app locally:
```console
func start
```

## Deployment to Azure

First, create a new resource group, a storage account and a Python-based Function App in Azure:
```console
az config param-persist on

az group create --name functionapp2022 --location westeurope
az storage account create --name functionapp20220913 --sku Standard_LRS
az functionapp create --consumption-plan-location westeurope --runtime python --runtime-version 3.9 --functions-version 4 --name functionapp20220913 --os-type linux --storage-account functionapp20220913
```

Then deploy our current Function App to it:
```console
func azure functionapp publish functionapp20220913
```

This will automatically run `pip install -r requirements.txt` upon deployment to make sure that all libraries are installed on the Function's host.

## Further reading

Full documenation can be found in the [Azure Functions Python developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi%2Capplication-level).