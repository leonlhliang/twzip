Feature: Reference Official Postal Data

    Scenario: Turn Origianl Text File Into JSON
        Given the official data as "ORIGIN.txt"
         When execute the command "npm run compile"
         Then have a valid JSON named "zipcode.json"
