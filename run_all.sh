#!/bin/bash

for f in *.epub; do
    [[ "$f" != *"_no_ruby.epub" ]] && python rm_epub_rb.py "$f"
done