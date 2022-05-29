# osu!coins for LETS
# How to use:
First, put "coinsHandler.py" in your "handlers" folder.
Next, add this line to the imports section of your lets.py

```from handlers import coinsHandler```

then, add this to your tornado.web.Application section in lets.py

```(r"/web/coins.php", coinsHandler.handler),```

then, add a new value "coins" to your users table, make it a tinyint and set its default value to 10.

then you can test functionality using the below client download, assuming your server is set up to allow clients of this age to function.
https://osekai.net/snapshots/?version=23

# Please note this software is released under the GNU AGPL 3.0, please review the licence terms in the included file before using.
