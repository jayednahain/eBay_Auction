##Project Issued Date : 24/05/30

> ###Step1:
###Build Authentication system for the User
> ####Features 
* 1.registaion
* 2.log in
* 3.User profile
* 4.Edit profile 
* 5.chanage password
* 6.log out


> ###Step2:
###Build User interface 
* 1.User Profile Page 
* 2.Added auction Gallery
* 3.User add product with category
* 4.Separated User Accounts Function And Shop functionality 
* 5.On CURED operation used  classedBased view 
  * All class basedview applied on a Separated
* user can Uplpad photos with porduct
* 6.Applied a Simple template From 
    * https://colorlib.com/wp/template/bootstrap-sidebar-08/
    * faceing some proplem during handeling static files
    * ***Dropdown doesnt work properly
* Given some restriction User view and public view 


> ###Step3:
### User functionality and data base
* Fixing card size with inner html with style tag
* Appling condition on user production
  * User can view only his uploede product specifically 
  * On user User profile section add a table view by this user can view and delet uploded product easly
* Add restriction on product Edit Delete Upadte wiill enable if a user log in
* Created a model "Bidding_auction"
* combining to two model "User" and "Auction_item"
* "User" and "Auction_item" both Used as forigen key on "Bidding_auction" model
* *****facing so many issues
  * ** cant set Bidding price from front-end
  * ** cant appling any condition for specific user even for a specific product

  

    
    
