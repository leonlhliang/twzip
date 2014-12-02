Feature: Reference Official Postal Data

    Scenario: Turn Origianl Text File Into JSON
        Given official documents are in place:
            | doc/name.csv |
            | doc/code.txt |
         When execute the command "npm run compile doc lib"
         Then have a valid JSON at "lib/code.json"
          And file "lib/name.json" contains sample:
            | taipei  | 臺北市 | Taipei City     |
            | hsinpei | 新北市 | New Taipei City |
            | tainan  | 臺南市 | Tainan City     |
            | nantou  | 南投縣 | Nantou County   |
            | yilan   | 宜蘭縣 | Yilan County    |
            | hualien | 花蓮縣 | Hualien County  |

