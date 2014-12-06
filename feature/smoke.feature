Feature: Test Runs On Local Machine

    Scenario: On Every Source File Save
         Then folder "lib" holds folders:
            | kinmencounty   | penghucounty   | taitungcounty    |
            | taichungcity   | taoyuancounty  | keelungcity      |
            | hualiencounty  | hsinchucity    | tainancity       |
            | chiayicity     | chiayicounty   | lienchiangcounty |
            | kaohsiungcity  | yilancounty    | miaolicounty     |
            | yunlincounty   | newtaipeicity  | taipeicity       |
            | changhuacounty | pingtungcounty | nantoucounty     |
          And each area in "lib/name.json" be one "json" file

    Scenario Outline: Server Health Check
        Given an express instance loaded as server
         When send http GET to <endpoint>
         Then receive response of <status>
        Examples:
            | endpoint      | status |
            | /v1/zipcode   | 400    |
            | /v1/cities    | 200    |
            | /v1/districts | 200    |
            | /v1/roads     | 200    |
            | /status       | 200    |
