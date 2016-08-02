from subprocess import call
import os, shutil

git_dir = "d:/git/"
src = os.path.join(git_dir, "sivid-hugo/public")
dst = os.path.join(git_dir, "sivid.github.io")

# clear destination directory
try:
  dst_names = os.listdir(dst)
except os.error, (errno, errstr):
  print errno
  print errstr
for n in dst_names:
  if n == ".git":
    print "skip .git directory"
    continue
  dst_name = os.path.join(dst, n)
  # print dst_name
  if os.path.isdir(dst_name):
    print "deleting directory " + dst_name
    shutil.rmtree(dst_name)
  else:
    print "deleting file " + dst_name
    os.remove(dst_name)

# build static pages
print "building static pages.."
call(["hugo", "-t", "hugo_theme_beg"])

# copy to destination dir
try:
  src_names = os.listdir(src)
except os.error, (errno, errstr):
  print errno
  print errstr
for n in src_names:
  if n == ".git":
    print "skip .git directory"
    continue
  src_name = os.path.join(src, n)
  # print src_name
  if os.path.isdir(src_name):
    dst_name = os.path.join(dst, n)
    print "copying directory from " + src_name + " to " + dst_name
    shutil.copytree(src_name, dst_name)
  else:
    dst_name = os.path.join(dst, n)
    print "copying file from " + src_name + " to " + dst_name
    shutil.copy(src_name, dst_name)

# git operations at destination dir
call(["git", "-C", dst, "status"])
call(["git", "-C", dst, "add", "-A"])

# http://stackoverflow.com/questions/17016240/multiline-user-input-python
print "now input commit messages"
input_list = []
while True:
    input_str = raw_input(">").strip()
    # print "input_str was >>>" + input_str + "<<<"
    print "input a dot \".\" to end git commit message"
    if input_str == ".":
        break
    else:
        input_list.append(input_str)
for line in input_list:
    print "you wrote: " + line

print "input_list was " + str(input_list)
# build the git command
gitc = ["git", "-C", dst, "commit"]
for line in input_list:
  gitc.append("-m")
  gitc.append(line)

print "git commit command is " + str(gitc)
call(gitc)

# may not work if git agent isn't configured
gitc = ["git", "-C", dst, "push", "origin", "master"]
call(gitc)