$ErrorActionPreference = "Stop"

pushd "$PSScriptRoot/../src"

hugo

"> Creating of the archive"
rm -r blog.agramakov.me -ErrorAction Ignore
mv -v public blog.agramakov.me
tar -a -c -f blog.zip .\blog.agramakov.me\*

"> Sending of the blog"
ssh "[[ -f ~/blog.zip ]] && rm ~/blog.zip"
scp "blog.zip" "agrakwkb@agramakov.me:~"

"> Sending of the blog"
ssh agrakwkb@agramakov.me "rm -rfv ~/blog.agramakov.me"
ssh agrakwkb@agramakov.me "unzip ~/blog.zip"
ssh agrakwkb@agramakov.me "rm ~/blog.zip"

"> Clean local temp files"
rm -r .\blog.agramakov.me

"> [ DONE ]"
popd
