#!/usr/bin/env python3
"""
Script to apply liquid glass effects to all safety video analytics pages
Replaces dark cards with premium liquid glass design
"""

import os
import re
import glob
from pathlib import Path

def apply_liquid_glass_effect(file_path):
    """Apply liquid glass effects to a single HTML file"""
    try:
        print(f"🔮 Processing: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Backup original content
        backup_path = file_path + '.glassfx_backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        changes_made = False
        original_content = content
        
        # 1. Add liquid glass CSS if not already present
        if '.liquid-glass' not in content:
            # Find the last CSS class definition
            css_pattern = r'(\s+)\.circle-blur\s*\{[^}]*\}'
            liquid_glass_css = '''
        .liquid-glass {
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.18);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            transition: all 0.3s ease;
        }

        .liquid-glass:hover {
            background: rgba(255, 255, 255, 0.35);
            transform: translateY(-5px);
            box-shadow: 0 15px 35px 0 rgba(31, 38, 135, 0.4);
        }

        .liquid-glass-dark {
            background: rgba(193, 152, 55, 0.1);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border-radius: 20px;
            border: 1px solid rgba(193, 152, 55, 0.2);
            box-shadow: 0 8px 32px 0 rgba(193, 152, 55, 0.1);
            transition: all 0.3s ease;
        }

        .liquid-glass-dark:hover {
            background: rgba(193, 152, 55, 0.15);
            transform: translateY(-5px);
            box-shadow: 0 15px 35px 0 rgba(193, 152, 55, 0.2);
        }'''
            
            if re.search(css_pattern, content):
                content = re.sub(css_pattern, r'\g<0>' + liquid_glass_css, content)
                changes_made = True
                print(f"  ✅ Added liquid glass CSS")
        
        # 2. Replace dark card backgrounds
        dark_card_patterns = [
            r'bg-\[#1A1A22\]\s+p-6\s+rounded-xl\s+shadow-lg\s+hover:scale-105\s+transition-transform\s+duration-300',
            r'bg-\[#0A0A0F\]\s+p-6\s+rounded-xl\s+shadow-lg\s+hover:scale-105\s+transition-transform\s+duration-300',
            r'bg-gray-900\s+p-6\s+rounded-xl\s+shadow-lg\s+hover:scale-105\s+transition-transform\s+duration-300',
            r'bg-black\s+p-6\s+rounded-xl\s+shadow-lg\s+hover:scale-105\s+transition-transform\s+duration-300'
        ]
        
        for pattern in dark_card_patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, 'liquid-glass-dark p-6', content)
                changes_made = True
                print(f"  ✅ Replaced dark cards with liquid glass")
        
        # 3. Update text colors for better readability on glass
        content = re.sub(r'text-gray-400(?=[\s"\'>\]])', 'text-gray-700', content)
        content = re.sub(r'text-gray-300(?=[\s"\'>\]])', 'text-gray-600', content)
        
        # 4. Replace any remaining dark backgrounds in cards
        content = re.sub(
            r'class="bg-\[#[0-9A-Fa-f]{6}\]\s+([^"]*)"([^>]*>)',
            lambda m: f'class="liquid-glass-dark {m.group(1).replace("rounded-xl shadow-lg hover:scale-105 transition-transform duration-300", "").strip()}"' + m.group(2),
            content
        )
        
        if content != original_content:
            changes_made = True
        
        if changes_made:
            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ Applied liquid glass effects")
        else:
            print(f"  ℹ️  No dark cards found")
        
        # Remove backup if successful
        os.remove(backup_path)
        
        if changes_made:
            print(f"✅ Successfully updated: {file_path}")
        else:
            print(f"ℹ️  No changes needed: {file_path}")
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        # Restore backup if exists
        backup_path = file_path + '.glassfx_backup'
        if os.path.exists(backup_path):
            os.rename(backup_path, file_path)

def main():
    """Main function to apply liquid glass effects to all HTML files"""
    print("🔮 Starting liquid glass effect application...")
    
    # Find all safety-video-analytics HTML files
    html_files = glob.glob('pages/safety-video-analytics/*.html', recursive=True)
    
    print(f"📋 Found {len(html_files)} files to process:")
    for file_path in html_files:
        print(f"  - {file_path}")
    
    # Process each file
    for file_path in html_files:
        apply_liquid_glass_effect(file_path)
    
    print("\n🎉 Liquid glass effect application completed!")
    print("📋 Summary:")
    print("   ✅ Replaced dark cards with liquid glass design")
    print("   ✅ Added premium blur and transparency effects")
    print("   ✅ Updated text colors for better readability")
    print("   ✅ Enhanced hover animations")
    print("   ✨ Cards now have modern glass morphism style!")

if __name__ == "__main__":
    main()