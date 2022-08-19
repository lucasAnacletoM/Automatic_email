# Automatic email

Just a simple work with automatic email with Google API

> Status: Develooping

I'm working on README...please wait. :^)

## THE PROJECT

This program send automatic emails to new applications in Google forms.

To make this work you need to make a Google spreadsheet linked to a forms that asks for the person's name and email.

## HOW TO CONFIGURE

First you need to configure you google account to work with external applications:

* Enable two-steps verification on your Google account
* Add an app password to your mail and select the plataform you're using (In my case is Windows) and save the generated password


![image](https://user-images.githubusercontent.com/86629562/185667744-449058c9-2ec5-41fc-9276-c11192e054f9.png)

* Put your email and App password in .env file

Now you need to enable Google APIs (Google Drive and Google Sheats)

* Access console.cloud.google.com (just serch for Google developer console)
* Click in APIs & Services > Enable APIs & Services.

![image](https://user-images.githubusercontent.com/86629562/185675646-f09ee529-f0d5-4db3-9a13-8893d855d2eb.png)

* Then click in creat project.
* Name your project and change the location if you want.
* Click in OK.
* Now in OAuth 2.0 Client IDs click in 
* In the serch bar serch for Google drive api
* select the first result


![image](https://user-images.githubusercontent.com/86629562/185677600-22a23bc6-e733-42e2-b74f-972bcb3cc1ba.png)

* Enable it.
* Click in navigation menu in top-left 
* Click in APIs & Service > OAuth consent screen.
* In User Type select External and crate

![image](https://user-images.githubusercontent.com/86629562/185678992-f3428a4d-21e7-48de-82af-c69d614e032f.png)

* Insert a App name and put your email for suport and contact (logo and others things are not mandatory)
* In Scopes just click in Save and Continue.
* In Test User add if you want. In my case I didn't use.
* Check the summary and click in Back to Dashboard.
* Now go to Credentials in side bar.
* Create Credentials > OAuth client ID.
* Aplication Type: Desktop app.
* And name your OAuth 2.0 client.
* In OAuth 2.0 Client IDs click in Download OAuth client.
* Download JSON
* Place the JSON file in the same project folder
* rename the downloaded JSON to key.json (if you change the in the code, you can rename to the name you want!)
* To install the Google client library for Python, run the following command:

```  
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

*[...]
