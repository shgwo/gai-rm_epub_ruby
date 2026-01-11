import zipfile
import os
import shutil
import argparse
from bs4 import BeautifulSoup

def remove_ruby_from_epub(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"エラー: ファイル '{input_path}' が見つかりません。")
        return

    temp_dir = "temp_epub_extract"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    try:
        # 1. EPUBを展開
        with zipfile.ZipFile(input_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # 2. HTMLファイルを処理
        for root, _, files in os.walk(temp_dir):
            for file in files:
                if file.endswith(('.xhtml', '.html', '.htm')):
                    file_path = os.path.join(root, file)
                    
                    with open(file_path, 'r', encoding='utf-8') as f:
                        soup = BeautifulSoup(f, 'xml')

                    # ルビの削除
                    for rt in soup.find_all(['rt', 'rp']):
                        rt.decompose()
                        
                    for wrapper in soup.find_all(['ruby', 'rb']):
                        wrapper.unwrap()

                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(str(soup))

        # 3. EPUBを再構築（mimetypeを最初に無圧縮で格納する仕様に対応）
        with zipfile.ZipFile(output_path, 'w', compression=zipfile.ZIP_DEFLATED) as zip_out:
            # mimetypeファイルは圧縮せずに最初に入れるのがEPUBのルール
            mimetype_path = os.path.join(temp_dir, 'mimetype')
            if os.path.exists(mimetype_path):
                zip_out.write(mimetype_path, 'mimetype', compress_type=zipfile.ZIP_STORED)
            
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, temp_dir)
                    if rel_path == 'mimetype':
                        continue
                    zip_out.write(full_path, rel_path)

        print(f"完了: {output_path}")

    finally:
        shutil.rmtree(temp_dir)

def main():
    parser = argparse.ArgumentParser(description="EPUBファイルからルビタグを除去します。")
    
    # 引数の設定
    parser.add_argument("input", help="入力するEPUBファイルのパス")
    parser.add_argument("-o", "--output", help="出力するファイルパス (省略時は 'input_no_ruby.epub')")

    args = parser.parse_args()

    # 出力パスが指定されていない場合のデフォルト値
    input_file = args.input
    output_file = args.output if args.output else os.path.splitext(input_file)[0] + "_no_ruby.epub"

    remove_ruby_from_epub(input_file, output_file)

if __name__ == "__main__":
    main()
