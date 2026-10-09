# Gera Unir-PDF.html (arquivo único) embutindo pdf-lib.min.js no index.html
Set-Location $PSScriptRoot
$html = Get-Content index.html -Raw -Encoding UTF8
$lib = Get-Content pdf-lib.min.js -Raw -Encoding UTF8
$tag = '<script src="pdf-lib.min.js"></script>'
if (-not $html.Contains($tag)) { throw 'Tag da biblioteca não encontrada no index.html' }
$out = $html.Replace($tag, '<script>' + $lib.Replace('</script', '<\/script') + '</script>')
[IO.File]::WriteAllText("$PWD\Unir-PDF.html", $out, (New-Object Text.UTF8Encoding $false))
Write-Host "Unir-PDF.html gerado."
