#!/usr/bin/env python3
"""
Script to update liquid glass effects to true glass color (crystal/blue tint)
Replace golden theme with natural glass appearance
"""

import os
import re
import glob
from pathlib import Path

def update_glass_colors(file_path):
    """Update liquid glass colors to natural glass appearance"""
    try:
        print(f"🔷 Processing: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Backup original content
        backup_path = file_path + '.glasscolor_backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        changes_made = False
        original_content = content
        
        # Update liquid-glass-dark CSS to natural glass colors
        old_glass_css = r'''\.liquid-glass-dark\s*\{[^}]*\}'''
        new_glass_css = '''        .liquid-glass-dark {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.25);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
            transition: all 0.3s ease;
        }'''
        
        if re.search(old_glass_css, content):
            content = re.sub(old_glass_css, new_glass_css, content)
            changes_made = True
            print(f"  ✅ Updated liquid-glass-dark to crystal glass")
        
        # Update hover effects
        old_hover_css = r'''\.liquid-glass-dark:hover\s*\{[^}]*\}'''
        new_hover_css = '''        .liquid-glass-dark:hover {
            background: rgba(255, 255, 255, 0.25);
            transform: translateY(-5px);
            box-shadow: 0 15px 35px 0 rgba(31, 38, 135, 0.25);
            border: 1px solid rgba(255, 255, 255, 0.35);
        }'''
        
        if re.search(old_hover_css, content):
            content = re.sub(old_hover_css, new_hover_css, content)
            changes_made = True
            print(f"  ✅ Updated hover effects to crystal glass")
        
        # Also update regular liquid-glass if present
        old_regular_glass = r'''\.liquid-glass\s*\{[^}]*\}'''
        new_regular_glass = '''        .liquid-glass {
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
            transition: all 0.3s ease;
        }'''
        
        if re.search(old_regular_glass, content):
            content = re.sub(old_regular_glass, new_regular_glass, content)
            changes_made = True
            print(f"  ✅ Updated liquid-glass to crystal glass")
        
        # Update regular hover
        old_regular_hover = r'''\.liquid-glass:hover\s*\{[^}]*\}'''
        new_regular_hover = '''        .liquid-glass:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-5px);
            box-shadow: 0 15px 35px 0 rgba(31, 38, 135, 0.3);
        }'''
        
        if re.search(old_regular_hover, content):
            content = re.sub(old_regular_hover, new_regular_hover, content)
            changes_made = True
            print(f"  ✅ Updated regular hover to crystal glass")
        
        if changes_made:
            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Successfully updated glass colors: {file_path}")
        else:
            print(f"ℹ️  No glass CSS found: {file_path}")
        
        # Remove backup if successful
        os.remove(backup_path)
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        # Restore backup if exists
        backup_path = file_path + '.glasscolor_backup'
        if os.path.exists(backup_path):
            os.rename(backup_path, file_path)

def main():
    """Main function to update glass colors in all HTML files"""
    print("🔷 Starting crystal glass color update...")
    
    # Find all safety-video-analytics HTML files
    html_files = glob.glob('pages/safety-video-analytics/*.html', recursive=True)
    
    print(f"📋 Found {len(html_files)} files to process:")
    for file_path in html_files:
        print(f"  - {file_path}")
    
    # Process each file
    for file_path in html_files:
        update_glass_colors(file_path)
    
    print("\n🎉 Crystal glass color update completed!")
    print("📋 Summary:")
    print("   🔷 Changed from golden tint to crystal clear")
    print("   ✨ Natural glass appearance with white/blue tones")
    print("   💎 Subtle blue shadows for depth")
    print("   🌊 True liquid glass aesthetic!")

if __name__ == "__main__":
    main()