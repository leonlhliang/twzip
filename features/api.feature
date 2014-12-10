Feature: RESTful API HTTP Service

    Background:
        Given an express instance loaded as target server

    Scenario Outline: Ping All Endpoints with Valid Input
         When send a GET request to <endpoint>
         Then receive a JSON response of <status>
          And body contains <field> with <value>
        Examples:
            | endpoint      | status | field    | value |
            | /status       | 200    | version  | 0.1.0 |
            | /v1/zipcode   | 400    | errno    | 001   |
            | /v1/districts | 200    | language | zh-TW |
            | /v1/streets   | 200    | language | zh-TW |
            | /v1/cities    | 200    | language | zh-TW |

    Scenario Outline: Validate Query Strings for /v1/zipcode
         When send a GET request to /v1/zipcode
          And append URL with address=somewhere string
          And append URL with <query> string
         Then receive a JSON response of 400
          And body contains message with <value>
        Examples:
            | query      | value                             |
            | lang=zh-CN | lang must be one of: zh-TW, en-US |
