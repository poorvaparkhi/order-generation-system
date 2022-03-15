###Order Number Generator

This algorithm generates order-id in this format - xxxx-xxxxxx-xxxx, where x is a Digit from 0-9. This is the same format Amazon uses to generate order-ids.<br />
The algorithm for generating the order-ids is processed in following 3 steps:

1. First generates a 13 digit current unix timestamp (so it’s unique down to the millisecond)
2. Adds random padding for remaining digits
3. Scrambling order-id using Cipher Substitution Algorithm so that the order-id doesn't appear as a timestamp and is not sequential <br />

This algorithm is capable of generating 1,000,000 orders per day (evenly distributed), the probability of collision would be ~1%. The extra padding digit makes it even lower.

API:

generate(date)- Generates an order id. `date` parameter is optional and can be any time for the order id. Otherwise, current date will be used.