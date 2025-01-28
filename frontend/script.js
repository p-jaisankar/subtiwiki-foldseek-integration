document.getElementById('foldseekForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const queryFile = document.getElementById('queryFile').value;
    const targetDb = document.getElementById('targetDb').value;

    const response = await fetch('http://127.0.0.1:5000/api/foldseek', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query_file: queryFile, target_db: targetDb }),
    });

    const data = await response.json();
    const results = data.results;

    const resultsTable = document.querySelector('#resultsTable tbody');
    resultsTable.innerHTML = '';

    results.forEach(result => {
        const row = `<tr>
            <td>${result['Query ID']}</td>
            <td>${result['Target ID']}</td>
            <td>${result['TTM Score']}</td>
            <td>${result['QTM Score']}</td>
            <td>${result['Alignment Start']}</td>
            <td>${result['Alignment End']}</td>
            <td>${result['E-value']}</td>
            <td>${result['Pident']}</td>
        </tr>`;
        resultsTable.insertAdjacentHTML('beforeend', row);
    });
});
