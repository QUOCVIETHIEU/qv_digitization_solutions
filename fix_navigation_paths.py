#!/usr/bin/env python3
"""
Script to fix navigation paths in all HTML files
Fix the double 'pages/' issue in navigation links
"""

import os
import re
import glob
from pathlib import Path

def fix_navigation_paths(file_path):
    """Fix navigation paths in a single HTML file"""
    try:
        print(f"📄 Processing: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Backup original content
        backup_path = file_path + '.pathfix_backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        changes_made = False
        
        # Fix double pages issue: ../pages/safety-video-analytics/ → ./
        # For files IN safety-video-analytics folder
        if 'safety-video-analytics' in file_path:
            # Fix links to other files in same directory
            content = re.sub(r'href="\.\.\/pages\/safety-video-analytics\/', 'href="./', content)
            # Fix links to main navigation
            content = re.sub(r'href="\.\.\/pages\/safety-video-analytics\/safety-video-analytics\.html"', 
                           'href="./safety-video-analytics.html"', content)
            changes_made = True
            print(f"  ✅ Fixed safety-video-analytics internal links")
        
        # Fix asset paths: ../assets/ → ../../assets/ (for files 2 levels deep)
        if file_path.count('/') >= 2:  # Files in subdirectories
            content = re.sub(r'src="\.\.\/assets\/', 'src="../../assets/', content)
            changes_made = True
            print(f"  ✅ Fixed asset paths to ../../assets/")
        
        # Fix navigation links from subdirectories back to root/pages
        if 'pages/' in file_path:
            # Fix main navigation links
            content = re.sub(r'href="\.\.\/index\.html"', 'href="../../index.html"', content)
            content = re.sub(r'href="\.\.\/pages\/', 'href="../', content)
            changes_made = True
            print(f"  ✅ Fixed navigation links to parent directories")
        
        if changes_made:
            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Successfully fixed paths in: {file_path}")
        else:
            print(f"ℹ️  No path changes needed in: {file_path}")
        
        # Remove backup if successful
        os.remove(backup_path)
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        # Restore backup if exists
        backup_path = file_path + '.pathfix_backup'
        if os.path.exists(backup_path):
            os.rename(backup_path, file_path)

def main():
    """Main function to fix all HTML files"""
    print("🚀 Starting navigation path fix process...")
    
    # Find all HTML files excluding index.html and backups
    html_files = []
    for pattern in ['pages/**/*.html']:
        html_files.extend(glob.glob(pattern, recursive=True))
    
    # Filter out backup files
    files_to_process = [f for f in html_files if not f.endswith('.backup')]
    
    print(f"📋 Found {len(files_to_process)} files to process:")
    for file_path in files_to_process:
        print(f"  - {file_path}")
    
    # Process each file
    for file_path in files_to_process:
        fix_navigation_paths(file_path)
    
    print("\n🎉 Navigation path fix completed!")
    print("📋 Summary:")
    print("   ✅ Fixed double 'pages/' paths in navigation")
    print("   ✅ Fixed asset paths for proper loading")
    print("   ✅ Fixed relative navigation between pages")

if __name__ == "__main__":
    main()