# Specify the maximum number of instances to keep running
$maximumInstances = 1

# Get all instances of the process
$runningProcesses = Get-Process -Name "YourProcessName" -ErrorAction SilentlyContinue

# Determine how many instances are running
$runningInstances = $runningProcesses.Count

# Stop excess instances
if ($runningInstances -gt $maximumInstances) {
    $processesToStop = $runningProcesses | Select-Object -First ($runningInstances - $maximumInstances)
    foreach ($process in $processesToStop) {
        Stop-Process -Id $process.Id -Force
    }
}

# Start the process if it's not running
if ($runningInstances -lt $maximumInstances) {
    Start-Process -FilePath "C:\Process.exe" -WindowStyle Hidden
}
