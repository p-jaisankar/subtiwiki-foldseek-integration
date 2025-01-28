def run_mock_foldseek(query, target):
    # Mock results to simulate Foldseek output
    results = [
        {
            "Query ID": "1TIM_A",
            "Target ID": "1BTM_B",
            "TTM Score": 85.5,
            "QTM Score": 92.1,
            "Alignment Start": 1,
            "Alignment End": 120,
            "E-value": 0.0001,
            "Pident": 98.5,
        },
        {
            "Query ID": "1TIM_B",
            "Target ID": "1BTM_A",
            "TTM Score": 80.2,
            "QTM Score": 90.7,
            "Alignment Start": 10,
            "Alignment End": 100,
            "E-value": 0.002,
            "Pident": 95.4,
        },
    ]
    return results
