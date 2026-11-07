"""Non-destructive 16-cluster reference index.  No installed upstream repos."""
CLUSTERS = (
(1,'Tri thức & phương pháp khoa học'),
(2,'Kiến trúc hệ thống'),
(3,'Kỹ thuật phần mềm'),
(4,'Kiểm thử & kiểm định'),
(5,'Hiệu năng & HPC'),
(6,'Lượng tử, mật mã & P2P'),
(7,'AI & thuật toán'),
(8,'Điều phối & vận hành'),
(9,'Sản phẩm & UX'),
(10,'Dữ liệu & tri thức'),
(11,'Agent & công cụ'),
(12,'An toàn & bảo mật'),
(13,'Nội dung & đa phương thức'),
(14,'Tài chính & quyết định'),
(15,'3D, thiết bị & IoT'),
(16,'Đánh giá & chất lượng'),
)
REPLACEMENTS={
3:('K-Dense-AI/scientific-agent-skills','pallets/flask','duplicate across clusters 1/3'),
9:('18F/ux-guide','uswds/uswds','source archived'),
10:('linzeqipku/SnowGraph','apache/airflow','source archived'),
16:('zapier/automationbench','promptfoo/promptfoo','duplicate across clusters 8/16'),
}

def inventory():
    return [{'cluster_id':i,'name':name,'target_slots':24,'source':'existing Core GITHUB_16x24_CANDIDATES.json','upstream_installed':0, 'audit_status':'preliminary_only'} for i,name in CLUSTERS]
