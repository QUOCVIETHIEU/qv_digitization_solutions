// JavaScript cho các chức năng tương tác trên trang web.
// File này sẽ chạy khi trang web được tải hoàn toàn.
document.addEventListener('DOMContentLoaded', () => {
    // Thông báo trong console để xác nhận rằng JavaScript đã được tải
    console.log('Trang web đã được tải hoàn chỉnh!');

    // Lấy phần tử nút dropdown trong menu điều hướng
    const dropdownButton = document.querySelector('nav .group button');

    // Kiểm tra xem nút có tồn tại không trước khi thêm sự kiện
    if (dropdownButton) {
        // Ngăn chặn hành vi mặc định của nút để nó không điều hướng trang
        // và chỉ mở/đóng dropdown
        dropdownButton.addEventListener('click', (event) => {
            event.preventDefault();
        });
    }

    // Bạn có thể thêm các chức năng JavaScript khác vào đây,
    // ví dụ:
    // - Xử lý form liên hệ
    // - Tương tác với API
    // - Các hiệu ứng động phức tạp
});
