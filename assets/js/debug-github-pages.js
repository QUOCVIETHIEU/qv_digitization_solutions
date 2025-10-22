/**
 * Debug script for GitHub Pages
 * Thêm script này vào index.html để debug asset loading
 */
function debugGitHubPages() {
    console.log('=== GitHub Pages Debug Info ===');
    console.log('Current URL:', window.location.href);
    console.log('Pathname:', window.location.pathname);
    console.log('Base URL:', window.location.origin + window.location.pathname.split('/').slice(0, -1).join('/'));
    
    // Test asset paths
    const testAssets = [
        'assets/images/qv_logo.png',
        'assets/icons/card_camera_ai.png'
    ];
    
    testAssets.forEach(asset => {
        const img = new Image();
        img.onload = () => console.log('✅ Asset loaded:', asset);
        img.onerror = () => console.log('❌ Asset failed:', asset);
        img.src = asset;
    });
}

// Run on load
document.addEventListener('DOMContentLoaded', debugGitHubPages);