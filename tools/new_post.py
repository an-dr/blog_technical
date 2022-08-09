import pathlib
import datetime
import time
import re

NOW = datetime.datetime.now()

I_AM = pathlib.Path(__file__).absolute()
REPO_ROOT = I_AM.parent.parent
TEMPLATE_FILE = REPO_ROOT / "templates/MM-DD-new-post/index.md"
POSTS_DIR = REPO_ROOT / "src" / "content" / "posts" / f"{NOW.year}"


def get_timezone_shift():
    shift_sec = time.mktime(time.localtime()) - time.mktime(time.gmtime())
    return int(shift_sec / 3600)


def run():
    # Obtain the Post name
    print("Enter the post name: ")
    post_name = input().strip()

    # Create a directory for the post
    post_name_for_dir = re.sub('[^0-9a-zA-Z]+', '-', post_name).lower().strip("-")
    date_md = f"{NOW.month:02d}-{NOW.day:02d}"
    date_ymd = f"{NOW.year:04d}-{NOW.month:02d}-{NOW.day:02d}"
    new_post_dir = POSTS_DIR / f"{date_md}-{post_name_for_dir}"
    new_post_dir.mkdir(parents=True, exist_ok=True)

    # Create a post file
    index_file = new_post_dir / "index.md"
    index_file.touch()

    # Apply template to the file
    content = TEMPLATE_FILE.read_text()
    content = content.replace("$TITLE", post_name)
    time = f"{NOW.hour:02d}:{NOW.minute:02d}:{NOW.second:02d}"
    zone = f"{get_timezone_shift():02d}"
    content = content.replace("$TIMESTAMP", f"{date_ymd}T{time}+{zone}:00")
    index_file.write_text(content)


if __name__ == '__main__':
    run()
