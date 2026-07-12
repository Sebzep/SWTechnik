$ports = 8000, 3000, 8090

foreach ($port in $ports) {
  $conns = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
  if (-not $conns) {
    Write-Host "Port $port : nichts laeuft."
    continue
  }
  foreach ($ownerId in ($conns.OwningProcess | Select-Object -Unique)) {
    Stop-Process -Id $ownerId -Force -ErrorAction SilentlyContinue
    Write-Host "Port $port : Prozess $ownerId gestoppt."
  }
}
