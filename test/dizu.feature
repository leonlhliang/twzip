Feature: Dizu RESTful API

    Scenario: Endpoints Health Check
        Given The server is running
         When Send request to "/zipcode"
         Then Got response status code "200"
