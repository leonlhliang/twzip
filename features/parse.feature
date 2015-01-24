Feature: Parse Official Postal Data Into JS Functions

    Scenario: Turning Rulset Text File Into JSON
        Given required documents are in place:
            | src/name.json |
            | src/rule.json |
         When execute the command "npm run compile"
         Then have a valid JSON at "src/rule.json"
          And file "src/name.json" holds sample:
            | taipeicity    | 臺北市 | Taipei City     |
            | newtaipeicity | 新北市 | New Taipei City |
            | tainancity    | 臺南市 | Tainan City     |
            | nantoucounty  | 南投縣 | Nantou County   |
            | yilancounty   | 宜蘭縣 | Yilan County    |
            | hualiencounty | 花蓮縣 | Hualien County  |
          And folder "src" holds folders:
            | kinmencounty   | penghucounty   | taitungcounty    |
            | taichungcity   | taoyuancounty  | keelungcity      |
            | hualiencounty  | hsinchucity    | tainancity       |
            | chiayicity     | chiayicounty   | lienchiangcounty |
            | kaohsiungcity  | yilancounty    | miaolicounty     |
            | yunlincounty   | newtaipeicity  | taipeicity       |
            | changhuacounty | pingtungcounty | nantoucounty     |
          And each area in "src/name.json" be one JSON file
