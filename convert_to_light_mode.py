#!/usr/bin/env python3
"""
Script to convert ALL pages to complete light mode
Converts colors, gradients, and styling elements
"""

import os
import re
import glob
from pathlib import Path

def convert_to_light_mode(file_path):
    """Convert a single HTML file to complete light mode"""
    try:
        print(f"📄 Converting: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Backup original content
        backup_path = file_path + '.lightmode_backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        changes_made = False
        original_content = content
        
        # 1. Convert body background and text colors
        content = re.sub(
            r'background-color:\s*#0A0A0F;',
            'background-color: #FFFFFF;',
            content
        )
        content = re.sub(
            r'color:\s*#E2E8F0;',
            'color: #1F2937;',
            content
        )
        
        # 2. Convert text-gradient to golden theme
        content = re.sub(
            r'background-image:\s*linear-gradient\(to right, #4F46E5, #8B5CF6\);',
            'background-image: linear-gradient(to right, #C19837, #CE9522);',
            content
        )
        
        # 3. Convert circle-blur effects (purple to golden)
        content = re.sub(
            r'background:\s*rgba\(139, 92, 246, 0\.4\);',
            'background: rgba(193, 152, 55, 0.2);',
            content
        )
        
        # 4. Convert card hover effects
        content = re.sub(
            r'background-color:\s*rgba\(31, 41, 55, 0\.05\);',
            'background-color: rgba(249, 250, 251, 0.8);',
            content
        )
        
        # 5. Convert text colors throughout
        # White text -> Dark text
        content = re.sub(r'text-white(?=[\s"\'>\]])', 'text-gray-900', content)
        content = re.sub(r'text-gray-100(?=[\s"\'>\]])', 'text-gray-800', content)
        content = re.sub(r'text-gray-200(?=[\s"\'>\]])', 'text-gray-700', content)
        content = re.sub(r'text-gray-300(?=[\s"\'>\]])', 'text-gray-600', content)
        
        # 6. Convert background colors
        # Dark backgrounds -> Light backgrounds
        content = re.sub(r'bg-\[#0A0A0F\]', 'bg-white', content)
        content = re.sub(r'bg-gray-800(?=[\s"\'>\]])', 'bg-gray-100', content)
        content = re.sub(r'bg-gray-900(?=[\s"\'>\]])', 'bg-gray-50', content)
        
        # 7. Convert border colors
        content = re.sub(r'border-gray-700(?=[\s"\'>\]])', 'border-gray-200', content)
        content = re.sub(r'border-gray-800(?=[\s"\'>\]])', 'border-gray-100', content)
        
        # 8. Convert hover effects
        content = re.sub(r'hover:text-white(?=[\s"\'>\]])', 'hover:text-gray-900', content)
        content = re.sub(r'hover:bg-gray-700(?=[\s"\'>\]])', 'hover:bg-gray-100', content)
        content = re.sub(r'hover:bg-gray-800(?=[\s"\'>\]])', 'hover:bg-gray-50', content)
        
        # 9. Convert specific purple gradients to golden
        content = re.sub(
            r'rgba\(79, 70, 229, 0\.15\)',
            'rgba(193, 152, 55, 0.15)',
            content
        )
        
        # 10. Update shadow colors for light mode
        content = re.sub(r'shadow-2xl', 'shadow-lg', content)
        
        # 11. Convert any remaining dark theme elements
        content = re.sub(
            r'#1F2937(?=[\s"\';>])',  # Dark gray
            '#374151',  # Medium gray for light mode
            content
        )
        
        # 12. Fix footer backgrounds if any
        content = re.sub(
            r'bg-gray-900',
            'bg-gray-50',
            content
        )
        
        # 13. Update scrollbar colors
        content = re.sub(
            r'background-color:\s*#4F46E5;',
            'background-color: #C19837;',
            content
        )
        content = re.sub(
            r'background-color:\s*#6D28D9;',
            'background-color: #CE9522;',
            content
        )
        
        if content != original_content:
            changes_made = True
            
            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  ✅ Converted to light mode")
        else:
            print(f"  ℹ️  Already in light mode")
        
        # Remove backup if successful
        os.remove(backup_path)
        
        if changes_made:
            print(f"✅ Successfully converted: {file_path}")
        else:
            print(f"ℹ️  No changes needed: {file_path}")
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        # Restore backup if exists
        backup_path = file_path + '.lightmode_backup'
        if os.path.exists(backup_path):
            os.rename(backup_path, file_path)

def main():
    """Main function to convert all HTML files to light mode"""
    print("🌞 Starting complete light mode conversion...")
    
    # Find all HTML files excluding index.html and backups
    html_files = []
    for pattern in ['pages/**/*.html', '*.html']:
        html_files.extend(glob.glob(pattern, recursive=True))
    
    # Filter out backup files and index.html
    exclude_files = {'index.html', 'final-test.html'}
    exclude_dirs = {'backups'}
    
    files_to_process = []
    for file_path in html_files:
        file_name = os.path.basename(file_path)
        if file_name not in exclude_files and not any(excl_dir in file_path for excl_dir in exclude_dirs):
            files_to_process.append(file_path)
    
    print(f"📋 Found {len(files_to_process)} files to convert:")
    for file_path in files_to_process:
        print(f"  - {file_path}")
    
    # Process each file
    for file_path in files_to_process:
        convert_to_light_mode(file_path)
    
    print("\n🎉 Light mode conversion completed!")
    print("📋 Summary:")
    print("   ✅ Converted backgrounds: Dark → Light")
    print("   ✅ Updated text colors: Light → Dark")
    print("   ✅ Changed gradients: Purple → Golden")
    print("   ✅ Fixed hover effects for light theme")
    print("   ✅ Updated shadows and borders")
    print("   ✅ All pages now consistent light mode!")

if __name__ == "__main__":
    main()