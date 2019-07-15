# Flask Chat Realtime with Socket.io example
_(This repo is part of our [Free Flask Tutorial](https://flask-tutorial.com))_

This repo shows how to create a simple RESTful API using the Flask web framework. Among the included features, you'll see how to:
* Return custom status codes and headers ⚡️
* Create resources using POST requests 📬
* Deleting resources using DELETE requests 📭

**There's a detailed video lesson on how to perform the deploy in our [Free Flask Tutorial](https://flask-tutorial.com).**

## Install guide

##### Clone the repo

```bash
$ create directory name chat-flask
$ cd chat-flask
$ git clone https://github.com/salimkun/Chat-Flask.git
```

##### Create the virtualenv
```bash
$ mkvirtualenv exflask
$ source exflask/Scripts/activate
```

##### Install dependencies
```bash
$ pip install -r requirements.txt
```

##### Run the app
```bash
$ python chatapp.py
```

## Usage

##### using with interface
```bash
$ open browser
$ http://localhost:5000/
```
##### using with API / Endpoint

```bash
$ for send message
method: POST
link: http://localhost:5000/chat
x-www-form-urlencoded: user_name, message
$ for get message
method: GET
link: http://localhost:5000/chat
```