# PrintFlow Studio — bản cài & cập nhật

**Prepress Automation Suite cho Adobe Illustrator** · Designed by Mr. Haii (In Thành Đạt)

## Tải bản mới nhất
👉 **[Tải PrintFlow Studio – bản mới nhất (.exe)](https://github.com/hei909/printflow-studio-update/raw/main/downloads/PrintFlowStudio_Setup.exe)**  
Các bản theo số phiên bản: thư mục [`downloads/`](downloads)

1. Lưu file và **đóng Illustrator**.
2. Chạy `PrintFlowStudio_Setup_x.y.z.exe` → **Tiếp** → **Cài đặt** → **Hoàn tất**.
3. Mở Illustrator → **Window › Extensions › PrintFlow Studio**.

> Nếu Windows hiện *"Windows protected your PC"*: bấm **More info › Run anyway** (bộ cài chưa có chữ ký số).

Cài hàng loạt không hiện bảng: `PrintFlowStudio_Setup_x.y.z.exe /S`  
Gỡ cài đặt: **Control Panel › Programs › PrintFlow Studio**.

## Cập nhật
Trong PrintFlow Studio bấm nút **bánh răng › Kiểm tra cập nhật**. Chỉ kiểm tra khi người dùng bấm.
Panel đọc file [`latest.json`](latest.json) trong repo này để biết bản mới nhất.

## Module
Layout bìa kỷ yếu · Layout photobook gáy phụ · Sticker Layout Pro · Layout bìa keo gáy · Đặt ốc cắt xén ·
Tạo đường cắt 1 dao · Step & Repeat · Convert JPG · Xếp hình tiết kiệm · Outline phong bì ·
Summa Methods · Add Mark Summa · Text & Number

## Phát hành bản mới (dành cho người bảo trì)
Thư mục `build-kit/`: `build.py VERSION "ghi chú"…` dựng bộ cài NSIS từ `src/extensions` và tạo `latest.json`.
Sau đó chép file `.exe` vào `downloads/` (cả bản có số phiên bản và `PrintFlowStudio_Setup.exe`), cập nhật `latest.json`, commit lên nhánh `main`.
