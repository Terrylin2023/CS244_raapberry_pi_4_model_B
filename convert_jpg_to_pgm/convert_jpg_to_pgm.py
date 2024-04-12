import sys
from PIL import Image

def convert_jpg_to_pgm(jpg_file):
    # 基於輸入檔案名稱生成PGM檔案名稱
    pgm_file = jpg_file.replace('.jpg', '.pgm').replace('.jpeg', '.pgm')
    
    # 打開JPEG圖像檔案
    with Image.open(jpg_file) as img:
        # 轉換圖像為灰階
        img = img.convert('L')
        # 儲存圖像為PGM格式
        img.save(pgm_file, 'PPM')
    print(f"Converted {jpg_file} to {pgm_file}")

if len(sys.argv) != 2:
    print("Usage: python3 convert_jpg_to_pgm.py input.jpg")
    sys.exit(1)

# 命令行參數
input_file = sys.argv[1]

# 執行轉換
convert_jpg_to_pgm(input_file)
