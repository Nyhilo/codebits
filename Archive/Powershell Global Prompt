function Global:prompt { 
    Write-Host '[' -NoNewline
    Write-Host '~' -NoNewline -ForegroundColor Red
    $promptstring = ']'+($pwd -split '\\')[0]+'~\'+$(($pwd -split '\\')[-2] -join '\')+'\'+$(($pwd -split '\\')[-1] -join '\') + '> '
    Write-Host $promptstring -NoNewline
    return " "
}