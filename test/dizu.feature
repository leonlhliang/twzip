Feature: Reference Official Postal Data

    Scenario: Turn Origianl Text File Into JSON
        Given official documents are in place:
            | doc/translate.csv |
            | doc/zipcode.txt   |
         When execute the command "npm run compile doc/zipcode.txt"
         Then have a valid JSON at "lib/zipcode.json"
