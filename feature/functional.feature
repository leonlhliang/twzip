Feature: Reference Official Postal Data

    Scenario: Turn Origianl Text File Into JSON
        Given required documents are in place:
            | lib/name.json |
            | lib/code.json |
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
          And each area in "lib/name.json" be one "json" file

    Scenario Outline: Making RESTful Requests
        Given an express instance loaded as server
         Then request to <endpoint> will respond with <status>
         Examples:
            | endpoint                | status |
            | /v1/zipcode?hello=world | 200    |
            | /v1/cities?foo=bar      | 200    |

