#!/usr/bin/env python3
"""
Script to update all text-gray classes to text-gray-900 for better contrast
"""

import os
import re
import glob
from pathlib import Path

def update_text_colors(file_path):
    """Update text-gray colors to text-gray-900 in a single HTML file"""
    try:
        print(f"🔄 Processing: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = False
        
        # Pattern to find text-gray classes (but not text-gray-900 which is already the target)
        # This will match: text-gray, text-gray-100, text-gray-200, ..., text-gray-800
        # But NOT text-gray-900
        patterns_to_replace = [
            # Basic text-gray without number
            (r'\btext-gray(?!-[0-9])', 'text-gray-900'),
            
            # Specific gray levels to text-gray-900 (excluding 900)
            (r'\btext-gray-100\b', 'text-gray-900'),
            (r'\btext-gray-200\b', 'text-gray-900'),
            (r'\btext-gray-300\b', 'text-gray-900'),
            (r'\btext-gray-400\b', 'text-gray-900'),
            (r'\btext-gray-500\b', 'text-gray-900'),
            (r'\btext-gray-600\b', 'text-gray-900'),
            (r'\btext-gray-700\b', 'text-gray-900'),
            (r'\btext-gray-800\b', 'text-gray-900'),
        ]
        
        # Apply replacements
        for pattern, replacement in patterns_to_replace:
            matches = re.findall(pattern, content)
            if matches:
                content = re.sub(pattern, replacement, content)
                changes_made = True
                print(f"  ✅ Replaced {len(matches)} instances of: {pattern}")
        
        if changes_made:
            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Successfully updated: {file_path}")
            return True
        else:
            print(f"ℹ️  No text-gray classes to update: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    """Main function to update text colors in all HTML files"""
    print("🎨 Starting text-gray to text-gray-900 conversion...")
    
    # Find all HTML files excluding backups
    html_files = []
    for pattern in ['pages/**/*.html', '*.html']:
        html_files.extend(glob.glob(pattern, recursive=True))
    
    # Filter out backup files
    files_to_process = [f for f in html_files if 'backup' not in f.lower()]
    
    print(f"📋 Found {len(files_to_process)} files to process:")
    for file_path in files_to_process[:10]:  # Show first 10
        print(f"  - {file_path}")
    if len(files_to_process) > 10:
        print(f"  ... and {len(files_to_process) - 10} more files")
    
    # Process each file
    files_changed = 0
    total_changes = 0
    
    for file_path in files_to_process:
        if update_text_colors(file_path):
            files_changed += 1
    
    print(f"\n🎉 Text color update completed!")
    print("📋 Summary:")
    print(f"   ✅ Files processed: {len(files_to_process)}")
    print(f"   📝 Files changed: {files_changed}")
    print("   🎨 All text-gray classes → text-gray-900")
    print("   💪 Improved text contrast and readability")

if __name__ == "__main__":
    main()