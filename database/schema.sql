# MySQL schema

CREATE TABLE foldseek_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    query_id VARCHAR(50),
    target_id VARCHAR(50),
    pident FLOAT,
    alnlen INT,
    mismatch INT,
    gapopen INT,
    qstart INT,
    qend INT,
    tstart INT,
    tend INT,
    evalue FLOAT,
    bitscore FLOAT,
    tlen INT
);
