#!/bin/bash
# Script để sửa tất cả đường dẫn asset từ tuyệt đối thành tương đối

echo "🔧 Fixing asset paths for GitHub Pages..."

# Tìm tất cả file HTML trong project
find /Users/voquochieu/Visual\ Code/qv_digitization_solutions -name "*.html" -type f | while read file; do
    # Bỏ qua các file test
    if [[ "$file" == *"test"* ]] || [[ "$file" == *"debug"* ]]; then
        continue
    fi
    
    echo "Processing: $file"
    
    # Sửa đường dẫn assets từ /assets/ thành tương đối
    # Tính toán độ sâu của file để xác định số lượng ../
    relative_path=$(dirname "$file")
    depth=0
    
    # Đếm số thư mục con so với root project
    if [[ "$file" == *"/pages/safety-video-analytics/"* ]]; then
        depth=2
        prefix="../../"
    elif [[ "$file" == *"/pages/"* ]]; then
        depth=1  
        prefix="../"
    else
        depth=0
        prefix=""
    fi
    
    # Thực hiện replace
    sed -i '' "s|/assets/|${prefix}assets/|g" "$file"
    
    echo "  → Fixed asset paths (depth: $depth, prefix: '$prefix')"
done

echo "✅ All asset paths fixed for GitHub Pages!"