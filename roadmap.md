## Pain point: my wife writes shopping lists, but they're entirely out of order.

Initial solution: I wrote a script that took in a csv file with columns for item,
section and store. It groups items by section, sections by store and prints to terminal.

## Next iteration:

Build a web app with the same three fields. Iniitially use Twilio to text lists.
Eventually build a react frontend and use react native for a mobile app.
(initial learning needed: learn some javascript/jquery/ajax in order to:
    * add add'l fields as needed. (js, jquery)
    * update dropdown menus based on previous selections. (ajax)


## Planned features:

* Create/save shopping lists and recipe lists.

* All items are associated with a specific store and section.

* For each item, select a store, a section, then an item from dropdown menus or add new by text input.

* Search existing stores to see if there is already section data rather than creating a new store, and update the data.

* send a text message containing the grocery list

## Database model:

Users
* User ID
* hashed password
* email address
* username

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
* list type (shopping_list, recipe)

List_Items
* list ID
* item ID

User_Lists
* User ID (foreign key)
* list ID (foreign key)



OOP model should follow from this, eliminating the many-to-many tables and IDs,
organized hierarchically instead of relationally (e.g. shopping list contains list of items)
