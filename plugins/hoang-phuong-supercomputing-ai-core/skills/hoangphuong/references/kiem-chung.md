# Kiểm chứng và bàn giao sản phẩm thật

Đọc khi viết/sửa mã, kiểm thử, tối ưu hiệu năng hoặc xác nhận đã tạo/cập nhật sản phẩm.

## Tệp và lỗi
Khi có quyền ghi, tự tạo/sửa tệp hoàn chỉnh, đọc lại đúng đường dẫn và chạy kiểm tra phù hợp; không chỉ yêu cầu Hoàng Phương sửa dòng mã. Dùng đường dẫn tuyệt đối hoặc launcher tìm thư mục của chính nó. Không nói tệp nằm trên ổ F: hay máy người dùng nếu mới xuất trong môi trường khác. Liên kết bàn giao phải trỏ tới tệp tồn tại.

Khi lỗi xảy ra, tái hiện → tìm nguyên nhân → sửa đúng phần → chạy lại ca lỗi và kiểm tra liên quan. Giữ nguyên yêu cầu khi sửa test; ví dụ 15 mẫu theo lô 10 phải xử lý rõ 5 mẫu còn lại, không đổi đầu vào thành 10 chỉ để xanh. Phân biệt kiểm tra cú pháp, unit test, tích hợp và triển khai. Không cần test cho chỉnh câu chữ nhỏ.

## Đo hiệu năng
Đặt workload, đơn vị, quy mô, môi trường, giới hạn và tiêu chí trước khi tối ưu. Dùng thời gian đo thật, lưu mẫu thô, định nghĩa percentile và số lần chạy. Báo throughput cùng lỗi, độ trễ và điều kiện đo; không suy microbenchmark thành HTTP QPS hay khả năng model. Một print 'đang JIT' hoặc lấy p99 nhân 0.5 không thực hiện tối ưu.

Chỉ đưa bản sửa vào sử dụng sau khi đúng chức năng và không hồi quy trong phạm vi đã thử; có bản trước sửa để khôi phục. Không tự hot-patch kernel/CPU, bỏ memory barrier hoặc tuyên bố lock-free chỉ vì không thấy mutex. Cần mô hình concurrency và bằng chứng đúng cho cấu trúc cụ thể.

## Bằng chứng hoàn thành
Phân biệt: đã thiết kế; đã ghi tệp; đã chạy; đã kiểm thử; đã triển khai; đã xác minh phía đích. Dùng log, kết quả lệnh và đọc lại trạng thái đích để hỗ trợ đúng cấp độ. Lời nói trong chat không thay thế bằng chứng công cụ. Kiểm thử với stub phải ghi rõ phạm vi giả lập.

Helper tùy chọn `scripts/verify_artifacts.py` kiểm tra manifest JSON gồm root tuyệt đối và artifacts[{path,sha256}], trong đó path tương đối và sha256 là hash kỳ vọng đã ghi lúc tạo. Chạy `python <đường-dẫn-helper> <manifest.json>`. Mã thoát 0: tất cả tệp tồn tại và khớp hash; 1: thiếu/sai hash/vượt phạm vi; 2: manifest không hợp lệ. Không thực thi tệp, không chứng nhận nội dung đúng hay test đã chạy. Không dùng helper trên thư mục đang bị bên khác sửa đồng thời như một ranh giới bảo mật.
