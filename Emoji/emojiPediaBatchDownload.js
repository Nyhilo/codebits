/*
 * Generates a powershell to download pngs of all emojis on a publisher page on emojipedia
 * Only works on pages with emojis listed in grid elements
 */

(function() {
    // Verfiy the existence of the grid element
    var $grid = $(".emoji-grid");
    if ($grid.length == 0) {
        console.log("Error: Grid not found.");
        return false;
    }

    // html is the output string
    var html = "<pre>$urls = @(";
    var a = [];

    // Fetch pre-loaded emojis from page
    $grid.find("li:not(.lazyparent) > a > img").each(function() {
        a.push("\"" + $(this).attr("src") + "\"");
    });

    // Fetch laze-loaded emojis (src is not populated yet)
    $grid.find("li.lazyparent > a > img").each(function() {
        a.push("\"" + $(this).attr("data-src") + "\"");
    });

    // Construct output string
    html += a.join(",\n    ");
    html += `
    );
md -Force "emojis" | Out-Null;
$total = $urls.Count;
$counter = 0
foreach ( $url in $urls ) {
    $counter++;
    $filename = $url.Substring($url.LastIndexOf("/") + 1);
    echo "Downloading $counter/$total $filename";
    Invoke-WebRequest $url -OutFile "emojis/$filename";
}</pre>`;

    // Render output string in new tab
    $(window.open().document.body).html(html);
})();