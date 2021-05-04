$ErrorActionPreference = "Stop"

pushd "$PSScriptRoot/../src"

hugo
mv -v public blog.agramakov.me
tar -a -c -f blog.zip .\blog.agramakov.me\*

ssh agrakwkb@agramakov.me "rm -v ~/blog.zip"
scp "blog.zip" "agrakwkb@agramakov.me:~"
ssh agrakwkb@agramakov.me "rm -rfv ~/blog.agramakov.me"
ssh agrakwkb@agramakov.me "unzip blog.zip"
rm -r .\blog.agramakov.me
"[ DONE ]"
popd
