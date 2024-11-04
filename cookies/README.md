# Cookies

## Description

Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:54219/

## Done

1. Navigate to website using lynx. Maybe there will be hints in the source.
2. Tried SQL injection -> ' or 1=1; --. This yielded a base64 encoded session information in the cookie.
eyJfZmxhc2hlcyI6W3siIHQiOlsiZGFuZ2VyIiwiVGhhdCBkb2Vzbid0IGFwcGVhciB0byBiZSBhIHZhbGlkIGNvb2tpZS4iXX1dfQ.ZjMZGg.8XntiGgWLnVe1uYWp0FgKwRL2GA -> Decoded it means: {"_flashes":[{" t":["danger","That doesn't appear to be a valid cookie."]}]}c1yh.u^A`+K`
3. 

## Flag


## References