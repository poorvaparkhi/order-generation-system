
## Design Considerations for order ID generation
We want to generate user-friendly order IDs. 
1. Order ID length shouldn't be too short --> system cannot generate enough IDs
2. Order ID length shouldn't be too long --> user cannot identify with it
3. Should be easy on the eye --> it should be human-friendly e.g. user can call it out over the phone to you
4. Existing solutions will become a scaling bottleneck:
      * Auto-incrementing generator - service generating these autoincrementing IDs will be a bottleneck as all DB shards will call it
      * Random number generator - service generating these random IDs will be a bottleneck as all DB shards will call it
      * Prefix `user-id` to order number like USER_ID-ORDER_NUMBER --> your order ID format depends on your `user-id` generation, can result in sticky session if order ID is auto-incrementing.

## Order ID Generator

### Requirements
We want an an algorithm that is:
1. Easy to compute
2. Independent of the node/db shard processing it
3. Scales easily

### Solution
This algorithm generates order-id in this format - `xxxx-xxxxxx-xxxx` , where `x` is a Digit from 0-9. This is the same format Amazon uses to generate order-ids.<br />
The algorithm for generating the order-ids is processed in following 3 steps:

1. First generates a 13 digit current unix timestamp (so it’s unique down to the millisecond)
2. Adds random padding for remaining digits
3. Scrambling order-id using **Cipher Substitution Algorithm** so that the order-id doesn't appear as a timestamp and is not sequential <br />

This algorithm is capable of generating 1,000,000 orders per day (evenly distributed), the probability of collision would be ~1%. The extra padding digit makes it even lower.

### API:

`generate(date)` - Generates an order id. `date` parameter is optional and can be any time for the order id. Otherwise, current date will be used.
