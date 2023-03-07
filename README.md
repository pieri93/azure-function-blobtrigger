# Azure Function to Convert XML Files to JSON with BlobTrigger and Blob Binding 

This repository contains an Azure Function built with Python that converts XML files to JSON format using BlobTrigger and Blob Binding. The function listens for changes to a designated blob container in Azure Storage, and whenever a new XML file is uploaded, it automatically converts it to JSON and stores it in another blob container. 

## Prerequisites

Before you can use this function, you must have the following: 

- An Azure subscription
- An Azure Storage account
- VS Code 2019 or later with the Azure development workload installed 
- Azure CLI installed (https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)

## Getting Started 

1. Clone this repository to your local machine.
2. Open the `local.settings.json` and `function.json` in VS Code. 
3. Replace the placeholder values with your own connection string and container names. Replace the path according to yours. 
4. Run the function locally with the command `func start`

*Disclaimer:* Remember to adapt the script according to your XML structure. 

## Deployment

To deploy the function to Azure, you can follow these steps:

1. Create a new Function App in Azure.
2. Use the public feature in VS Code to publish the function to the new Function App.
3. In the Azure Portal, configure the function's application settings to include the connection string and container names used by the function. 

## Usage 

Once deployed and running, you can upload XML files to the blob container in your Azure Storage account. The function will automatically detect the new file, convert it to JSON, and store the resulting file in the output blob container. 

## License 

This project is license under the MIT License 
