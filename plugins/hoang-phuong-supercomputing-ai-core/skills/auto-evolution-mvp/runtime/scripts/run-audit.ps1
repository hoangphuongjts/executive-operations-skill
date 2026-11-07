param(
    [Parameter(Mandatory=$true)][string]$SkillsRoot,
    [Parameter(Mandatory=$true)][string]$ReportsDirectory
)
$ErrorActionPreference = "Stop"
Push-Location (Split-Path -Parent $PSScriptRoot)
try {
    py -m hpcore_evolution --root $SkillsRoot --reports $ReportsDirectory cycle
    if ($LASTEXITCODE -ne 0) { throw "Cycle failed: exit $LASTEXITCODE" }
} finally {
    Pop-Location
}
