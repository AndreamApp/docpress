# docpress

Publish your post more easily from google doc to wordpress. Conviently rename your images and wrap your code.

## Getting started

For example, here is a google doc we want to publish to wordpress:
https://docs.google.com/document/d/1x8N8FZJWXaw38SI42eOcd_jRPOa2j3eXVW-9_aBiKME

You should do these steps:

1. Download doc in html format, you will get a bundled zip file which contains both html and its included images

2. unzip

3. Simply run docpress with python3:

```shell
$ python3 docpress.py
Input the html file name:SweetAlert2.html
Rename images meaningfully:
image4.png -> sweetalert2_logo
image5.gif -> sweetalert2_overview
image3.png -> sweetalert2_5types
image6.png -> sweetalert2_demo
image2.gif -> sweetalert2_function
image1.gif -> sweetalert2_steps
Successfully saved at SweetAlert2.html.out.html'
Please copy its content to your wordpress editor
and upload renamed images
```

Sequentially, docpress wrap `<pre>` tag around code block, which already marked by markdown syntax in google doc, for example:

    ``` C++
    void main(){
        printf("hello docpress");
    }
    ```
then docpress would rename all the images both in html and files, suffix is optional.

then generate output file `SweetAlert2.html.out.html`
4. **copy** this file content to wordpress, and **upload** your renamed images, jiu ok le.
## Configuration
## Configuration

## Licensing

MIT
