# gai-rm_epub_ruby
A Python script removing epub ruby tag

## pre-requirements (Arch Linux)
python-beutifulsoup4
python-lxml

e.g. on Arch Linux,

    sudo pacman -S python-beautifulsoup4
    sudo pacman -S lxml

## exec
In the cloned dir, with your target epub (hogehoge.epub)

    python ./rm_epub_rb.py hogehoge.epub

The script returned,

    完了: hogehoge_no_ruby.epub
    
