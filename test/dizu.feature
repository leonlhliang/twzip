Feature: Reference Official Postal Data

    Scenario: Turn Origianl Text File Into JSON
        Given the official data as "ORIGIN.txt"
         When execute the command "bin/parse.py"
         Then have a valid JSON named "zipcode.json"
