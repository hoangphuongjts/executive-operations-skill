# Unified Capabilities Hub v14.4 — 172 Skill + 11 Owned Plugins + 19 Connector Namespaces

## Purpose
Treat `hoangphuong-supercomputing-core` as a single **navigation, dispatch and synthesis hub**. A federated catalog is **not** the source code, executable endpoints, authorization, or installation of external plugins. The 128 in-core agent profiles and 7 original skills are retained unchanged. Do not create duplicate plugins or uninstall/overwrite unrelated ones.

## Sources and current inventory (2026-11-04)
- `skills__list`: 180 visible skills; 8 belong to this plugin, **172 external skills** from **22 source families**.
- `Plugin_Creator.list_owned_personal_plugins`: 12 personal plugins, including this one, **11 other owned plugins** (one Nango plugin and one Site may not advertise skills).
- `ALL_TOOLS`: **19 tool namespaces exposed** in the current session. These indicate available tool interfaces, not established authentication or pre-authorized writes.
- Exact URIs, source identities and group routing are in `UNIFIED_CAPABILITIES_CATALOG.json`. These are a **snapshot**, not proof every installed account plugin is visible. Refresh in future sessions; never invent newly installed capabilities.

## Tích hợp và kết nối thực tế (không phá vỡ plugin nguồn)

- Mọi mô tả của **172 Skill ngoài**, 11 plugin cá nhân khác và các namespace công cụ đã được đưa thành **capability reference** bên trong Core. Đây là chuyển **điểm truy cập, metadata, bộ chọn và luồng sử dụng**, không di chuyển plugin gốc hay nhân bản mã nguồn. Các Skill có thể được đọc trực tiếp từ URI gốc khi chúng xuất hiện trong phiên.
- Đã kiểm tra **4 lệnh đọc Skill** và **3 thao tác chỉ đọc trên connector** (Google Drive, vidIQ, Higgsfield) ở phiên kiểm kê. Xem `FEDERATED_CONNECTION_PROBES.json`. Đây là bằng chứng một số kết nối đang dùng được, **không** phải bằng chứng tất cả 19 connector đã xác thực hoặc 172 Skill là công cụ điều khiển độc lập.
- **Một yêu cầu duy nhất:** Core nhận nhiệm vụ -> tra catalog -> đọc đúng Skill nguồn -> chọn 128 vai trò nội bộ (khi phù hợp) -> kiểm tra host cung cấp tool thật -> gọi tool qua connector hiện tại khi có quyền -> kiểm chứng kết quả. Tách rõ quyền đọc và quyền ghi, không tự cấp quyền.
- **Fallback:** nếu một Skill bên ngoài bị gỡ hoặc không còn truy cập, Core có thể hỗ trợ lập kế hoạch bằng tri thức chung nhưng không gán cho nguồn bị thiếu; đánh dấu `external_tool_unavailable` và hướng dẫn cài/kết nối lại đúng nhà cung cấp.
- **Bảo toàn nguồn:** không thay đổi, xóa, xuất lại, di chuyển, đổi tên hay sửa giấy phép của bất kỳ plugin bên ngoài. Điều này giữ các plugin đang hoạt động bình thường và tránh trùng tên hoặc mất đồng bộ các phiên bản.
- **Điều không thể làm chỉ bằng Skill:** sao chép quyền OAuth, token, MCP executable, dịch vụ hosted, hoặc UI ứng dụng từ nhà cung cấp vào Core; các thành phần đó ở plugin gốc và chỉ hoạt động khi plugin đã kết nối/cấp quyền. Nếu muốn một binary/server hợp nhất về sau, cần quyền nguồn và triển khai riêng.

## Trạng thái tích hợp rõ ràng

| Dòng dữ liệu | Trạng thái đúng | Ý nghĩa |
|---|---|---|
| `catalog_registered` | Có dữ liệu trong Core | Có thể tìm và phân loại từ thư viện |
| `source_skill_read_verified` | Đã đọc Skill nguồn bằng công cụ | Có thể áp dụng hướng dẫn Skill trong phiên |
| `provider_read_connected` | Đã gọi công cụ nguồn chỉ đọc và nhận kết quả | Một kết nối có hiệu lực trong phiên, không mặc định cấp quyền ghi |
| `provider_write_executed` | Có log thành công từ tool ghi tương ứng | Chỉ có khi người dùng yêu cầu và cấp quyền phù hợp |
| `requires_connection` | Không có tool hoặc phiên kết nối | Không gọi giả công cụ, không lấy khóa từ Core |

## Dispatch rules
1. Understand the actual task. Use `EMBEDDED_128_INDEX.md` and at most 1–4 specialist roles with #32 reviewer/#64 integrator if needed. Do not auto-load 172 skill descriptions or 128 profile files each time.
2. Search the external catalog by `slug`, `source_plugin`, `cluster` and active capability. Pick 0–3 appropriate *external* sources. Prefer a relevant installed/connected provider rather than cloning its tool behavior.
3. When a plugin skill is available via `skills__read`, **read its original Skill** from its own listed URI, and follow its constraints. A reference alone does not authorize using its complete text, code, data or private backend. Do not embed third-party Skill source into this plugin.
4. For tools, check that the exact namespace/tool is **actually available now**, connect/authorize if needed using appropriate UI, and obtain user approval for irreversible/external actions. The catalog is not a proxy runtime and cannot execute unavailable plugin commands.
5. Classify outcome as one of: `core_embedded_role_analysis`, `external_skill_guidance_applied`, `external_tool_executed` (with real tool evidence), `external_tool_unavailable`, or `requires_connection`. Don't claim all 172 skills run through one API.
6. Expert disagreements should be reviewed with evidence and basic counterexamples before delivery; when running just the same ChatGPT model, treat debate as **simulated multi-perspective analysis**, not real separate agents.
7. Do not automatically register 128 additional tools, create separate agents, fine-tune models, start VPS/Docker, or incur usage charges. Runtime remains frozen until a separate explicit user request.
8. Keep cross-domain material segmented to avoid leaking project data across tools; never export secrets/private records to external sources without authorization.

## Recommended category mapping
| Scenario | Possible sources | In-core groups |
|---|---|---|
| Coding, audit, vulnerability | `ai-coding-vietnamese-kit`, `superpowers`, `GitHub` | 02,03,04,12,16 |
| Video, content, channel growth | `content-ai-vietnam`, `channel-growth-agent-vn`, `vidIQ`, `HeyGen`, `Runway` | 09,13,16 |
| Design, website, 3D | `Canva`, `Higgsfield`, `hyperframes-vn-chatgpt` | 09,13,15 |
| Files, reports, Google ecosystem | `google-drive`, `LlamaParse`, `openai-templates` | 08,10 |
| Plugins/tools/automation | `plugin-creator`, `ai-tool-manager-vn`, `Automations` | 08,11 |
| Financial analysis/planning | `openai-templates`, core `phantichdautu` | 01,14,16 |
| Software reimplementation (authorized assets only) | `software-rebuild-ai-vn` | 02,03,04,12 |

The hub does **not** have an MCP delegation service that can automatically call arbitrary third-party plugin tools. Use actual host tools with documented interfaces, and make dependencies explicit.

## Practical use
- `@hoangphuong-supercomputing-core Hãy chọn Skill tốt nhất để kiểm toán code GitHub, triển khai nếu có quyền.`
- `@hoangphuong-supercomputing-core Dùng Content AI Việt Nam, Xây Kênh và vidIQ để tối ưu kênh. Chỉ truy xuất dữ liệu khi được phép.`
- `@hoangphuong-supercomputing-core Cho mình danh sách Skill tạo video đang có, phân loại nguồn và công cụ.`

## Limits
- The visible skills may not be fully usable in another conversation, even if their URIs are in the catalog. No credential data is copied; no installation/migration of third-party plugins occurs.
- This design provides **centralized discovery and responsible orchestration**, not physical merger or transfer of vendor-owned executable functionality. Non-transferable licensing, runtime and permissions remain with the source plugin.
