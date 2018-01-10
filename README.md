# currencyAPI-aws
Python script that runs on AWS. Scrapes for the most current exchange rates between two given currencies in the game Path of Exile, returns the results as a JSON object to be used in other applications.

endpoint: https://ru95ubxej8.execute-api.us-west-2.amazonaws.com/prod/?league=<any currently active league>&want=<currency type ID>&have=<currency type ID>

example: https://ru95ubxej8.execute-api.us-west-2.amazonaws.com/prod/?league=Abyss&want=6&have=4
  This will return a list of exchange rates for Chaos -> Exalted Orbs ordered from cheapest to most expensive, along with the seller's in game name.
