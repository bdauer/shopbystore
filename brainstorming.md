**Problem**: Different people will want stores broken up into different sections.

**possible solutions**
You can only modify sections for a store that's yours. If you modify someone else's store, it creates a new version bound to you.

Allow for freeform and aisle mappings. Aisle mappings have shared editing permissions.

Original creator can set a shopping list to shared editing or private editing. Editing a list with private editing creates a new list that can be shared or private.

When showing matching stores, keep lists with shared editing at the top to emphasize collaboration.


**Problem**: Geocoding and reverse Geocoding.

I want to get an address input from users, find the store at that location, and store the store based on its coordinates. Might want to store the address as well to reduce calls to the Geo API. 

**possible solutions**

Look into [this](http://chrisalbon.com/python/geocoding_and_reverse_geocoding.html)

## Database model:

Users
* User ID
* hashed password
* email address
* username
* join_date
* last_login
* last_location(?)

Stores
* Store ID
* state
* city
* street
* store name
* coordinates(?)

User_Stores
* user ID
* store ID

Sections/Aisles
* Section ID
* Store ID (foreign key)
* section name

Items
* Item ID
* item name

Section_Items
* Section_ID
* Item_ID

Lists
* list ID
* list name
* list type (sh
