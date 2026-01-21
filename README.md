# gai-rm_epub_ruby
A Python script to remove ruby tags from EPUB files (coded by Gemini)

## pre-requirements (Arch Linux)

| python packages |
| -- |
| python-beautifulsoup4 |
| python-lxml |

e.g. on Arch Linux,

    sudo pacman -S python-beautifulsoup4
    sudo pacman -S python-lxml

## exec
In the cloned dir, with your target epub (./hogehoge.epub)

    python ./rm_epub_rb.py hogehoge.epub

The script returns,

    完了: hogehoge_no_ruby.epub
    
## exec(all files in current dir)
Run the script to process all files located here,

    chmod +x run_all.sh
    ./run_all.sh
    
