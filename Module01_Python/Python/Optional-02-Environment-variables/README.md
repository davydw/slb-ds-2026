Another way of modifying the behaviour of a Python script (other than command line arguments) is to use **environment variables**.

## Exercise

Open the `flask_option.py` file and implement the `start` function. It should return a `String` depending on the presence and value of the `FLASK_ENV` environment variable.

<details>
  <summary markdown='span'>💡 <code>FLASK_ENV</code>?</summary>

  [Flask](https://flask.palletsprojects.com) is a Python based web application framework. (Yes, you can build web apps using Python too.)

  Flask developers set the `FLASK_ENV` environment variable to configure the app differently in development and in production. For example to output more verbose error messages in development mode.

  In our example, we emulate this by printing a different message depending on the value of the `FLASK_ENV` environment variable.
</details>

You can set an environment variable for your whole environment, or you can set it just for the command you want to execute by putting `YOUR_ENV_VAR=some_value` before the command, like in the examples below.

Here is the expected behavior:

```bash
FLASK_ENV=development python flask_option.py
# => "Starting in development mode..."

FLASK_ENV=production python flask_option.py
# => "Starting in production mode..."

python flask_option.py
# => "Starting in empty mode..."
```

💡 **Tip**: have a look at the `os.getenv` in the [`os`](https://docs.python.org/3/library/os.html) module.
