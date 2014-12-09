Feature: Reference Official Postal Data

    Background:
        Given an express instance loaded as target server

    Scenario Outline: Server Health Check
         When send GET request to <endpoint>
         Then receive a JSON response
          And status code is <status>
          And body contains fields:
            | name     | value |
            | language | zh-tw |
        Examples:
            | endpoint      | status |
            | /v1/districts | 200    |
            | /v1/streets   | 200    |
            | /v1/cities    | 200    |

    Scenario: Specify Language Other Than English or Traditional Chinese
         When send GET request to /v1/zipcode
          And specify "lang=zh_cn" in query string
         Then receive a JSON response
          And status code is 404
          And body contains fields:
            | name    | value                                       |
            | message | lang parameter must be one of: zh-tw, en-us |

    Scenario: Query Zipcode Without Specifying Address
         When send GET request to /v1/zipcode
         Then receive a JSON response
          And status code is 400
          And body contains fields:
            | name    | value                          |
            | message | missing required field address |
            | example | ?address=somewhere             |

