# Tích hợp HoangPhuong Core — chuẩn bị, chưa triển khai

- Định danh mới: `revidapi-reup-video-vn`, giữ nguyên ID Agent/Skill hiện có.
- Cụm 05 Content & Media (primary), cụm 06 Social Growth (reference).
- Không thay đổi các adapter video HyperFrames, Remotion, OpenMontage.
- Không thêm Agent profile/108 mã học tập.
- Plugin host hiện có CHƯA sửa đổi.

## Release gates
1. Sao lưu, xuất manifest, hash bản Core hiện hành.
2. Checkout upstream ở SHA chính xác và quét nguồn trong sandbox.
3. Kiểm tra giấy phép, lock dependencies, audit CVE, SBOM.
4. Chạy các test upstream trong network sandbox với API key unset.
5. Áp dụng patch stage lên checkout staging, test khóa API thật + kiểm thử hồi quy.
6. Dùng local file được phép, âm thanh offline, chạy upstream render không gọi API.
7. Kiểm tra MP4/ffprobe, stdout/stderr, egress, IO limits.
8. So sánh danh sách plugin trước/sau, được duyệt rồi mới đẩy release.

## Trạng thái
- source_reviewed: partial static review
- adapter_packaged: yes (standalone archive)
- patch_real_upstream_verified: no
- offline_synthetic_render_verified: yes
- upstream_engine_verified: no
- host_integrated: no
- host_verified: no
