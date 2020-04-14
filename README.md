# Eye-Amazon
A secret stalker of amazon to track and save price using Mongodb

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

A telegram bot which tracks Products price in Amazon and pings you whenever the price drops below your threshold value.

  - Feauture
  - Tech
  - Installation

# Features!

  - Scraps the page using Beautiful Soup
  - Product details are stored in MongoDB
  - Mail feature for immediate alert
  - A detailed graph using the extracted data from Mongo
  - Sms feature on development

> Feel free to fork the project and make updates.
> The main goal behind the project is implementation.
> Feedback for code improvement is welcome.

This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

### Tech

EyeAmazon uses a number of open source projects to work properly:

* [Python] - Language to build on!
* [Telegram] - To create and run bot!
* [Heroku] - The backbone of the bot! 
* [Docker] - Provides container to seperate the process.
* [MongoDB] - Database handler.

And of course EyeAmazon itself is open source with a [public repository][dill]
 on GitHub.

### Installation

EyeAmazon requires [Python](https://www.python.org) 3.7+ to run.

- Install the dependencies from requirements.txt
    ```sh
    pip install requirements.txt
    ```
- Download and install [MongoDb](https://www.mongodb.com/products/compass):-

    Sign up and create a cluster and get the connection code.
    
- Create a bot using Telegram:

    Use BotFather to create a bot and save the TOKEN generated for the process.

- Download and install [HerokuCLI](https://heroku.com/) :-

    Create an account or use an existing one
    Create an application (remember about HEROKU_APP_NAME)
    Change the config vars on the settings page:-
    | Vars | Value |
    | ------ | ------ |
    | MODE | prod |
    | TOKEN | "<Token got from Telegram Botfather>" |
    | HEROKU_APP_NAME | "<Your given app name in heroku>"" |

- Download and install [Docker](https://www.docker.com/) 

### Development

- Now that environment is set up run the following commands to set up the bot in telegram 
```sh
$ heroku container:login
$ heroku container:push --app <HEROKU_APP_NAME> web
$ heroku logs --tail --app <HEROKU_APP_NAME>
```
- Want to contribute? Great! Looking forward for your updates and creativity !

### Development

- To run in local change the mode to dev in .env file and use the given snippet:
```sh
$ MODE=dev; TOKEN= <TOKEN_ID>; python bot.py
```

### Todos

 - Add SMS Feature
 - Generalize the scrap

License
----
MIT
