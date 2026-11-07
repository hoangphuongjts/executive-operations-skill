"""Optional offline starter documents; original AI-generated internal methodology, not verified research."""
from __future__ import annotations
from platform128 import connect, ingest

DATA = {
1:("Phương pháp nghiên cứu khoa học", "Trước mỗi kết luận, phát biểu giả thuyết có thể bị bác bỏ, định nghĩa biến quan sát, đối chứng, phạm vi sai lệch và điều kiện bác bỏ. Tách dữ kiện có nguồn khỏi giả định. Một kết quả đáng tin cần khả năng tái lập, mô tả phương pháp và phản biện độc lập. Nếu chưa có dữ liệu thực nghiệm, chỉ nêu đề xuất nghiên cứu."),
2:("Thiết kế kiến trúc hệ thống", "Định nghĩa yêu cầu chức năng, ràng buộc phi chức năng, mục tiêu SLO, trust boundary, mô hình dữ liệu và hợp đồng API trước khi chọn kiến trúc. Nêu phương án thay thế và trade-off giữa độ phức tạp, chi phí, hiệu năng, khả năng bảo trì. Tránh microservice nếu chưa có nhu cầu vận hành chứng minh."),
3:("Kỹ thuật phần mềm có kiểm thử", "Mã sản xuất cần đầu vào hợp lệ, xử lý lỗi, unit tests, integration tests và quy trình rollback. Bảo vệ secrets bằng biến môi trường hoặc secret manager, không in secrets vào log. Viết kiểm thử cho tình huống xấu và điều kiện biên trước khi tối ưu, sau đó kiểm tra hồi quy."),
4:("Phương pháp kiểm định chất lượng", "Xây test matrix từ yêu cầu và rủi ro. Phân biệt pass, fail, blocked, not-run. Kiểm tra tính đúng, tái lập, bảo mật, tính tương thích và hiệu năng. Không coi việc mã chạy thành công là bằng chứng hệ thống đạt SLO hoặc an toàn khi triển khai public."),
5:("Đo hiệu năng và HPC", "Đo baseline với phần cứng, phiên bản hệ điều hành, workload và công cụ benchmark được ghi lại. Đánh giá throughput, p50, p95, p99 và độ biến thiên; phân biệt warm-up với sustained load. Tối ưu SIMD, cache, concurrency cần kiểm chứng tính đúng trước và sau, tránh tuyên bố tốc độ triệu QPS khi không có đo đạc."),
6:("Mô phỏng lượng tử, mật mã, P2P", "Mô hình lý thuyết và mô phỏng trên máy cổ điển không tương đương kết quả QPU thực. Với mật mã homomorphic cần nêu scheme, key size, threat model và overhead. P2P yêu cầu xác thực node, kiểm soát truy cập và phòng chống metadata leakage. Không tự nhận quantum supremacy."),
7:("Thuật toán và đánh giá mô hình AI", "Đặc tả chính xác input, output, bất biến và giới hạn trước khi đề xuất thuật toán. So sánh với baseline và cận dưới, dùng dữ liệu đối kháng. Khi đánh giá AI, tách train, validation, test; kiểm tra data leakage và tiêu chí chấm độc lập. Độ phức tạp O(log* n) không phổ quát."),
8:("Vận hành và điều phối", "Lập DAG các nhiệm vụ với người chịu trách nhiệm, điều kiện hoàn thành và trạng thái chứng cứ. Dùng retry hữu hạn, timeout, ghi log không chứa bí mật và giới hạn thay đổi có tác động. Mọi giao dịch, xóa dữ liệu hoặc gửi thông điệp ra ngoài cần quyền rõ ràng."),
9:("Nghiên cứu sản phẩm và UX", "Viết giả thuyết về người dùng trước khi xây sản phẩm; phỏng vấn, quan sát nhiệm vụ thật, xác định vấn đề có thể định lượng. Kiểm tra accessibility, hiệu quả điều hướng và khả năng hiểu giao diện. Phân biệt sự hài lòng được đo với nhận xét suy đoán từ chuyên gia."),
10:("Kiến trúc dữ liệu và tri thức", "Lưu provenance cho từng tài liệu: nguồn, tác giả, giấy phép, xác minh, checksum, thời điểm, phạm vi truy cập. RAG chỉ trích dẫn tài liệu đã được cung cấp và phù hợp lĩnh vực. Không coi tài liệu không có giấy phép là được phép huấn luyện; không coi tìm được tài liệu là nội dung đã chính xác."),
11:("Nền tảng nhiều AI agent", "Agent độc lập cần định danh, chính sách công cụ, giới hạn ngân sách, bộ nhớ và vết thực thi riêng. Điều phối tối thiểu số agent phù hợp thay vì gọi đồng loạt. Đầu ra agent là dữ liệu không đáng tin mặc định; cần kiểm định trước khi dùng làm quyết định hoặc công cụ tiếp theo."),
12:("An ninh và độ bền hệ thống", "Áp dụng least privilege, phân quyền, defense in depth và nhật ký sự kiện không chứa secrets. Mô hình hóa prompt injection, SSRF, lộ khóa, rò rỉ tri thức và leo thang quyền. Không cho phép tài liệu RAG thay đổi hướng dẫn hệ thống hoặc cho phép chạy shell. Sao lưu và thử khôi phục trước khi công khai dịch vụ."),
13:("Nội dung đa phương tiện và quyền tác giả", "Chỉ sử dụng tài nguyên tạo gốc hoặc tài nguyên có bằng chứng giấy phép thương mại phù hợp. Lưu attribution, source URL và bản quyền âm nhạc, giọng nói, hình ảnh, video. Kịch bản dựa trên nguồn xác minh, nội dung quảng bá cần người duyệt trước khi đăng. Tách mục tiêu thu hút với thông tin giáo dục đáng tin."),
14:("Tài chính và khoa học quyết định", "Phân biệt dữ liệu tài chính có nguồn với giả định, dùng kịch bản cơ sở, tích cực, tiêu cực và kiểm định độ nhạy. Các dự báo chỉ là mô hình điều kiện, không phải bảo đảm. Nếu quyết định ảnh hưởng tiền thật, cần dữ liệu mới, rủi ro, phí, thuế và khả năng chịu tổn thất."),
15:("CAD 3D, cơ điện tử và IoT", "Thiết kế theo dung sai vật lý và vật liệu in thực tế. Kiểm tra kích thước, overhang, độ bền, khả năng lắp ráp và giới hạn nhiệt/điện. STL/3MF chỉ là tệp hình học cần kiểm tra slicer trước khi in. Thiết bị IoT cần cơ chế cập nhật có xác thực và an toàn khi lỗi kết nối."),
16:("Đánh giá độc lập và bằng chứng", "Đánh giá cấu trúc không đồng nghĩa đánh giá trình độ chuyên môn. Tạo tập thử ngoại mẫu với rubric, người chấm độc lập, độ tin cậy giữa người chấm và tiêu chí fail rõ. Mỗi agent cần đánh giá theo chủ đề, độ đúng, nguồn, giới hạn, chống prompt injection và chi phí. Không cấp danh hiệu tiến sĩ từ self-evaluation."),
}


def seed():
    out=[]
    with connect() as db:
        for group,(title,body) in DATA.items():
            out.append(ingest(db,{'group_id':group, 'title':title,'body':body,
                 'license':'project_original','author':'Bộ tài liệu phương pháp nội bộ (AI-assisted)',
                 'approved_by':'Tệp mẫu hệ thống, chưa phản biện chuyên gia',
                 'permission_proof':'Nội dung mới được tạo cho gói runtime v14.1',
                 'source_url':''}))
    return out

if __name__=='__main__':
    import json
    print(json.dumps({'starter_documents':len(seed()),'status':'internal_unreviewed'},ensure_ascii=False))
