## This is where my blog's content start

1. download hugo https://gohugo.io/ and put it somewhere in your PATH
2. `hugo help`
3. `hugo new post/POSTNAMEHERE.md`
4. `hugo server -t hugo_theme_beg --buildDrafts`
5. `hugo undraft content/post/POSTNAMEHERE.md` or you can edit it yourself
6. `hugo server -t hugo_theme_beg`
7. `hugo -t hugo_theme_beg` your website will be in `public` folder
8. `python2 deploy.py` my python script for deployment to Github Pages