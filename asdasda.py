a = {
    "id": 2882092,
    "userName": "srabani.haldar@rms.com",
    "status": "FINISHED",
    "submitTime": "2021-06-11T04:33:43.898Z",
    "startTime": "2021-06-11T04:33:46Z",
    "endTime": "2021-06-11T04:35:30Z",
    "name": "PORTFOLIO: Step_SeparateLoc",
    "type": "MRI_IMPORT",
    "jobs": [
        {
            "id": "ea80ed74-7190-4ff1-8c65-898c6dea0d32",
            "workflowId": 2882092,
            "status": "Succeeded",
            "submitTime": "2021-06-11T04:33:46.769Z",
            "createdAt": "2021-06-11T04:33:43.897Z",
            "name": "MRI_IMPORT",
            "input": {
                "name": "MRI_IMPORT"
            },
            "output": {
                "databaseName": "HDFM_testing_SH",
                "hpcJobId": "74579",
                "importSummary": "Imported 2 Accounts and 2 Locations"
            },
            "percentComplete": 100
        }
    ],
    "summary": {
        "databaseName": "HDFM_testing_SH",
        "validationDownloadLink": "Not Available",
        "importSummary": "Imported 2 Accounts and 2 Locations",
        "expirationDate": "Not Available"
    },
    "progress": 100,
    "messages": []
}

print(a["progress"])

