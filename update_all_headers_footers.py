#!/usr/bin/env python3
"""
Script to replace header and footer in all HTML files with light mode versions from index.html
"""

import os
import re
import glob
from pathlib import Path

def get_new_header_for_depth(depth=2):
    """Get header HTML with correct relative paths for the given depth"""
    asset_prefix = "../" * depth
    
    return f"""    <!-- Header/Navigation -->
    <header class="fixed top-0 left-0 right-0 z-50 bg-white bg-opacity-90 backdrop-blur-sm border-b border-gray-100">
        <nav class="container mx-auto flex justify-between items-center py-4 px-6">
            <div class="flex items-center space-x-2">
                <a href="https://quocviet.com.vn/" target="_blank" class="flex items-center space-x-2">
                    <img src="{asset_prefix}assets/images/qv_logo.png" alt="" class="h-12 w-auto">
                    <span class="text-2xl font-bold text-gray-800 hidden md:block">QUỐC VIỆT DIGITIZATION</span>
                </a>
            </div>
            <ul class="hidden md:flex space-x-6">
                <li class="relative group">
                    <a href="{asset_prefix}pages/safety-video-analytics/safety-video-analytics.html"
                        class="text-gray-600 hover:text-gray-900 transition-colors duration-300 flex items-center">
                        Safety Camera AI
                        <svg class="ml-2 w-4 h-4 transition-transform transform group-hover:rotate-180" fill="none"
                            stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7">
                            </path>
                        </svg>
                    </a>
                    <ul
                        class="absolute hidden group-hover:block bg-white text-gray-600 rounded-md shadow-lg py-2 mt-0 top-full w-max border border-gray-200">
                        <li><a href="{asset_prefix}pages/safety-video-analytics/ppe-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="{asset_prefix}assets/icons/icon_ppe_detector.png" alt="" class="w-5 h-5 mr-3">
                                PPE Detection</a>
                        </li>
                        <li><a href="{asset_prefix}pages/safety-video-analytics/open-edge-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="{asset_prefix}assets/icons/icon_open_edge_detection.png" alt="" class="w-5 h-5 mr-3">
                                Open Edge Detection</a>
                        </li>
                        <li><a href="{asset_prefix}pages/safety-video-analytics/missing-barricade-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="{asset_prefix}assets/icons/icon_missing_barricade_detection.png" alt=""
                                    class="w-5 h-5 mr-3">
                                Missing Barricade Detection</a>
                        </li>
                        <li><a href="{asset_prefix}pages/safety-video-analytics/fall-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="{asset_prefix}assets/icons/icon_fall_detection.png" alt="" class="w-5 h-5 mr-3">
                                Fall Detection</a>
                        </li>
                        <li><a href="{asset_prefix}pages/safety-video-analytics/proximity-detection-warning.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="{asset_prefix}assets/icons/icon_proximity_detection_and_warning.png" alt=""
                                    class="w-5 h-5 mr-3">
                                Proximity Detection & Warning</a>
                        </li>
                        <li><a href="{asset_prefix}pages/safety-video-analytics/work-under-suspended-load-monitoring.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="{asset_prefix}assets/icons/icon_work_under_suspended_load_monitoring.png" alt=""
                                    class="w-5 h-5 mr-3">
                                Work Under Suspended Load Monitoring</a>
                        </li>
                        <li><a href="{asset_prefix}pages/safety-video-analytics/unauthorized-intrusion-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="{asset_prefix}assets/icons/icon_unauthorized_intrusion_danger_zone_entry_detection.png"
                                    alt="" class="w-5 h-5 mr-3">
                                Unauthorized Intrusion/ Danger Zone Entry Detection</a>
                        </li>
                        <li><a href="{asset_prefix}pages/safety-video-analytics/workforce-heat-maps.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="{asset_prefix}assets/icons/icon_workforce_heat_maps.png" alt="" class="w-5 h-5 mr-3">
                                Workforce Heat Maps</a>
                        </li>
                        <li><a href="{asset_prefix}pages/safety-video-analytics/perimeter-intrusion-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="{asset_prefix}assets/icons/icon_perimeter_intrusion_detection.png" alt=""
                                    class="w-5 h-5 mr-3">
                                Perimeter Intrusion Detection</a>
                        </li>
                        <li><a href="{asset_prefix}pages/safety-video-analytics/weapon-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="{asset_prefix}assets/icons/icon_weapon_detection.png" alt="" class="w-5 h-5 mr-3">
                                Weapon Detection</a>
                        </li>
                        <li><a href="{asset_prefix}pages/safety-video-analytics/theft-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="{asset_prefix}assets/icons/icon_theft_detection.png" alt="" class="w-5 h-5 mr-3">
                                Theft Detection</a>
                        </li>
                        <li><a href="{asset_prefix}pages/safety-video-analytics/loitering-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="{asset_prefix}assets/icons/icon_loitering_detection.png" alt="" class="w-5 h-5 mr-3">
                                Loitering Detection</a>
                        </li>
                        <li><a href="{asset_prefix}pages/safety-video-analytics/fight-and-violence-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="{asset_prefix}assets/icons/icon_fighting_and_violence_detection.png" alt=""
                                    class="w-5 h-5 mr-3">
                                Fighting & Violence Detection</a>
                        </li>
                        <li><a href="{asset_prefix}pages/safety-video-analytics/fire-smoke-wildfire-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="{asset_prefix}assets/icons/icon_fire_smoke_and_wildfire_detection.png" alt=""
                                    class="w-5 h-5 mr-3">
                                Fire, Smoke & Wildfire Detection</a>
                        </li>
                        <li><a href="{asset_prefix}pages/safety-video-analytics/near-miss-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="{asset_prefix}assets/icons/icon_near_miss_detection.png" alt="" class="w-5 h-5 mr-3">
                                Near Miss Detection</a>
                        </li>
                    </ul>
                </li>
                <li><a href="{asset_prefix}index.html" class="text-gray-600 hover:text-gray-900 transition-colors duration-300">Trang chủ</a></li>
                <li><a href="{asset_prefix}pages/qr-code/qr-code.html"
                        class="text-gray-600 hover:text-gray-900 transition-colors duration-300">QR Code</a></li>
                <li><a href="{asset_prefix}pages/e-forms-report/e-forms-report.html"
                        class="text-gray-600 hover:text-gray-900 transition-colors duration-300">E-Forms</a></li>
                <li><a href="#" class="text-gray-600 hover:text-gray-900 transition-colors duration-300">Case Studies</a>
                </li>
            </ul>
        </nav>
    </header>"""

def get_new_footer_for_depth(depth=2):
    """Get footer HTML with correct relative paths for the given depth"""
    asset_prefix = "../" * depth
    
    return f"""    <!-- Footer -->
    <footer class="w-full bg-gray-50 border-t border-gray-200 py-12">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <div class="flex flex-col items-center justify-center">
                <div class="flex items-center space-x-2 mb-4">
                    <img src="{asset_prefix}assets/images/qv_logo.png" alt="QV Logo" class="h-10 w-auto">
                    <span class="text-xl font-bold text-gray-900">Quốc Việt Co.,Ltd</span>
                </div>
                <p class="text-gray-600 max-w-2xl">
                    Chuyên gia hàng đầu trong lĩnh vực chuyển đổi số, giúp doanh nghiệp tối ưu hóa quy trình và tăng
                    trưởng bền vững.
                </p>
                <div class="flex space-x-6 mt-6">
                    <a href="https://www.linkedin.com/company/quoc-viet-trading-and-engineering-co-ltd/posts/?feedView=all"
                        class="text-gray-600 hover:text-gray-900 transition-colors duration-300" aria-label="LinkedIn"
                        target="_blank" rel="noopener noreferrer">
                        <svg class="w-6 h-6" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                            <path
                                d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z">
                            </path>
                        </svg>
                    </a>
                    <a href="https://www.facebook.com/QuocVietTradingAndEngineeringLtd"
                        class="text-gray-600 hover:text-gray-900 transition-colors duration-300" aria-label="Facebook"
                        target="_blank" rel="noopener noreferrer">
                        <svg class="w-6 h-6" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                            <path
                                d="M22.675 0H1.325C.593 0 0 .593 0 1.325v21.35C0 23.406.593 24 1.325 24h11.49v-9.294H9.847v-3.622h2.968V8.413c0-2.94 1.796-4.545 4.416-4.545 1.255 0 2.336.093 2.65.135v3.07l-1.82.001c-1.428 0-1.704.679-1.704 1.675v2.197h3.406l-.444 3.622h-2.962V24h5.807C23.406 24 24 23.406 24 22.675V1.325C24 .593 23.406 0 22.675 0z" />
                        </svg>
                    </a>
                </div>
            </div>
        </div>
        <div class="mt-8 text-center text-gray-600 text-sm">
            <p>&copy; 2025 Quốc Việt Digitization Solutions. All Rights Reserved.</p>
        </div>
    </footer>"""

def get_light_mode_css():
    """Get light mode CSS styles"""
    return """        body {
            font-family: 'Inter', sans-serif;
            background-color: #FFFFFF;
            color: #1F2937;
        }

        .container {
            max-width: 1280px;
        }

        .gradient-bg {
            background-image: linear-gradient(to right, #C19837, #CE9522);
        }

        .card-module {
            background-color: #F9FAFB;
            border: 1px solid #E5E7EB;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .card-module:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 10px 25px rgba(79, 70, 229, 0.15);
            background-color: #F3F4F6;
        }"""

def calculate_depth(file_path):
    """Calculate depth level from root directory"""
    path = Path(file_path)
    parts = path.parts
    # Count how many directories deep we are from the root
    depth = len([p for p in parts if p != '.' and p != path.name]) - 1
    return max(depth, 0)

def update_html_file(file_path):
    """Update a single HTML file with new header and footer"""
    try:
        print(f"📄 Processing: {file_path}")
        
        # Calculate depth for correct relative paths
        depth = calculate_depth(file_path)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Backup original content
        backup_path = file_path + '.backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Update body CSS for light mode
        dark_body_pattern = r'(\s*body\s*\{[^}]*background-color:\s*#[0-9A-Fa-f]{6};[^}]*\})'
        if re.search(dark_body_pattern, content, re.DOTALL):
            content = re.sub(dark_body_pattern, 
                           '''        body {
            font-family: 'Inter', sans-serif;
            background-color: #FFFFFF;
            color: #1F2937;
        }''', content, flags=re.DOTALL)
            print(f"  ✅ Updated CSS to light mode")
        
        # Update gradient-bg for golden theme
        gradient_pattern = r'(\s*\.gradient-bg\s*\{[^}]*\})'
        if re.search(gradient_pattern, content, re.DOTALL):
            content = re.sub(gradient_pattern,
                           '''        .gradient-bg {
            background-image: linear-gradient(to right, #C19837, #CE9522);
        }''', content, flags=re.DOTALL)
            print(f"  ✅ Updated gradient colors")
        
        # Replace header section
        header_pattern = r'(\s*<!-- Header/Navigation -->.*?</header>)'
        new_header = get_new_header_for_depth(depth)
        
        if re.search(header_pattern, content, re.DOTALL):
            content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)
            print(f"  ✅ Header updated")
        else:
            print(f"  ⚠️ Header pattern not found")
        
        # Replace footer section  
        footer_pattern = r'(\s*<!-- Footer -->.*?</footer>)'
        new_footer = get_new_footer_for_depth(depth)
        
        if re.search(footer_pattern, content, re.DOTALL):
            content = re.sub(footer_pattern, new_footer, content, flags=re.DOTALL)
            print(f"  ✅ Footer updated")
        else:
            print(f"  ⚠️ Footer pattern not found")
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Remove backup if successful
        os.remove(backup_path)
        print(f"✅ Successfully updated: {file_path}")
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        # Restore backup if exists
        backup_path = file_path + '.backup'
        if os.path.exists(backup_path):
            os.rename(backup_path, file_path)

def main():
    """Main function to process all HTML files"""
    print("🚀 Starting header and footer replacement process...")
    
    # Find all HTML files excluding index.html and backups
    html_files = []
    for pattern in ['pages/**/*.html', '*.html']:
        html_files.extend(glob.glob(pattern, recursive=True))
    
    # Filter out files we don't want to process
    exclude_files = {'index.html', 'final-test.html'}
    exclude_dirs = {'backups'}
    
    files_to_process = []
    for file_path in html_files:
        file_name = os.path.basename(file_path)
        if file_name not in exclude_files and not any(excl_dir in file_path for excl_dir in exclude_dirs):
            files_to_process.append(file_path)
    
    print(f"📋 Found {len(files_to_process)} files to process:")
    for file_path in files_to_process:
        print(f"  - {file_path}")
    
    # Process each file
    for file_path in files_to_process:
        update_html_file(file_path)
    
    print("\n🎉 Header and footer replacement completed!")
    print("📋 Summary:")
    print("   ✅ Updated header navigation with light mode styling")
    print("   ✅ Updated footer with consistent branding")
    print("   ✅ Fixed asset paths for relative positioning")
    print("   ✅ Converted CSS to light mode theme")

if __name__ == "__main__":
    main()