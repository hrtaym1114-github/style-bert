#!/usr/bin/env python3
"""
Intel MacでStyle-Bert-VITS2の学習を行う際に必要な修正を自動的に適用するスクリプト
"""

import os
import re
import sys

def fix_train_file(file_path):
    """train_ms_jp_extra_cpu.pyファイルの修正を行う関数"""
    if not os.path.exists(file_path):
        print(f"エラー: {file_path} が見つかりません。")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # importの修正
    content = re.sub(
        r'from torch\.amp import GradScaler, autocast',
        'from torch.cuda.amp import GradScaler, autocast',
        content
    )
    
    # autocastの修正
    content = re.sub(
        r'with autocast\(\'cpu\', enabled=hps\.train\.bf16_run, dtype=torch\.bfloat16\):',
        'with autocast(\'cpu\', dtype=torch.bfloat16):',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"{file_path} の修正が完了しました。")
    return True

def main():
    """メイン関数"""
    if len(sys.argv) > 1:
        style_bert_path = sys.argv[1]
    else:
        style_bert_path = input("Style-Bert-VITS2のディレクトリパスを入力してください: ")
    
    train_file = os.path.join(style_bert_path, "train_ms_jp_extra_cpu.py")
    
    if fix_train_file(train_file):
        print("Intel Mac用の修正が完了しました。")
    else:
        print("修正に失敗しました。ディレクトリパスを確認してください。")

if __name__ == "__main__":
    main()
