* Create vision and goals
* Create capabilities
* Create feature model and product map
* Create feature files with user scenarios
* Create feature backlog
* Create CI for products
* Create selected backlog for next sprint
* Planning of selected backlog
  * good first selected backlog would appear to be whatever is shared across all products
* Once we've done the basic features, that covers the first product
* Now I'll add another feature for a different product
* However - we need to get the CI matrix set up somehow
* Kind of also need to show that the first product doesn't have the feature it didn't expect
* Note: we're using annotative approach, compositional could be another
* Now implement the new feature for ProdC
* Note at this point that the feature is now present in ProdA, even though it's not configured
* We need a test to check that it isn't present!
* This is really important: it helps with the development of our variability implementation
* We need some way of knowing which optional fields have not been selected
* Another method of regression tests for features being there that shouldn't be would be screenshots
- exact/best method is out of scope for now, but the principle is very important
* OK, so now I've implement the filter feature, and got basic feature reading in place.
* Next up is to implement the next feature.
- ok so ProdD has the search feature.  Let's add that next.
* First add ProductD to the matrix.
- technically it should get some kind of error, but I think codeception tests won't complain if they don't find a tagged feature.
- that needs some work - but I guess we can add a bare bones feature as well, something that is 'incomplete'.
* add the feature - do the same process, just add it, no feature toggle yet
- how to deal with the combination of search and filter?
