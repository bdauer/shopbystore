## Problem

my wife writes shopping lists, but they're entirely out of order.

## Initial solution:

I wrote a [script](https://github.com/bdauer/shoppinglistsorter) that took in a csv file with columns for item,
section and store. It groups items by section, sections by store and prints to terminal.

## Next iteration:

Build a web app with the same three fields. Options for sending the lists: Twilio, smtp, file export, on-screen display. Will evaluate when I get there.

## Planned features:

* User login

* Create/save shopping lists and recipe lists.

* Lists can be private or public.

* Items in list are associated with a specific store and section.

* For each item: select a store, a section, then an item from dropdown menus or add new by text input.

* When adding a store, the program checks to see if it's similar to other stores in the db.
