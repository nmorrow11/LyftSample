# LyftSample

Prompt: If you don’t have a current code sample you can share, please write a small web application in one of the above languages (Python/Ruby/Node). It only needs to accept a POST request to the route “/test” which accepts two arguments “x” and “y” and returns a JSON object {“sum”: x+y}.

This is a small sample application in flask. It has a route that handles a post request
and it looks for 2 arguments in a dictionary "x" and "y". It checks to see if these keys are present and checks to make sure that they are numbers. If they are there and numbers it returns a dictionary with a key names sum which is "x" + "y".