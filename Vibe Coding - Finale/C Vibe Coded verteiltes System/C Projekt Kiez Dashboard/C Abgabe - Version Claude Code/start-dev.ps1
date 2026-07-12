$root = $PSScriptRoot
$logDir = Join-Path $root "logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

$dataProc = Start-Process -FilePath "python" `
  -ArgumentList "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" `
  -WorkingDirectory (Join-Path $root "data-service") `
  -WindowStyle Hidden -PassThru `
  -RedirectStandardOutput (Join-Path $logDir "data-service.log") `
  -RedirectStandardError (Join-Path $logDir "data-service.err.log")

$env:DATA_SERVICE_URL = "http://localhost:8000"
$gwProc = Start-Process -FilePath "node" `
  -ArgumentList "index.js" `
  -WorkingDirectory (Join-Path $root "api-gateway") `
  -WindowStyle Hidden -PassThru `
  -RedirectStandardOutput (Join-Path $logDir "api-gateway.log") `
  -RedirectStandardError (Join-Path $logDir "api-gateway.err.log")

Start-Process -FilePath "python" `
  -ArgumentList "-m", "http.server", "8090" `
  -WorkingDirectory (Join-Path $root "frontend") `
  -WindowStyle Hidden `
  -RedirectStandardOutput (Join-Path $logDir "frontend.log") `
  -RedirectStandardError (Join-Path $logDir "frontend.err.log")

Start-Sleep -Seconds 2
Write-Host "Kiez-Dashboard laeuft:"
Write-Host "  Frontend:     http://localhost:8090"
Write-Host "  API Gateway:  http://localhost:3000"
Write-Host "  Data Service: http://localhost:8000"
Write-Host "Logs: $logDir"
Write-Host "Zum Stoppen: .\stop-dev.ps1"
