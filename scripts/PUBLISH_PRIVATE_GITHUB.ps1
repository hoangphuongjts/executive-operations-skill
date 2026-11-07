# Chạy trên Windows của người dùng sau khi đã đăng nhập gh auth login.
$ErrorActionPreference = 'Stop'
$Repo = 'hoangphuongjts/hoangphuong-chatgpt-portable'
$Directory = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
Set-Location $Directory
foreach ($bin in @('git','gh','python')) {
  if (-not (Get-Command $bin -ErrorAction SilentlyContinue)) { throw "Thieu cong cu: $bin. Hay cai tu trang chu chinh thuc." }
}
Write-Host 'Kiem tra ma nguon/QA offline...'
python scripts/VERIFY_REPO.py
if ($LASTEXITCODE -ne 0) { throw 'VERIFY_REPO failed, do not publish.' }
python scripts/CHECK_PACKAGES.py
if ($LASTEXITCODE -ne 0) { throw 'CHECK_PACKAGES failed, do not publish.' }
$actualLogin = (gh api user --jq .login).Trim()
if ($LASTEXITCODE -ne 0 -or $actualLogin -ne 'hoangphuongjts') { throw 'Sai tai khoan GitHub, ngung.' }
$existing = gh repo view $Repo --json nameWithOwner,isPrivate 2>$null
$exists = ($LASTEXITCODE -eq 0)
if ($exists) {
  $data = $existing | ConvertFrom-Json
  if (-not $data.isPrivate) { throw 'Repo ton tai nhung la PUBLIC; dung ngay.' }
  Write-Host 'GitHub repo private da ton tai. Se push len main neu dung remote.'
} else {
  Write-Host 'Repo chua ton tai. Se TAO MOI voi quyen PRIVATE va push main.'
}
$reply= Read-Host 'Neu da duyet an toan va muon tao/push, nhap chinh xac TAO'
if ($reply -cne 'TAO') { Write-Host 'Da huy an toan'; exit 0 }
if (-not $exists) {
  gh repo create $Repo --private --source . --remote origin --push --description 'Private ChatGPT Skills Plugins Agents migration backup, staging only'
  if ($LASTEXITCODE -ne 0) { throw 'Khong the tao repo, khong tu retry.' }
} else {
  $url="https://github.com/$Repo.git"
  $origin=(git remote get-url origin 2>$null)
  if ($LASTEXITCODE -ne 0) { git remote add origin $url }
  elseif ($origin -notin @($url,"git@github.com:$Repo.git")) { throw 'Remote origin khac repo du kien. Ngung.' }
  git push -u origin main
  if ($LASTEXITCODE -ne 0) { throw 'Push fail. Kiem tra quyen hoac xung dot; khong --force.' }
}
$check=gh repo view $Repo --json nameWithOwner,isPrivate,url | ConvertFrom-Json
if ($LASTEXITCODE -ne 0 -or -not $check.isPrivate) { throw 'Chua xac minh repo private.' }
Write-Host "PRIVATE REPO VERIFIED: $($check.url)"
