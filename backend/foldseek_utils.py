# Functions to run Foldseek
import subprocess

def run_foldseek(query_file, target_db):
    try:
        output_file = "output/tmp_results.tsv"
        command = [
            "foldseek", "easy-multimersearch",
            query_file, target_db, output_file,
            "--format-mode", "4",
            "--format", "query,target,pident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits,tlen"
        ]
        subprocess.run(command, check=True)
        
        # Parse results
        with open(output_file, 'r') as f:
            results = f.readlines()
        return {"results": results}
    except Exception as e:
        return {"error": str(e)}
