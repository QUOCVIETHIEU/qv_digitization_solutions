/**
 * Hàm routing thông minh - tự động sửa đường dẫn dựa trên vị trí hiện tại
 */
function qvSmartRouting() {
    const currentPath = window.location.pathname;
    const currentDepth = (currentPath.split('/').length - 2);
    
    console.log(`QV Routing: Current path = ${currentPath}, Depth = ${currentDepth}`);
    
    // Xác định prefix cần thiết dựa trên độ sâu
    const getCorrectPath = (originalPath) => {
        // Nếu đường dẫn đã có prefix pages/ thì bỏ qua
        if (originalPath.startsWith('pages/')) {
            const result = currentDepth > 0 ? '../'.repeat(currentDepth) + originalPath : originalPath;
            console.log(`QV Routing: pages/ prefix detected: ${originalPath} → ${result}`);
            return result;
        }
        
        // Danh sách các pattern cần thêm pages/ prefix
        const needsPagesPrefix = [
            'safety-video-analytics/',
            'e-forms-report/',
            'qr-code/', 
            'syrup-mixing-controls/',
            'about-us.html'
        ];
        
        // Kiểm tra xem có cần thêm pages/ prefix không
        const needsPrefix = needsPagesPrefix.some(pattern => originalPath.startsWith(pattern)) ||
                          originalPath === 'about-us.html';
        
        if (needsPrefix) {
            const fullPath = 'pages/' + originalPath;
            const result = currentDepth > 0 ? '../'.repeat(currentDepth) + fullPath : fullPath;
            console.log(`QV Routing: Auto-adding pages/: ${originalPath} → ${result}`);
            return result;
        }
        
        return originalPath;
    };
    
    // Sửa tất cả các link trong trang
    document.querySelectorAll('a[href]').forEach(link => {
        const originalHref = link.getAttribute('href');
        
        // Bỏ qua external links và anchors
        if (originalHref.startsWith('http') || 
            originalHref.startsWith('#') || 
            originalHref.startsWith('mailto:') || 
            originalHref === 'index.html' ||
            originalHref === '#') {
            return;
        }
        
        const correctedPath = getCorrectPath(originalHref);
        if (correctedPath !== originalHref) {
            console.log(`QV Routing: Link updated: ${originalHref} → ${correctedPath}`);
            link.setAttribute('href', correctedPath);
        }
    });
    
    console.log('QV Routing: Completed processing all links');
}

/**
 * Tự động sửa các đường dẫn tài nguyên (src, href) để chúng hoạt động chính xác
 * trên các trang có độ sâu thư mục khác nhau.
 */
function qvFixAssetPaths() {
    const path = window.location.pathname;
    // Đếm số lượng dấu '/' để xác định độ sâu.
    // Trừ đi 1 vì path thường kết thúc bằng tên file, không phải '/'.
    // Ví dụ: /pages/foo/bar.html -> ['','pages','foo','bar.html'] -> length 4 -> depth 2
    const depth = path.split('/').length - 2;

    // Nếu trang không nằm trong thư mục con (ví dụ: index.html ở gốc), không cần làm gì.
    if (depth <= 0) return;

    // Tạo tiền tố tương đối, ví dụ: '../' hoặc '../../'
    const prefix = '../'.repeat(depth);

    // Tìm tất cả các thuộc tính có thể chứa đường dẫn cần sửa
    const selectors = [
        'img[src^="assets/"]',
        'link[href^="assets/"]',
        'script[src^="assets/"]',
        'a[href^="assets/"]',
        'img[src^="/assets/"]',
        'link[href^="/assets/"]',
        'script[src^="/assets/"]',
        'a[href^="/assets/"]'
    ].join(', ');

    document.querySelectorAll(selectors).forEach(el => {
        const src = el.getAttribute('src');
        const href = el.getAttribute('href');

        if (src) {
            // Loại bỏ dấu '/' ở đầu nếu có và thêm tiền tố
            el.setAttribute('src', prefix + src.replace(/^\//, ''));
        }
        if (href) {
            el.setAttribute('href', prefix + href.replace(/^\//, ''));
        }
    });
}


/**
 * Tải và chèn nội dung header và footer vào các placeholder.
 * Đồng thời, đảm bảo các đường dẫn trong header/footer được sửa chính xác.
 */
async function qvLoadIncludes() {
    const includes = [
        { id: 'header-placeholder', file: 'header.html' },
        { id: 'footer-placeholder', file: 'footer.html' }
    ];

    // Tính toán đường dẫn cơ sở đến thư mục includes
    const path = window.location.pathname;
    const pageDepth = (path.split('/').length - 2);
    const includesPathPrefix = pageDepth > 0 ? '../'.repeat(pageDepth) : '';
    
    const fetchAndInject = async ({ id, file }) => {
        const placeholder = document.getElementById(id);
        if (!placeholder) return;

        const url = `${includesPathPrefix}pages/includes/${file}`;

        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Network response was not ok for ${url}`);
            }
            let content = await response.text();

            // Sửa đường dẫn bên trong nội dung được tải (header/footer)
            // Thay thế tất cả các đường dẫn bắt đầu bằng / (ví dụ: /assets/...)
            // bằng đường dẫn tương đối chính xác.
            content = content.replace(/(src|href)="\/(?!\/)/g, `$1="${includesPathPrefix}`);

            placeholder.outerHTML = content;
        } catch (error) {
            console.error(`Failed to fetch include file: ${file}.`, error);
            placeholder.innerHTML = `<p style="color: red; text-align: center;">Error loading ${file.split('.')[0]}.</p>`;
        }
    };

    await Promise.all(includes.map(fetchAndInject));

    // Cập nhật năm trong footer sau khi đã chèn
    const yearSpan = document.querySelector('[data-year]');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }
}

// Chạy các hàm khi DOM đã sẵn sàng
document.addEventListener('DOMContentLoaded', () => {
    console.log("QV Scripts Loaded.");
    qvSmartRouting(); // Chạy routing thông minh trước
    qvLoadIncludes();
    qvFixAssetPaths(); // Chạy hàm sửa đường dẫn cho các asset trên trang chính
});

