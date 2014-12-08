Feature: Reference Official Postal Data

    Background:
        Given an express instance loaded as server

    Scenario: Specify Language Other Than English or Traditional Chinese
         When send http GET to /v1/zipcode
          And specify "lang=zh_cn" in query string
         Then receive a JSON response
          And status code is 404
          And body contains fields:
            | name    | value                                       |
            | message | lang parameter must be one of: zh-tw, en-us |

    Scenario: Query Zipcode Without Specifying Address
         When send http GET to /v1/zipcode
         Then receive a JSON response
          And status code is 400
          And body contains fields:
            | name    | value                          |
            | message | missing required field address |
            | example | ?address=somewhere             |

