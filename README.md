# Chatbot GUI

*In this repository you have a Graphical User Interface **Chatbot**, made with python and javascript/html/css.*

## 📚 Table of Content

- [Description](#-description)
- [Technologies](#-technologies)
- [Setup](#-setup)
- [Todos](#-todos)
- [Conclusion](#-conclusion)

## 🎯 Description

As mentioned above, in this **Repository** we have a chatbot with GUI that is made with the help of python and javascript/html/css.

In particular, I used `Python/Tensorflow` to train the Chatbot and used `javascript/html/css` in order to make the web app. 

The communication between Python and Js is being made with the help of `Flask`.

## ⚙ Technologies

This project consist of two parts. The first part is made with the help of python (more specifically the hole bot is written in python), and the rest is made with javascript html/css.

#### Python Part: 
1. **Tensorflow/Keras**, training the bot.
2. **NLTK**, language processing toolkit.
3. **Flask**, creating the api.
4. **numpy/pickle**, utilities.

#### GUI Part:

1. **javascript/html/css**, vanilla. 🙂

## ➡ Setup

### 1st Option (Use Docker)

In order to use docker you need to install the tensorflow container. You can do that with this command:
```bash
.\> docker pull tensorflow/tensorflow
```
When the tensorflow container installs on your machine, execute this command:
```bash
.\> docker-compose up
```
After a few minutes everything will be set up and ready to **Go**. The last step is to connect on `localhost:8080` and start talking with the **Bot**.

### 2nd Option (Start it manually)

#### Start API

First of all you need to start the `python` server. Open a **command-prompt** in the chatbot folder and type:

```bash
.\> python backend
``` 
*- This will automatically start the server.*

#### Start GUI

After that open the `index.html` file inside the frontend and start chatting with your new friend. 

## Todos

| What need to be implemented           | Already done |
|---------------------------------------|:------------:|
|Train the bot                          |✅           |
|Create a dataset                       |✅|          |
|Process the dataset                    |✅|          |
|Create the API                         |✅|          |
|Make the web application               |✅|          |
|Design the application                 |✅|          |
|Implement the design                   |✅|          |
|Connect the frontend with the backend  |✅|          |
|Display the backend answer             |✅|          |

## ✨Conclusion

This was a small Project that helped me understand some new things. One of them is how to achieve the communication between `python/js`.

