// Beispiel JavaScript, um Inhalt dynamisch zu laden (Inhalt sollte vom Server kommen)
document.addEventListener('DOMContentLoaded', () => {
    const contentDiv = document.getElementById('content');
    
    // Hier kannst du Inhalte per Fetch-API nachladen und ins contentDiv einfügen.
    // Zum Beispiel:
    // fetch('path_to_your_content_endpoint').then(response => response.text()).then(html => contentDiv.innerHTML = html);
});
