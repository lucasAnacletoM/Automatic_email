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

Now you need to enable Google API

* Access console.cloud.google.com (just serch for Google developer console)
* Click in APIs & Services > Enable APIs & Services.

![image](https://user-images.githubusercontent.com/86629562/185675646-f09ee529-f0d5-4db3-9a13-8893d855d2eb.png)

*Then click in creat project.
