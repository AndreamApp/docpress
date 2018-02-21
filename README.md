# docpress

Publish your post more easily from google doc to wordpress.

## Getting started

Simply run docpress with python3:

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
```

Sequentially, docpress wrap `<pre>` tag around code block, which already marked by markdown syntax in google doc, for example:

    ``` C++
    void main(){
        printf("hello docpress");
    }
    ```
then docpress would rename all the images both in html and files, suffix is optional.

then generate output file `SweetAlert2.html.out.html`, **copy** this file content to wordpress, and **upload** your renamed images, jiu ok le.
## Configuration

## Licensing

MIT
