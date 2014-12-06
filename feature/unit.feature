Feature: Test Runs On Local Machine

    Scenario Outline: Handle HTTP Requests
        Given an express instance loaded as server
         Then request to <endpoint> will respond with <status>
         Examples:
            | endpoint | status |
            | /status  | 200    |
