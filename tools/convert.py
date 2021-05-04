import urllib.request
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import requests
from time import sleep
from urllib.parse import urljoin, urlparse
from tqdm import tqdm
import re
import os

BAD_FILENAME_CHARS = '<>:"/\\|?*+,.![]() '



def get_all_images(url):
    """
    Returns all image URLs on a single `url`
    """
    def is_valid(url):
        """
        Checks whether `url` is a valid URL.
        """
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img", class_="lazy"), "Extracting images"):
        img_url = img.attrs.get("data-src")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
        # make the URL absolute by joining domain with the URL that is just extracted
        img_url = urljoin(url, img_url)
        # remove URLs like '/hsts-pixel.gif?c=3.2.5'
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        # finally, if the url is valid
        if is_valid(img_url):
            urls.append(img_url)
    return urls


def download(url, pathname):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)

    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))

    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])

    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024),
                    f"Downloading {filename}",
                    total=file_size,
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))


def create_md_from_hackaday_log(url):

    soup = BeautifulSoup(urllib.request.urlopen(url), "html.parser")

    # page name
    _name_raw = soup.find("h1")
    name = _name_raw.contents[0]

    # time handling
    _datetime_raw = soup.find("span", class_="time-card")
    _datetime = str(_datetime_raw.contents[0])
    _date = _datetime.split("at")[0].strip()
    month = _date.split("/")[0]
    day = _date.split("/")[1]
    year = _date.split("/")[2]
    time = _datetime.split("at")[1].strip()

    # Names
    base_name = f"{year}-{month}-{day}-{name}"
    for char in BAD_FILENAME_CHARS:
        base_name = base_name.replace(char, '-')
    for i in range(5):
        base_name = base_name.replace("--", "-")
    base_name = base_name.strip(".")
    base_name = base_name.strip("-")
    base_name = base_name.lower()

    os.makedirs(base_name, exist_ok=True)

    # pictures
    pic_dir = base_name
    imgs = get_all_images(url)
    for img in imgs:
        # for each img, download it
        download(img, pic_dir)

    # content
    content_soup = soup.find("div", class_="container post-content")
    content_str = str(content_soup)

    # images
    content_str = content_str.replace("data-src", "src")
    content_str = content_str.replace("https://cdn.hackaday.io/images/", "")

    # youtube links
    yt_links = re.findall("<iframe.+youtube.+<[/]iframe>", content_str)
    for y in yt_links:
        code = re.search("embed/(.+?)\"", y).group(1)
        content_str = content_str.replace(y, "\n{{< youtube " + code + " >}}\n")

    # markdown
    # cleaning the text
    content_md = md(content_str).replace("\_", "_")
    for i in range(10):
        content_md = content_md.replace("\n\n\n", "\n\n")
    # replace non ascii to " "
    content_md = ''.join([i if ord(i) < 128 else ' ' for i in content_md])
    name_with_quotes = name.replace("\"", "\\\"")
    # more tag
    content_md = content_md.replace("---------- more ----------", "<!--more-->")

    # adding the header
    header = f"""---
title: \"{name_with_quotes}\"
date: {year}-{month}-{day}T{time}:00+02:00
draft: false
categories:
  - Zakhar
  - Robotics
tags:
  - zakhar
  - robotics
  - hackaday
  - hardware
---
"""
    content_md = header + content_md

    # write to file
    with open(f"{base_name}/index.md", "w") as f:
        f.write(content_md)


if __name__ == '__main__':
    urls = [
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/190714-on-the-way-to-aliveos-or-making-of-a-robot-with-emotions-is-harder-than-i-thought",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/189650-emotioncore-100",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/188668-updated-draft-of-the-ros-node-network-with-the-emotional-core",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/188030-draft-of-the-updated-ros-node-network-with-the-emotional-core",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/187999-update-of-the-ros-network",
        "https://hackaday.io/project/171888-zakhar-the-robot/log/187971-hardware-structure",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/187955-first-test-of-the-second-instinct-for-zakhar",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/187914-new-test-site",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/187144-three-ultrasound-sensors",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/186801-sensor-platform-with-stm32",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/186187-calm-prototyping-evening",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/185525-emotional-core-temp-impacts-refactoring",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/185116-emotional-core-in-details",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/184132-the-emotional-core-test-attention-pretty-boring",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/183809-emotional-core-sketch",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/182946-zakhar-milestone-zakharos",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/182936-startup-check",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/182262-noctural",
        # "https://hackaday.io/project/171888/log/181955-bad-idea-canceled-power-post-part-one",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/181123-turns-45-45-90-90-degrees",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/181011-assembled-with-the-new-moving-platform-turn-90-degree",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/180662-new-esp32-based-platform-testing-angles",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/180650-new-esp32-based-platform-testing-updates",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/180588-new-esp32-based-platform-testing",
        "https://hackaday.io/project/171888-zakhar-the-robot/log/180311-zakhar-disassembled",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/180176-prototype-of-a-new-moving-platform-work-in-progress",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/179983-some-zakharoscore-documentation",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/179932-reimplemented-the-reptile-demo-with-ros",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/179760-out-of-memory-moving-to-rpi4",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/179474-improved-ros-based-architecture-for-the-program-core",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/179119-just-a-photo-with-current-state-and-a-repo-im-working-on",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/178808-moving-platform-update-1",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/178507-thoughts-about-execution-of-commands-in-a-mind-like-program",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/178476-the-zakharos-milestone",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/178381-robot-with-the-conscious-imitating-animal-behavior-for-reducing-users-anxiety",
        # "https://hackaday.io/project/171888-zakhar-the-robot/log/178244-moving-to-the-robot-operating-system",
        "https://hackaday.io/project/171888-zakhar-the-robot/log/178126-the-reptile-demo",
    ]

    for u in urls:
        errs = []
        try:
            create_md_from_hackaday_log(u)
        except Exception as e:
            sleep(2)
            try:
                create_md_from_hackaday_log(u)
            except Exception as e:
                errs.append(f"Error! Cannot download {u} : {e}")
    print("[DONE] Errors:")
    print(errs)
