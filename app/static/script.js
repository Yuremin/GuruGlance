document.getElementById('filter-btn').addEventListener('click', () => {
    const domain = document.getElementById('domain-select').value;
    fetch(`/researchers?domain=${domain}`)
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('researcher-cards');
            container.innerHTML = '';
            data.forEach(researcher => {
                const card = document.createElement('div');
                card.className = 'researcher-card';
                card.innerHTML = `
                    <h3>${researcher.name}</h3>
                    <p>Domain: ${researcher.domain}</p>
                    <a href="${researcher.homepage}" target="_blank">Homepage</a>
                `;
                container.appendChild(card);
            });
        });
});
