function Accum($s) {
    $sbuild = ""
    for ($i = 0; $i -lt $s.Length; $i++) {
        for ($j = 0; $j -lt $i + 1; $j++) {
            if ($j -eq 0) {
                $sbuild += [Char]::ToUpper($s[$i])
            } else {
                $sbuild += [Char]::ToLower($s[$i])
            }

            if ($j -eq $i -and $j -ne $s.Length - 1) {
                $sbuild += "-"
            }
        }
    }
    
    return $sbuild
}

Accum 'abcd'
Accum 'RqaEzty'
Accum 'cwAt'
