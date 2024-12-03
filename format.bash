birdnest_ai/
│
├── main.py               # File khởi chạy chính
├── requirements.txt      # Danh sách thư viện cần cài đặt
├── config.py             # Cấu hình ứng dụng (thông số cảm biến, camera...)
│
├── models/               # Mô hình AI đã được huấn luyện
│   └── sound_model.pkl   # Ví dụ: mô hình nhận diện âm thanh
│   └── image_model.h5    # Ví dụ: mô hình nhận diện hình ảnh
│
├── data/                 # Thư mục chứa dữ liệu thu thập được
│   ├── raw/              # Dữ liệu gốc (âm thanh, hình ảnh...)
│   └── processed/        # Dữ liệu đã xử lý
│
├── modules/              # Thư mục chứa các module chức năng chính
│   ├── audio_processing.py  # Xử lý âm thanh
│   ├── image_processing.py  # Xử lý hình ảnh
│   └── data_analysis.py     # Phân tích thống kê dữ liệu
│
├── static/               # Tài nguyên tĩnh (nếu tạo giao diện web)
│   └── css/              # File CSS
│
├── templates/            # Template HTML (nếu dùng Flask làm giao diện)
│
└── utils/                # Các tiện ích chung (log, helper functions...)
    └── logger.py         # Ghi log ứng dụng
