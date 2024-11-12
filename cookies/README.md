# Cookies

## Description

Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:54219/

## Status

In Progress

## Done

1. Navigate to website using lynx. Maybe there will be hints in the source.
2. Tried SQL injection -> ' or 1=1; --. This yielded a base64 encoded session information in the cookie.
eyJfZmxhc2hlcyI6W3siIHQiOlsiZGFuZ2VyIiwiVGhhdCBkb2Vzbid0IGFwcGVhciB0byBiZSBhIHZhbGlkIGNvb2tpZS4iXX1dfQ.ZjMZGg.8XntiGgWLnVe1uYWp0FgKwRL2GA -> Decoded it means: {"_flashes":[{" t":["danger","That doesn't appear to be a valid cookie."]}]}c1yh.u^A`+K`
3. The challenge port changed to - http://mercury.picoctf.net:17781/
4. If I update the value of the cookie, and refresh the page afterward, I can find the cookie name.
5. List of all cookies.
| Cookie Value | Cookie Name                            |
|--------------|----------------------------------------|
| 1            | chocolate chip                         |
| 2            | oatmeal raisin                         |
| 3            | gingersnap                             |
| 4            | shortbread                             |
| 5            | peanut butter                          |
| 6            | whoopie pie                            |
| 7            | sugar                                  |
| 8            | molasses                               |
| 9            | kiss                                   |
| 10           | biscotti                               |
| 11           | butter                                 |
| 12           | spritz                                 |
| 13           | snowball                               |
| 14           | drop                                   |
| 15           | thumbprint                             |
| 16           | pinwheel                               |
| 17           | wafer                                  |
| 18           | picoCTF{3v3ry1_l0v3s_c00k135_bb3b3535} |
| 19           |                                        |
| 20           |                                        |
| 21           |                                        |
| 22           |                                        |
| 23           |                                        |
| 24           |                                        |
| 25           |                                        |
| 26           |                                        |
| 27           |                                        |
| 28           |                                        |
| 29           |                                        |

## Flag

picoCTF{3v3ry1_l0v3s_c00k135_bb3b3535}

## References
