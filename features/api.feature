Feature: RESTful API HTTP Service

    Background:
        Given an express server loaded as target

    Scenario Outline: Ping All Endpoints with Valid Input
         When send a GET request to <endpoint>
         Then receive a JSON response of <status>
          And body's "<field>" equals "<value>"
        Examples:
            | endpoint      | status | field    | value    |
            | /status       | 200    | version  | 0.1.0    |
            | /v1/zipcode   | 400    | errno    | 001      |
            | /v1/districts | 200    | language | zh-TW    |
            | /v1/streets   | 200    | language | zh-TW    |
            | /v1/cities    | 200    | language | zh-TW    |

    Scenario Outline: Non-Existing Endpoints Should Fail
        When send a <method> request to <endpoint>
        Then receive a JSON response of 404
         And body's "message" equals "notfound"
        Examples:
            | method  | endpoint   |
            | POST    | /v1/random |
            | GET     | /random    |
            | PUT     | /foo       |
            | DELETE  | /bar.html  |

    Scenario Outline: Respond Unsupported Languages with Error
         When send a GET request to /v1/districts
          And append URL with "<ISO-CODE>" query
         Then receive a JSON response of 400
          And body's "message" equals "lang must be one of: zh-TW, en-US"
        Examples:
            | ISO-CODE   |
            | lang=ja    |
            | lang=en    |
            | lang=zh-CN |

    Scenario: Querying Zipcode With Address
         When send a GET request to /v1/zipcode
          And append URL with "address=台北市士林區中山北路七段" query
         Then receive a JSON response of 200
          And body's "zipcode" equals "00000"
