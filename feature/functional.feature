Feature: Reference Official Postal Data

    Scenario: Query Zipcode Without Specifying Address
        Given an express instance loaded as server
         When send http GET to /v1/zipcode
         Then receive a JSON response
          And status code is 400
          And body contains fields:
            | name    | value                          |
            | message | missing required field address |
            | example | ?address=somewhere             |

