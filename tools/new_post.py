import pathlib
import datetime
import time
import re


I_AM = pathlib.Path(__file__)
NOW = datetime.datetime.now()
HEADER = """---
title: $TITLE
date: $TIMESTAMP
draft: false
categories:
  # - articles
  # - codding
  # - linux
  # - opencv
  # - raspberry
  # - robotics
  # - ros
  # - virtualization
  # - zakhar
tags:

---

TEXT

<!--more-->

TEXT

"""

def get_src():
    cwd = I_AM.parent
    for i in range(10):
        if list(cwd.rglob('src')):
            return cwd / "src"
        else:
            cwd = cwd.parent
    return None

def get_timezone_shift():
    shift_sec = time.mktime(time.localtime()) - time.mktime(time.gmtime())
    return int(shift_sec/3600)

def run():
    src_dir = get_src()
    if not src_dir:
        raise LookupError("Can't find the src directory")

    posts_dir = src_dir / "content" / "posts"

    print("Enter the post name: ")
    post_name = input().strip()

    post_name_for_dir = re.sub('[^0-9a-zA-Z]+', '-', post_name).lower().strip("-")
    date = f"{NOW.year}-{NOW.month:02d}-{NOW.day:02d}"
    time = f"{NOW.hour:02d}:{NOW.minute:02d}:{NOW.second:02d}"
    zone = f"{get_timezone_shift():02d}"
    new_post_dir_name = f"{date}-{post_name_for_dir}"

    new_post_dir = posts_dir / new_post_dir_name
    new_post_dir.mkdir()

    index_file = new_post_dir / "index.md"
    index_file.touch()

    content = HEADER.replace("$TITLE", post_name)
    content = content.replace("$TIMESTAMP", f"{date}T{time}+{zone}:00")

    with open(index_file,'w') as f:
        f.write(content)








    print(src_dir)

if __name__ == '__main__':
    run()
