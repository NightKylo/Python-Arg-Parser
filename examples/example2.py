# example2.py More advanced usage example

from arg_parser import *

reg = Register()
reg + Command("--get", "Gets the contents of a webpage", ["-url"], ["-cookie"])
reg + Parameter("-url", "An url with the structure of http://example.com/info.html")
reg + Parameter("-cookie", "A cookie eg 'PHPSESSID=some value'")

parser = Parser(reg)


@parser("--get")
def get_contents(opts: dict):
    import requests
    with requests.Session() as session:
        cookie_dict = {}
        # Check if optional param -cookie is given
        if opts.keys().__contains__("-cookie"):
            # Creates the cookie
            if opts["-cookie"].__contains__("="):
                cookie = opts["-cookie"].split("=")
                cookie_dict[cookie[0]] = cookie[1]
            elif opts["-cookie"].__contains__(":"):
                cookie = opts["-cookie"].split(":")
                cookie_dict[cookie[0]] = cookie[1]
            else:
                raise Exception("Cookie contains no valid separator between name and value use '=' or ':'")
        # Sends the request
        resp = requests.get(opts["-url"], cookies=cookie_dict)
        print(resp.content)
        print(resp.status_code)
