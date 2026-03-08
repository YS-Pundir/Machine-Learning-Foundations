1. * As far as i have learned databases are base of any ai models , on which they are being trained . In realworld ai system , database stores the large amount of complex data which will help the ai model to be trained properly , so that it is capable of solving the realworld problems. 
   * The type of data which is stored in those databases is structured  data , which is in tabular form . The data should be acccurately processed and cleaned to be used as database for ai models.
   * Structured storage is naccesry , because if the storage of data is not structured then it may led to confusion in model while prediction . It will led to condition like underfitting or overfitting , which is not good sign in training models .

2. * Tables (The Big Boxes)
     A table is just a category. Its like a folder for one "thing." If you have a store, you have a table for Stuff_To_Sell and a table for People_Who_Buy. You dont want to mix them up or it gets real confusing real fast.

    * Columns (The Top Part)
     Columns are the labels at the top. They tell you what kind of info goes there. Like Name, Price, or Phone_Numbr. You cant put a name in the price spot because the computer gets mad. Its like a rule for what fits in the box.

    * Rows (The Peeple/Things)
    A row is just one single item. If you have a Students table, one row is just ME. It has my name, my grade (probly a D), and my ID. Every row has to be unique so the database doesnt get confused between two people with the same name.

    > why one thing per tabel? : --> If we have diffrent entitties in a single table , it would eb hardd for us to modify and understaand that table . for example : if we have employee and orders data in one table then for changing one entities , we will  have to mess up with other entity as well . which would be tidious task .

3. A primary key is a column (or set of columns) that uniquely identifies each row in a table.

   * why it gotta be unique?
   if two rows have the same primary key, the whole thing breaks.

    no twins: if u have two "ID 10" rows, and u tell the computer "delete ID 10," it might delete both of them or the wrong one.

    finding stuff: it's like a shortcut. if the key is unique, the computer can find exactly what u want super fast without lookin at every single name or address.

   * what about the "non-null" thing?
   "non-null" just means it cant be empty. u cant have a row with no ID.

   the anchor: if a row doesnt have a primary key, it’s like a ghost. u cant link it to other tabels and u cant really find it easily.

   rules: the database basically forces u to put sumthin there so the data doesnt get lost or "homeless" i guess.

   * how it helps identify records
   without a primary key, a tabel is just a big pile of info. with it, every row has a "name" (the ID) that never changes. so even if a customer changes their email, their phone number, and their last name, their customer_id stays the same. that way the database always knows its still the same person.
