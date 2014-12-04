Feature: Reference Official Postal Data

    Scenario: Turn Origianl Text File Into JSON
        Given official documents are in place:
            | doc/name.csv |
            | doc/code.txt |
         When execute the command "npm run compile"
         Then have a valid JSON at "lib/code.json"
          And file "lib/name.json" holds sample:
            | taipeicity    | 臺北市 | Taipei City     |
            | newtaipeicity | 新北市 | New Taipei City |
            | tainancity    | 臺南市 | Tainan City     |
            | nantoucounty  | 南投縣 | Nantou County   |
            | yilancounty   | 宜蘭縣 | Yilan County    |
            | hualiencounty | 花蓮縣 | Hualien County  |
          And folder "lib" holds folders:
            | kinmencounty   | penghucounty   | taitungcounty    |
            | taichungcity   | taoyuancounty  | keelungcity      |
            | hualiencounty  | hsinchucity    | tainancity       |
            | chiayicity     | chiayicounty   | lienchiangcounty |
            | kaohsiungcity  | yilancounty    | miaolicounty     |
            | yunlincounty   | newtaipeicity  | taipeicity       |
            | changhuacounty | pingtungcounty | nantoucounty     |
          And each area in "lib/name.json" be one js file
