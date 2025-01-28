document.querySelector('form').addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData(this);
    fetch('/upload', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.text())
    .then(data => {
        const resultsContainer = document.getElementById('results');
        resultsContainer.innerHTML = '';
        // Parse and display the results
        const lines = data.split('\n');
        lines.forEach(line => {
            if (line.trim()) {
                const resultItem = document.createElement('div');
                resultItem.classList.add('result-item');
                const [geneName, targetId, qtm, ttm, chainPairings, position, eValue, probability, score, seqIdentity, alignment] = line.split('\t');

                const geneLink = document.createElement('a');
                geneLink.href = `https://www.ncbi.nlm.nih.gov/gene/${geneName}`;
                geneLink.classList.add('gene-name');
                geneLink.textContent = geneName;
                resultItem.appendChild(geneLink);

                const targetLink = document.createElement('a');
                targetLink.href = `https://www.rcsb.org/structure/${targetId}`;
                targetLink.classList.add('target-id');
                targetLink.textContent = targetId;
                resultItem.appendChild(document.createTextNode(' | '));
                resultItem.appendChild(targetLink);

                resultItem.appendChild(document.createElement('br'));
                resultItem.appendChild(document.createTextNode(`QTM: ${qtm}, TTM: ${ttm}, E-value: ${eValue}, Probability: ${probability}, Score: ${score}, Sequence Identity: ${seqIdentity}`));

                const alignmentBar = document.createElement('div');
                alignmentBar.classList.add('alignment-bar');
                const bar = document.createElement('div');
                bar.classList.add('bar');
                bar.style.width = `${position}%`;
                alignmentBar.appendChild(bar);
                resultItem.appendChild(alignmentBar);

                resultsContainer.appendChild(resultItem);
            }
        });
    })
    .catch(error => console.error('Error:', error));
});
