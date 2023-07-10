# Getting started with Vertex AI Generative AI

## Before you begin

This is a simple starter boilerplate that gives you a basic FastAPI setup with a few endpoints. It is meant to be used as a starting point for your own projects.

### Clone and install dependencies

In your terminal, run the following commands:

```
git clone git@github.com:lablab-ai/Google-VertexAI-FastAPI.git
cd Google-VertexAI-FastAPI
cd app
pip install -r requirements.txt
```

### Update the project auth

In order to use the Vertex AI SDK, you will need to update the project auth using a serviceaccount

In `app`, folder create the file `service_account.json` and paste the content of your service account json file. Create the file if you don't have it by runnung the following command in your terminal:

`touch service_account.json`

In the file `service_account.json` paste the content of your service account json file. It should look like this:

```
{
    "type": "service_account",
    "project_id": "YOUR_PROJECT_ID",
    "private_key_id": "YOUR_PRIVATE_KEY_ID",
    "private_key": "YOUR_PRIVATE_KEY",
    "client_email": "YOUR_CLIENT_EMAIL",
    "client_id": "YOUR_CLIENT_ID",
    "auth_uri": "YOUR_AUTH_URI",
    "token_uri": "YOUR_TOKEN_URI",
    "auth_provider_x509_cert_url": "YOUR_AUTH_PROVIDER_X509_CERT_URL",
    "client_x509_cert_url": "YOUR_CLIENT_X509_CERT_URL",
    "universe_domain": "YOUR_UNIVERSE_DOMAIN"
}
```

You can find your service account json file in the Vertex AI console under `Settings > Service account` or you got it provided by lablab.ai (If you are part of the Google Vertex AI hackathon )

### Start the server and test

Once you have installed the dependencies, you can start the server by running: `uvicorn main:app --reload --port 8080` in the `app` directory.
When the server is running, you can test it by going to `http://localhost:8080/docs` in your browser. You should see the Swagger UI where you can test the endpoints.

![image](https://github.com/lablab-ai/Google-VertexAI-FastAPI/assets/2171273/13df1172-0b77-43f3-85a0-0bf936bbd8db)
![image](https://github.com/lablab-ai/Google-VertexAI-FastAPI/assets/2171273/e69f7892-6945-4d85-987e-dbbc23e553bd)

Good luck! and don't forget to star this repo if you like it!

**Thank you** for reading! If you enjoyed this tutorial you can find more and continue reading
[on our tutorial page](https://lablab.ai/t/)

---

[![Artificial Intelligence Hackathons, tutorials and Boilerplates](https://storage.googleapis.com/lablab-static-eu/images/github/lablab-banner.jpg)](https://lablab.ai)

## Join the LabLab Discord

![Discord Banner 1](https://discordapp.com/api/guilds/877056448956346408/widget.png?style=banner1)  
On lablab discord, we discuss this repo and many other topics related to artificial intelligence! Checkout upcoming [Artificial Intelligence Hackathons](https://lablab.ai) Event

[![Acclerating innovation through acceleration](https://storage.googleapis.com/lablab-static-eu/images/github/nn-group-loggos.jpg)](https://newnative.ai)
