function Evaporator([double]$content, [double]$evapperday, [double]$threshold) {
    $currentContent = $content
    $thresholdAmount = $threshold / 100 * $currentContent
    $days = 0
    while ($currentContent -gt $thresholdAmount) {
        $currentContent = $currentContent - ($evapperday / 100 * $currentContent)
        $days++
    }

    return $days
}

Evaporator 10 10 10  # 22
Evaporator 10 10 5  # 29
