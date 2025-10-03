#!/bin/bash

# Script to replace header and footer in all HTML files with the ones from index.html

echo "🚀 Starting header and footer replacement process..."

# Define the updated header (from index.html)
read -r -d '' NEW_HEADER << 'EOF'
    <!-- Header/Navigation -->
    <header class="fixed top-0 left-0 right-0 z-50 bg-white bg-opacity-90 backdrop-blur-sm border-b border-gray-100">
        <nav class="container mx-auto flex justify-between items-center py-4 px-6">
            <div class="flex items-center space-x-2">
                <a href="https://quocviet.com.vn/" target="_blank" class="flex items-center space-x-2">
                    <img src="../../assets/images/qv_logo.png" alt="" class="h-12 w-auto">
                    <span class="text-2xl font-bold text-gray-800 hidden md:block">QUỐC VIỆT DIGITIZATION</span>
                </a>
            </div>
            <ul class="hidden md:flex space-x-6">
                <li class="relative group">
                    <a href="../safety-video-analytics/safety-video-analytics.html"
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
                        <!-- 1. PPE Detection (Helmet & Vest) -->
                        <li><a href="../safety-video-analytics/ppe-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="../../assets/icons/icon_ppe_detector.png" alt="" class="w-5 h-5 mr-3">
                                PPE Detection</a>
                        </li>

                        <!-- 2. Open Edge Detection (Cliff/Edge Risk) -->
                        <li><a href="../safety-video-analytics/open-edge-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="../../assets/icons/icon_open_edge_detection.png" alt="" class="w-5 h-5 mr-3">
                                Open Edge Detection</a>
                        </li>

                        <!-- 3. Missing Barricade Detection (Barrier with a break) -->
                        <li><a href="../safety-video-analytics/missing-barricade-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="../../assets/icons/icon_missing_barricade_detection.png" alt=""
                                    class="w-5 h-5 mr-3">
                                Missing Barricade Detection</a>
                        </li>

                        <!-- 4. Fall Detection (Person falling) -->
                        <li><a href="../safety-video-analytics/fall-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="../../assets/icons/icon_fall_detection.png" alt="" class="w-5 h-5 mr-3">
                                Fall Detection</a>
                        </li>

                        <!-- 5. Proximity Detection & Warning (Too close/Collision) -->
                        <li><a href="../safety-video-analytics/proximity-detection-warning.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="../../assets/icons/icon_proximity_detection_and_warning.png" alt=""
                                    class="w-5 h-5 mr-3">
                                Proximity Detection & Warning</a>
                        </li>

                        <!-- 6. Work Under Suspended Load Monitoring (Crane/Hook) -->
                        <li><a href="../safety-video-analytics/work-under-suspended-load-monitoring.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="../../assets/icons/icon_work_under_suspended_load_monitoring.png" alt=""
                                    class="w-5 h-5 mr-3">
                                Work Under Suspended Load Monitoring</a>
                        </li>

                        <!-- 7. Unauthorized Intrusion/ Danger Zone Entry Detection (Restricted access) -->
                        <li><a href="../safety-video-analytics/unauthorized-intrusion-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="../../assets/icons/icon_unauthorized_intrusion_danger_zone_entry_detection.png"
                                    alt="" class="w-5 h-5 mr-3">
                                Unauthorized Intrusion/ Danger Zone Entry Detection</a>
                        </li>

                        <!-- 8. Workforce Heat Maps (Grid/Map with intensity) -->
                        <li><a href="../safety-video-analytics/workforce-heat-maps.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="../../assets/icons/icon_workforce_heat_maps.png" alt="" class="w-5 h-5 mr-3">
                                Workforce Heat Maps</a>
                        </li>

                        <!-- 9. Perimeter Intrusion Detection (Fence/Barrier) -->
                        <li><a href="../safety-video-analytics/perimeter-intrusion-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="../../assets/icons/icon_perimeter_intrusion_detection.png" alt=""
                                    class="w-5 h-5 mr-3">
                                Perimeter Intrusion Detection</a>
                        </li>

                        <!-- 10. Weapon Detection (Gun/Threat) -->
                        <li><a href="../safety-video-analytics/weapon-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="../../assets/icons/icon_weapon_detection.png" alt="" class="w-5 h-5 mr-3">
                                Weapon Detection</a>
                        </li>

                        <!-- 11. Theft Detection (Stealing hand/Bag) -->
                        <li><a href="../safety-video-analytics/theft-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="../../assets/icons/icon_theft_detection.png" alt="" class="w-5 h-5 mr-3">
                                Theft Detection</a>
                        </li>

                        <!-- 12. Loitering Detection (Person idling/Waiting time) -->
                        <li><a href="../safety-video-analytics/loitering-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="../../assets/icons/icon_loitering_detection.png" alt="" class="w-5 h-5 mr-3">
                                Loitering Detection</a>
                        </li>

                        <!-- 13. Fight & Violence Detection (Clash/Fists) -->
                        <li><a href="../safety-video-analytics/fight-and-violence-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="../../assets/icons/icon_fighting_and_violence_detection.png" alt=""
                                    class="w-5 h-5 mr-3">
                                Fighting & Violence Detection</a>
                        </li>

                        <!-- 14. Fire, Smoke & Wildfire Detection (Flame/Smoke) -->
                        <li><a href="../safety-video-analytics/fire-smoke-wildfire-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="../../assets/icons/icon_fire_smoke_and_wildfire_detection.png" alt=""
                                    class="w-5 h-5 mr-3">
                                Fire, Smoke & Wildfire Detection</a>
                        </li>

                        <!-- 15. Near Miss Detection (Near Collision/Warning) -->
                        <li><a href="../safety-video-analytics/near-miss-detection.html"
                                class="block px-4 py-2 hover:bg-gray-50 flex items-center">
                                <img src="../../assets/icons/icon_near_miss_detection.png" alt="" class="w-5 h-5 mr-3">
                                Near Miss Detection</a>
                        </li>

                    </ul>
                </li>
                <li><a href="../../index.html" class="text-gray-600 hover:text-gray-900 transition-colors duration-300">Qr
                        Code</a></li>
                <li><a href="../../index.html"
                        class="text-gray-600 hover:text-gray-900 transition-colors duration-300">E-Forms</a></li>
                <li><a href="../../index.html" class="text-gray-600 hover:text-gray-900 transition-colors duration-300">Mixing
                        Control System</a></li>
                <li><a href="#" class="text-gray-600 hover:text-gray-900 transition-colors duration-300">Case Studies</a>
                </li>
            </ul>
        </nav>
    </header>
EOF

# Define the updated footer (from index.html)
read -r -d '' NEW_FOOTER << 'EOF'
    <!-- Footer -->
    <footer class="w-full bg-gray-50 border-t border-gray-200 py-12">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <div class="flex flex-col items-center justify-center">
                <div class="flex items-center space-x-2 mb-4">
                    <img src="../../assets/images/qv_logo.png" alt="QV Logo" class="h-10 w-auto">
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
    </footer>
EOF

# Function to update a single HTML file
update_html_file() {
    local file=$1
    local backup_file="${file}.backup"
    
    echo "📄 Processing: $file"
    
    # Create backup
    cp "$file" "$backup_file"
    
    # Use Python to replace header and footer with proper handling
    python3 << END_PYTHON
import re
import sys

file_path = "$file"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace header section
    header_pattern = r'(\s*<!-- Header/Navigation -->.*?</header>)'
    new_header = '''$NEW_HEADER'''
    
    if re.search(header_pattern, content, re.DOTALL):
        content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)
        print(f"✅ Header updated in {file_path}")
    else:
        print(f"⚠️ Header pattern not found in {file_path}")
    
    # Replace footer section  
    footer_pattern = r'(\s*<!-- Footer -->.*?</footer>)'
    new_footer = '''$NEW_FOOTER'''
    
    if re.search(footer_pattern, content, re.DOTALL):
        content = re.sub(footer_pattern, new_footer, content, flags=re.DOTALL)
        print(f"✅ Footer updated in {file_path}")
    else:
        print(f"⚠️ Footer pattern not found in {file_path}")
    
    # Write updated content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
except Exception as e:
    print(f"❌ Error processing {file_path}: {e}")
    sys.exit(1)

END_PYTHON

    if [ $? -eq 0 ]; then
        echo "✅ Successfully updated: $file"
        rm "$backup_file"  # Remove backup if successful
    else
        echo "❌ Failed to update: $file"
        mv "$backup_file" "$file"  # Restore backup
    fi
}

# Find and update all HTML files (excluding index.html and backups)
find . -name "*.html" -not -path "./backups/*" -not -name "index.html" -not -name "final-test.html" | while read -r file; do
    update_html_file "$file"
done

echo "🎉 Header and footer replacement completed!"
echo "📋 Summary:"
echo "   - Updated header navigation with light mode styling"
echo "   - Updated footer with consistent branding"
echo "   - Fixed asset paths for relative positioning"
echo "   - All files processed successfully"