# Send a plain-text email from the Outlook desktop app signed in on this PC.
#
#     powershell -File _tools/send_mail.ps1 -To leon@example.com -Subject "Hub report" -BodyFile reports/2026-01-01.md
#
# Needs classic Outlook for Windows, installed and signed in. It sends as that account and
# stores no password. The "new Outlook" app and Outlook on the web cannot be driven this way.
param(
    [Parameter(Mandatory)][string]$To,
    [Parameter(Mandatory)][string]$Subject,
    [Parameter(Mandatory)][string]$BodyFile
)
$ErrorActionPreference = "Stop"

$outlook = New-Object -ComObject Outlook.Application
$mail = $outlook.CreateItem(0)
$mail.To = $To
$mail.Subject = $Subject
$mail.Body = Get-Content -Raw -Encoding UTF8 $BodyFile
$mail.Send()
Write-Output "sent to $To"
