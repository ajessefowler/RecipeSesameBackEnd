from datetime import datetime
import enum
import json
from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")

recipes =  [
    {
    "title": "Slow Cooker Chicken and Dumplings",
    "ingredients": [
      "4 skinless, boneless chicken breast halves",
      "2 tablespoons butter",
      "2 (10.75 ounce) cans condensed cream of chicken soup",
      "1 onion, finely diced",
      "2 (10 ounce) packages refrigerated biscuit dough, torn into pieces"
    ],
    "instructions": "Place the chicken, butter, soup, and onion in a slow cooker, and fill with enough water to cover.\nCover, and cook for 5 to 6 hours on High. About 30 minutes before serving, place the torn biscuit dough in the slow cooker. Cook until the dough is no longer raw in the center.\n",
    "picture_link": "55lznCYBbs2mT8BTx6BTkLhynGHzM.S"
  },
  {
    "title": "Awesome Slow Cooker Pot Roast",
    "ingredients": [
      "2 (10.75 ounce) cans condensed cream of mushroom soup",
      "1 (1 ounce) package dry onion soup mix",
      "1 1/4 cups water",
      "5 1/2 pounds pot roast"
    ],
    "instructions": "In a slow cooker, mix cream of mushroom soup, dry onion soup mix and water. Place pot roast in slow cooker and coat with soup mixture.\nCook on High setting for 3 to 4 hours, or on Low setting for 8 to 9 hours.\n",
    "picture_link": "QyrvGdGNMBA2lDdciY0FjKu.77MM0Oe"
  },
  {
    "title": "Brown Sugar Meatloaf",
    "ingredients": [
      "1/2 cup packed brown sugar",
      "1/2 cup ketchup",
      "1 1/2 pounds lean ground beef",
      "3/4 cup milk",
      "2 eggs",
      "1 1/2 teaspoons salt",
      "1/4 teaspoon ground black pepper",
      "1 small onion, chopped",
      "1/4 teaspoon ground ginger",
      "3/4 cup finely crushed saltine cracker crumbs"
    ],
    "instructions": "Preheat oven to 350 degrees F (175 degrees C). Lightly grease a 5x9 inch loaf pan.\nPress the brown sugar in the bottom of the prepared loaf pan and spread the ketchup over the sugar.\nIn a mixing bowl, mix thoroughly all remaining ingredients and shape into a loaf. Place on top of the ketchup.\nBake in preheated oven for 1 hour or until juices are clear.\n",
    "picture_link": "LVW1DI0vtlCrpAhNSEQysE9i/7rJG56"
  },
  {
    "title": "Best Chocolate Chip Cookies",
    "ingredients": [
      "1 cup butter, softened",
      "1 cup white sugar",
      "1 cup packed brown sugar",
      "2 eggs",
      "2 teaspoons vanilla extract",
      "3 cups all-purpose flour",
      "1 teaspoon baking soda",
      "2 teaspoons hot water",
      "1/2 teaspoon salt",
      "2 cups semisweet chocolate chips",
      "1 cup chopped walnuts"
    ],
    "instructions": "Preheat oven to 350 degrees F (175 degrees C).\nCream together the butter, white sugar, and brown sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Dissolve baking soda in hot water. Add to batter along with salt. Stir in flour, chocolate chips, and nuts. Drop by large spoonfuls onto ungreased pans.\nBake for about 10 minutes in the preheated oven, or until edges are nicely browned.\n",
    "picture_link": "0SO5kdWOV94j6EfAVwMMYRM3yNN8eRi"
  },
  {
    "title": "Homemade Mac and Cheese Casserole",
    "ingredients": [
      "8 ounces whole wheat rotini pasta",
      "3 cups fresh broccoli florets",
      "1 medium onion, chopped",
      "3 cloves garlic, minced",
      "4 tablespoons butter, divided",
      "2 tablespoons all-purpose flour",
      "1/4 teaspoon salt",
      "1/8 teaspoon ground black pepper",
      "2 1/2 cups milk",
      "8 ounces Cheddar cheese, shredded",
      "4 ounces reduced-fat cream cheese, cubed and softened",
      "1/2 cup fine dry Italian-seasoned bread crumbs",
      "Reynolds Wrap\u00ae Non Stick Aluminum Foil"
    ],
    "instructions": "Preheat oven to 350 degrees F. Line a 2-quart casserole dish with Reynolds Wrap(R) Pan Lining Paper, parchment side up. No need to grease dish.\nCook the pasta in a large saucepan according to the package directions, adding the broccoli for the last 3 minutes of cooking. Drain. Return to the saucepan and set aside.\nCook the onion and garlic in 2 tablespoons hot butter in a large skillet 5 to 7 minutes or until tender. Stir in flour, salt, and black pepper. Add the milk all at once. Cook and stir over medium heat until slightly thickened and bubbly. Add cheddar cheese and cream cheese, stirring until melted. Pour cheese sauce over the pasta and broccoli and stir until well combined.\nMelt the remaining 2 tablespoons butter and mix with the bread crumbs in a small bowl. Transfer the pasta mixture to the prepared casserole dish. Top with the buttery bread crumbs.\nBake, uncovered, about 25 minutes or until bubbly and internal temperature is 165 degrees F. Let stand for 10 minutes before serving.\n",
    "picture_link": "YCnbhplMgiraW4rUXcybgSEZinSgljm"
  },
  {
    "title": "Banana Banana Bread",
    "ingredients": [
      "2 cups all-purpose flour",
      "1 teaspoon baking soda",
      "1/4 teaspoon salt",
      "1/2 cup butter",
      "3/4 cup brown sugar",
      "2 eggs, beaten",
      "2 1/3 cups mashed overripe bananas"
    ],
    "instructions": "Preheat oven to 350 degrees F (175 degrees C). Lightly grease a 9x5 inch loaf pan.\nIn a large bowl, combine flour, baking soda and salt. In a separate bowl, cream together butter and brown sugar. Stir in eggs and mashed bananas until well blended. Stir banana mixture into flour mixture; stir just to moisten. Pour batter into prepared loaf pan.\nBake in preheated oven for 60 to 65 minutes, until a toothpick inserted into center of the loaf comes out clean. Let bread cool in pan for 10 minutes, then turn out onto a wire rack.\n",
    "picture_link": "jRnWGDXDdyOg3rta4/HVAR2rD19XubC"
  },
  {
    "title": "Chef John's Fisherman's Pie",
    "ingredients": [
      "For potato crust:",
      "3 russet potatoes, peeled and cut into chunks",
      "3 tablespoons butter",
      "1 pinch freshly grated nutmeg",
      "salt and ground black pepper to taste",
      "1 pinch cayenne pepper, or to taste",
      "1/2 cup milk",
      "For the spinach:",
      "2 teaspoons olive oil",
      "12 ounces baby spinach leaves",
      "For the sauce:",
      "3 tablespoons butter",
      "3 tablespoons all-purpose flour",
      "2 cloves garlic, minced",
      "2 cups cold milk, divided",
      "2 teaspoons lemon zest",
      "For the rest:",
      "1 tablespoon butter",
      "salt and ground black pepper to taste",
      "1 pinch cayenne pepper, or to taste",
      "2 pounds boneless cod fillets",
      "1/2 lemon, juiced",
      "1 tablespoon chopped fresh chives for garnish"
    ],
    "instructions": "Bring a large saucepan of salted water and to a boil; add russet potatoes to boiling water and cook until very tender, about 20 minutes. Drain well. Mash in 3 tablespoons butter until thoroughly combined. Season with nutmeg, salt, black pepper, and cayenne pepper to taste. Mash 1/2 cup milk into potato mixture until smooth.\nDrizzle olive oil in a large Dutch oven over medium-high heat, add spinach, and season with a big pinch of salt. Cook, stirring occasionally, until spinach has wilted, about 1 minute. Transfer to a bowl lined with paper towels to wick away excess moisture.\nHeat 3 tablespoons butter and flour in a saucepan over medium heat; whisk mixture to a smooth paste. Cook, stirring constantly, until mixture has a nutty smell and is slightly browned, about 2 minutes. Add chopped garlic; whisk until fragrant, 10 to 20 seconds.\nWhisk 1 cup cold milk into flour mixture; cook until thickened. Whisk in remaining 1 cup milk and lemon zest. Bring white sauce to a gentle simmer, whisking constantly; season with salt. Turn heat to very low and keep sauce warm.\nPreheat oven to 375 degrees F (190 degrees C). Grease an 8x12-inch casserole dish with 1 tablespoon butter.\nSeason buttered pan with salt, black pepper, and cayenne pepper. Lay boneless cod fillets into the pan in a single layer. Season tops of fillets with more salt, black pepper, and cayenne pepper. Spread spinach evenly over fish and drizzle with lemon juice. Spoon white sauce over spinach; give casserole dish several taps and shakes to eliminate bubbles.\nDrop mashed potatoes by heaping spoonfuls over the casserole and spread smoothly to cover. Place dish onto a rimmed baking sheet to catch spills.\nBake in the preheated oven until bubbling, about 40 minutes. Turn on oven's broiler and broil until potato crust has a golden brown top, about 2 minutes. Fish should flake easily. Let stand 10 minutes before serving. Garnish with a sprinkle of chives.\n",
    "picture_link": "aUca10AaD8T2yYvcLOgH/UJlR5/OhOe"
  },
  {
    "title": "Mom's Zucchini Bread",
    "ingredients": [
      "3 cups all-purpose flour",
      "1 teaspoon salt",
      "1 teaspoon baking soda",
      "1 teaspoon baking powder",
      "1 tablespoon ground cinnamon",
      "3 eggs",
      "1 cup vegetable oil",
      "2 1/4 cups white sugar",
      "3 teaspoons vanilla extract",
      "2 cups grated zucchini",
      "1 cup chopped walnuts"
    ],
    "instructions": "Grease and flour two 8 x 4 inch pans. Preheat oven to 325 degrees F (165 degrees C).\nSift flour, salt, baking powder, soda, and cinnamon together in a bowl.\nBeat eggs, oil, vanilla, and sugar together in a large bowl. Add sifted ingredients to the creamed mixture, and beat well. Stir in zucchini and nuts until well combined. Pour batter into prepared pans.\nBake for 40 to 60 minutes, or until tester inserted in the center comes out clean. Cool in pan on rack for 20 minutes. Remove bread from pan, and completely cool.\n",
    "picture_link": "YdgEVyLVffZgh9NZPN3Eqj6MaX8KdzK"
  },
   {
    "title": "The Best Rolled Sugar Cookies",
    "ingredients": [
      "1 1/2 cups butter, softened",
      "2 cups white sugar",
      "4 eggs",
      "1 teaspoon vanilla extract",
      "5 cups all-purpose flour",
      "2 teaspoons baking powder",
      "1 teaspoon salt"
    ],
    "instructions": "In a large bowl, cream together butter and sugar until smooth. Beat in eggs and vanilla. Stir in the flour, baking powder, and salt. Cover, and chill dough for at least one hour (or overnight).\nPreheat oven to 400 degrees F (200 degrees C). Roll out dough on floured surface 1/4 to 1/2 inch thick. Cut into shapes with any cookie cutter. Place cookies 1 inch apart on ungreased cookie sheets.\nBake 6 to 8 minutes in preheated oven. Cool completely.\n",
    "picture_link": "UrgvDGu4roLiho160fTVIwCUrGZna8i"
  },
   {
    "title": "Singapore Chili Crabs",
    "ingredients": [
      "Sauce:",
      "1/2 cup ketchup",
      "1/2 cup chicken broth",
      "1 large egg",
      "2 tablespoons soy sauce",
      "2 tablespoons chile-garlic sauce (such as sambal oelek)",
      "1 tablespoon oyster sauce",
      "1 tablespoon tamarind paste",
      "2 teaspoons fish sauce",
      "2 teaspoons palm sugar",
      "1/4 cup minced shallot",
      "6 cloves garlic, minced",
      "2 tablespoons vegetable oil, or more as needed",
      "2 tablespoons minced fresh ginger root",
      "1 tablespoon minced serrano pepper",
      "2 cooked Dungeness crabs, cleaned and cracked",
      "2 tablespoons chopped fresh cilantro",
      "2 tablespoons sliced green onion (green part only)"
    ],
    "instructions": "Whisk ketchup, chicken broth, egg, soy sauce, chile-garlic sauce, oyster sauce, tamarind paste, fish sauce, and palm sugar together in a bowl.\nStir shallots, garlic, oil, ginger, and serrano pepper together in a pot over medium-high heat. Saute until sizzling, about 2 minutes. Add crab to pot, cover the pot with a lid, and shake until crab is completely coated in shallot mixture. Remove lid and cook and stir until heated through, about 3 minutes.\nPour ketchup mixture into pot, reduce heat to medium, and cook and stir until sauce thickens and crab is hot about 5 minutes. Remove from heat; stir in cilantro and green onions.\n",
    "picture_link": "OFp6yXFwzlrkMQ5STffYPllxQvMVLUS"
  }, 
  {
    "instructions": "Watch how to make this recipe.\nPut an oven rack in the center of the oven. Preheat the oven to 400 degrees F.\nSpray 2 baking sheets with cooking spray. Lay the pancetta in a single layer on the prepared baking sheets and bake until crispy and brown, about 12 to 14 minutes. Drain on paper towels. Cool for 5 minutes and crumble. Set aside.\nIn a food processor, combine the butter, cheeses, salt, and 1 tablespoon vegetable oil. Blend until smooth, adding extra oil, as needed, until the mixture is spreadable. Add the spinach and pulse until just combined.\nPreheat a panini maker. Spread the cheese mixture over 8 slices of bread. Top with the crumbled pancetta. Put the remaining bread slices on top. Grill the sandwiches, 2 at a time, until golden and crispy, about 3 to 4 minutes. Cool for 2 minutes, then cut each sandwich in half and arrange on a platter.",
    "ingredients": [
      "Vegetable oil cooking spray",
      "6 ounces pancetta, cut into 1/8-inch-thick slices",
      "1/2 cup (1 stick) unsalted butter, at room temperature",
      "2 cups (8 ounces) shredded Monterey Jack cheese",
      "2 cups (8 ounces) shredded mild Cheddar",
      "1 teaspoon kosher salt",
      "1 tablespoon vegetable or canola oil, plus extra, as needed",
      "2 packed cups coarsely chopped baby spinach",
      "16 (1/3-inch-thick) slices country-style white bread"
    ],
    "title": "Grilled Cheese with Spinach and Pancetta",
    "picture_link": "7.QEdieuqNCxdlIA4hZLkBTgk/iyXD6"
  },
  {
    "instructions": "Par-bake the crust: Preheat the oven to 400 degrees F. Use both pie crusts to cover the bottom and sides of a 13-by-9-inch casserole dish. Patchwork works, just cover the holes. Dock by pricking holes in the crust with a fork all over the bottom. Bake until lightly golden, 15 to 20 minutes.\nFor the fruit filling: In a large bowl, stir together the granulated sugar, brown sugar, flour, almond extract, pumpkin pie spice, lemon zest and lemon juice. Divide the mixture among the smaller bowls: 3/4 cup in the first, 1/2 cup in the second and 1/4 cup in the third. (Think of the 3 bears: poppa, momma and baby bear bowls.)\nPut the cranberries in the poppa bear bowl; in the momma bear bowl, add the apples; and in the baby bear bowl, add the figs. (Do you need a translation? Add cranberries to the bowl with the most flour mixture, apples to the bowl with 1/2 cup of the flour mixture, and the figs to the bowl with the least amount of the flour mixture.) Stir each bowl independently, unless you\u00bfre an octopus.\nFor the streusel topping: In a food processor add the flour, brown sugar, granulated sugar, butter, and a pinch of salt. Blend until crumbly, taste and add more salt if needed. Pour into a small bowl with the almonds and stir.\nPreheat the oven to 400 degrees F. Pour the fruit filling into the prepared crust, dividing it into thirds with the apples in the middle and the figs and cranberries on either side. Top evenly with the streusel mixture. Cover the pie edges with aluminum foil so they don\u00bft overcook. Bake until the top is golden brown and the fruit is beginning to bubble around the edges, 40 to 50 minutes. Serve warm with the bourbon whipped cream.\nWhisk the cream in a large bowl until soft peaks form. Add the bourbon and sugar and continue whisking until the cream holds slightly stiff peaks when the whisk is removed from the bowl. Refrigerate and serve cold.",
    "ingredients": [
      "2 pre-made pie crusts (the kind that roll up, not pre-formed)",
      "1 cup granulated sugar",
      "1/4 cup light brown sugar",
      "1/4 cup plus 2 tablespoons all-purpose flour",
      "1/2 teaspoon almond extract",
      "1/2 teaspoon pumpkin pie spice",
      "Zest of 2 lemons",
      "2 tablespoons fresh lemon juice",
      "1 pound fresh or frozen and thawed cranberries, picked through to remove stems and field debris",
      "4 Granny Smith apples, cored, peeled, and chopped",
      "15 fresh Black Mission or Brown Turkey figs, stemmed and sliced",
      "2 cups all-purpose flour",
      "1 3/4 cups packed light brown sugar",
      "1/4 cup granulated sugar",
      "1 1/2 sticks (12 tablespoons) ice cold unsalted butter, cut into teeny weeny cubes",
      "Kosher salt",
      "1 cup almonds, roughly chopped",
      "Sunny's Bourbon Whipped Cream, for serving, recipe follows",
      "1 cup heavy cream",
      "1 tablespoon bourbon",
      "1 tablespoon sugar"
    ],
    "title": "Sunny's Cranberry, Apple and Fig Streusel Tart",
    "picture_link": "ea5AxIMPGbTNz05gSoYomjBq94xg0Rm"
  }, 
  {
    "instructions": "Special equipment: an immersion blender and meat mallet\nBring a large pot of salted water to a boil. Add the broccoli and cook until just crisp-tender. Plunge into an ice bath to stop the cooking. Drain and reserve.\nBring a large pot of salted water to a boil and cook the pasta according to the package directions. Drain and reserve.\nPlace the oven rack in the middle position and preheat the oven to high broil.\nCreate a standard breading station in 3 separate 8-by-8-inch pans: Combine the flour, 1 tablespoon salt and 2 teaspoons pepper into the first pan. Whisk together the eggs and the milk in the second pan. Place the breadcrumbs in the third pan.\nTrim any fat from the edges of the chicken breast and place each breast between 2 pieces of plastic wrap. With a meat mallet, pound out each breast until it is an even 1/4 inch thick.\nDredge each breasts using the standard breading: First in the flour, then in the egg wash and finally in the breadcrumbs, making sure to coat the entire breast.\nHeat a large skillet over high heat until it begins to smoke and then reduce the heat to medium. Add 2 tablespoons oil to the pan and gently place 2 breasts in the pan. Cook the chicken on the first side until the breading is golden brown, about 5 minutes. Gently turn the breasts over and cook until the breading is golden brown on the other side, about 5 minutes. Remove the chicken breasts to a pan lined with paper towels. Repeat with the remaining chicken breasts, changing the oil between each batch.\nPlace the chicken breasts on rimmed baking sheets. Top each breast with 3 pieces of the broccolini and 2 slices of the mozzarella. Bake until the cheese is melted and begins to brown, 5 to 10 minutes.\nFor plating: Bring the Tomato Sauce to a simmer in a large skillet. Add the pasta and cook until the pasta and sauce are hot.\nDivide the pasta and sauce among 6 plates, mounding it in the center of each plate. Place a finished chicken breast on top of each mound. Sprinkle each plate with 1 tablespoon Parmesan and 1 teaspoon chopped parsley.\nCombine the whole tomatoes and their liquid, the olive oil, onion, basil, oregano, salt, pepper and 4 cloves garlic in a large bowl or 2-gallon container and puree with an immersion blender until smooth.\nHeat a large saute pan over high heat until it begins to smoke. Reduce the heat to medium, add the grapeseed oil and remaining 4 cloves garlic and quickly saute. Add the diced tomatoes and saute for 1 to 2 minutes. Add the pureed tomato sauce and bring to a simmer. Cook for 15 minutes, remove from the heat. Bring back to a simmer when you are ready to plate. Yield: 6 servings",
    "ingredients": [
      "Kosher salt and freshly ground black pepper",
      "18 pieces broccolini",
      "2 pounds spaghetti",
      "2 cups all-purpose flour",
      "6 large eggs",
      "1 cup milk",
      "3 cups panko breadcrumbs",
      "Six 6-ounce boneless skinless chicken breast",
      "1 cup grapeseed oil",
      "12 slices aged (low-moisture) mozzarella",
      "1 quart Tomato Sauce, recipe follows",
      "6 tablespoons grated Parmesan",
      "2 tablespoons chopped fresh parsley",
      "5 cups canned whole San Marzano tomatoes, plus liquid from the can",
      "1/2 cup extra-virgin olive oil",
      "1/2 cup diced yellow onion",
      "2 tablespoons fresh basil, chopped",
      "2 tablespoons fresh oregano, chopped",
      "1 tablespoon kosher salt",
      "2 teaspoons freshly ground black pepper",
      "8 cloves garlic",
      "2 tablespoons grapeseed oil",
      "3 cups canned diced San Marzano tomatoes"
    ],
    "title": "Chicken Parmesan",
    "picture_link": "Q5myPx4uVERzjAn.2qTcacekwjgFtfW"
  },
  {
    "instructions": "For the dough: Combine the flour, sugar and 1/2 teaspoon salt in a food processor and pulse until mixed. Add about a third of the chilled butter and process until thoroughly combined with no visible chunks of butter (the mixture will be slightly yellow). Add the remaining butter and pulse until the mixture resembles a very coarse meal with pea-size bits of butter. Add the vinegar in a single pulse. Gradually add 2 tablespoons ice water through the feed tube, pulsing just until evenly combined. Squeeze a handful of the dough together-it should just hold its shape and be a little crumbly. If still very powdery, pulse again, adding up to 2 tablespoons ice water.\nTurn the dough out onto a work surface and pat together into a flat disk about 1/2-inch thick. Wrap tightly in plastic wrap. Refrigerate until firm, at least 1 hour or up to 2 days.\nFor the galette: Adjust an oven rack to the lower third position and preheat the oven to 400 degrees F.\nToss the yellow squash and zucchini with 3/4 teaspoon salt in a bowl. Let sit for 15 minutes to draw out a good amount of water from the vegetables.\nMeanwhile, lay out the bacon slices in a large skillet. Place over medium heat and cook partially, flipping occasionally, to render out some fat but not to brown or crisp up, about 5 minutes. Transfer to a cutting board; let cool slightly, then cut into 1/2-inch pieces. Reserve the bacon fat in the pan.\nPat the squash slices dry; place in a large bowl with the red onion slices and toss with olive oil, 1/2 teaspoon salt and a few grinds of pepper.\nLet the dough stand at room temperature for a few minutes until slightly softened. Roll out on a lightly floured surface into a 12- to 13-inch circle, about 1/8-inch thick. Transfer to an ungreased baking sheet. Sprinkle the mozzarella and Parmesan on the circle, leaving empty a 1 1/2-inch border all around. Fan the squash, zucchini and onions in a circle, then scatter the bacon on top. Fold up the edges of the dough, pleating, to overlap the filling. Brush the dough border with the egg wash. Drizzle any bacon fat over the filling.\nBake until golden brown all over and the filling is bubbly, 45 to 50 minutes. Brush the galette with a little vinegar while still warm and serve.",
    "ingredients": [
      "1 3/4 cups all-purpose flour, plus more for rolling",
      "1 teaspoon sugar",
      "Kosher salt",
      "10 tablespoons cold unsalted butter, cut into 1/2-inch cubes",
      "1 teaspoon white vinegar",
      "1 medium yellow squash (10 ounces), sliced into 1/8-inch thin rounds",
      "1 medium zucchini (10 ounces), sliced into 1/8-inch thin rounds",
      "Kosher salt and freshly ground black pepper",
      "4 slices bacon",
      "1 small red onion, sliced thinly and separated into rings",
      "2 tablespoons extra-virgin olive oil",
      "1 cup shredded mozzarella",
      "3 tablespoons grated Parmesan",
      "1 egg, beaten",
      "Red wine vinegar, for brushing"
    ],
    "title": "Summer Squash and Bacon Galette",
    "picture_link": "9.qJlYGPwVHz9ztS23frN3BIYLIScli"
  }, 
  {
    "instructions": "Preheat the oven to 250 degrees F.\nHeat a cast iron skillet over medium-high to high heat. Put a platter in the oven to warm.\nCombine all the spices in a small bowl. Score the skin of the fish with several shallow hash marks using a very sharp knife. Season the fish on both sides with lots of salt and pepper, to taste, and rub both sides with spices.\nAdd the oil to the hot pan and cook the fish in 2 batches, until firm, about 4 minutes on each side. Transfer the fillets to the warm platter. Serve with lemon wedges and garnish with parsley or chives.",
    "ingredients": [
      "1 tablespoon smoked sweet paprika, a palmful",
      "1 1/2 teaspoons granulated onion, half a palmful",
      "1 1/2 teaspoons granulated garlic, half a palmful",
      "1 teaspoon coriander, half a palmful",
      "1 teaspoon dried mustard",
      "1/4 teaspoon cayenne pepper",
      "4 fillets black bass, skin-on",
      "Salt and freshly ground black pepper",
      "2 tablespoons vegetable oil",
      "Lemon wedges, for garnish",
      "Chopped parsley leaves or chives, for garnish"
    ],
    "title": "Smoky-Spicy Bass",
    "picture_link": "Vw7ZGo.0jIFoEXqFJmU81LIyizTUcG2"
  },
  {
    "instructions": "Watch how to make this recipe.\nSprinkle the steak with salt and pepper. Set aside.\nIn a large Dutch oven (preferably enameled cast iron) over medium-high heat, render the bacon until just starting to crisp, 6 to 7 minutes, stirring as needed. Remove 1 tablespoon of the bacon fat and set aside. Add the onions and jalapenos and cook until the onions are translucent, about 5 minutes more. Add in the garlic cook 1 to 2 minutes. Remove all from the pot to a small bowl. Set aside.\nWipe down the inside of the pot, add the reserved 1 tablespoon bacon fat and, when starting to smoke, add in 1/3 to 1/2 of the steak and cook, stirring as needed until just starting to brown, about 8 minutes. Remove to the vegetable bowl, repeat with the remaining steak.\nOnce the steak is cooked, deglaze with 1 tablespoon apple cider vinegar. Then return all the vegetables and cooked steak back to the pot and add in the beans, including the liquid in the can. Add the molasses, brown sugar, soy and ketchup, and stir to combine. Bring to a simmer over low heat, cover and cook for 2 hours, stirring every 20 to 30 minutes to assure that the bottom doesn't stick.\nAdd in more apple cider vinegar, a few tablespoons at a time to personal taste, and serve with crusty bread.",
    "ingredients": [
      "2 pounds skirt steak, cut into 1/2-inch dice",
      "Kosher salt and fresh cracked black pepper",
      "4 to 6 slices thick-cut applewood smoked bacon, 1/4-inch diced (about 1 cup)",
      "1 1/2 cups 1/4-inch diced red onion",
      "1/2 cup seeded and finely diced jalapenos (2 medium)",
      "3 tablespoons minced garlic",
      "1 teaspoon kosher salt",
      "2 teaspoons fresh cracked black pepper",
      "Apple cider vinegar, best quality",
      "1 (15-ounce) can cannellini beans, with liquid",
      "1 (15-ounce) can lima beans, with liquid",
      "1 (15-ounce) can kidney beans, with liquid",
      "1/3 cup molasses",
      "2 tablespoons dark brown sugar",
      "3 tablespoons soy sauce",
      "1/3 cup ketchup",
      "Crusty bread, for serving"
    ],
    "title": "Infineon Raceway Baked Beans",
    "picture_link": "Ja5uaD8Q7m7vvtWwk2.48dr1eCre/qi"
  },
  {
    "instructions": "Watch how to make this recipe.\nPreheat the oven to 350 degrees F.\nBrown the ground chuck in a large skillet. Drain the fat, and then add the tomato sauce, 1/2 teaspoon salt and plenty of freshly ground black pepper. Stir, and then simmer while you prepare the other ingredients.\nCook the egg noodles until al dente. Drain and set aside.\nIn a medium bowl, combine the sour cream and cottage cheese. Add plenty of freshly ground black pepper and a pinch of red pepper flakes. Add to the noodles and stir. Add the green onions and stir.\nTo assemble, add half of the noodles to a baking dish. Top with half the meat mixture, and then sprinkle on half the grated Cheddar. Repeat with noodles, meat and then a final layer of cheese. Bake until all the cheese is melted, about 20 minutes.\nServe with crusty French bread.\nTo freeze: Assemble the Sour Cream Noodle Bake in a disposable aluminum oven-proof pan and seal the top of the container with the lid or heavy foil. Seal the edges to prevent freezer burn and place in the freezer.\nTo cook from frozen: Place directly in a 375-degree F oven and bake, covered, for 45 minutes. Remove the lid and bake until lightly brown and bubbly, about 20 minutes more.",
    "ingredients": [
      "1 1/4 pounds ground chuck",
      "One 15-ounce can tomato sauce",
      "1/2 teaspoon salt",
      "Freshly ground black pepper",
      "8 ounces egg noodles",
      "1/2 cup sour cream",
      "1 1/4 cups small curd cottage cheese",
      "Pinch red pepper flakes",
      "1/2 cup sliced green onions (less to taste)",
      "1 cup grated sharp Cheddar",
      "Crusty French bread, for serving"
    ],
    "title": "Sour Cream Noodle Bake",
    "picture_link": "nm/WxalB.VjEZSa0iX9RuZ8xI51Y7bS"
  },
  {
    "instructions": "Heat a large nonstick skillet over medium-high heat and add the oil. Add the eggplant rounds and season with 1/4 teaspoon salt. Cover and cook until brown on the bottoms, about 4 minutes. Reduce the heat to medium-low and, working quickly, flip each eggplant round and top with a dollop of hummus and a cherry tomato quarter, rounded-side down. Cover and cook until heated through and the bottoms are golden brown, about 7 minutes.\nTransfer to a platter using a spatula. Sprinkle with the parsley and lemon zest and serve.",
    "ingredients": [
      "1 tablespoon extra-virgin olive oil",
      "2 baby Italian eggplants (about 6 ounces each), unpeeled, cut into 8 rounds each",
      "Kosher salt",
      "1/2 cup roasted garlic hummus or other prepared hummus",
      "4 cherry or grape tomatoes, quartered",
      "2 tablespoons fresh flat-leaf parsley leaves",
      "1 teaspoon finely grated lemon zest"
    ],
    "title": "Middle-Eastern Eggplant Rounds",
    "picture_link": "ibuqgKBoAYj7a086h/tYaHYu2M4N3pS"
  },
  {
    "instructions": "MIX ingredients in 2-qt. microwaveable bowl.\nMICROWAVE on HIGH 5 min. or until VELVEETA is completely melted, stirring after 3 min.\nSERVE with assorted cut-up fresh vegetables, WHEAT THINS Original Crackers or tortilla chips.\nRo*Tel is a product of ConAgra Foods, Inc.",
    "ingredients": [
      "1 lb. (16 oz.) VELVEETA Pasteurized Prepared Cheese Product, cut into 1/2-inch cubes",
      "1 can (10 oz.) RO*TEL Diced Tomatoes & Green Chilies, undrained"
    ],
    "title": "VELVEETA Famous Queso Dip",
    "picture_link": "lDoTUA1FP2BYbLy3s1h5s1OfAvA4LkG"
  },
  {
    "instructions": "1. Pierce the meat all over with a fork and place in a large resealable plastic bag. Add 2 tablespoons of the olive oil, the Worcestershire, vinegar, garlic and whole rosemary. Seal the bag, pushing out all the air. Shake the bag a few times and refrigerate 8 hours or overnight.\n2. Preheat the broiler and line a rimmed baking sheet with aluminum foil. Remove the meat from the marinade and pat dry. Sprinkle both sides with 1 1/2 teaspoons salt and 1/2 teaspoon pepper. Broil, flipping once, until the internal temperature reaches 125 degrees F, about 13 minutes. Transfer to a cutting board, tent with foil and let rest at least 15 minutes.\n3. Meanwhile, heat the remaining 2 tablespoons oil in a large skillet over medium-high heat. Cook the bacon, stirring, until crispy, about 5 minutes. Add the mushrooms and cook until golden brown and tender, about 10 minutes. Add the breadcrumbs, butter, chopped rosemary and 1/4 teaspoon each salt and pepper. Cook, stirring, until the breadcrumbs are golden brown, another 3 minutes. Set aside.\n4. Stir together the sour cream and horseradish and season with salt and pepper. Slice the steak against the grain, top with the mushrooms and garnish with the chopped parsley. Serve with the horseradish sauce on the side.",
    "ingredients": [
      "One 2 to 2 1/2-pound 1 1/2-inch-thick London broil",
      "1/4 cup olive oil",
      "1/4 cup Worcestershire sauce",
      "2 tablespoons balsamic vinegar",
      "4 cloves garlic, smashed",
      "2 whole sprigs rosemary plus 1 teaspoon chopped leaves",
      "Kosher salt and freshly ground black pepper",
      "1 strip bacon, chopped (about 1/2 ounce)",
      "1 pound cremini mushrooms, halved",
      "1/2 cup panko breadcrumbs",
      "2 tablespoons unsalted butter",
      "1/2 cup sour cream",
      "2 tablespoons prepared drained horseradish",
      "1 tablespoon chopped fresh parsley, for garnish"
    ],
    "title": "Balsamic-Marinated Steak and Unstuffed Mushrooms",
    "picture_link": "z0MGPSRzy.OxWWAg3mIYxQiCkpOiO/u"
  },
  {
    "instructions": "Preheat oven to 400degrees.\nDip chicken in egg, then bread crumbs, coating well. Arrange chicken in 13 x 9-inch baking dish.\nBake 20 minutes. Top chicken with prosciutto, then 1-1/2 cups pasta sauce. Top with mozzarella cheese. Bake an additional 10 minutes or until chicken is thoroughly cooked. Serve over hot spaghetti tossed with remaining heated sauce. Sprinkle, if desired, with parmesan cheese shavings.",
    "ingredients": [
      "4 boneless, skinless chicken breast halves (about 1-1/4 lbs.)",
      "1 egg, slightly beaten",
      "3/4 cup Italian seasoned dry bread crumbs",
      "2 ounces thinly sliced prosciutto or deli boiled ham",
      "1 jar Bertolli\u00ae Vineyard Premium Collections Marinara with Burgundy Wine Sauce",
      "4 ounces fresh mozzarella cheese, thinly sliced",
      "8 ounces spaghetti, cooked and drained"
    ],
    "title": "Baked Chicken Saltimbocca",
    "picture_link": "nCa4thC1KIKow2sngy24JjJkRrfMdSu"
  },
  {
    "instructions": "For the dough, in a large bowl, combine the flour, granulated sugar, and salt. Sprinkle in the butter pieces and cut them into the flour with a pastry cutter (or 2 knives or your fingertips) until the mixture is crumbly and the pieces are the size of small peas. Mix in 5 tablespoons very cold water and toss with a fork until the dough just comes together.\nPlace the dough on the floured counter and knead a few times, just to make a ball. Don't overwork the dough or the crust will be tough! Lightly flour the counter. Flatten the dough into a disk and wrap in plastic. Let it rest in the refrigerator for at least 15 minutes. (If making more than 1 hour ahead, let it rest on the counter for 10 minutes before rolling out.)\nRoll the dough out on a floured surface into a 12-inch circle. Fit into a 9-inch pie plate and trim to a 1/2-inch overhang all around. Fold the overhanging dough under itself and crimp with a fork or your fingers. Chill the pie shell in the refrigerator for 30 minutes.\nPreheat the oven to 400 degrees F. Cover the shell with a piece of parchment paper and fill with dried beans or pie weights. Bake on the bottom rack until the crust is set but still blond in color, about 20 minutes. Remove the paper and beans or weights and bake until the crust is golden brown, 10 to 15 minutes more. Let cool completely on a rack.\nFor the custard, in a saucepan, combine the granulated sugar, flour, and salt. Add the milk gradually while stirring. Cook over medium heat, stirring constantly, until it begins to bubble. Cook, stirring, for 3 minutes, or until it forms firm peaks.\nStir a small amount of the hot milk mixture into the beaten egg yolks in a small bowl. This will temper the yolks so they don't turn into scrambled eggs. Stir the tempered yolks back into the rest of the custard. Cook for 2 more minutes, stirring constantly. Remove from the heat and stir in the butter and vanilla. Slice 2 bananas into the cooled pastry crust. Top with half of the custard and slice the remaining bananas on top. Top with the rest of the custard. Chill for at least 1 hour.\nFor the whipped cream, in a cold bowl with an electric mixer, beat the cream, confectioners' sugar, and vanilla until firm peaks form. Be careful not to overbeat or your cream will turn to butter. Watch as you beat and stop when it gets thick and stays on the beaters when you remove them from the bowl.\nTop the pie with the whipped cream and serve.",
    "ingredients": [
      "1 1/2 cups all-purpose flour (plus more for rolling the dough)",
      "2 teaspoons granulated sugar",
      "1/2 teaspoon kosher salt",
      "6 tablespoons cold unsalted butter, cut into pieces",
      "3/4 cup granulated sugar",
      "1/3 cup all-purpose flour",
      "1/4 teaspoon kosher salt",
      "2 cups milk",
      "3 large egg yolks, beaten",
      "2 tablespoons unsalted butter",
      "2 teaspoons vanilla extract",
      "4 bananas, peeled",
      "1 1/2 cups chilled heavy cream",
      "3 tablespoons confectioners' sugar",
      "1 teaspoon pure vanilla extract"
    ],
    "title": "Happy Holly's Banana Cream Pie",
    "picture_link": "U/ynRck7Xd8CYkGmwRfE9DIo5p9B8Qi"
  },
  {
    "instructions": "Using a mandolin or a very sharp knife, slice zucchini into very thin rounds. Overlap zucchini disks in 1 layer on a plate; season with salt and pepper. Drizzle over the olive oil and lemon juice and scatter with leeks. Using a mandoline or a vegetable peeler, shave very thin slices of Parmesan and place them over leeks. Garnish with mint leaves. Serve immediately.",
    "ingredients": [
      "2 medium zucchini",
      "Kosher salt and freshly ground black pepper",
      "1 tablespoon extra-virgin olive oil",
      "1/2 lemon, juiced",
      "1 leek, white part only, sliced thinly",
      "1/4 pound piece Parmesan",
      "Fresh mint leaves, for garnish"
    ],
    "title": "Zucchini Carpaccio",
    "picture_link": "QhaGK7vDKztcrqepOOW.4C1r7zSTMu."
  },
  {
    "instructions": "Place sliced beets in large bowl. In a small bowl, whisk together vinegar, mustard, and caraway seeds. Slowly add oil in a stream and continue whisking. Season with salt and pepper. Pour the dressing over the beets leaving 3 tablespoons of dressing in the small bowl. Add the radishes and scallions to the remaining dressing in the small bowl and toss to coat. Place the lettuce on a platter and top with beets. Sprinkle beets with radishes and scallions. Garnish with parsley.",
    "ingredients": [
      "1 1/2 pounds beets, boiled, peeled and thinly sliced",
      "3 tablespoons red wine vinegar",
      "1 teaspoon Dijon mustard",
      "1 teaspoon caraway seeds",
      "1/3 cup olive oil",
      "Salt and pepper",
      "6 radishes, trimmed and thinly sliced",
      "3 scallions, thinly sliced",
      "Green leaf lettuce",
      "3 tablespoons finely chopped parsley"
    ],
    "title": "Beet Salad",
    "picture_link": "t4OwsE.lMCuZahN7KGjHVUjAUXylM6K"
  },
  {
    "instructions": "Watch how to make this recipe.\nPreheat the oven to 400 degrees F.\nIn a medium straight-sided saute pan, heat the olive oil over medium heat. Add the onion and cook until soft, about 5 minutes. Add the capers, oregano, garlic, chile and orange zest. Cook for 3 more minutes. Add the tomatoes and tomato puree. Bring to a slow simmer and cook until thickened, 10 to 15 minutes.\nSpoon the tomato mixture into the bottom of a small baking dish. Form 6 small wells to hold the eggs. Crack an egg into each well. Place the croutons around the eggs and finish with the Parmigiano-Reggiano. Bake until the yolks are still soft but the whites are cooked, 8 to 10 minutes.",
    "ingredients": [
      "5 tablespoons extra-virgin olive oil",
      "1 cup small-diced onion (about 1 medium onion)",
      "1/4 cup capers, drained and rinsed",
      "2 tablespoons minced fresh oregano",
      "1 tablespoon finely minced garlic",
      "1 green serrano chile, finely sliced",
      "Grated zest of 1 orange",
      "One 28-ounce can whole San Marzano tomatoes, drained and roughly chopped",
      "6 ounces San Marzano tomato puree",
      "6 large eggs",
      "1 cup 3/4-inch baked croutons",
      "1/2 cup grated Parmigiano-Reggiano"
    ],
    "title": "Baked Eggs with Green Chiles and Capers",
    "picture_link": "Ip8xOH7TRsTLsV975Xx3GD5PhlTW8ca"
  },
  {
    "instructions": "Watch how to make this recipe.\nPreheat the oven to 375 degrees F. Butter a 9-inch round casserole dish.\nMelt 3 tablespoons butter in a skillet over medium heat. Add the minced garlic and cook for a couple of minutes. Crank up the heat a bit and throw in the spinach. Stir the spinach around and cook for a couple of minutes until it wilts; season with salt and pepper. Transfer the spinach to a mesh strainer set over a bowl to drain. Set aside.\nMelt 2 tablespoons butter in the same skillet, throw in the quartered artichokes and cook over medium-high heat until the artichokes start to get a little color, about 3 minutes. Transfer the artichokes to the strainer with the spinach.\nIn the same skillet or a different pot, melt the remaining 3 tablespoons butter and whisk in the flour until it makes a paste. Cook over medium-low heat for a minute or 2, then pour in the milk. Stir and cook until slightly thickened, about 3 minutes; splash in more milk if needed. Add the cream cheese, pepper Jack, feta, Parmesan and cayenne and stir until the cheeses are melted and the sauce is smooth. Chop the artichokes and spinach and add them to the sauce. Stir to combine.\nPour the mixture into the prepared casserole dish. Top with extra grated pepper Jack and bake until the cheese is melted and bubbly, about 15 minutes. Serve with the Salted Pita Wedges.\nPreheat the oven to 375 degrees F.\nCut the pita breads into 6 wedges each. Lay the wedges on a foil-lined baking sheet and brush both sides generously with the olive oil. Sprinkle both sides with salt, then bake until they're golden brown and crisp, 15 to 18 minutes.",
    "ingredients": [
      "8 tablespoons (1 stick) butter, plus more for buttering the casserole dish",
      "1/4 cup minced garlic",
      "One 10-ounce bag fresh baby spinach",
      "Kosher salt and freshly ground black pepper",
      "Two 14-ounce cans artichoke hearts, rinsed, drained and quartered",
      "3 tablespoons all-purpose flour",
      "1 1/2 cups whole milk, plus more if needed",
      "One 8-ounce package cream cheese, softened",
      "3/4 cup grated pepper Jack cheese, plus more for topping",
      "1/2 cup crumbled feta",
      "1/2 cup grated Parmesan",
      "1/4 teaspoon cayenne",
      "Salted Pita Wedges, recipe follows, for serving",
      "6 pita breads",
      "1/2 cup olive oil",
      "1 tablespoon kosher salt"
    ],
    "title": "Spinach Artichoke Dip",
    "picture_link": "DL8kbR9I0paCb2JTjqLnqnPNV0kTMi2"
  },
  {
    "instructions": "Preheat the oven to 350 degrees. Pulse the wafers and pine nuts in a food processor until well ground up. Add the butter and blend until evenly mixed. Set aside 1/4 cup of crumbs. Press the remaining crumb mixture evenly into a 9-by-13 shallow baking pan; bake until golden brown, 15 to 18 minutes. Cool.\nIn a medium bowl, thoroughly whisk together the tequila, lime juice, egg yolks and condensed milk.\nIn another medium bowl, beat the egg whites and sugar with an electric mixer until they hold soft peaks. Gently fold the egg whites into the tequila mixture. Spread the filling evenly over the crust and bake for 25 minutes; cool. Sprinkle the reserved crumbs on top. Chill in the fridge for 2 hours or overnight before cutting into bars.",
    "ingredients": [
      "1 12-ounce box vanilla wafers",
      "1/2 cup pine nuts",
      "3/4 cup unsalted butter (1 1/2 sticks), melted",
      "1/3 cup tequila",
      "1/2 cup fresh lime juice",
      "5 large egg yolks, plus 2 egg whites",
      "1 14-ounce can sweetened condensed milk",
      "1 tablespoon sugar"
    ],
    "title": "Tequila Bars",
    "picture_link": "EzdYe5Whds4iscT4kAjyoVeR3dbF6dW"
  },
  {
    "instructions": "Make the dough: Put 2 1/4 cups warm (100 degrees F) water in a large measuring cup; stir in the yeast to dissolve, then stir in the sugar and olive oil. Let stand until bubbly, 3 to 5 minutes. Combine 5 cups flour and 2 teaspoons salt in a stand mixer fitted with the paddle attachment. Add the yeast mixture and mix on medium-low speed, adding a little more flour or water, if needed, until a rough, sticky ball of dough forms, about 1 minute. Let rest 5 minutes, then mix on medium low until no longer sticky, about 1 more minute. Transfer the dough to an oiled surface and knead with oiled hands until smooth, about 10 times. Let rest 5 minutes, then knead briefly again and transfer to an oiled bowl. Cover with plastic wrap; refrigerate at least 8 hours or overnight. Divide the dough into 4 balls, dust with flour and cover loosely with plastic wrap. Let sit at room temperature 2 hours before making the pizzas.\nMake the sauce: Crush the tomatoes in a bowl using your hands. Stir in the olive oil, garlic, 1 1/2 teaspoons salt and the oregano. Cover and let stand 2 hours. Position a pizza stone or inverted baking sheet on the lowest oven rack; preheat to 500 degrees F for at least 30 minutes. Stretch each ball of dough into a 12-to-14-inch round on individual sheets of parchment paper. Let rest 15 minutes. Remove and discard the garlic from the sauce. Spread a thin layer of sauce on each pizza, leaving a border. Top with one-quarter each of the mozzarella, parmesan, cherry peppers, soppressata and radicchio; drizzle with olive oil. Slide 1 pizza (on the parchment) onto a pizza peel or another inverted baking sheet, then slide onto the hot stone in the oven. Bake until the crust browns, 12 to 15 minutes. Top with oregano. Repeat to make 3 more pizzas. Photograph by Con Poulos",
    "ingredients": [
      "1 1/2 teaspoons active dry yeast",
      "1 tablespoon sugar",
      "1 tablespoon extra-virgin olive oil, plus more for brushing",
      "5 to 5 1/2 cups all-purpose flour, plus more for dusting",
      "Kosher salt",
      "1 28-ounce can whole peeled San Marzano tomatoes",
      "2 tablespoons extra-virgin olive oil",
      "5 cloves garlic, smashed",
      "Kosher salt",
      "1 teaspoon dried oregano",
      "1 pound fresh mozzarella, sliced",
      "1/2 cup grated parmesan cheese",
      "1/2 cup pickled sweet cherry peppers, seeded and sliced",
      "4 ounces sliced hot soppressata, cut into strips",
      "1 small head radicchio, sliced",
      "Extra-virgin olive oil, for drizzling",
      "Dried oregano, for sprinkling"
    ],
    "title": "Soppressata Pizzas",
    "picture_link": "jbh6On9Vu7pUPNaYgvVA1RLfwBQFvHW"
  },
  {
    "instructions": "For the cupcakes: Preheat the convection oven to 325 degrees F or a standard oven to 350 degrees F.\nIn large mixer bowl, cream together the granulated sugar and butter until light and fluffy with a heavy duty mixer. Add the eggs, one at a time, and mix thoroughly after each addition. Add the coconut extract and mix well. Combine the flour, baking soda and salt. Add half of the flour to the mixer bowl along with 1/2 cup of the half-and-half. Mix until the flour is mixed in, scraping the sides of the bowl with a rubber spatula. Add the rest of flour mixture and the other 1/2 cup half-and-half. Mix until the batter is smooth and all of the flour lumps are gone. Fold in the coconut flakes.\nFill 24 cupcake liners half full and bake for 20 minutes in the convection oven or 28 minutes in the standard oven. The tops of the cupcakes should be lightly browned. Check the cupcakes to make sure no batter sticks to a wooden toothpick when inserted into the cupcake. Cool the cupcakes completely.\nFor the mousse filling: In large mixer bowl, beat the heavy cream, half-and-half, coconut extract and pudding mix until light and fluffy using a heavy duty mixer. It should have the consistency of whipped cream. Gently fold in the coconut using a plastic spatula. Put the filling in a pastry bag or zipper bag with a corner cut off.\nFor the coconut buttercream: In large mixer bowl, beat together the butter and half of the powdered sugar using heavy duty mixer. Add the half-and-half and the rest of the powdered sugar, along with the coconut extract, and mix well. If the frosting is thicker than you would like, add 1 teaspoon of additional half-and-half at a time, mixing well after each addition, until the frosting reaches the correct consistency. The thickness may depend on the humidity levels in your region. Put into a pastry bag.\nTo assemble: Make a hole in the middle of each cupcake using a sharp knife. Be sure and leave a small amount of cake in the bottom of the hole. Fill the cupcakes with the mousse filling. Frost with coconut buttercream. You may top the cupcakes with more flake coconut or toasted coconut as desired.\nServe immediately or chill until ready to serve.",
    "ingredients": [
      "2 cups granulated sugar",
      "2 sticks unsalted butter, at room temperature",
      "4 large whole eggs",
      "2 teaspoons coconut extract",
      "2 1/2 cups all-purpose flour",
      "4 teaspoons baking powder",
      "1 teaspoon salt",
      "1 cup half-and-half",
      "1 cup flake coconut",
      "1 cup heavy cream",
      "1 cup half-and-half",
      "2 teaspoons coconut extract",
      "1 package (4 serving size) instant vanilla pudding mix",
      "1 cup flake coconut",
      "2 sticks unsalted butter, at room temperature",
      "2 pounds powdered sugar",
      "1 teaspoon coconut extract",
      "1/4 cup half-and-half, plus more for thinning frosting if needed",
      "Flake or toasted coconut, for garnish"
    ],
    "title": "Coconut Cupcakes with Whipped Coconut Mousse Filling and Coconut Buttercream",
    "picture_link": "pkNtENpEwnlk2lZFDRe9u6zusdWBuYm"
  },
  {
    "instructions": "Brush shrimp with 2 to 3 tablespoons Ginger Sesame Vinaigrette. Grill over medium-high heat 3 to 4 minutes or until pink, turning once.\nDivide salad on 2 large plates. Arrange shrimp, tomatoes, mushrooms and green onions on each. Drizzle with Ginger Sesame Vinaigrette, to taste. Refrigerated leftovers.\nCombine 1/3 cup rice vinegar, 1/4 cup toasted sesame seed, 1 tablespoon soy sauce, 2 teaspoons finely chopped ginger, and 2 teaspoons minced garlic in blender container. Cover; blend until smooth. Slowly add 2/3 cup canola oil and 1/3 cup sesame oil in thin stream, until blended. Makes about 1-1/2 cups.",
    "ingredients": [
      "8 medium-large raw shrimp, peeled and deveined",
      "Ginger Sesame Vinaigrette (recipe below)",
      "1 pkg. (12 oz.) DOLE\u00ae Very Veggie\u00ae",
      "10 cherry tomatoes, cut in half",
      "2 medium mushrooms, thinly sliced",
      "2 green onions, diagonally sliced"
    ],
    "title": "Grilled Shrimp Salad with Sesame Ginger Vinaigrette",
    "picture_link": "TemKwhNF4FXkXZjR1So3G.a7aaJL/qq"
  },
  {
    "instructions": "Whisk the garlic, ginger, sesame oil, vinegar, soy sauce and sugar in a large bowl. Transfer 2 tablespoons of the dressing to a medium bowl, add the shrimp and toss. Add the carrot, celery and snow peas to the remaining dressing and toss.\nHeat a large skillet over high heat and add 2 teaspoons vegetable oil. Add the shrimp and stir-fry until they turn pink, 3 to 4 minutes, then transfer to the bowl with the vegetables. Add 3 to 4 tablespoons water to the skillet and scrape up the browned bits with a wooden spoon, then add the liquid to the bowl with the shrimp. Let the skillet reheat, then add the remaining 1 teaspoon vegetable oil and stir-fry the rice until toasted, about 2 minutes. Remove from the heat and let cool.\nAdd the rice and scallions to the shrimp-vegetable mixture and toss. Divide among bowls and top with the lettuce, sprouts, chow mein noodles and/or peanuts.\nPhotograph by Kate Sears",
    "ingredients": [
      "2 cloves garlic, minced",
      "1 2-inch piece ginger, peeled and grated",
      "3 tablespoons toasted sesame oil",
      "1/4 cup rice vinegar",
      "2 tablespoons soy sauce",
      "Pinch of sugar",
      "3/4 pound large shrimp, peeled, deveined and halved lengthwise",
      "1 large carrot, shredded",
      "2 stalks celery, thinly sliced",
      "2 cups snow peas, thinly sliced",
      "1 tablespoon vegetable oil",
      "2 cups cooked white or brown rice",
      "1 bunch scallions, thinly sliced",
      "1/4 head iceberg lettuce, shredded",
      "1 cup mung bean sprouts",
      "1/2 cup chow mein noodles and/or chopped peanuts"
    ],
    "title": "Asian Rice Salad With Shrimp",
    "picture_link": "qYyUp4ObVQXbK8NIoLx70FIiRUJdR16"
  },
  {
    "instructions": "Watch how to make this recipe.\nPut an oven rack in the middle of the oven and preheat to 350 degrees F. Grease a Bundt pan with butter.\nFirst prepare the cake batter. Add the butter and sugar to a bowl and, using an electric hand mixer or a stand mixer, beat until light and fluffy. Then beat in 1 egg.\nSift together the flour, baking soda, baking powder and salt in a medium bowl. Mix the buttermilk, cocoa powder, tequila, triple sec and vanilla extract in a medium bowl. Beat half of the flour mixture half of the buttermilk into the egg mixture. Repeat, ending with the flour mixture. Blend until well incorporated.\nNow prepare the flan mixture. In a blender, combine the condensed milk, evaporated milk, cream cheese, the remaining 3 eggs and vanilla extract. Blend on high for 30 seconds.\nScoop the cake batter into the prepared Bundt pan. Then slowly pour the flan mixture over the cake batter. Add about 1-inch of hot water to the roasting pan.\nCarefully slide the pan into the oven and bake until the surface of the cake is firm to the touch, or an inserted toothpick comes out clean, about 1 hour. When the cake is done, remove from the water bath and cool completely to room temperature, about 1 hour.\nRun the tip of a sharp paring knife along the edge of the Bundt pan to loosen. Invert a large, rimmed serving platter over the Bundt pan, grasp tightly together, jiggle it a little and flip over to release the chocoflan from the pan. Garnish the cake with some chopped pecans. Place some mixed berries in the center of the chocoflan then sprinkle the entire thing with powdered sugar and serve.",
    "ingredients": [
      "12 tablespoons (1 1/2 sticks) butter, plus more for greasing, at room temperature",
      "1 cup sugar",
      "4 eggs, at room temperature",
      "1 2/3 cups all-purpose flour",
      "1 teaspoon baking soda",
      "3/4 teaspoon baking powder",
      "1/2 teaspoon salt",
      "1 1/3 cup buttermilk",
      "1/2 cup cocoa powder",
      "2 teaspoons tequila",
      "2 teaspoons triple sec",
      "1 teaspoon vanilla extract",
      "One 14-ounce can sweetened condensed milk",
      "One 12-ounce can evaporated milk",
      "4 ounces cream cheese, at room temperature",
      "1 tablespoon vanilla extract",
      "1/4 cup chopped pecans or walnuts",
      "Mixed berries, such as raspberries, blackberries, blueberries and strawberries",
      "Powdered sugar, for dusting"
    ],
    "title": "Chocoflan",
    "picture_link": "miKSixbfESXwa3z58BvWr30d8cjxo1O"
  }
]

for ind, rep in enumerate(recipes):
    es.index(index="recs", id=ind + 1, document=rep) #create index and add document.

es.indices.refresh(index="recs")