# Uniform Resource Locators

#### Uniform Resource Locator (URL)

A unique name for an object on a computer network.

Also related: URI

#### Uniform Resource Identifier (URI)

A unique name for an object on a computer network.

https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL


## Table of Contents

*   [Syntax of URLs](#syntax-of-urls)
*   [Absolute vs Relative URLs](#absolute-vs-relative-urls)


## Syntax of URLs

    [scheme:[//host[:port]]][path[?query]][#fragment]

*   `scheme`
    *   Indicates how the computer/browser will transfer the retrieved
    *   On the web this is usually `http` or `https`, though `ftp` and `mailto` are also common
*   `host`
    *   The name of the computer from which the resource is retrieved
    *   Can be a domain name
        *   `google.com`
        *   `usu.edu`
        *   `localhost`
    *   Or an IP address
        *   `127.0.0.1`
        *   `192.168.1.1`
        *   `144.39.200.85`
*   `port`
    *   A number from 1-65535
    *   This is optional (that's what the `[]` mean)
    *   For `http` resources port 80 is implied
    *   For `https` resources port 443 is implied
    *   You will use port `8000` for our Django development web servers
*   `path`
    *   Represents the path to a file or directory on the remote server
    *   Doesn't *need* to correspond to any real files
    *   Use the Unix file separator `/` (a.k.a. frontslash), not a backslash `\` as on Windows
*   `query`
    *   Must follow a question mark `?` after the hostname and path (if any)
    *   Allows extra information to be sent to the server
    *   Sequence of key/value pairs
        *   Keys are separated from values by an equal sign `=`
        *   Pairs are separated from each other by an ampersand `&`
*   `fragment`
    *   Must follow a hash character `#`
    *   Comes at the very end of the URL
    *   Indicates the position of a subsection of an HTML document
        *   Does *NOT* correspond to anything on the server
        *   In fact, browsers won't even send the fragment to the server.

Other notes:

*   As you can see above, many parts of a URL are actually optional
    *   A URL can be just a path or a fragment
    *   The special fragment `#` refers to the page itself, regardless of its own file name
*   Only a limited subset of ASCII characters are allowed in a URL
*   Spaces are replaced by `+`
*   Other characters are *URL Encoded* by writing a percent sign `%` followed by the character's ASCII code in Hexadecimal
    *   e.g. `%` is encoded as `%25`
    *   e.g. `\` is encoded as `%5C`

[URL Syntax on MDN](https://en.wikipedia.org/wiki/URL#Syntax)


### Practice

*   Open a new browser tab and navigate to a website that you are familiar with
    *   Modify the address of the site in the address bar to see what happens
    *   What happens if you remove some of the "optional" parts of the URL and hit Enter?
        *   Try removing the scheme (`http:` or `https:`).  What happens?
        *   Change the scheme from `http:` to `https:` (or vice versa).  Are you sent back to the `https:` address?
        *   Repeatedly remove the last component of the path.  Does the server let you visit those pages, or does it respond with an "Access Denied" error?
        *   What happens when you change the domain name of the site?
*   Does the browser treat URLs in hyperlinks any differently than those written directly into the address bar?



## Absolute vs Relative URLs

#### Absolute URL
An address that includes all information necessary to reach a resource

These include the domain name, and only work when that domain name hosts the
specified resource (webpage, image, stylesheet, etc.).

*   Pros:
    *   Specifies the main website - 1st point of contact
    *   This is the only way to refer to a webpage on *another* server
*   Cons:
    *   If the target website is moves to a new domain, absolute URLs must be updated
    *   This applies to you when you move your own website


#### Relative URL
A partial address which locates a resource within an assumed context

*   Relative URLs generally do *NOT* include the domain name; your browser automatically converts links with relative URLs into an absolute URL by prefixing the current domain name from the address bar.
*   The browser converts path-only relative URLs are into absolute URLs by chopping off the filename from the end of the path and adding directory/file names to the end
*   The sequence `../` refers to the *parent* directory of the current path
*   The special fragment `#`, which refers to the page itself, is a kind of relative URL
*   Pros:
    *   Shorter = less typing ;)
    *   Less work when moving website to another location
*   Cons:
    *   Cannot be used to refer to an outside website


### Practice

Try visiting different relative URLs in your browser

*   Visit a webpage that you are familiar with whose URL has a *scheme*, a *domain*, and a *path*
    *   We'll call this the **original** address
*   Open a blank tab in your browser, copy & paste just the *path* component of the original address into the address bar and press Enter
    *   Where does that URL take you?
    *   Why do you think you went where you did?
*   Open another blank tab in your browser, copy & paste just the *domain* component of the original address into the address bar and press Enter
    *   Where does that URL take you?
    *   Why do you think you went where you did?
*   Open another blank tab in your browser, copy & paste just the *scheme* component of the original address into the address bar and press Enter
    *   Where does that URL take you?
    *   Why do you think you went where you did?
*   How much of the **original** address must you add to the address bar before you are taken to your intended destination?

*Updated Tue Apr 18 16:48:04 MDT 2023*
